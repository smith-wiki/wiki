---
title: Calling AWS services and prices using the AWS Price List
summary: AWS pricing catalogs expose SKU-level rates but omit some offer types and remain informational.
url: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html
author: "Amazon Web Services"
kind: documentation
retrieved: 2026-09-23T09:21:02Z
sha256: "5ce3083f8d4eaae0bbae481d740e59d01deac9d01c01f1c47c8094a15f85f106"
---

## Overview

AWS billing documentation describes the Price List, a catalog of prices by product SKU and attributes, available through a Query API and as downloadable Bulk API files in JSON and CSV. Written for customers building cost tooling, it is authoritative for what the catalog covers and candid about its gaps: EC2 Spot prices and time-limited free-tier offers are excluded, Savings Plans are missing from the Query API, and the values are informational, with service pricing pages taking precedence. A rate catalog is not a bill; the [AWS Pricing Calculator](../aws-pricing-calculator/) turns rates and assumed usage into estimates.

## Key points

- AWS Price List catalogs products by SKU and attributes. Query API prices can support scenario planning, forecasts, and cost control; Bulk API publishes region/service price files in JSON and CSV. (`Overview`, `Product`, `Attribute`, `AWS Price List Query API`, `AWS Price List Bulk API`)
- The catalog excludes EC2 Spot prices and time-limited free-tier offers; the Query API excludes Savings Plan prices. Price List API values are informational; where they differ from service pricing pages, the service page governs AWS charges. (Opening paragraphs below title; `Overview`, note below `AWS Price List Query API`, note below `AWS Price List Bulk API`)
