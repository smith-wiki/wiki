---
title: Model Checking TLA+ Specifications
summary: Original TLC paper explains finite model instantiation, reachable-state exploration, and error traces.
---

## Source

- **Type:** Research paper by the model checker's authors
- **Authors:** Yuan Yu, Panagiotis Manolios, and Leslie Lamport
- **Original:** [Model Checking TLA+ Specifications](https://lamport.azurewebsites.net/pubs/yuanyu-model-checking.pdf)
- **Published:** 1999, in *Correct Hardware Design and Verification Methods* (CHARME '99), LNCS 1703, pp. 54-66; PDF dated June 25, 1999
- **Suggested citation:** Yu, Manolios, and Lamport. "Model Checking TLA+ Specifications." CHARME '99, 1999.

## Representation

- **ID:** `yuanyu-model-checking-2026-09-23`
- **Retrieved:** 2026-09-23T09:00:17Z
- **Preserved representation:** `raw/sources/yuanyu-model-checking-2026-09-23.pdf`
- **Format:** PDF
- **Fixity:** `sha256:7d8713bb8793f08c9c26b08c3a87535b6c43cfd259295c09a91d01d1f1ba6210`

## Evidence

### `finite-instance-of-an-unbounded-specification`

- **Authors explain:** A TLA+ specification may allow arbitrarily many processes or unbounded queues. TLC supplies fixed constants and state constraints to define a finite model, then exhaustively checks its reachable states if the run completes.
- **Locator:** Section 1, discussion of finite-state models; section 3, paragraphs beginning "Traditional model checking works on finite-state specifications" and "With TLC, one bounds the number of states by choosing a model"

### `violations-and-traces`

- **Authors explain:** TLC explores reachable states for invariant violations or deadlock and reports a path from an initial state to a bad state. The paper qualifies its minimal-length trace guarantee to single-worker runs.
- **Locator:** Section 3, paragraph beginning "These declarations, together with the constraint, define the model that TLC tries to check" and footnote 5; section 4, error-reporting description

## Source criticism

This is the historical 1999 implementation paper, not documentation for present TLC releases. It states that TLC did not *yet* check liveness; Lamport's later [tools page](../lamport-tla-tools/) says TLC checks safety **and** liveness. A completed finite exploration does not prove the original unbounded specification for every parameterization or prove any separately written implementation.

## Connections

- [TLA+](../../entities/tla-plus/) distinguishes the specification from a finite model.
- [Learn TLA+ example](../learntla-conceptual-overview/) illustrates why two transfers can reveal a design error.
- [Lean comparison](../../research/lean-versus-tla/) contrasts TLC's finite exploration with deductive proofs.
