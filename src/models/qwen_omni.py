import soundfile as sf
import torch

from .base import VoiceAssistant
from transformers import Qwen2_5OmniForConditionalGeneration, Qwen2_5OmniProcessor
from qwen_omni_utils import process_mm_info
import tempfile


class QwenOmniAssistant(VoiceAssistant):
    def __init__(self):
        self.model = Qwen2_5OmniForConditionalGeneration.from_pretrained("Qwen/Qwen2.5-Omni-7B", torch_dtype="auto", device_map="auto")
        self.processor = Qwen2_5OmniProcessor.from_pretrained("Qwen/Qwen2.5-Omni-7B")
        self.model.disable_talker()

    def generate_audio(
        self,
        audio,
        max_new_tokens=2048,
    ):
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".wav") as temp_file:
            temp_filename = temp_file.name
            # Write the audio data to the file
            sf.write(temp_file.name, audio['array'], audio['sampling_rate'], format='wav')

        messages = [
            {"role": "system", "content": [
                {"type": "text", "text": "You are a helpful assistant."} # "text": "You are Qwen, a virtual human developed by the Qwen Team, Alibaba Group, capable of perceiving auditory and visual inputs, as well as generating text and speech."
            ], },
            {"role": "user", "content": [
                {"type": "audio", "audio": temp_filename},
            ]
             },
        ]
        text = self.processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        audios, images, videos = process_mm_info(messages, use_audio_in_video=False)
        inputs = self.processor(text=text, audio=audios, images=images, videos=videos, return_tensors="pt", padding=True, use_audio_in_video=False)
        inputs = inputs.to(self.model.device).to(self.model.dtype)
        with torch.no_grad():
            text_ids = self.model.generate(
                **inputs,
                return_audio=False,
                max_new_tokens=max_new_tokens
            )[:, inputs.input_ids.size(1):]

        text = self.processor.batch_decode(text_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        return text
