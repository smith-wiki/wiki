---
title: Your Privacy and Kagi
summary: Kagi's policy statements about search-query logging, billing metadata, and debugging retention.
url: https://kagi.com/privacy
author: Kagi
kind: webpage
retrieved: 2026-09-23T11:41:53Z
sha256: "1a5ba0827ffac9f1e99168b3ebb99c0fb17e0d1590e1f4808477db0b7701d9e6"
---

## Overview

Kagi's privacy policy for its paid services explains what data the browser and servers handle, how long debugging logs are kept, what billing records hold, and how AI features and privacy-oriented access work. It is the company's own policy, described as a living document, not an audit. It gives no separate retention rule for the Search API, promises no zero data retention there, and leaves the "short period" for query logs undefined; that is the contrast the wiki draws with [Brave's announcement](../brave-search-api-announcement/).

## Key points

- Search queries may be logged temporarily for debugging and are purged automatically after a short period. (Section "Payment information")
- Sampled load-balancer and virtual-machine logs are kept for seven days and sampled Sentry error data for 90 days; temporarily stored browser requests are not linked to an account. (Section "On our servers" > "Debugging retention periods")
- Kagi keeps usage volume for billing while treating search-query text as temporary debugging data. (Section "Payment information")
