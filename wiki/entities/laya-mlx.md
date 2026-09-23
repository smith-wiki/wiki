---
title: Laya-MLX
summary: Independent MLX inference port of Laya's published checkpoints for Apple Silicon.
---

[Laya-MLX](../../sources/laya-mlx-repository/) is an independent Apache-2.0 port of [Laya](../laya/) to Apple's MLX runtime. It reimplements inference and checkpoint conversion for all three upstream models and retains their question formatting, routing, weights, and output schema; it is not an official ConvAI release or a new trained model. Its Python API and CLI work on Apple Silicon; training and fine-tuning remain upstream. ([mizorewww and Laya-MLX contributors, n.d.](../../sources/laya-mlx-repository/))

## What its measurements show

On one M3 Max, the pinned benchmark table reports FP16 end-to-end median latency of 17.75 ms for one short English question and 10.91 ms for the multilingual checkpoint. The same repository's README still advertises older 13.42/7.39 ms figures: **Contradiction:** the current table does not reproduce the headline. Measurements include tokenization and synchronized inference but exclude model loading; long contexts are slower. The port matched upstream's selected answers on 63 of 63 validation questions per checkpoint and precision, not a representative proof of model accuracy. Default batching caps each forward pass at 16 questions. ([mizorewww and Laya-MLX contributors, n.d.](../../sources/laya-mlx-repository/))

**Inference:** Choose this port to run Laya locally on a supported Mac, not as evidence that Laya intrinsically outperforms hosted [Jev](../jev/): the MLX study compares two Laya runtimes, not Laya with Jev on the same hardware. ([mizorewww and Laya-MLX contributors, n.d.](../../sources/laya-mlx-repository/))
