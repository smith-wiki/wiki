---
title: "Kamouflage: Loss-Resistant Password Management"
summary: A stolen password vault opens onto plausible decoy credential sets, forcing an attacker to verify candidates against external sites.
url: https://crypto.stanford.edu/~dabo/pubs/papers/passwordmgr.pdf
author: "Hristo Bojinov, Elie Bursztein, Xavier Boyen, and Dan Boneh"
publisher: ESORICS 2010
kind: paper
retrieved: 2026-09-23T11:33:24Z
sha256: "758e7dc8ed3c573518b92d1ed3208314265ce977bf0e39a0c56a8cfdfa42fee9"
---

## Overview

Bojinov, Bursztein, Boyen, and Boneh describe Kamouflage, a password manager that stores one real credential set alongside many decoy sets. An incorrect master-password guess opens a plausible but false set, shifting an attacker with a stolen device from cheap local verification to login attempts at the actual websites. Their ESORICS 2010 paper is original design and prototype evidence, including a Firefox password-manager replacement and experiments on password patterns, not a guarantee that real services always throttle. The model initially excludes outside knowledge about the user, then examines a stronger adversary. Unlike [honey encryption](../honey-encryption-juels-ristenpart/), Kamouflage explicitly stores many decoys; unlike [Smith's proposal](../andy-smith-every-password-correct/), its output is a static credential collection, not a living email and document account.

## Key points

- The vault contains one real and many false password sets; guesses of the master password return a valid-looking set, requiring online tests at the external sites to verify credentials. (Section 1, "Our contribution"; sections 3-4)
- Decoys must reproduce patterns shared across a user's passwords and each site's requirements; otherwise the real set can stand out. (Section 1, "Our contribution"; section 4.1, "Password set generation")
- Adding, removing, or updating entries must change decoys as well as the real set so that snapshots do not expose which is genuine. (Section 4, "Database operations")
- The basic threat model assumes no external knowledge about the victim, while its extended model considers personal side information and counts both offline work and online checks. (Section 3, "Threat model")
