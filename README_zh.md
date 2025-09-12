<div align="center">
    <h1>
    SynParaSpeech: 面向语音生成与理解的副语言数据集自动化构建方法
    </h1>
    <p>
    <!-- 若有logo可添加：<img src="path/to/logo.png" alt="SynParaSpeech Logo" width="300"> -->
    </p>
    <a href="https://arxiv.org/abs/2406.05692"><img src="https://img.shields.io/badge/arXiv-2406.05692-red?logo=arxiv&logoColor=white" alt="arXiv:2406.05692"></a>
    <a href="https://shawnpi233.github.io/SynParaSpeech"><img src="https://img.shields.io/badge/Demos-🌐-blue" alt="Demos"></a>
    <a href="https://huggingface.co/datasets/shawnpi/SynParaSpeech"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Dataset%20Access-Download-orange" alt="Dataset Access"></a>
    <a href="README_zh.md"><img src="https://img.shields.io/badge/Language-English-green" alt="简体中文"></a>
    <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img src="https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-blue.svg" alt="License: CC BY-NC-ND 4.0"></a>
</div>
SynParaSpeech是首个大规模副语言数据集自动化构建框架，可支持更逼真的语音合成与更鲁棒的语音理解研究。它通过生成高质量数据（包含笑声、咳嗽等副语言声音，并与语音、文本及精确时间戳对齐），解决了现有资源的关键缺陷。

与受限于隐私、标注不完整或真实性不足的传统数据集不同，**SynParaSpeech** 实现了多维度统一：
- 🤖 副语言语音-文本对的自动化合成
- 🌐 多语言覆盖（中文和日语）
- ⏱️ 用于事件定位的精确时间戳标注
- 📊 同时支持副语言TTS（文本到语音）和事件检测任务


## ✨ 核心亮点

- 🚀 **首个大规模副语言数据集自动化构建流程**，摆脱对人工标注的依赖。  
- 🌍 覆盖**中文和日语**，包含6个细粒度副语言类别（如笑声、叹息、清嗓子等）。  
- 🎧 **120小时数据量**，含10万条音频片段，每个副语言事件均配有精确时间戳标注。  
- 🎤 通过微调提升TTS模型（CosyVoice2、F5-TTS）的副语言语音生成自然度。  
- 🔍 通过提示调优增强副语言事件检测模型（Gemini 2.5 Pro、Qwen 2.5 Omni、Kimi Audio）的性能。  


## 📊 流程概述

![SynParaSpeech流程](statics/figs/synparaspeech.png)  
*流程包含5个阶段：带标签文本合成、音频合成、人工辅助验证、副语言语音生成、副语言语音理解。*


## 🗞 最新动态

- **[2026-09-17]** 🎉 SynParaSpeech首次发布：
  - 📄 论文已提交至ICASSP 2026
  - 🎧 [数据集及音频样本](https://github.com/ShawnPi233/SynParaSpeech)
  - 📊 TTS与事件检测任务的基准测试结果


### 📅 发布计划

* ✅ SynParaSpeech数据集（120小时，中文/日语）
* ✅ 带副语言标注的音频样本
* [ ] 微调后的TTS模型权重（CosyVoice2-SFT、F5-TTS-SFT）
* [ ] 副语言事件检测的提示调优代码


## 📦 数据集详情

### 📌 SynParaSpeech基本信息

| 特征                | 具体说明                                                                 |
|---------------------|--------------------------------------------------------------------------|
| 总时长              | 120小时                                                                   |
| 音频片段数量        | 10万条                                                                    |
| 支持语言            | 中文、日语                                                                |
| 副语言类别          | 6类（如笑声、叹息、清嗓子、喘气、啧啧声等）                              |
| 标注信息            | 副语言事件的精确时间戳，与语音和文本精准对齐                              |
| 合成方法            | 通过语音转换技术自动融合副语言音频与普通语音                              |


## 🔍 核心功能

### 🔊 副语言TTS
使用SynParaSpeech微调主流TTS模型（CosyVoice2、F5-TTS），显著提升以下性能：
- 副语言声音融入的自然度
- 语音与副语言声音的音色一致性
- 生成音频与文本时间戳的对齐精度

输入输出示例：
```text
输入文本：  "这电影, [laugh] 太有趣了!"
输出音频：  [在标注位置自然插入笑声的语音]
```

### 🎯 副语言事件检测
基于SynParaSpeech的提示调优可增强模型的以下能力：
- 副语言事件检测（准确率、F1分数）
- 事件时间定位（平均绝对误差）
- 跨中文和日语的泛化能力


## 📜 引用说明

如果使用SynParaSpeech，请引用以下文献：

```bibtex
@inproceedings{bai2026synparaspeech,
  title     = {SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding},
  author    = {Bingsong Bai and Qihang Lu and Zihan Sun and Songbai Pu and Wenbing Yang and Yingming Gao and Ya Li and Jun Gao},
  booktitle = {ICASSP 2026-2026 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  year      = {2026},
  organization = {IEEE}
}
```


## 🙏 致谢
感谢以下开源项目社区提供的基础工具支持：[CosyVoice](https://github.com/FunAudioLLM/CosyVoice)、[Whisper](https://github.com/openai/whisper)、[SeedVC](https://arxiv.org/abs/2411.09943)。


## 🪪 许可证

数据集及代码采用**CC BY 4.0**许可协议，旨在促进开放研究与合作。
