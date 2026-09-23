---
title: Can every wrong password reveal plausible decoy data?
rkey: password-decoy-authentication
date: 2026-09-23
brief: Wrong-key plausibility has cryptographic precedents, but a live AI-generated account needs consistent state and must not expose a new credential oracle.
turn_url: https://github.com/smith-wiki/wiki/issues/82
mode: QUESTION_ANSWER
---

## Answer

**Inference:** [The post's idea](../../sources/andy-smith-every-password-correct/) could waste an uninformed attacker's time, but "every wrong password works" is not an established defense for a live account. [Honey encryption](../../sources/honey-encryption-juels-ristenpart/) makes *offline* wrong-key decryptions look plausible under a modeled message distribution; [Kamouflage](../../sources/kamouflage-password-management/) hides real vault credentials among decoys; [honeywords](../../sources/honeywords-juels-rivest/) detect use of false credentials. [VeraCrypt's outer volume](../../sources/veracrypt-hidden-volume/) shows a real alternate-password decoy. None establishes indistinguishable AI-generated email and documents across repeated online interactions. ([Juels and Ristenpart, n.d.](../../sources/honey-encryption-juels-ristenpart/); [Bojinov et al., n.d.](../../sources/kamouflage-password-management/))

**Inference:** Deliberately outdated records invite a current-fact check; sends, edits, APIs, timing, and MFA can reveal the real session or let a false one affect real data. [Password-triggered decoys](../../concepts/password-triggered-decoys/) maps the precedents, and [the oracle boundary](../../notes/decoy-logins-move-the-password-oracle/) explains these failure modes. Continue to rate-limit guesses and require normal authenticators for genuine access. ([VeraCrypt project, n.d.](../../sources/veracrypt-hidden-volume-requirements/); [OWASP Cheat Sheet Series, n.d.](../../sources/owasp-authentication-cheat-sheet/); [National Institute of Standards and Technology, 2025](../../sources/nist-authenticator-verifier-requirements/))

**Uncertainty:** Can a bounded, isolated decoy account withstand an attacker who knows one recent fact and probes read/write behavior over multiple sessions? No cited source tests that design.
