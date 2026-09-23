---
title: Lean's Cedar software verification case study
summary: Lean FRO's account of Cedar's executable models, proofs, and differential testing against Rust.
url: https://lean-lang.org/use-cases/cedar/
author: "Lean FRO"
kind: webpage
captures:
  - retrieved: 2026-09-23T08:40:36Z
    sha256: "87e57374dc192669709940486100b44e500ebaa7af0b18cc2fe10d642bc976e7"
    type: text/html
---

## Overview

A case study on the Lean website retells how the Cedar team at AWS verifies its authorization language: executable Lean models of the evaluator, authorizer, and validator beside the production Rust code, proofs of correctness and security properties about the models, and millions of random differential tests before each release. The Lean FRO wrote it to showcase Lean in industry, and it carries no date. It is a secondhand, promotional overview; the engineers' own [AWS blog post](../aws-lean-cedar/) gives the worked theorem and draws the line between the proved model and the Rust implementation more precisely.

## Key points

- Cedar's evaluator determines expression values, authorizer makes authorization decisions, and validator type-checks policies to prevent evaluation errors. (`The Cedar Verification Approach`)
- The Cedar team writes executable Lean models beside production Rust, proves correctness and security properties about the models, and compares model and implementation on millions of random inputs before release. (`The Cedar Verification Approach`)
- Lean's small trusted proof-checking kernel supports the proofs; the production verification process incorporates the model, proofs, and testing. (`Benefits for Production Software`)
