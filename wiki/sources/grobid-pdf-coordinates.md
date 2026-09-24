---
title: GROBID PDF coordinates
summary: Official figure and table box conventions in TEI and JSON, including page units and CropBox alignment.
url: https://grobid.readthedocs.io/en/latest/Coordinates-in-PDF/
author: GROBID project
kind: documentation
captures:
  - retrieved: 2026-09-24T08:44:21Z
    sha256: "065b4d84d8928c33caf34fad71307b15753b2b92e6b85338a3cf9d2e7289a848"
    type: text/html
---

## Overview

GROBID's documentation explains how clients request and interpret structure coordinates in PDF-to-TEI and JSON extraction. It explicitly covers figures and tables, the origin and units of its rectangles, one-based page numbers, page-size metadata, and the CropBox/MediaBox pitfall. These details are operational evidence for turning a detected figure into a repeatable crop or page overlay rather than citing an approximate heatmap. It is a project specification, not an accuracy study: the existence of a returned box cannot certify a correct figure boundary or caption. The page builds on the wiki's [scientific PDF structure extraction](../../concepts/scientific-pdf-structure-extraction/) and supports the new [visual evidence retrieval](../../concepts/visual-evidence-retrieval/) provenance contract.


## Key points

- `teiCoordinates=figure` requests coordinates for figures and tables in full-text TEI; JSON annotation services also expose `figure` positions (Getting the coordinates of identified structures; GROBID service).
- Coordinates use upper-left origin, x to the right, y downward, and PDF units rather than pixels; the first page is 1 (Coordinate system in the PDF; Coordinates in JSON results).
- JSON uses page size and a list of `p,x,y,w,h` boxes; TEI can encode multiple boxes as `page,x,y,w,h` entries separated by semicolons (Coordinates in JSON results; Coordinates in TEI/XML results).
- GROBID uses CropBox, falling back to MediaBox, and instructs scaling against page dimensions before aligning PDF boxes with another tool's raster (How do GROBID coordinates relate to other tools?; CropBox vs MediaBox coordinate mismatch).
