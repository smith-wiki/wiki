---
title: "What if every password were correct?"
summary: Andy Smith proposes password-specific AI decoy data for incorrect logins as a way to obscure whether a password worked.
url: https://andysmith.ai/2026/Sep/23/what-if-every-password-were-correct/
author: "Andy Smith"
published: 2026-09-23
kind: webpage
captures:
  - retrieved: 2026-09-23T11:29:22Z
    sha256: "8c458e25f2a2dfd81cc62d2de77ebdfd1b763069ab35e046eb922c566412fce7"
    type: text/html
---

## Overview

Andy Smith's short thought experiment asks whether a wrong password could open an apparently valid account filled with AI-generated documents and emails, unique to that password and seemingly outdated. The intended effect is to make a stranger unsure whether a guessed credential actually reached the genuine account. This is the primary statement of the proposal, not an implementation or a measured security result; it does not specify a threat model, how an account retains state, or how data would be distinguished by its owner. Earlier work on [honey encryption](../honey-encryption-juels-ristenpart/) and [Kamouflage](../kamouflage-password-management/) gives concrete but narrower precedents. The [verification-boundary note](../../notes/decoy-logins-move-the-password-oracle/) examines the online variant.

## Key points

- The post proposes showing apparently valid but stale data after an incorrect password instead of an immediate rejection. (Paragraph beginning "What if, after entering the wrong password")
- It proposes generating documents, emails, and data with AI, separately for each incorrect password. (Paragraph beginning "What if, after entering the wrong password, a hacker saw documents")
- The expected advantage is uncertainty for an attacker without independent knowledge of what the genuine account contains; no experiment or mechanism is offered. (Closing paragraph)
