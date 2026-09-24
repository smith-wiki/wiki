---
title: Model Checking TLA+ Specifications
summary: Original TLC paper explains finite model instantiation, reachable-state exploration, and error traces.
url: https://lamport.azurewebsites.net/pubs/yuanyu-model-checking.pdf
author: "Yuan Yu, Panagiotis Manolios, and Leslie Lamport"
publisher: "CHARME '99, LNCS 1703"
published: 1999-06-25
kind: paper
retrieved: 2026-09-23T09:00:17Z
sha256: "7d8713bb8793f08c9c26b08c3a87535b6c43cfd259295c09a91d01d1f1ba6210"
---

## Overview

Yuan Yu, Panagiotis Manolios, and Leslie Lamport's CHARME '99 paper introduces TLC, the model checker for TLA+. It explains how TLC turns a specification that allows unbounded parameters into a finite model with chosen constants and state constraints, explores the model's reachable states for invariant violations or deadlock, and reports an error trace. As the original paper by the tool's authors it is authoritative for TLC's design at that time, but it predates liveness checking, which Lamport's later [tools page](../lamport-tla-tools/) says TLC now performs. A completed finite run proves nothing about other parameter values or about implementations.

## Key points

- A TLA+ specification may allow arbitrarily many processes or unbounded queues. TLC supplies fixed constants and state constraints to define a finite model, then exhaustively checks its reachable states if the run completes. (Section 1, discussion of finite-state models; section 3, paragraphs beginning "Traditional model checking works on finite-state specifications" and "With TLC, one bounds the number of states by choosing a model")
- TLC explores reachable states for invariant violations or deadlock and reports a path from an initial state to a bad state. The paper qualifies its minimal-length trace guarantee to single-worker runs. (Section 3, paragraph beginning "These declarations, together with the constraint, define the model that TLC tries to check" and footnote 5; section 4, error-reporting description)
