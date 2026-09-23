---
title: "Honey Encryption: Security Beyond the Brute-Force Bound"
summary: Honey encryption produces plausible plaintext under incorrect keys, but its guarantee depends on a matching message distribution and limited side information.
url: https://www.iacr.org/archive/eurocrypt2014/84410181/84410181.pdf
author: "Ari Juels and Thomas Ristenpart"
publisher: EUROCRYPT 2014
kind: paper
captures:
  - retrieved: 2026-09-23T11:32:19Z
    sha256: "1275a60cfec3745d0f7ec237b0b6a8df43d997271e1ab51ea000ab78f189ac47"
    type: application/pdf
---

## Overview

Juels and Ristenpart introduce honey encryption for data protected by low-entropy keys: an incorrect decryption yields a plausible message rather than an obvious error. Their distribution-transforming encoder maps ciphertext decryption results into the expected message distribution, and the paper analyzes message recovery under explicit key and message assumptions. This original EUROCRYPT 2014 paper is authoritative for the construction and its conditional guarantees, not evidence that arbitrary personal emails can be simulated convincingly. Its demonstrations focus on structured secrets such as credit-card numbers and RSA private keys; the authors identify natural-language messages as a harder modeling problem. Unlike [honeywords](../honeywords-juels-rivest/), it concerns offline decryption rather than server-side login, and [Smith's proposal](../andy-smith-every-password-correct/) extends the intuition to an interactive account.

## Key points

- A wrong decryption key yields a valid-looking but bogus plaintext; examples cover RSA private keys and credit-card numbers, not a fully interactive mailbox. (Abstract; section 7)
- The distribution-transforming encoder must approximate the actual message distribution; a bad estimate weakens the additional message-recovery guarantee. (Sections 1, "DTEs" and "Limitations of HE"; 4, "Distribution-Transforming Encoders")
- Side information about the message, correlation with keys or other messages, and user password typos limit the proposed protection. (Section 1, "Limitations of HE"; section 7.3, "Deployment considerations")
- Constructing a convincing encoder for human-generated email or password vaults remains an open practical modeling challenge in the paper. (Section 8, "Conclusion")
