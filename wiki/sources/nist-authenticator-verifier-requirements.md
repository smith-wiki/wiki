---
title: "NIST SP 800-63B-4: Authenticator and Verifier Requirements"
summary: NIST requires password verification, offline-resistant storage, and limits on failed online guesses for network authentication.
url: https://pages.nist.gov/800-63-4/sp800-63b/authenticators/
author: "National Institute of Standards and Technology"
published: 2025-07-31
kind: specification
captures:
  - retrieved: 2026-09-23T11:34:11Z
    sha256: "dc1d7071d2e305ea1fee14d7bf75de5eb6bcbd3d9d9bcb19d78adf7ae6f7de75"
    type: text/html
---

## Overview

NIST's SP 800-63B-4 specifies authentication and authenticator-management requirements for networked digital identity services, including centrally verified passwords, storage of password verifiers, throttling, and cryptographic authenticators. It is normative guidance for systems in its scope, not a study of deception or a prohibition on all decoy environments. NIST distinguishes control of an authenticator from the content shown after a login: access to a genuine subscriber account is established by proof of that control. The password section requires rate limiting and salted password hashing resistant to offline attack, while the general requirements specify controls for online guessing. This official standard provides the operational baseline against which [the decoy-login idea](../andy-smith-every-password-correct/) should be judged; its concerns are distinct from the offline vault threat model of [Kamouflage](../kamouflage-password-management/).

## Key points

- Passwords sent to a central verifier are not phishing-resistant; verifiers check the entire submitted password. (Section 3.1.1, "Passwords" and "Password Verifiers")
- Verifiers must salt and hash passwords to resist offline attacks and limit failed authentication attempts per subscriber account. (Section 3.1.1.2, "Password Verifiers")
- The general rate-limiting rule caps consecutive failed attempts with a specific authenticator on a single account at 100 unless otherwise specified; lower limits and risk-based controls are allowed. (Section 3.2.2, "Rate Limiting (Throttling)")
- Cryptographic authenticators can offer phishing resistance through channel or verifier-name binding; password-only logins do not. (Section 3.2.5, "Phishing Resistance")
