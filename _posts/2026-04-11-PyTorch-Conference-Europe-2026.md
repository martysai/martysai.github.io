---
title: "PyTorch Conference Europe 2026"
permalink: /pytorch-conference-europe-2026/
header:
  overlay_color: "#333"
author_profile: true
toc: false
classes: wide
related: false
share: false
---

I flew to Paris to attend [PyTorch Conference Europe](https://pytorch.org/event/pytorch-conference-europe/) as a listener. Two days focused on talks around open source and what's happening across the industry.

![PyTorch Conference Europe 2026](/assets/pytorchcon-europe-2026.jpg){: width="600" }

What surprised me: remarkably little hype around agents, but a lot of concrete, practical content. Key highlights below, in order.

**1. HuggingFace announced [Kernels Hub](https://huggingface.co/docs/kernels/index).** Why this matters: there are many accelerators, and for some of them certain attention implementations run fast while for others they're slow. Having a centralized hub of kernels means you don't have to write them from scratch every time. HF also promises to audit kernels for vulnerabilities to prevent remote code execution on the user's side.

**2. [ExecuTorch](https://executorch.ai/) is now part of PyTorch Core.** ExecuTorch matters because niche platforms and accelerators like NPUs exist, and sometimes you want to test open models on-device and compare against production offerings such as [Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica). You don't want to figure out how to compile a model for each specific platform (Qualcomm, Intel, etc.) — ExecuTorch does it for you. Integration with PyTorch Core means the Linux Foundation and Meta will jointly maintain the project, signaling a serious bet on edge AI and open infrastructure.

**3. Plenty of on-device talks.** I was surprised to realize that on-device ML is no longer niche. Over two days I attended more than five talks exclusively about edge AI. Use cases varied widely:
* *Meta* is embedding ultra-small models into their smart glasses and phones. Energy efficiency is critical, so these are not language models.
* *Google DeepMind* continues to invest in Gemma (v4 is impressive — on-device models now handle tool calling and search).
* *Intel and Qualcomm* are building their own deployment and optimization stacks for their platforms — potential synergies with Microsoft Applied Sciences, making connections with both teams very valuable.

**4. I met the developers of [Gemma 4 and Edge Gallery](https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/) for mobile devices.** Technically, these are our future direct competitors. Notably, they don't work with Apple at all — the much-discussed Google–Apple contract for building Apple Foundation Models and fixing Siri is a separate story, unrelated to Edge Gallery and Gemma.

**5. Mistral released [Voxtral Realtime](https://mistral.ai/news/voxtral-transcribe-2)** — a fast, high-quality on-device ASR with streaming support. This could be significant for many on-device scenarios, as voice input is becoming a trend in the edge world.

**6. On a personal note,** I got to meet the maintainers of HF Transformers and PEFT and pitch our feature requests for [PEFT](https://huggingface.co/docs/peft/en/index): there are several extensions on top of LoRA that we'd love to see upstream, but the process has been slow so far.

This was PyTorch's first conference in Europe, and I'm very grateful for that. The main takeaway for me: it's important to see what's happening across different corners of the industry — especially at Tier-1 companies.