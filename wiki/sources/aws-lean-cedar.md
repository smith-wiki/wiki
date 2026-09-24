---
title: Lean Into Verified Software Development
summary: Cedar engineers explain their Lean authorizer theorem, validator proof, and differential testing against Rust.
url: https://aws.amazon.com/blogs/opensource/lean-into-verified-software-development/
author: "Kesha Hietala and Emina Torlak"
publisher: "AWS Open Source Blog"
published: 2024-04-08
kind: article
retrieved: 2026-09-23T08:40:52Z
sha256: "51b24c2135d6f4c501a104b047914e9bc603bf711041dd9d92e9580c957458c8"
---

## Overview

Kesha Hietala and Emina Torlak of the AWS Cedar team describe how they use Lean for verification-guided development of Cedar, an authorization policy language: executable Lean models of core components, proofs of properties such as a forbid policy overriding any permit, and differential random testing of the production Rust code against those models. Written for engineers on the AWS Open Source Blog, it includes a worked theorem, the effort behind a larger proof, and practical lessons. It is a first-party account: effort and testing figures are self-reported, and differential testing samples behavior rather than proving that the Rust matches the model. [Lean's case study](../lean-cedar-verification/) retells the same project.

## Key points

- Cedar maintains executable Lean models of core components and proves properties of those models, while a separate optimized Rust implementation is checked against them using millions of randomly generated differential test inputs; model, proofs, and tests are refreshed before a release. (`How Cedar uses Lean for verification-guided development`)
- `isAuthorized` returns `allow` only with no satisfied `forbid` and at least one satisfied `permit`. Their `forbid_trumps_permit` theorem states that any satisfied forbid in the policy set entails a `deny` decision for every request, entity set, and policy set satisfying that premise. Its proof uses `intro`, `unfold`, and `simp` with an auxiliary theorem. (`A quick tour of modeling and verifying Cedar with Lean` > `def isAuthorized` and `theorem forbid_trumps_permit`)
- The validator soundness proof establishes that a policy accepted by the validator does not cause a type error on evaluation; its proof used 4,686 lines and 18 person-days. Modeling recursive structures required accommodating Lean's well-founded termination checker. (`A quick tour of modeling and verifying Cedar with Lean` > table, following two paragraphs, and `One challenge of using Lean is its strict termination checking`)
- Start with simple proof automation, build tailored `simp` lemmas, and allow for a learning curve and changes to recursive definitions. (`Takeaways`)
