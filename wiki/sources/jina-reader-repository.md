---
title: Jina Reader repository
summary: Pinned open-source Reader implementation documents browser and direct engines, self-hosting, and Markdown rules.
url: https://raw.githubusercontent.com/jina-ai/reader/1574bfd380d249c86c82db4dace0d9c8fe17e2b1/README.md
author: Jina AI
kind: repository
captures:
  - retrieved: 2026-09-24T07:47:52Z
    sha256: "583b250f78916c63a244eeb2903077548bcc39e9245f471947857fe84c70536c"
    type: text/plain
  - retrieved: 2026-09-24T07:48:09Z
    sha256: "f4c407c8cac75d2de10bdd4b1f0b5e7f4d1151696bb7c9d68c26dea2b0027e95"
    type: text/plain
    url: https://raw.githubusercontent.com/jina-ai/reader/1574bfd380d249c86c82db4dace0d9c8fe17e2b1/src/services/markify.ts
---

## Overview

Jina's pinned repository documents the open-source branch of its Reader service and includes the converter implementation. It describes headless Chrome and direct curl fetching, a Docker image for local operation, and separate SaaS storage and proxy facilities not bundled in the open branch. The `markify.ts` source contains dedicated image, code, table, MathML, and `figcaption` handling, but rules do not establish success rates on arbitrary pages. Its README describes `auto` as a hybrid that can prefer curl, so explicitly selecting the browser engine is safer when JavaScript completeness matters. Generated alt text is a model-created description, distinct from an author's caption; the repository's self-hosting instructions do not imply parity with the hosted anti-bot network.

The hosted interface and model-created alt option are described separately in the [Reader API documentation](../jina-reader-documentation/).

## Key points
- The open-source branch offers stateless or optional bucket-cached Docker operation with bundled headless Chrome; MongoDB-backed SaaS storage is absent. (README, opening note; Self-host with Docker)
- `x-engine` selects browser, curl without JavaScript, or auto; browser waits/selectors help SPA extraction. (README, Using request headers; SPA fetching)
- The converter emits Markdown images, code, GFM tables with headers, MathML-to-LaTeX, and figcaption text on separate lines. (src/services/markify.ts, processImage, getCodeText, processTr, processMath, processFigcaption)
- Generated alt descriptions and image/URL retention are optional; they do not recreate original figure captions. (README, Using request headers; Generated alt)
