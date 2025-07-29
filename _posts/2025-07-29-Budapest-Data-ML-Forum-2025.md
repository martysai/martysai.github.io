---
permalink: /budapest-data-ml-forum/
header:
  overlay_color: "#333"
author_profile: true
toc: false
classes: wide
related: false
share: false
---

On June 18, I gave an online talk at the [Budapest Data+ML Forum](https://budapestdataml.com/en/). The event is a solid, mid-sized conference that draws practitioners from Central Europe; it is a good place to exchange technical expertise with other engineers. My session focused on Phi Silica, a small language model designed to run entirely on Copilot+ PC laptops, and on Rewrite, a publicly available paraphrasing tool built on top of the small language model.

![OPRO](/assets/budapest-data-ml-bears.jpg){: width="500" }

I covered a diverse set of approaches our team has applied for the model's optimization, including:
* [QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs](https://arxiv.org/abs/2404.00456). One of the best existing approaches toward outlier removal and subsequent quantization.
* [EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty](https://arxiv.org/abs/2401.15077). Speculative decoding that gave a throughput boost during Phi Silica generation.

More importantly, I focused on my personal contributions as well:
* [Rewrite](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica#text-intelligence-skills): a publicly available paraphrasing tool shipped with multiple tones.
* [Soft prompts](https://huggingface.co/docs/peft/en/conceptual_guides/prompting) and [LoRA](https://huggingface.co/docs/peft/en/package_reference/lora) adapters for quality improvements in Rewrite.

I'm pleased with the steady progress toward practical, small language models. If you're experimenting with on-device LMs on Copilot+ PCs, I’d love to compare benchmarks – feel free to reach out.
