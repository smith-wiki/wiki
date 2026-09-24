---
title: Laya-MLX source repository
summary: Independent Apple Silicon MLX inference port with local parity checks and hardware-specific latency runs.
url: https://raw.githubusercontent.com/mizorewww/laya-mlx/0a859518634112655cb97c745dbf04f5191aaf13/README.md
author: mizorewww and Laya-MLX contributors
kind: repository
retrieved: 2026-09-23T12:53:31Z
sha256: "e09c88ac8f49dac2d8305bac7ec124266d466c969a40d0e0e3e76c10fd65feed"
---

## Overview

The pinned [Laya-MLX](../../entities/laya-mlx/) repository reimplements ConvAI Innovations' [Laya](../../entities/laya/) inference on Apple Silicon using MLX. Its contributors provide conversion and inference code, preconverted weights, a Python API and router, and measured parity against pinned upstream PyTorch checkpoints. It is an independent port, not a new model or an official ConvAI release; training and fine-tuning remain upstream. Its BENCHMARKS file discloses the M3 Max machine, warmups, synchronization, excluded load time, prompt fixtures, precision differences, and raw results. The README's headline 13.42/7.39 ms for one short question is stale relative to its own current benchmark table's 17.75/10.91 ms; report the measured configuration, not a timeless speed guarantee.

## Key points

- The port supports all three upstream checkpoints and preserves question formatting, weights, schema, calibration, and routing; it does not implement training. (`README.md`, "Supported checkpoints")
- Its FP32/FP16 tests match upstream selected answers on 63/63 questions per checkpoint and precision; this is limited parity testing, not proof of task accuracy. (`BENCHMARKS.md`, "Numerical parity and stability")
- Current M3 Max FP16 table reports 17.75 ms English and 10.91 ms multilingual P50 on short, single-question requests; full-context requests take longer. (`BENCHMARKS.md`, "End-to-end short input latency", "Full-context latency")
- The README still advertises 13.42 ms and 7.39 ms, numbers inconsistent with its pinned BENCHMARKS table. (`README.md`, "Performance on M3 Max"; `BENCHMARKS.md`, "End-to-end short input latency")
- Results exclude weight load/download, use 50 timed iterations after five warmups, and batch-size 64 for the 50-question run versus a public default of 16. (`BENCHMARKS.md`, "Method")
- Precision can move probabilities without changing the selected answer; the shipped `choice:11+` temperature is clamped to prevent exaggerated certainty. (`README.md`, "Python API"; `BENCHMARKS.md`, "Numerical parity and stability")
