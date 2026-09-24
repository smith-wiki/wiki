---
title: "Chonkie chunkers at commit 664454b"
summary: Pinned Chonkie docs and implementations describe neural separator prediction and SlumberChunker's LLM-guided recursive boundary choices, without retrieval-quality scores.
url: https://raw.githubusercontent.com/chonkie-inc/chonkie/664454b689d68614bcfc0b1d57fc2a28b5862825/README.md
author: Chonkie contributors
kind: repository
captures:
  - retrieved: 2026-09-24T09:01:33Z
    sha256: "d5109d089b2343e18b492e13fb98855a2d17b6acd6400e1934d95216468bc5f0"
    type: text/plain
  - retrieved: 2026-09-24T09:01:53Z
    sha256: "b0972763695b68956239aa8baef7b41728c1653fd86f824efdcdb2c747237e9f"
    type: text/plain
    url: https://raw.githubusercontent.com/chonkie-inc/chonkie/664454b689d68614bcfc0b1d57fc2a28b5862825/docs/oss/chunkers/slumber-chunker.mdx
  - retrieved: 2026-09-24T09:02:10Z
    sha256: "322a4f4e76e1ac9ec0566a914b01b40d30ef1db66278668d5ce33a8af4d30c80"
    type: text/plain
    url: https://raw.githubusercontent.com/chonkie-inc/chonkie/664454b689d68614bcfc0b1d57fc2a28b5862825/docs/oss/chunkers/neural-chunker.mdx
  - retrieved: 2026-09-24T09:04:03Z
    sha256: "5a828d905608705aa570e8435d62be255c728296491e1bdad92603442c35bc36"
    type: text/plain
    url: https://raw.githubusercontent.com/chonkie-inc/chonkie/664454b689d68614bcfc0b1d57fc2a28b5862825/src/chonkie/chunker/slumber.py
  - retrieved: 2026-09-24T09:04:37Z
    sha256: "f724cf0383f5454d74b81051a25a8c76dc57b853469ddde74ecb2d0f427d3d73"
    type: text/plain
    url: https://raw.githubusercontent.com/chonkie-inc/chonkie/664454b689d68614bcfc0b1d57fc2a28b5862825/src/chonkie/chunker/neural.py
---

## Overview

These pinned Chonkie README, documentation, and implementation files describe two boundary selectors rather than comparable measured retrieval systems. NeuralChunker uses a token-classification model to predict source-text separators. SlumberChunker first generates small recursive candidate pieces and asks a Genie-backed LLM which candidate starts a new topic, emitting contiguous original text. This source is useful for checking actual defaults, failure handling, and what "LLM-driven" means in this library. It is not an independently assessed quality study: docs use qualitative claims, and neither captured implementation supplies a query-to-passage benchmark. The docs also disagree with the pinned implementation about Slumber's default chunk size and Neural's default model, so reproduce results against a specified source commit and configuration. Compare Chroma's different GPT-4o splitter without transferring its score to Slumber; the upstream [web capture fidelity](../../concepts/web-capture-fidelity/) contract remains independent.

## Key points

- NeuralChunker predicts separator spans with a Hugging Face token-classification pipeline and returns slices of original text (src/chonkie/chunker/neural.py, `NeuralChunker`).
- Its source default is `mirth/chonky_distilbert_base_uncased_1`, while the accompanying neural docs show a ModernBERT default; supported models use different window strides (src/chonkie/chunker/neural.py, `DEFAULT_MODEL` and `SUPPORTED_MODEL_STRIDES`; docs/oss/chunkers/neural-chunker.mdx, usage).
- Slumber recursively generates candidate pieces of at most `candidate_size` before asking a Genie for a topic-shift split index; it outputs source slices rather than rewritten summaries (src/chonkie/chunker/slumber.py, `_recursive_split` and `chunk`).
- Pinned source defaults to `chunk_size=2048` with a character tokenizer and `candidate_size=128`; the accompanying docs show 1024 for the chunk size (src/chonkie/chunker/slumber.py, `__init__`; docs/oss/chunkers/slumber-chunker.mdx, usage).
- On exhausted extraction retries, Slumber logs a warning and keeps the candidate group together, a boundary-quality failure worth counting during evaluation (src/chonkie/chunker/slumber.py, `_get_split_index_json` and `_get_split_index_text`).
- No captured README, documentation, or implementations report a query-to-passage retrieval comparison for these two methods (README.md, Chunkers and Benchmarks; docs/oss/chunkers/neural-chunker.mdx; docs/oss/chunkers/slumber-chunker.mdx).
