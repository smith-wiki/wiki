---
title: "VeraCrypt Hidden Volume"
summary: Two passwords reveal an outer decoy volume or a hidden sensitive volume, under strict operational conditions.
url: https://veracrypt.io/en/Hidden%20Volume.html
author: "VeraCrypt project"
kind: documentation
retrieved: 2026-09-23T11:36:21Z
sha256: "625866a496b91c10f9ad2779925ccd2b7468ec36bc7f9cbfef827ce8cdc8ded7"
---

## Overview

The VeraCrypt project's hidden-volume documentation describes a storage arrangement with a hidden encrypted volume inside a larger outer encrypted volume. The outer password exposes files that can serve as plausible decoys; a substantially different password opens the hidden files. The implementation uses random-looking free space to obscure the existence of the hidden volume. This is first-party documentation of a real alternate-password view, not a claim that every possible password opens useful data or that online accounts can be simulated. The project's separate [security requirements](../veracrypt-hidden-volume-requirements/) warn that repeated observations and activity outside the encrypted volume can break the intended deniability. The example informs [Smith's proposal](../andy-smith-every-password-correct/) while remaining a local-storage design with two intended passwords.

## Key points

- The outer volume is meant to contain sensitive-looking decoy files, while truly sensitive files are stored in a hidden volume. ("Hidden Volume", paragraphs beginning "The password for the hidden volume" and "A hidden volume can be mounted")
- The entered password selects either outer or hidden volume by decrypting the appropriate header; arbitrary wrong passwords do not mount a volume. ("Hidden Volume", paragraph beginning "VeraCrypt first attempts")
- The claimed inability to prove the hidden volume exists is explicitly conditional on the creation and security precautions. ("Hidden Volume", footnote beginning "Provided that all the instructions")
