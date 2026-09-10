<h1 align="center">VoiceBench: Benchmarking LLM-Based Voice Assistants</h1>

<p align="center">
  <a href="https://matthewcym.github.io/VoiceBench/">🏆 Leaderboard</a> |
  <a href="https://arxiv.org/abs/2410.17196">📄 Paper</a> |
  <a href="https://huggingface.co/datasets/hlt-lab/voicebench">🤗 Data</a>
</p>


> We encourage new result submissions through the [issue tracker](https://github.com/matthewcym/VoiceBench/issues). The leaderboard will be updated accordingly.


## News
* **`2026.04.20`** Check out [HalluAudio](https://github.com/Feiyuzhao25/halluaudio), a comprehensive benchmark for hallucination detection in LALMs.
* **`2025.04.20`** Released `wildvoice`, a crowd-sourced dataset comprising human-recorded speech with diverse accents.
* **`2025.04.12`** Released `bbh`, a crowd-sourced dataset comprising human-recorded speech, for evaluating the reasoning ability of voice assistants. 
* **`2024.12.11`** Updated the VoiceBench Leaderboard to include `mmsu`.
* **`2024.12.10`** Added a curated list of awesome voice assistants.
* **`2024.11.24`** Expanded the test samples in VoiceBench to include `mmsu`, covering 12 diverse domains from `mmlu-pro`.
* **`2024.11.12`** Updated the VoiceBench Leaderboard to include: 1) Mini-Omni2, GPT-4o-Audio, and Whisper-v3+GPT-4o, and 2) multiple-choice QA from OpenBookQA.
* **`2024.10.30`** Expanded the test samples in VoiceBench to include: 1) the complete set of open-ended QA from `alpacaeval`, and 2) multiple-choice QA from `openbookqa`.

## Table of Contents
- [**Setup**](#setup)
- [**Dataset**](#dataset)
- [**Evaluation**](#evaluation)
- [**Awesome Voice Assistants**](#awesome-voice-assistants)
- [**Citation**](#citation)


## Setup
```shell
conda create -n voicebench python=3.10
conda activate voicebench
pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu121
pip install xformers==0.0.23 --no-deps
pip install -r requirements.txt
```

## Dataset

The data used in this project is available at [VoiceBench Dataset](https://huggingface.co/datasets/hlt-lab/voicebench) hosted on Hugging Face.

You can access it directly via the link and integrate it into your project by using the Hugging Face `datasets` library.

### How to Use the Dataset

To load the dataset in your Python environment:

```python
from datasets import load_dataset

# Load the VoiceBench dataset
# Available subset: alpacaeval, commoneval, sd-qa, ifeval, advbench, ...
dataset = load_dataset("hlt-lab/voicebench", 'alpacaeval')
```

### Available Data

| Subset          | # Samples | Audio Source |       Task Type       |
|-----------------|:---------:|:------------:|:---------------------:|
| alpacaeval      |    199    |  Google TTS  |     Open-Ended QA     |
| alpacaeval_full |    636    |  Google TTS  |     Open-Ended QA     |
| commoneval      |    200    |    Human     |     Open-Ended QA     |
| wildvoice       |   1,000   |    Human     |     Open-Ended QA     |
| openbookqa      |    455    |  Google TTS  |  Multiple-Choice QA   |
| mmsu            |   3,074   |  Google TTS  |  Multiple-Choice QA   |
| sd-qa           |    553    |    Human     |  Reference-Based QA   |
| mtbench         |    46     |  Google TTS  |     Multi-Turn QA     |
| ifeval          |    345    |  Google TTS  | Instruction Following |
| bbh             |   1,000   |    Human     |       Reasoning       |
| advbench        |    520    |  Google TTS  |        Safety         |


**PS**: `alpacaeval` contains `helpful_base` and `vicuna` data, while `alpacaeval_full` is constructed with the complete data. `alpacaeval_full` is used in the leaderboard.


## Evaluation
### Step 1: Get the Voice Assistant's Response
To obtain the responses from the voice assistant model, run the following command:
```shell
python main.py --model naive --data alpacaeval --split test --modality audio
```

**Supported Arguments:**
- `--model`: Specifies the model to use for generating responses. Replace `naive` with the model you want to test (e.g., `qwen2`, `diva`).
- `--data`: Selects the subset of the dataset. Replace `alpacaeval` with other subsets like `commoneval`, `sd-qa`, etc., depending on your evaluation needs.
- `--split`: Chooses the data split to evaluate.
    - For most datasets (`alpacaeval`, `commoneval`, `ifeval`, `advbench`), use `test` as the value.
    - For the `sd-qa` subset, you should provide a region code instead of `test`, such as `aus` for Australia, `usa` for the United States, etc.
- `--modality`: Use `audio` for spoken instructions, `text` for text-based instructions.

This will generate the output and save it to a file named naive-alpacaeval-test-audio.jsonl.

### Step2: Automatic GPT-4 Evaluation
For datasets `alpacaeval`, `commoneval`, `wildvoice`, and `sd-qa`, we use `gpt-4o-mini` to evaluate the responses. Run the following command to get the GPT score:
```shell
python api_judge.py --src_file naive-alpacaeval-test-audio.jsonl
```
The GPT evaluation scores will be saved to `result-naive-alpacaeval-test-audio.jsonl`.

**Note:** This step should be skipped for other datasets, as they are not evaluated using GPT-4.

### Step3: Get the Final Results
To generate the final evaluation results, run:
```shell
python evaluate.py --src_file result-naive-alpacaeval-test-audio.jsonl --evaluator open
```
**Supported Arguments:**
- `--evaluator`: Specifies the evaluator type:
    - Use `open` for `alpacaeval`, `commoneval`, and `wildvoice`.
    - Use `qa` for `sd-qa`.
    - Use `ifeval` for `ifeval`.
    - Use `harm` for `advbench`.
    - Use `mcq` for `openbookqa` and `mmsu`.
    - Use `bbh` for `bbh`.

## Awesome Voice Assistants
| Title                                                                                                                                                                                                                                                                                                                                        |    Date    |                                   Code                                   |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------:|:------------------------------------------------------------------------:|
| [**Unified Audio Intelligence Without Regressing on Text Intelligence**](https://arxiv.org/abs/2607.05196) | 2026-07-06 | [HF](https://huggingface.co/collections/nvidia/nemotron-labs-audex) |
| [**ParaBridge: Bridging Paralinguistic Perception and Dialogue Behavior in Speech Language Models**](https://arxiv.org/abs/2606.10581) &nbsp; ![Star](https://img.shields.io/github/stars/AmphionTeam/ParaBridge) | 2026-06-09 | [Github](https://github.com/AmphionTeam/ParaBridge) |
| [**Audio Interaction Model**](https://arxiv.org/abs/2606.05121) &nbsp; ![Star](https://img.shields.io/github/stars/xzf-thu/Audio-Interaction) | 2026-06-03 | [Github](https://github.com/xzf-thu/Audio-Interaction) |
| [**Sympatheia: Emotionally Adaptive Voice Assistant with Continuous Affect Conditioning**](https://arxiv.org/abs/2606.00851) &nbsp; ![Star](https://img.shields.io/github/stars/susameddin/sympatheia) | 2026-05-30 | [Github](https://github.com/susameddin/sympatheia) |
| [**Liberating LLM Capabilities in Full-Duplex Speech Models**](https://arxiv.org/abs/2606.07547) &nbsp; ![Star](https://img.shields.io/github/stars/zly-idleness/lws_demo) | 2026-05-04 | [Github](https://github.com/zly-idleness/lws_demo) |
| [**MiniCPM-o 4.5: Towards Real-Time Full-Duplex Omni-Modal Interaction**](https://arxiv.org/abs/2604.27393) &nbsp; ![Star](https://img.shields.io/github/stars/OpenBMB/MiniCPM-V) | 2026-04-30 | [Github](https://github.com/OpenBMB/MiniCPM-V) |
| [**Nemotron 3 Nano Omni: Efficient and Open Multimodal Intelligence**](https://arxiv.org/abs/2604.24954) &nbsp; ![Star](https://img.shields.io/github/stars/NVIDIA-NeMo/Nemotron) | 2026-04-27 | [Github](https://github.com/NVIDIA-NeMo/Nemotron/tree/main/usage-cookbook/Nemotron-3-Nano-Omni) |
| [**Qwen3.5-Omni Technical Report**](https://arxiv.org/abs/2604.15804) | 2026-04-17 | [Demo](https://huggingface.co/spaces/Qwen/Qwen3.5-Omni-Online-Demo) |
| [**VoxMind: An End-to-End Agentic Spoken Dialogue System**](https://arxiv.org/abs/2604.15710) &nbsp; ![Star](https://img.shields.io/github/stars/MM-Speech/VoxMind) | 2026-04-17 | [Github](https://github.com/MM-Speech/VoxMind) |
| [**Resurfacing Paralinguistic Awareness in Large Audio Language Models**](https://arxiv.org/abs/2603.11947) | 2026-03-12 | -- |
| [**DuplexCascade: Full-Duplex Speech-to-Speech Dialogue with VAD-Free Cascaded ASR-LLM-TTS Pipeline and Micro-Turn Optimization**](https://arxiv.org/abs/2603.09180) &nbsp; ![Star](https://img.shields.io/github/stars/sbintuitions/DuplexCascade) | 2026-03-10 | [Github](https://github.com/sbintuitions/DuplexCascade) |
| [**Language-Aware Distillation for Multilingual Instruction-Following Speech LLMs with ASR-Only Supervision**](https://arxiv.org/abs/2603.07025) | 2026-03-07 | -- |
| [**X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLMs**](https://arxiv.org/abs/2603.24596) | 2026-03-06 | -- |
| [**DIFFA-2: A Practical Diffusion Large Language Model for General Audio Understanding**](https://arxiv.org/abs/2601.23161) &nbsp; ![Star](https://img.shields.io/github/stars/NKU-HLT/DIFFA) | 2026-01-30 | [Github](https://github.com/NKU-HLT/DIFFA) |
| [**CORD: Bridging the Audio-Text Reasoning Gap via Weighted On-policy Cross-modal Distillation**](https://arxiv.org/abs/2601.16547) | 2026-01-23 | -- |
| [**AzeroS: Extending LLM to Speech with Self-Generated Instruction-Free Tuning**](https://arxiv.org/abs/2601.06086) &nbsp; ![Star](https://img.shields.io/github/stars/AudenAI/Auden) | 2025-12-31 | [Github](https://github.com/AudenAI/Auden/tree/main/examples/azeros) |
| [**LFM2 Technical Report**](https://arxiv.org/abs/2511.23404) &nbsp; ![Star](https://img.shields.io/github/stars/Liquid4All/liquid-audio) | 2025-11-28 | [Github](https://github.com/Liquid4All/liquid-audio) |
| [**LongCat-Flash-Omni Technical Report**](https://arxiv.org/abs/2511.00279) &nbsp; ![Star](https://img.shields.io/github/stars/meituan-longcat/LongCat-Flash-Omni) | 2025-10-31 | [Github](https://github.com/meituan-longcat/LongCat-Flash-Omni) |
| [**Empathy Omni: Enabling Empathetic Speech Response Generation through Large Language Models**](https://arxiv.org/abs/2508.18655) &nbsp; ![Star](https://img.shields.io/github/stars/W311411/Empathy-Omni) | 2025-08-26 | [Github](https://github.com/W311411/Empathy-Omni) |
| [**OSUM-EChat: Enhancing End-to-End Empathetic Spoken Chatbot via Understanding-Driven Spoken Dialogue**](https://arxiv.org/abs/2508.09600) &nbsp; ![Star](https://img.shields.io/github/stars/ASLP-lab/OSUM)                                                                                                                                | 2025-08-13 |             [Github](https://github.com/ASLP-lab/OSUM)                   |
| [**DIFFA: Large Language Diffusion Models Can Listen and Understand**](https://arxiv.org/abs/2507.18452) &nbsp; ![Star](https://img.shields.io/github/stars/NKU-HLT/DIFFA)                                                                                                                                                                   | 2025-07-24 |             [Github](https://github.com/NKU-HLT/DIFFA)                   |
| [**Voxtral**](https://arxiv.org/abs/2507.13264)                                                                                                                                 | 2025-07-17 | [HF](https://huggingface.co/mistralai/Voxtral-Small-24B-2507) |
| [**Audio Flamingo 3: Advancing Audio Intelligence with Fully Open Large Audio Language Models**](https://arxiv.org/abs/2507.08128) &nbsp; ![Star](https://img.shields.io/github/stars/NVIDIA/audio-flamingo)                                                                                                                                 | 2025-07-10 |             [Github](https://github.com/NVIDIA/audio-flamingo)           |
| [**DeSTA2.5-Audio: Toward General-Purpose Large Audio Language Model with Self-Generated Cross-Modal Alignment**](https://arxiv.org/abs/2507.02768) &nbsp; ![Star](https://img.shields.io/github/stars/kehanlu/DeSTA2.5-Audio)                                                                                                               | 2025-07-03 |             [Github](https://github.com/kehanlu/DeSTA2.5-Audio)          |
| [**Stream-Omni: Simultaneous Multimodal Interactions with Large Language-Vision-Speech Model**](https://arxiv.org/abs/2506.13642) &nbsp; ![Star](https://img.shields.io/github/stars/ictnlp/Stream-Omni)                                                                                                                                     | 2025-06-16 |             [Github](https://github.com/ictnlp/Stream-Omni)              |
| [**Ming-Omni: A Unified Multimodal Model for Perception and Generation**](https://arxiv.org/abs/2506.09344) &nbsp; ![Star](https://img.shields.io/github/stars/inclusionAI/Ming)                                                                                                                                                             | 2025-06-11 |             [Github](https://github.com/inclusionAI/Ming)                |
| [**Step-Audio-AQAA: a Fully End-to-End Expressive Large Audio Language Model**](https://arxiv.org/abs/2506.08967)                                                                                                                                                                                                                            | 2025-06-10 | [HF](https://huggingface.co/stepfun-ai/Step-Audio-AQAA) |
| [**VITA-Audio: Fast Interleaved Cross-Modal Token Generation for Efficient Large Speech-Language Model**](https://arxiv.org/abs/2505.03739) &nbsp; ![Star](https://img.shields.io/github/stars/VITA-MLLM/VITA-Audio)                                                                                                                         | 2025-05-06 |             [Github](https://github.com/VITA-MLLM/VITA-Audio)            |
| [**LLaMA-Omni2: LLM-based Real-time Spoken Chatbot with Autoregressive Streaming Speech Synthesis**](https://arxiv.org/abs/2505.02625) &nbsp; ![Star](https://img.shields.io/github/stars/ictnlp/LLaMA-Omni2)                                                                                                                                | 2025-05-05 |             [Github](https://github.com/ictnlp/LLaMA-Omni2)              |
| [**Voila: Voice-Language Foundation Models for Real-Time Autonomous Interaction and Voice Role-Play**](https://arxiv.org/abs/2505.02707) &nbsp; ![Star](https://img.shields.io/github/stars/maitrix-org/Voila)                                                                                                                               | 2025-05-05 |             [Github](https://github.com/maitrix-org/Voila)               |
| [**Kimi-Audio Technical Report**](https://arxiv.org/abs/2504.18425) &nbsp; ![Star](https://img.shields.io/github/stars/MoonshotAI/Kimi-Audio)                                                                                                                                                                                                | 2025-04-25 |             [Github](https://github.com/MoonshotAI/Kimi-Audio)           |
| [**Qwen2.5-Omni Technical Report**](https://arxiv.org/abs/2503.20215) &nbsp; ![Star](https://img.shields.io/github/stars/QwenLM/Qwen2.5-Omni)                                                                                                                                                                                                | 2025-03-26 |             [Github](https://github.com/QwenLM/Qwen2.5-Omni)             |
| [**Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs**](https://arxiv.org/abs/2503.01743)                                                                                                                                                                                                    | 2025-03-03 |     [HF](https://huggingface.co/microsoft/Phi-4-multimodal-instruct)     |
| [**Nexus-O: An Omni-Perceptive And -Interactive Model for Language, Audio, And Vision**](https://arxiv.org/abs/2503.01879)                                                                                                                                                                                                                   | 2025-02-26 | [HF](https://huggingface.co/HiThink-Research/NEXUS-O) |
| [**M2-omni: Advancing Omni-MLLM for Comprehensive Modality Support with Competitive Performance**](https://arxiv.org/abs/2502.18778) &nbsp; ![Star](https://img.shields.io/github/stars/alipay/Ant-Multi-Modal-Framework) | 2025-02-26 | [Github](https://github.com/alipay/Ant-Multi-Modal-Framework/tree/main/prj/M2_omni) |
| [**Baichuan-Audio: A Unified Framework for End-to-End Speech Interaction**](https://arxiv.org/abs/2502.17239) &nbsp; ![Star](https://img.shields.io/github/stars/baichuan-inc/Baichuan-Audio)                                                                                                                                                | 2025-02-24 |         [Github](https://github.com/baichuan-inc/Baichuan-Audio)         |
| [**LLM-Enhanced Dialogue Management for Full-Duplex Spoken Dialogue Systems**](https://arxiv.org/abs/2502.14145) &nbsp; ![Star](https://img.shields.io/github/stars/HaoZhang6720/fullduplex-dialogue-data) | 2025-02-19 | [Github](https://github.com/HaoZhang6720/fullduplex-dialogue-data) (data pipeline) |
| [**FlexDuo: A Pluggable System for Enabling Full-Duplex Capabilities in Speech Dialogue Systems**](https://arxiv.org/abs/2502.13472)                                                                                                                                                                                                         | 2025-02-19 |                                    --                                    |
| [**Step-Audio: Unified Understanding and Generation in Intelligent Speech Interaction**](https://arxiv.org/abs/2502.11946) &nbsp; ![Star](https://img.shields.io/github/stars/stepfun-ai/Step-Audio)                                                                                                                                         | 2025-02-17 |            [Github](https://github.com/stepfun-ai/Step-Audio)            |
| [**DuplexMamba: Enhancing Real-time Speech Conversations with Duplex and Streaming Capabilities**](https://arxiv.org/abs/2502.11123) &nbsp; ![Star](https://img.shields.io/github/stars/khfs/DuplexMamba)                                                                                                                                    | 2025-02-16 |              [Github](https://github.com/khfs/DuplexMamba)               |
| [**Ola: Pushing the Frontiers of Omni-Modal Language Model with Progressive Modality Alignment**](https://arxiv.org/abs/2502.04328) &nbsp; ![Star](https://img.shields.io/github/stars/Ola-Omni/Ola)                                                                                                                                         | 2025-02-06 |                [Github](https://github.com/Ola-Omni/Ola)                 |
| [**SpeechGPT 2.0-preview**](https://www.open-moss.com/en/speechgpt2-preview/) &nbsp; ![Star](https://img.shields.io/github/stars/OpenMOSS/SpeechGPT-2.0-preview)                                                                                                                                                                             | 2025-01-26 |       [Github](https://github.com/OpenMOSS/SpeechGPT-2.0-preview)        |
| [**Baichuan-Omni-1.5 Technical Report**](https://arxiv.org/abs/2501.15368) &nbsp; ![Star](https://img.shields.io/github/stars/baichuan-inc/Baichuan-Omni-1.5)                                                                                                                                                                                | 2025-01-26 |       [Github](https://github.com/baichuan-inc/Baichuan-Omni-1.5)        |
| [**MiniCPM-o 2.6: A GPT-4o Level MLLM for Vision, Speech, and Multimodal Live Streaming on Your Phone**](https://openbmb.notion.site/MiniCPM-o-2-6-A-GPT-4o-Level-MLLM-for-Vision-Speech-and-Multimodal-Live-Streaming-on-Your-Phone-185ede1b7a558042b5d5e45e6b237da9) &nbsp; ![Star](https://img.shields.io/github/stars/OpenBMB/MiniCPM-o) | 2025-01-24 |              [Github](https://github.com/OpenBMB/MiniCPM-o)              |
| [**MinMo: A Multimodal Large Language Model for Seamless Voice Interaction**](https://arxiv.org/abs/2501.06282)                                                                                                                                                                                                                              | 2025-01-10 |                                    --                                    |
| [**OpenOmni: Large Language Models Pivot Zero-shot Omnimodal Alignment across Language with Real-time Self-Aware Emotional Speech Synthesis**](https://arxiv.org/abs/2501.04561) &nbsp; ![Star](https://img.shields.io/github/stars/RainBowLuoCS/OpenOmni.svg?style=social&label=Star)                                                       | 2025-01-08 |            [Github](https://github.com/RainBowLuoCS/OpenOmni)            |
| [**VITA-1.5: Towards GPT-4o Level Real-Time Vision and Speech Interaction**](https://arxiv.org/abs/2501.01957v1) &nbsp; ![Star](https://img.shields.io/github/stars/VITA-MLLM/VITA.svg?style=social&label=Star)                                                                                                                              | 2025-01-03 |               [Github](https://github.com/VITA-MLLM/VITA)                |
| [**OmniChat: Enhancing Spoken Dialogue Systems with Scalable Synthetic Data for Diverse Scenarios**](https://arxiv.org/abs/2501.01384)                                                                                                                                                                                                       | 2025-01-02 |                                    --                                    |
| [**SLAM-Omni: Timbre-Controllable Voice Interaction System with Single-Stage Training**](https://arxiv.org/abs/2412.15649) &nbsp; ![Star](https://img.shields.io/github/stars/X-LANCE/SLAM-LLM.svg?style=social&label=Star)                                                                                                                  | 2024-12-20 |              [Github](https://github.com/X-LANCE/SLAM-LLM)               |
| [**MERaLiON-AudioLLM: Bridging Audio and Language with Large Language Models**](https://arxiv.org/abs/2412.09818)                                                                                                                                                                                                                            | 2024-12-13 | [HF](https://huggingface.co/MERaLiON/MERaLiON-AudioLLM-Whisper-SEA-LION) |
| [**Lyra: An Efficient and Speech-Centric Framework for Omni-Cognition**](https://arxiv.org/abs/2412.09501v1) &nbsp; ![Star](https://img.shields.io/github/stars/dvlab-research/Lyra.svg?style=social&label=Star)                                                                                                                             | 2024-12-12 |             [Github](https://github.com/dvlab-research/Lyra)             |
| [**Continuous Speech Tokens Makes LLMs Robust Multi-Modality Learners**](https://arxiv.org/abs/2412.04917)                                                                                                                                                                                                                                   | 2024-12-06 |                                    --                                    |
| [**GLM-4-Voice: Towards Intelligent and Human-Like End-to-End Spoken Chatbot**](https://arxiv.org/abs/2412.02612) &nbsp; ![Star](https://img.shields.io/github/stars/THUDM/GLM-4-Voice.svg?style=social&label=Star)                                                                                                                          | 2024-12-03 |              [Github](https://github.com/THUDM/GLM-4-Voice)              |
| [**Advancing Speech Language Models by Scaling Supervised Fine-Tuning with Over 60,000 Hours of Synthetic Speech Dialogue Data**](https://arxiv.org/abs/2412.01078)                                                                                                                                                                          | 2024-12-02 |                                    --                                    |
| [**SALMONN-omni: A Codec-free LLM for Full-duplex Speech Understanding and Generation**](https://arxiv.org/abs/2411.18138)                                                                                                                                                                                                                   | 2024-11-27 |                                    --                                    |
| [**Ultravox: An Open-Weight Alternative to GPT-4o Realtime**](https://www.ultravox.ai/blog/ultravox-an-open-weight-alternative-to-gpt-4o-realtime) &nbsp; ![Star](https://img.shields.io/github/stars/fixie-ai/ultravox.svg?style=social&label=Star)                                                                                         | 2024-11-12 |              [Github](https://github.com/fixie-ai/ultravox)              |
| [**Freeze-Omni: A Smart and Low Latency Speech-to-speech Dialogue Model with Frozen LLM**](https://arxiv.org/abs/2411.00774) &nbsp; ![Star](https://img.shields.io/github/stars/VITA-MLLM/Freeze-Omni.svg?style=social&label=Star)                                                                                                           | 2024-11-01 |            [Github](https://github.com/VITA-MLLM/Freeze-Omni)            |
| [**OmniFlatten: An End-to-end GPT Model for Seamless Voice Conversation**](https://arxiv.org/abs/2410.17799)                                                                                                                                                                                                                                 | 2024-10-23 |                                    --                                    |
| [**Ichigo: Mixed-Modal Early-Fusion Realtime Voice Assistant**](https://arxiv.org/abs/2410.15316)       &nbsp; ![Star](https://img.shields.io/github/stars/janhq/ichigo.svg?style=social&label=Star)                                                                                                                                         | 2024-10-20 |                [Github](https://github.com/janhq/ichigo)                 |
| [**Mini-Omni2: Towards Open-source GPT-4o with Vision, Speech and Duplex Capabilities**](https://arxiv.org/abs/2410.11190) &nbsp; ![Star](https://img.shields.io/github/stars/gpt-omni/mini-omni2.svg?style=social&label=Star)                                                                                                               | 2024-10-15 |             [Github](https://github.com/gpt-omni/mini-omni2)             |
| [**Baichuan-Omni Technical Report**](https://arxiv.org/abs/2410.08565)                                                                                                                                                                                                                                                                       | 2024-10-11 |                                    --                                    |
| [**IntrinsicVoice: Empowering LLMs with Intrinsic Real-time Voice Interaction Abilities**](https://arxiv.org/abs/2410.08035)                                                                                                                                                                                                                 | 2024-10-09 |                                    --                                    |
| [**Distilling an End-to-End Voice Assistant Without Instruction Training Data**](https://arxiv.org/abs/2410.02678) &nbsp; ![Star](https://img.shields.io/github/stars/Helw150/levanter) | 2024-10-03 | [Github](https://github.com/Helw150/levanter/blob/will/distill/src/levanter/models/via.py) |
| [**EMOVA: Empowering Language Models to See, Hear and Speak with Vivid Emotions**](https://arxiv.org/abs/2409.18042) &nbsp; ![Star](https://img.shields.io/github/stars/emova-ollm/EMOVA) | 2024-09-26 | [Github](https://github.com/emova-ollm/EMOVA) |
| [**Moshi: a Speech-Text Foundation Model for Real-Time Dialogue**](https://arxiv.org/abs/2410.00037) &nbsp; ![Star](https://img.shields.io/github/stars/kyutai-labs/moshi.svg?style=social&label=Star)                                                                                                                                       | 2024-09-17 |              [Github](https://github.com/kyutai-labs/moshi)              |
| [**LLaMA-Omni: Seamless Speech Interaction with Large Language Models**](https://arxiv.org/abs/2409.06666) &nbsp; ![Star](https://img.shields.io/github/stars/ictnlp/LLaMA-Omni.svg?style=social&label=Star)                                                                                                                                 | 2024-09-10 |              [Github](https://github.com/ictnlp/LLaMA-Omni)              |
| [**Mini-Omni: Language Models Can Hear, Talk While Thinking in Streaming**](https://arxiv.org/abs/2408.16725) &nbsp; ![Star](https://img.shields.io/github/stars/gpt-omni/mini-omni.svg?style=social&label=Star)                                                                                                                             | 2024-08-29 |             [Github](https://github.com/gpt-omni/mini-omni)              |
| [**VITA: Towards Open-Source Interactive Omni Multimodal LLM**](https://arxiv.org/abs/2408.05211) &nbsp; ![Star](https://img.shields.io/github/stars/VITA-MLLM/VITA.svg?style=social&label=Star)                                                                                                                                             | 2024-08-09 |               [Github](https://github.com/VITA-MLLM/VITA)                |
| [**Qwen2-Audio Technical Report**](https://arxiv.org/abs/2407.10759) &nbsp; ![Star](https://img.shields.io/github/stars/QwenLM/Qwen2-Audio.svg?style=social&label=Star)                                                                                                                                                                      | 2024-07-15 |             [Github](https://github.com/QwenLM/Qwen2-Audio)              |
| [**PSLM: Parallel Generation of Text and Speech with LLMs for Low-Latency Spoken Dialogue Systems**](https://arxiv.org/abs/2406.12428)                                                                                                                                                                                                       | 2024-06-18 |                                    --                                    |
| [**LLaSM: Large Language and Speech Model**](https://arxiv.org/abs/2308.15930) &nbsp; ![Star](https://img.shields.io/github/stars/LinkSoul-AI/LLaSM.svg?style=social&label=Star)                                                                                                                                                             | 2023-08-30 |              [Github](https://github.com/LinkSoul-AI/LLaSM)              |


## Citation
If you use the VoiceBench in your research, please cite the following paper:
```
@article{chen2024voicebench,
  title={VoiceBench: Benchmarking LLM-Based Voice Assistants},
  author={Chen, Yiming and Yue, Xianghu and Zhang, Chen and Gao, Xiaoxue and Tan, Robby T. and Li, Haizhou},
  journal={arXiv preprint arXiv:2410.17196},
  year={2024}
}
```
