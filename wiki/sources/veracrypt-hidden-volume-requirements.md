---
title: "VeraCrypt Security Requirements for Hidden Volumes"
summary: Hidden-volume deniability depends on snapshot, write, metadata, and network-use discipline beyond encryption.
url: https://veracrypt.io/en/Security%20Requirements%20for%20Hidden%20Volumes.html
author: "VeraCrypt project"
kind: documentation
retrieved: 2026-09-23T11:36:48Z
sha256: "247374cc90bbe7a7d85a438d29ce0b02f8ced4397d3f5ca18a5ea2af54232132"
---

## Overview

The VeraCrypt project documents operational conditions for plausible deniability when using its [hidden volumes](../veracrypt-hidden-volume/). The guidance warns that an attacker comparing the encrypted container at multiple times can spot changed sectors; journaling and device behavior may preserve traces, while the operating system can leave plaintext artifacts elsewhere. For a hidden operating system, it recommends frequent decoy use and warns that activation records and server logs can reveal activity absent from the decoy. This is authoritative first-party risk guidance for its own product, not direct evidence about web services. Its relevance to [Smith's decoy-account proposal](../andy-smith-every-password-correct/) is analogical: a plausible screen is insufficient if an adversary can inspect state changes, metadata, or third-party records. The document explicitly says its list of threats is incomplete.

## Key points

- Comparing copies of a container over time can expose changed hidden-volume sectors, even when the outer password is disclosed. (Opening warning, first bullet)
- Journaling, wear leveling, and host applications may retain copies, metadata, or plaintext outside the hidden volume. (First bullet, sub-bullets; paragraph beginning "When a hidden volume is mounted")
- An infrequently used decoy operating system may reveal its purpose; activation times and network/server logs can distinguish hidden activity from decoy activity. (Hidden operating system bullets beginning "You should use the decoy operating system", "If the operating system requires activation", and "The computer may be connected")
