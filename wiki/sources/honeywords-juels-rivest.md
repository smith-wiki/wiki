---
title: "Honeywords: Making Password-Cracking Detectable"
summary: False password hashes make a stolen verifier file risky to exploit, while a separate honeychecker knows the real credential.
url: https://people.csail.mit.edu/rivest/pubs/JR13.pdf
author: "Ari Juels and Ronald L. Rivest"
publisher: ACM CCS 2013
published: 2013-11-04
kind: paper
captures:
  - retrieved: 2026-09-23T11:32:44Z
    sha256: "e0eb92c0373abb3f0d747efc2cc5b73c145e0f49abe3fbf00a61f83605d11f42"
    type: application/pdf
---

## Overview

Juels and Rivest propose mixing a user's real password hash with hashes of false honeywords so that a thief of the password file cannot confidently choose a genuine credential. A separate hardened honeychecker knows which candidate is real and can raise an alarm when a honeyword is used; the paper also considers silently admitting suspicious attempts for monitoring. This original CCS 2013 paper is authoritative for the proposed protocol and its assumptions, chiefly an attacker who steals hashed passwords but has not persistently compromised the login logic or the honeychecker. It is not a scheme in which every arbitrary string unlocks a believable account. [Kamouflage](../kamouflage-password-management/) hides a real vault among false ones instead; [Smith's proposal](../andy-smith-every-password-correct/) asks for interactive decoy content for every wrong password.

## Key points

- A stolen password-hash file contains hashes of real and false passwords, while a separate honeychecker identifies the genuine entry; using a false one can raise an alarm. (Abstract; sections 2.2-2.4)
- The design targets theft of the hash file rather than live observation of password entry or persistent control of login logic; the latter can undermine detection. (Section 2.1, "Attack scenarios")
- A guess matching none of the stored candidates is denied; the proposal does not make arbitrary wrong passwords into successful logins. (Section 2.4, "Login")
- The value of decoys depends on their flatness: an attacker who can distinguish false candidates from the real password erodes the protection. (Sections 3, "Flatness"; 4.1, "Legacy-UI password changes")
