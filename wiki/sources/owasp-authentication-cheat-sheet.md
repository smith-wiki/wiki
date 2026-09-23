---
title: "OWASP Authentication Cheat Sheet"
summary: Generic errors, similar response timing, throttling, and MFA reduce online credential-enumeration channels.
url: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
author: "OWASP Cheat Sheet Series"
kind: documentation
captures:
  - retrieved: 2026-09-23T11:38:24Z
    sha256: "afab72f685555b72b1fadf6da034d07258a9f01d0c0272d01b0cb1991caa49cb"
    type: text/html
---

## Overview

The OWASP Cheat Sheet Series gives operational guidance on designing password login, error handling, throttling, and multi-factor authentication. Its authentication section warns that differences in HTTP responses, page content, and processing time can disclose account or credential status even when the visible error text is generic. The rate-limiting discussion addresses interactive brute force and the availability cost of account lockouts. This living community guidance is useful for enumerating observable online failure paths, but it does not analyze or endorse a synthetic decoy-account system and is not a formal proof of indistinguishability. It complements [NIST's verifier requirements](../nist-authenticator-verifier-requirements/) and supplies a practical lens on the response channels in [Smith's proposal](../andy-smith-every-password-correct/).

## Key points

- Login, reset, and recovery responses should not distinguish incorrect credentials, nonexistent accounts, or disabled accounts through their visible message. ("Authentication and Error Messages", "Authentication Responses")
- Processing-time differences and even HTTP status codes can reveal cases hidden behind identical-looking error pages. ("Authentication Responses"; "Error Codes and URLs")
- Login throttling restricts interactive guessing; lockout counters should follow the account, and lockout can be abused for denial of service. ("Login Throttling"; "Account Lockout")
- MFA is recommended as a defense against password-related attacks rather than simply increasing the number of password guesses required. ("Multi-Factor Authentication")
