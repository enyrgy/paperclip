# Canonical link reference

Every URL used in campaign copy. Email files reference these **by name** rather than repeating the URL, so a link change is a one-line edit here instead of a hunt through nineteen files.

The GHL email editor has **no source view**, so plain-text copy cannot carry a hyperlink's URL, only its anchor text. Anchor text is therefore resolved against this table when a file is written.

**Provenance:** these URLs come from the Knowledge Base, the handoff's Key URLs section and the Implementation Guide, and were verified correct against GHL in a dedicated session. They are **resolved from the repo, not read out of the email action**. If a link is ever changed in GHL without updating here, the files silently drift.

---

## Calendars

| Name | URL | Use |
|---|---|---|
| **Consumer Discovery** | `https://api.leadconnectorhq.com/widget/booking/C0hV5CFHUhWOIzs4OedC` | Round-robin. Consumer funnel calls. |
| **Commercial Discovery** | `https://api.leadconnectorhq.com/widget/booking/VJ3PDGQsxhiSXhkzUwND` | Round-robin. Facility and operator calls. |
| **Investor Intro** | `https://api.leadconnectorhq.com/widget/booking/JtYjGrq6vF7aBiM3IZiG` | Scott only. |
| **Investor Presentation** | `https://api.leadconnectorhq.com/widget/booking/UpEku45jOQdYpj9qXlM5` | Collective. |

## Forms

| Name | URL |
|---|---|
| **Customer Testimonial** | `https://api.leadconnectorhq.com/widget/form/OjahkWeVDeozQkfG9dW2` |
| Customer Testimonial (no-track variant, used in WF-07) | `https://api.leadconnectorhq.com/widget/form/OjahkWeVDeozQkfG9dW2?notrack=true` |
| **Consumer Inquiry** | `https://api.leadconnectorhq.com/widget/form/dclY1TB3jA3eitWEQaCo` |
| **Accreditation** | `https://api.leadconnectorhq.com/widget/form/DBQBL51stonmfRcUBsMe` |

## Product and store

| Name | URL |
|---|---|
| **Order page** (Home System) | `https://shop.enyrgy.com/products/uvb-light-therapy` |
| **Device registration** | `https://api.enyrgy.com/` |
| Privacy policy | `https://shop.enyrgy.com/policies/privacy-policy` |
| Terms of service | `https://shop.enyrgy.com/policies/terms-of-service` |

## Lead magnet pages

| Name | URL |
|---|---|
| **Tired Test** | `https://go.enyrgy.com/tired-test` |
| **Vitamin D Assessment** | `https://go.enyrgy.com/vitamin-d-assessment` |
| **Synthesis Gap** | `https://go.enyrgy.com/synthesis-gap` |
| **Recovery Protocol** | `https://go.enyrgy.com/recovery-protocol` |
| **Winter Protocol** | `https://go.enyrgy.com/winter-protocol` |
| SMS opt-in proof page | `https://go.enyrgy.com/sms-opt-in` |

## Reviews

| Name | URL |
|---|---|
| **Google review (GBP)** | `https://g.page/r/CfN5Rj0CdmrfEAI/review` |
| **Trustpilot** | `https://www.trustpilot.com/evaluate/enyrgy.com` |

---

## How email files cite links

Anchor text is preserved exactly as it appears to the reader, with the resolved target noted beneath:

> `... grab a 15-minute call here: Book Call.`
>
> **Links:** `Book Call` -> Consumer Discovery

Where a full URL is written out in the body itself, as in the Consumer Drip touch 2 order link, it is left inline and needs no entry.
