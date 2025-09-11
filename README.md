<div align="center">
    <h1>
    SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding
    </h1>
    <p>
    <!-- 若有logo可添加：<img src="path/to/logo.png" alt="SynParaSpeech Logo" width="300"> -->
    </p>
    <a href="#" ><img src="https://img.shields.io/badge/Paper-Coming%20Soon-orange" alt="Paper"></a>
    <a href="https://shawnpi233.github.io/SynParaSpeech"><img src="https://img.shields.io/badge/Demos-🌐-blue" alt="Demos"></a>
    <a href="https://github.com/ShawnPi233/SynParaSpeech"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Dataset%20Access-Download-purple" alt="Dataset Access"></a>
    <a href="README_zh.md"><img src="https://img.shields.io/badge/语言-简体中文-green" alt="简体中文"></a>
    <a href="#"><img src="https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg" alt="License"></a>
</div>
SynParaSpeech is the first automated framework for constructing large-scale paralinguistic datasets, enabling more realistic speech synthesis and robust speech understanding. It addresses critical gaps in existing resources by generating high-quality data with paralinguistic sounds (e.g., laughter, coughing) that are aligned with speech, text, and precise timestamps.

Unlike traditional datasets limited by privacy, incomplete annotations, or poor realism, **SynParaSpeech** unifies:
- 🤖 Automated synthesis of paralinguistic speech-text pairs
- 🌐 Multilingual coverage (Chinese and Japanese)
- ⏱️ Precise timestamp annotations for event localization
- 📊 Support for both paralinguistic TTS and event detection tasks


## ✨ Highlights

- 🚀 **First automated pipeline** for large-scale paralinguistic dataset synthesis, eliminating reliance on manual annotation.  
- 🌍 Covers **Chinese and Japanese** with 6 fine-grained paralinguistic categories (e.g., laughter, sigh, throat clearing).  
- 🎧 **120 hours of data** with 100k clips, including precise timestamp annotations for paralinguistic events.  
- 🎤 Enhances TTS models (CosyVoice2, F5-TTS) via fine-tuning for more natural paralinguistic speech generation.  
- 🔍 Improves paralinguistic event detection (Gemini 2.5 Pro, Qwen 2.5 Omni, Kimi Audio) through prompt tuning.  


## 📊 Pipeline Overview

![SynParaSpeech Pipeline](statics/figs/synparaspeech.png)  
*The pipeline includes 5 stages: labeled text synthesis, audio synthesis, manual verification, paralinguistic speech generation, and paralinguistic speech understanding.*


## 🗞 News

- **[2026-09-17]** 🎉 Initial release of SynParaSpeech:
  - 📄 Paper submitted to ICASSP 2026
  - 🎧 [Dataset & audio samples](https://github.com/ShawnPi233/SynParaSpeech)
  - 📊 Benchmark results for TTS and event detection tasks

### 📅 Release Plan

* ✅ SynParaSpeech dataset (120 hours, Chinese/Japanese)
* ✅ Audio samples with paralinguistic annotations
* [ ] Fine-tuned TTS model checkpoints (CosyVoice2-SFT, F5-TTS-SFT)
* [ ] Prompt tuning code for paralinguistic event detection


## 📦 Dataset

### 📌 SynParaSpeech Details

| Feature                | Specification                                                                 |
|------------------------|-------------------------------------------------------------------------------|
| Total Duration         | 120 hours                                                                     |
| Number of Clips        | 100k                                                                          |
| Languages              | Chinese, Japanese                                                            |
| Paralinguistic Categories | 6 (e.g., laughter, sigh, throat clearing, gasp, tsk)                        |
| Annotations            | Precise timestamps for paralinguistic events, aligned with speech and text    |
| Synthesis Method       | Automated integration of paralinguistic audio and speech via voice conversion |


## 🔍 Key Capabilities

### 🔊 Paralinguistic TTS
Fine-tuning state-of-the-art TTS models (CosyVoice2, F5-TTS) with SynParaSpeech significantly improves:
- Naturalness of paralinguistic sound integration
- Timbre consistency between speech and paralinguistic cues
- Alignment of generated audio with text timestamps

Example input-output:
```text
Input Text:  "这电影, [laugh] 太有趣了!"
Output Audio: [Speech with natural laughter inserted at the annotated position]
```

### 🎯 Paralinguistic Event Detection
Prompt tuning with SynParaSpeech enhances models' ability to:
- Detect paralinguistic events (accuracy, F1 score)
- Localize events in time (mean absolute error)
- Generalize across Chinese and Japanese


## 📜 Citation

If you use SynParaSpeech, please cite:

```bibtex
@inproceedings{bai2026synparaspeech,
  title     = {SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding},
  author    = {Bingsong Bai and Qihang Lu and Zihan Sun and Songbai Pu and Wenbing Yang and Yingming Gao and Ya Li and Jun Gao},
  booktitle = {ICASSP 2026-2026 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  year      = {2026},
  organization = {IEEE}
}
```


## 🙏 Acknowledgement
We thank the open-source communities behind [CosyVoice](https://github.com/FunAudioLLM/CosyVoice), [Whisper](https://github.com/openai/whisper), and [SeedVC](https://arxiv.org/abs/2411.09943) for their foundational tools.


## 🪪 License

The dataset and code are licensed under **CC BY 4.0** to encourage open research and collaboration.
