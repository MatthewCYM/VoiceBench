# VoiceBench

This repo contains the code and data of:
[VoiceBench: Benchmarking LLM-Based Voice Assistants](https://arxiv.org/abs/2410.17196)

## News
* **`2025.04.20`** Released `wildvoice`, a crowd-sourced dataset comprising human-recorded speech with diverse accents.
* **`2025.04.12`** Released `bbh`, a crowd-sourced dataset comprising human-recorded speech, for evaluating the reasoning ability of voice assistants. 
* **`2024.12.11`** Updated the VoiceBench Leaderboard to include `mmsu`.
* **`2024.12.10`** Added a curated list of awesome voice assistants.
* **`2024.11.24`** Expanded the test samples in VoiceBench to include `mmsu`, covering 12 diverse domains from `mmlu-pro`.
* **`2024.11.12`** Updated the VoiceBench Leaderboard to include: 1) Mini-Omni2, GPT-4o-Audio, and Whisper-v3+GPT-4o, and 2) multiple-choice QA from OpenBookQA.
* **`2024.10.30`** Expanded the test samples in VoiceBench to include: 1) the complete set of open-ended QA from `alpacaeval`, and 2) multiple-choice QA from `openbookqa`.

## Table of Contents
- [**Leaderboard**](#leaderboard)
- [**Setup**](#setup)
- [**Dataset**](#dataset)
- [**Evaluation**](#evaluation)
- [**Awesome Voice Assistants**](#awesome-voice-assistants)
- [**Citation**](#citation)

## Leaderboard

| Rank | Model                         | AlpacaEval | CommonEval | WildVoice | SD-QA | MMSU  | OBQA  |  BBH  | IFEval | AdvBench | Overall |
|:----:|-------------------------------|:----------:|:----------:|:---------:|:-----:|:-----:|:-----:|:-----:|:------:|:--------:|:-------:|
|  1   | Whisper-v3-large+GPT-4o       |    4.80    |    4.47    |   4.62    | 75.77 | 81.69 | 92.97 | 87.20 | 76.51  |  98.27   |  87.80  |
|  2   | GPT-4o-Audio                  |    4.78    |    4.49    |   4.58    | 75.50 | 80.25 | 89.23 | 84.10 | 76.02  |  98.65   |  86.75  |
|  3   | GPT-4o-mini-Audio             |    4.75    |    4.24    |   4.40    | 67.36 | 72.90 | 84.84 | 81.50 | 72.90  |  98.27   |  82.84  |
|  4   | Whisper-v3-large+LLaMA-3.1-8B |    4.53    |    4.04    |   4.16    | 70.43 | 62.43 | 72.53 | 69.70 | 69.53  |  98.08   |  77.48  |
|  5   | Kimi-Audio                    |    4.46    |    3.97    |   4.20    | 63.12 | 62.17 | 83.52 | 69.70 | 61.10  |  100.00  |  76.91  |
|  6   | Whisper-v3-turbo+LLaMA-3.1-8B |    4.55    |    4.02    |   4.12    | 58.23 | 62.04 | 72.09 | 69.10 | 71.12  |  98.46   |  76.09  |
|  7   | Ultravox-v0.5-LLaMA-3.1-8B    |    4.59    |    4.11    |   4.28    | 58.68 | 54.16 | 68.35 | 67.80 | 66.51  |  98.65   |  74.86  |
|  8   | Ultravox-v0.4.1-LLaMA-3.1-8B  |    4.55    |    3.90    |   4.12    | 53.35 | 47.17 | 65.27 | 66.30 | 66.88  |  98.46   |  72.09  |
|  9   | Baichuan-Omni-1.5             |    4.50    |    4.05    |   4.06    | 43.40 | 57.25 | 74.51 | 62.70 | 54.54  |  97.31   |  71.32  |
|  10  | MiniCPM-o                     |    4.42    |    4.15    |   3.94    | 50.72 | 54.78 | 78.02 | 60.40 | 49.25  |  97.69   |  71.23  |
|  11  | Whisper-v3-turbo+LLaMA-3.2-3B |    4.45    |    3.82    |   4.04    | 49.28 | 51.37 | 60.66 | 63.90 | 69.71  |  98.08   |  71.02  |
|  12  | Baichuan-Audio                |    4.41    |    4.08    |   3.92    | 45.84 | 53.19 | 71.65 | 54.80 | 50.31  |  99.42   |  69.27  |
|  13  | MERaLiON                      |    4.50    |    3.77    |   4.12    | 55.06 | 34.95 | 27.23 | 62.60 | 62.93  |  94.81   |  65.04  |
|  14  | VITA-1.5                      |    4.21    |    3.66    |   3.48    | 38.88 | 52.15 | 71.65 | 55.30 | 38.14  |  97.69   |  64.53  |
|  15  | Phi-4-multimodal              |    3.81    |    3.82    |   3.56    | 39.78 | 42.19 | 65.93 | 61.80 | 45.35  |  100.00  |  64.32  |
|  16  | Ola                           |    4.12    |    2.97    |   3.19    | 33.82 | 45.97 | 67.91 | 51.10 | 39.57  |  90.77   |  59.42  |
|  17  | Lyra-Base                     |    3.85    |    3.50    |   3.42    | 38.25 | 49.74 | 72.75 | 59.00 | 36.28  |  59.62   |  59.00  |
|  18  | Ultravox-v0.5-LLaMA-3.2-1B    |    4.04    |    3.57    |   3.47    | 34.72 | 30.03 | 35.60 | 52.70 | 45.56  |  96.92   |  57.46  |
|  19  | DiVA                          |    3.67    |    3.54    |   3.74    | 57.05 | 25.76 | 25.49 | 51.80 | 39.15  |  98.27   |  57.39  |
|  20  | GLM-4-Voice                   |    3.97    |    3.42    |   3.18    | 36.98 | 39.75 | 53.41 | 52.80 | 25.92  |  88.08   |  56.48  |
|  21  | Qwen2-Audio                   |    3.74    |    3.43    |   3.01    | 35.71 | 35.72 | 49.45 | 54.70 | 26.33  |  96.73   |  55.80  |
|  22  | Freeze-Omni                   |    4.03    |    3.46    |   3.15    | 53.45 | 28.14 | 30.98 | 50.70 | 23.40  |  97.30   |  55.20  |
|  23  | Step-Audio                    |    4.13    |    3.09    |   2.93    | 44.21 | 28.33 | 33.85 | 50.60 | 27.96  |  69.62   |  50.84  |
|  24  | Megrez-3B-Omni                |    3.50    |    2.95    |   2.34    | 25.95 | 27.03 | 28.35 | 50.30 | 25.71  |  87.69   |  46.76  |
|  25  | Ichigo                        |    3.79    |    3.17    |   2.83    | 36.53 | 25.63 | 26.59 | 46.50 | 21.59  |  57.50   |  45.57  |
|  26  | Lyra-Mini                     |    2.99    |    2.69    |   2.58    | 19.89 | 31.42 | 41.54 | 48.40 | 20.91  |  80.00   |  45.26  |
|  27  | LLaMA-Omni                    |    3.70    |    3.46    |   2.92    | 39.69 | 25.93 | 27.47 | 49.20 | 14.87  |  11.35   |  41.12  |
|  28  | VITA-1.0                      |    3.38    |    2.15    |   1.87    | 27.94 | 25.70 | 29.01 | 47.70 | 22.82  |  26.73   |  36.43  |
|  29  | SLAM-Omni                     |    1.90    |    1.79    |   1.60    | 4.16  | 26.06 | 25.27 | 48.80 | 13.38  |  94.23   |  35.30  |
|  30  | Mini-Omni2                    |    2.32    |    2.18    |   1.79    | 9.31  | 24.27 | 26.59 | 46.40 | 11.56  |  57.50   |  33.49  |
|  31  | Mini-Omni                     |    1.95    |    2.02    |   1.61    | 13.92 | 24.69 | 26.59 | 46.30 | 13.58  |  37.12   |  30.42  |
|  32  | Moshi                         |    2.01    |    1.60    |   1.30    | 15.64 | 24.04 | 25.93 | 47.40 | 10.12  |  44.23   |  29.51  |

[//]: # (|      | KE-Omni-v1.5                  |    3.82    |    3.20    | 31.20 | 32.27 |    58.46   |       |  15.00 |  100.00  |         |)



We encourage you to submit new voice assistant results directly through the issue tracker. The ranking list will be updated accordingly.

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
| [**VITA-Audio: Fast Interleaved Cross-Modal Token Generation for Efficient Large Speech-Language Model**](https://arxiv.org/abs/2505.03739) &nbsp; ![Star](https://img.shields.io/github/stars/VITA-MLLM/VITA-Audio)                                                                                                                         | 2025-05-06 |             [Github](https://github.com/VITA-MLLM/VITA-Audio)            |
| [**LLaMA-Omni2: LLM-based Real-time Spoken Chatbot with Autoregressive Streaming Speech Synthesis**](https://arxiv.org/abs/2505.02625) &nbsp; ![Star](https://img.shields.io/github/stars/ictnlp/LLaMA-Omni2)                                                                                                                                | 2025-05-05 |             [Github](https://github.com/ictnlp/LLaMA-Omni2)              |
| [**Voila: Voice-Language Foundation Models for Real-Time Autonomous Interaction and Voice Role-Play**](https://arxiv.org/abs/2505.02707) &nbsp; ![Star](https://img.shields.io/github/stars/maitrix-org/Voila)                                                                                                                               | 2025-05-05 |             [Github](https://github.com/maitrix-org/Voila)               |
| [**Kimi-Audio Technical Report**](https://arxiv.org/abs/2504.18425) &nbsp; ![Star](https://img.shields.io/github/stars/MoonshotAI/Kimi-Audio)                                                                                                                                                                                                | 2025-04-25 |             [Github](https://github.com/MoonshotAI/Kimi-Audio)           |
| [**Qwen2.5-Omni Technical Report**](https://arxiv.org/abs/2503.20215) &nbsp; ![Star](https://img.shields.io/github/stars/QwenLM/Qwen2.5-Omni)                                                                                                                                                                                                | 2025-03-26 |             [Github](https://github.com/QwenLM/Qwen2.5-Omni)             |
| [**Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs**](https://arxiv.org/abs/2503.01743)                                                                                                                                                                                                    | 2025-03-03 |     [HF](https://huggingface.co/microsoft/Phi-4-multimodal-instruct)     |
| [**Nexus-O: An Omni-Perceptive And -Interactive Model for Language, Audio, And Vision**](https://arxiv.org/abs/2503.01879)                                                                                                                                                                                                                   | 2025-02-26 |                                    --                                    |
| [**M2-omni: Advancing Omni-MLLM for Comprehensive Modality Support with Competitive Performance**](https://arxiv.org/abs/2502.18778)                                                                                                                                                                                                         | 2025-02-26 |                                    --                                    |
| [**Baichuan-Audio: A Unified Framework for End-to-End Speech Interaction**](https://arxiv.org/abs/2502.17239) &nbsp; ![Star](https://img.shields.io/github/stars/baichuan-inc/Baichuan-Audio)                                                                                                                                                | 2025-02-24 |         [Github](https://github.com/baichuan-inc/Baichuan-Audio)         |
| [**LLM-Enhanced Dialogue Management for Full-Duplex Spoken Dialogue Systems**](https://arxiv.org/abs/2502.14145)                                                                                                                                                                                                                             | 2025-02-19 |                                    --                                    |
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
| [**Distilling an End-to-End Voice Assistant Without Instruction Training Data**](https://arxiv.org/abs/2410.02678)                                                                                                                                                                                                                           | 2024-10-03 |         [HF](https://huggingface.co/WillHeld/DiVA-llama-3-v0-8b)         |
| [**EMOVA: Empowering Language Models to See, Hear and Speak with Vivid Emotions**](https://arxiv.org/abs/2409.18042)                                                                                                                                                                                                                         | 2024-09-26 |                                    --                                    |
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
