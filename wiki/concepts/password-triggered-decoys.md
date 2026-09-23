---
title: Password-triggered decoys
summary: Alternate credentials or wrong-key decryptions reveal plausible false data to delay, detect, or redirect an attacker.
---

A password-triggered decoy is an alternate view of protected data reached with a credential other than the one that accesses the genuine data. Its security goal is not necessarily to make the password harder to guess; it makes a *candidate's correctness harder to determine*, or makes trying a false candidate detectable. [Smith's proposal](../../sources/andy-smith-every-password-correct/) imagines a unique, AI-generated, outdated account for every wrong password. **Inference:** That is a stronger and more stateful requirement than a fake vault or document. ([Smith, 2026](../../sources/andy-smith-every-password-correct/))

## Different mechanisms and threat models

- **Offline encrypted data:** [Honey encryption](../../sources/honey-encryption-juels-ristenpart/) turns wrong-key decryption into a plausible plaintext sampled from a modeled distribution. It cannot promise that every key yields a *unique* output, and useful side information may identify the true one. ([Juels and Ristenpart, n.d.](../../sources/honey-encryption-juels-ristenpart/))
- **Stolen password vault:** [Kamouflage](../../sources/kamouflage-password-management/) stores one real set among many plausible decoy credential sets. The attacker must test them against sites; the online sites remain correctness oracles. ([Bojinov et al., n.d.](../../sources/kamouflage-password-management/))
- **Stolen verifier file:** [Honeywords](../../sources/honeywords-juels-rivest/) stores false password hashes with a real hash and uses a separate honeychecker to detect a false candidate's use. Arbitrary wrong strings are still denied. ([Juels and Rivest, n.d.](../../sources/honeywords-juels-rivest/))
- **Duress storage:** [VeraCrypt hidden volumes](../../sources/veracrypt-hidden-volume/) use separate outer and hidden passwords, with real decoy files in the outer volume. These are two intended views, not an unbounded set of worlds. ([VeraCrypt project, n.d.](../../sources/veracrypt-hidden-volume/))

## Boundary for a live account

**Inference:** A realistic account must preserve relationships among old and new messages, timestamps, metadata, sessions, edits, and external actions. A fluent generator only addresses the appearance of individual records. [VeraCrypt's precautions](../../sources/veracrypt-hidden-volume-requirements/) show how changes, traces, and outside logs can unmask even a local decoy. An online decoy also needs to separate real and fake authority: [object-capability RPC](../object-capability-rpc/) illustrates that a session's methods, not the screen shown to the user, determine what operations it can perform. The [verification-boundary note](../../notes/decoy-logins-move-the-password-oracle/) explains why a convincing login screen is not enough. ([VeraCrypt project, n.d.](../../sources/veracrypt-hidden-volume-requirements/); [Varda and Faulkner, 2025](../../sources/cloudflare-capnweb-javascript-rpc/))
