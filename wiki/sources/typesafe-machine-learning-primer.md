---
title: TypeSafe AI machine learning primer
summary: TypeSafe AI's case for training decision models with RLCD, and what it means by calibrated probabilities.
url: https://docs.typesafe.ai/introduction/machine-learning-primer
author: TypeSafe AI
publisher: TypeSafe AI
kind: documentation
retrieved: 2026-09-23T14:53:08Z
sha256: "b4bc6fd7a4b3ad529b3020c01e61a556a4306d72fcae7b0d561731d798a141b9"
---

## Overview

TypeSafe AI's machine learning primer explains why the company trains [Jev](../../entities/jev/) differently from chat models. It argues that automation will be mostly machine-to-machine, contrasts reinforcement learning from human feedback (RLHF) and with verifiable rewards (RLVR) with its own reinforcement learning for calibrated decisions (RLCD), and defines calibration as a property of groups of predictions. It is first-party positioning written for developers and prospective customers: authoritative for the company's stated optimization goal, not evidence of how training is implemented, and it names no model backbone, dataset, or update algorithm. The interface that this training targets is described in the [TypeSafe AI System One guide](../typesafe-system-one-documentation/).

## Key points

- TypeSafe calls its training path RLCD and contrasts a decision and probability objective with generative RLHF and RLVR. ("Three post-training approaches")
- Under RLCD the model returns decisions and probabilities instead of generated text, and higher probability should mean a higher chance of being correct. ("RLCD and calibrated decisions")
- Calibration means group frequencies should track assigned probabilities, not that each individual answer is guaranteed correct. ("RLCD and calibrated decisions": "These rates describe groups of predictions")
- The page argues that preference optimization rewards sycophancy and narrows outputs through mode dropping. ("The problems with RLHF")
- The page names no model backbone, dataset, or training algorithm for RLCD. (Entire page)
