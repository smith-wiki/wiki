---
title: "SalesRLAgent: A Reinforcement Learning Approach for Real-Time Sales Conversion Prediction and Optimization"
summary: March 2025 sales-conversion probability paper preceding the later general-purpose Laya and Jev launches.
url: https://arxiv.org/pdf/2503.23303v1
author: Nandakishor Mukkunnoth
publisher: arXiv
published: 2025-03-30
kind: paper
retrieved: 2026-09-24T13:32:04Z
sha256: "b4cd4e69184fd2f5c2d511f448ff224736776382787bf683ecd5aa17d273477e"
---

## Overview

Nandakishor Mukkunnoth submitted this preprint on March 30, 2025. Its abstract proposes a specialized reinforcement-learning system for predicting conversion probabilities over successive sales-conversation turns, trained on synthetic GPT-4o-generated data and using Azure OpenAI embeddings. The author reports faster inference and better prediction than an LLM-only approach. The captured paper establishes chronology and the narrower sales domain; its evaluation runs on the author's own synthetic conversations, so it is not independent validation of the reported performance or a complete architectural comparison. The later [Laya](../../entities/laya/) family handles request-defined typed questions across domains, while [Jev](../../entities/jev/) is another general-purpose typed-decision product. An earlier sales-conversion model does not by itself establish scientific priority for every feature or that Jev copied Laya.

## Key points

- The initial submission is dated March 30, 2025, before the September 2026 Jev and Laya announcements. (arXiv v1 date)
- The abstract describes turn-by-turn sales conversion prediction with reinforcement learning and synthetic GPT-4o training data, not the later general-purpose `choice`/`score`/`noul` interface. (Abstract)
- Reported accuracy, latency, and conversion-rate improvements are the author's own results on synthetic GPT-4o conversations, not an independent evaluation. (Abstract; III-A Dataset Construction; VI Results and Evaluation)
