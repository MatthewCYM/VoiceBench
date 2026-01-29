from .base import VoiceAssistant
import io
import base64
import os
import soundfile as sf
import requests


class UltravoxGlm4p7Assistant(VoiceAssistant):
    """
    Ultravox-hosted GLM4P7 eval model via OpenAI-style chat/completions.

    Auth:
      - ULTRAVOX_API_KEY (required)
    Optional:
      - ULTRAVOX_GLM4P7_API_URL (required for public repo; no default is hardcoded)
    """

    def __init__(self):
        self.api_key = os.getenv("ULTRAVOX_API_KEY")
        self.api_url = os.getenv("ULTRAVOX_GLM4P7_API_URL")
        if not self.api_url:
            raise ValueError(
                "ULTRAVOX_GLM4P7_API_URL is not set. "
                "Set it to your Ultravox chat/completions endpoint URL."
            )

    def generate_audio(
        self,
        audio,
        max_new_tokens=2048,
    ):
        # Write the audio data to an in-memory buffer in WAV format
        buffer = io.BytesIO()
        sf.write(buffer, audio["array"], audio["sampling_rate"], format="WAV")
        buffer.seek(0)  # Reset buffer position to the beginning

        # Read buffer as bytes and encode in base64
        wav_data = buffer.read()
        encoded_string = base64.b64encode(wav_data).decode("utf-8")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        system_prompt = """You are a helpful assistant. Think step by step and then answer the question. When answering questions:
For multiple choice questions (A/B/C/D options):
- End your response with "The answer is [X]" where X is the letter (A, B, C, or D)"""

        payload = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_audio",
                            "input_audio": {"data": encoded_string, "format": "wav"},
                        }
                    ],
                },
            ],
            "max_new_tokens": max_new_tokens,
            "chat_template_kwargs": {
                "enable_thinking": True,
            },
        }

        response = requests.post(
            self.api_url,
            json=payload,
            headers=headers,
            timeout=300,
        )
        response.raise_for_status()
        result = response.json()

        def _strip_thinking(text: str) -> str:
            # Ultravox "thinking" mode may include chain-of-thought in the same content,
            # often delimited by a closing </think> tag. IFEval (and other format-sensitive
            # benchmarks) should evaluate only the final answer.
            if "</think>" in text:
                return text.rsplit("</think>", 1)[-1].lstrip()
            return text

        # Extract only the final content from the response, avoiding metadata
        if "choices" in result and len(result["choices"]) > 0:
            message = result["choices"][0].get("message", {})
            return _strip_thinking(message.get("content", ""))

        return result.get("text", result.get("response", str(result)))

