---
title: "OpenTalks.AI 2026: Production-Ready Adapters for On-Device Language Models"
permalink: /opentalks-ai-2026/
pubDate: 2026-03-07
---

I spoke at [OpenTalks.AI](https://opentalks.ai/) in Belgrade, Serbia. My talk covered the end-to-end journey of building production-ready adapters for on-device language models, from tuning through evaluation to real-world shipping.

![OpenTalks.AI 2026](/assets/open-talks-ai-2026.jpg)

The session walked through several core areas:

* **Adapter tuning for on-device models.** How [LoRA](https://huggingface.co/docs/peft/en/package_reference/lora) adapters are used to specialize a small base model (Phi Silica) for distinct skills — each skill/flavor gets its own lightweight adapter on top of frozen base weights.
* **Shipping Rewrite and Summarize.** Practical lessons from taking these [Text Intelligence skills](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica#text-intelligence-skills) from prototype to production on Copilot+ PCs — including Rewrite with multiple tone flavors (Auto, Casual, Formal, Concise) and Summarize for condensing long-form content.
* **Windows App SDK availability.** These Text Intelligence capabilities are available through the [Windows App SDK](https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/), enabling any developer building apps for Copilot+ PCs to integrate on-device language skills directly into their applications.

![Text Intelligence Platform](/assets/open-talks-ai-2026-text-intelligence.jpg)

The Text Intelligence platform is designed so that new skills can be added by training new adapters without retraining the base model.

It was great connecting with the AI community in Belgrade and seeing how rich the advancements in Natural Language Processing in both academia and industry are in 2026.
