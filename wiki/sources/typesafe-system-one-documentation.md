---
title: TypeSafe AI System One and AI primer
summary: Official account of Jev's typed decision interface and RLCD goal, without an implementation disclosure.
url: https://docs.typesafe.ai/concepts/system-one
author: TypeSafe AI
publisher: TypeSafe AI
kind: documentation
captures:
  - retrieved: 2026-09-23T14:52:47Z
    sha256: "a5deb2f825347ecc1a98b785fbb8423c24e371821fbe6dbc7c04bc150c91a293"
    type: text/html
  - retrieved: 2026-09-23T14:53:08Z
    sha256: "b4bc6fd7a4b3ad529b3020c01e61a556a4306d72fcae7b0d561731d798a141b9"
    type: text/html
    url: https://docs.typesafe.ai/introduction/machine-learning-primer
---

## Overview

TypeSafe AI's System One guide and AI primer explain the public contract of [Jev](../../entities/jev/) for software developers. The model takes text or structured text state plus predefined questions and returns bounded choices, scores, or boolean probabilities rather than prose. The primer calls the company's training approach reinforcement learning for calibrated decisions (RLCD) and describes calibration as a property of groups of predictions. These first-party pages are authoritative for the exposed interface and the company's stated optimization goal. They do not identify Jev's backbone, parameter count, token-level representation, decision-head topology, weights, or training implementation, so they cannot establish architectural identity with open-weight [Laya](../../entities/laya/). Shared terminology is weaker evidence than a disclosed implementation.

## Key points

- Jev is TypeSafe AI's flagship System One model; it accepts state and emits typed decisions and probabilities through `choice`, `score`, and `noul`. (`concepts/system-one`, opening and "How it differs from an LLM")
- Inputs are text, JSON objects, or arrays of text; the model does not accept image, audio, or video directly. (`concepts/system-one`, opening note)
- Applications can ask several independent questions and combine answers with deterministic checks. (`concepts/system-one`, "Fast judgments inside a larger workflow")
- TypeSafe calls its training path RLCD, contrasting a decision/probability objective with generative RLHF and RLVR. (`introduction/machine-learning-primer`, "Three post-training approaches" and "RLCD")
- Calibration means group frequencies should track assigned probabilities, not that each individual answer is guaranteed correct. (`introduction/machine-learning-primer`, "RLCD and calibrated decisions")
- Neither captured page identifies Jev's encoder, parameter count, decision-head implementation, or trainable weights. (`concepts/system-one`, entire page; `introduction/machine-learning-primer`, entire page)
