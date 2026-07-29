# ENYRGY
## Sunlight. Evolved.
### Enterprise Architecture
**The System of Record for How Enyrgy Runs, Connects, and Scales**
Version 1.0

Consumer Unit $2,995 · Commercial Unit $8,950 · OEM/White-Label · Investor Capital
600+ Customers · 25,000+ Treatments · 5 Countries · Zero Adverse Events
scott@enyrgy.com · 602-321-0322 · enyrgy.com

Author: Scott Hansbury, Co-founder & CEO, Enyrgy Inc
Last Updated: June 29, 2026 · Version 1.0 (Session 15 addendum appended July 28, 2026)

CONFIDENTIAL

---

## Session 15 Addendum (July 28, 2026) — pending a v1.1 refresh

This document is dated June 29, 2026 and predates several shipped systems; treat the body below as v1.0 and this addendum as the current-state override until a v1.1 refresh folds it in. The consolidated open-items list lives in `Enyrgy_Master_TODO.md`.

**Now live since v1.0 was written:** the Shopify to GHL native integration plus WF-27/28/29 (which substantially build the "missing purchase sync" the body flags as the top gap — reconcile and ratify rather than rebuild); Google Business Profile (verified/live); the full Paperclip agent org (deployed, KB loaded, compliance gate proven, GHL bridge read-write, heartbeats staged and tuned).

**New operational-reliability findings (add to the Security & Compliance and Open Decisions layers at v1.1):**

- **Agent confabulation under resource starvation.** When the Paperclip agent org is credit-starved or budget-hard-stopped, it does not fail quietly. It produces confident, specific, fabricated claims. In the ENY-20 incident a QC audit and a COO "live verification" both reported a systemic data-lifecycle failure that did not exist (invented contact tag states, a workflow's last-edit timestamp misread as its last-run time). Governance control: **every agent audit or "live verification" must be checked against the live GHL account before any action; agent escalations are leads, not facts.**
- **Phantom task completion (platform correctness bug).** A run that died on "Credit balance is too low" was auto-flipped to `done` with no execution, masking the unresolved item. Required fix: runs that die on a credit/budget error must transition to `blocked`, never `done`.
- **Cost dynamics of starvation.** Running out of credit is more expensive than maintaining headroom: dying runs are re-woken and replay an ever-growing issue thread, multiplying context-replay cost, and orchestrator agents (CEO/COO/CRO) amplify this. Standing rule: keep Anthropic credit buffered and Paperclip budgets with headroom; monitor the Costs page.

**Still open from the body (unchanged, tracked in the Master TODO):** system-of-record ownership map; Device-App-to-GHL usage-data flow; OEM/Lumanova data-boundary formalization; metric-governance owner; and the Shopify Privacy Policy still showing the old Scottsdale address.

---

## How To Read This Document

This is the Enterprise Architecture (EA) for Enyrgy Inc. It sits one layer above the GoHighLevel CRM Implementation Guide (v3.8.4), which documents the marketing and revenue-automation layer in depth. Where this document describes the CRM, it summarizes and points to that guide rather than duplicating it.

Below the EA sit two consumer-layer reference documents that this EA points to rather than duplicates: the **Consumer Funnel Architecture** (the ICP-Dartboard top-of-funnel system: how leads enter, how they are segmented, the suppression logic, and the on-site CTA integration) and the **Consumer TOFU Map and 90-Day Plan** (the traffic strategy that fills the funnel: which content attracts each ICP on which channel, and the phased rollout). When this EA references consumer routing or the dartboard, those two documents hold the detail.

The EA is organized in six architectural layers, each a self-contained section so a reader can go straight to the layer they care about:

1. **Business Architecture**, what Enyrgy sells, to whom, how it makes money, and how the company is organized. Read this if you are an investor, partner, or new executive.
2. **Application & Systems Architecture**, the actual software systems in production, what each owns, and how they connect. Read this if you are operating or extending the stack.
3. **Data Architecture**, where each piece of data lives, which system is its source of truth, and how it flows. Read this if you are building an integration or auditing data.
4. **Integration Architecture**, the webhook and sync topology that ties the systems together, including the gaps that are not yet built. Read this if you are commissioning integration work.
5. **Security & Compliance Architecture**, the regulatory gates (Reg D, A2P/CTIA, FDA wellness guardrails) and how they are enforced in the system. Read this before shipping anything customer- or investor-facing.
6. **Infrastructure Architecture**, domains, DNS, email sending, telephony, and the physical facility.

A final section, **Open Architectural Decisions**, collects every unresolved design question in one place so nothing hides inside a layer. The two largest open items, system-of-record ownership and the Shopify to GoHighLevel sync, appear there and are cross-referenced from the layers they touch.

A note on figures: the canonical company metrics used throughout this document are a $3.5M capital raise, 25,000-plus treatments completed, and a return rate under 1%. Earlier source documents carried minor variances on these numbers; the reconciliation and the governance rule that owns them going forward are recorded in the Open Architectural Decisions section.

---

## Table of Contents

**1. Business Architecture**
- 1.1 What Enyrgy Is
- 1.2 The Product and Its Mechanism
- 1.3 Revenue Streams
- 1.4 Value Chain
- 1.5 Customer Segments
- 1.6 Organization

**2. Application & Systems Architecture**
- 2.1 Systems Overview
- 2.2 What Each System Owns
- 2.3 How The Systems Connect (Conceptual)

**3. Data Architecture**
- 3.1 Systems Of Record
- 3.2 The Core Data Flow
- 3.3 Consent And Segmentation Data
- 3.4 Data Governance Gaps

**4. Integration Architecture**
- 4.1 Integration Topology Today
- 4.2 Live Webhook Endpoints
- 4.3 The Missing Shopify-To-GHL Sync
- 4.4 The Device-App Data Boundary
- 4.5 OEM / Lumanova Boundary

**5. Security & Compliance Architecture**
- 5.1 Securities Compliance (Reg D)
- 5.2 Messaging Compliance (A2P / CTIA / TCPA)
- 5.3 FDA Wellness Guardrails
- 5.4 Data Security And Privacy

**6. Infrastructure Architecture**
- 6.1 Domains And DNS
- 6.2 Email Sending Infrastructure
- 6.3 Telephony
- 6.4 Physical Facility

**7. Open Architectural Decisions**
- 7.1 System-Of-Record Ownership (HIGH)
- 7.2 Shopify-To-GHL Purchase Sync (HIGH)
- 7.3 Device-App Data Flow (MEDIUM)
- 7.4 OEM / Partner Data Boundary (MEDIUM)
- 7.5 Metric Governance (MEDIUM)
- 7.6 Paperclip Activation (operational)

**8. Appendix: System & Endpoint Reference**

---

# SECTION 1, BUSINESS ARCHITECTURE

## 1.1 What Enyrgy Is

Enyrgy is a health-technology company that designs, manufactures, and sells the Enyrgy Vitamin D Primal Light Platform, an app-connected narrow-band UVB/UVA light system that triggers the body's natural synthesis of vitamin D, nitric oxide, and serotonin simultaneously. Sessions run two to five minutes, are personalized to skin type using MED-based (Minimal Erythemal Dose) dosing, and are tracked through a mobile app with gamified habit formation. The platform is manufactured in the USA at the company's Phoenix facility.

The strategic position is category creation, not competition. Enyrgy is not a better supplement and not a better light box; it is a new category, intelligent, dose-controlled phototherapy, defined by the triple pathway that neither supplements nor existing light products can replicate. The long-term vision is to become the category-defining brand in intelligent light wellness.

## 1.2 The Product and Its Mechanism

The platform's differentiation rests on the Triple-Pathway Advantage™:

- **Pathway 1, Vitamin D Synthesis.** Roughly 2.4x more efficient than sunlight; two to four minutes of session time is equivalent to two to four hours of mid-day sun.
- **Pathway 2, Nitric Oxide Release.** UVA triggers enzyme-independent photorelease of nitric oxide from preformed stores in the skin, supporting cardiovascular regulation and blood pressure. This is a pathway no oral product can open: supplements feed the enzymatic route (substrate to eNOS to NO), while light releases NO directly from skin stores. The light pathway is additive to, not a replacement for, the enzymatic one.
- **Pathway 3, Serotonin Production.** Supports sleep, mood, and cognitive function, with users reporting improvements within weeks.

No other single solution delivers all three pathways at once. Supplements deliver vitamin D only. Sunlight requires roughly sixty times the time and carries UVA aging and cancer risk. Red light therapy operates on a different mechanism entirely, which is why roughly 90 percent of Enyrgy customers use both. Safety is engineered in: the device skews heavily UVB with minimal UVA (the inverse of natural sunlight), and the app calculates each user's personal MED by skin type and shuts the session off automatically.

## 1.3 Revenue Streams

Enyrgy operates four distinct revenue streams, each with its own buyer, sales motion, and margin profile.

| Revenue Stream | Buyer | Price | Margin | Status |
|----------------|-------|-------|--------|--------|
| Consumer Unit (DTC direct) | Individuals | $2,995 | 66% | Active, primary revenue driver |
| Commercial Unit (B2B) | Wellness studios, clinics, gyms, clubs | $8,950 one-time + service fee | 78% | Active, growing |
| OEM / White-Label | Brand partners who resell under their own label | Wholesale | Variable | Active, 1 signed partner (Lumanova / Luma D Light) |
| Investor Capital | Accredited investors, family offices | Private credit, see Section 5 | N/A | Active raise |

A fifth, future stream is anticipated: SaaS revenue derived from device usage data (usage insights, progress tracking, dosage personalization). It is not yet in production and is noted here as a roadmap item rather than a current stream.

## 1.4 Value Chain

The end-to-end value chain spans five stages, each owned by an identifiable part of the system or organization:

1. **Manufacture.** Devices and patented LED light cards are built at the Phoenix facility (Made in USA). The OEM/Lumanova relationship is a manufacturing arrangement: Enyrgy manufactures, Lumanova sells under the Luma D Light brand.
2. **Demand generation.** Top-of-funnel demand is generated primarily through podcast appearances (the proven number-one channel), organic social, referral, and word of mouth, with paid media planned for a later phase. All four buyer types have dedicated channels.
3. **Capture and nurture.** Every lead, regardless of source, is captured into GoHighLevel within 24 hours and routed by funnel type into the appropriate automated nurture. This is the layer the Implementation Guide v3.7 documents in full.
4. **Sale and close.** Automation hands off to a human at the moment of real buying intent: discovery calls, demos, proposals, and any contract, legal, or financial instrument are human-owned.
5. **Fulfillment and retention.** Orders are fulfilled from Phoenix; post-purchase onboarding, device activation, reviews, referrals, and reactivation are automation-supported with human oversight.

## 1.5 Customer Segments

Enyrgy serves two primary commercial markets (Consumer and Commercial) plus Partner, Investor, and Vendor relationships. The consumer market is segmented using the ICP-Dartboard model, which weights testing and spend toward the highest-value profiles. The full consumer segmentation, routing, and on-site capture detail lives in the Consumer Funnel Architecture document; the summary below covers the buyer profiles.

**Consumer (DTC, $2,995):**
- **Bullseye, The Stack Optimizer (60%).** Age 35 to 65, household income $150K-plus, already owns red light gear, takes D3 but suspects it is not enough, tracks labs and HRV. Buys through trusted voices, not cold ads. The core message closes a gap: oral D cannot replicate the full synthesis cascade.
- **Inner Ring, The Performance Athlete (35%).** Serious recreational or competitive athlete for whom recovery is the training ceiling. Reached through the nitric-oxide-to-recovery connection.
- **Inner Ring, The SAD Sufferer (seasonal).** Skews female, high-latitude, pain-driven rather than optimization-driven, with an August to October purchase window.
- **Outer Ring, The Energy & Sleep Seeker (5%).** Health-aware but pre-biohacker; highest education burden, lowest urgency; engaged through an interactive quiz rather than a guide.

**Commercial (B2B, $8,950 plus service):**
- **Bullseye, The Believer-Operator.** Independent wellness or longevity studio where the owner is the sole decision maker and motivation is modality completion first, revenue second.
- **Inner Rings, Franchise Gym Operator, Club Operator, Health-Conscious Employer.** Each a distinct, higher-complexity sale; the franchise motion in particular can convert one approval into a large multi-unit order.
- **Outer Ring, The Revenue-Line Operator.** Explicitly the wrong buyer; qualified out, because an unused device produces no results and no word of mouth.

## 1.6 Organization

Enyrgy runs on a deliberately small human team augmented by an AI agent layer.

| Name | Role | Owns |
|------|------|------|
| Scott Hansbury | Co-founder & CEO | Strategy, investor relationships, OEM oversight, brand |
| David Letourneau | President & Co-Founder | Operational execution, discovery and demo calls (primary) |
| Brian Cameron | CFO | Finance, investor financial materials |
| Dennis Lan | Director, Supply Chain | Sourcing, procurement, manufacturing supply chain |
| Dario Pompeii | Senior Engineer | Device and platform engineering |
| Millie Carrillo | Affiliate Manager | Affiliate program management and partner relationships |
| Thea Cartier | Social Media Manager | Organic social content and channel management |

The mobile app is developed and maintained by an outsourced engineering partner, **Outcode LLC (Utah)**. The Device App (api.enyrgy.com) is therefore a proprietary Enyrgy asset built and maintained by an external vendor, a dependency noted here and in the systems and integration layers.

The operating philosophy is explicit: **agents own the process, humans own the relationship.** Agents handle anything that benefits from speed, consistency, and scale (capture, routing, scheduled nurture, scoring, monitoring, compliance-gate enforcement). Humans handle anything that benefits from judgment, trust, and authority (every live call, every negotiation, every legal or financial instrument). The dividing line is the moment a prospect signals real intent. This split is implemented operationally through the Paperclip agent system described in Section 2 and in full in the Implementation Guide.

A scientific advisory board (Dr. Bruce Hollis, Dr. William Grant, Dr. Samantha Kimball) provides clinical credibility and is a core asset of the business architecture, particularly for investor and skeptical-buyer contexts.

---

# SECTION 2, APPLICATION & SYSTEMS ARCHITECTURE

## 2.1 Systems Overview

Enyrgy's production stack is a set of best-of-breed SaaS systems plus one proprietary device application, connected at the edges rather than unified in a single platform. The systems in production today are:

| System | Category | Primary Responsibility |
|--------|----------|------------------------|
| Shopify | E-commerce | Storefront, checkout, payment capture, order system of record for purchases |
| GoHighLevel (GHL) | CRM / marketing automation | Lead capture, segmentation, nurture, pipelines, contact system of record for leads |
| Paperclip | AI agent orchestration | Autonomous execution of capture, routing, nurture, scoring, and monitoring inside GHL |
| Device App (api.enyrgy.com) | Proprietary application | Device registration, MED dosing control, session tracking, gamified habit data |
| LC Email (mg.enyrgy.com) | Transactional/marketing email | Authenticated outbound email on a dedicated sending domain |
| LC Phone | Telephony / SMS | Toll-free voice and A2P SMS |
| Trustpilot | Reviews | Third-party review collection and social proof |
| FlexOffers | Affiliate management | Tracking and reporting of closed sales attributed to affiliates |
| Payment processing | Payments | Card processing for Shopify checkout and financing |

## 2.2 What Each System Owns

**Shopify** is the commerce engine. It owns the product catalog, the checkout experience at shop.enyrgy.com, and the transactional record of every purchase. It is, today, the de facto system of record for the act of buying. The order URL is shop.enyrgy.com/products/uvb-light-therapy.

**GoHighLevel** is the relationship engine and the system of record for leads and contacts. It owns 56 contact fields, roughly 92 tags, five pipelines, six calendars, the five drip campaigns, and workflows WF-01 through WF-18. It segments every contact into one of five funnels (Consumer, Commercial, Investor, Partner, Vendor) and runs the ICP-Dartboard consumer routing. The sub-account is GtXjla7Ld1dordsTWrVy. The Implementation Guide (v3.8.4) is the authoritative reference for everything inside GHL.

**Paperclip** is the agent layer that operates GHL. It is not a separate data store; it is an orchestration system that executes inside GHL through a C-suite of agents (CEO, COO, CRO) and their divisions. The Dispatcher routes inbound leads, Sales Outreach runs the drips, the SDR books calls at score thresholds, Sentinel monitors for stale leads, and the Audit and Compliance agent enforces the investor gate. Paperclip connection is a pending Phase 2 task; the workflows it will operate are already built and published.

**The Device App at api.enyrgy.com** is the proprietary heart of the product. It owns device registration, the MED dosing calculation by Fitzpatrick skin type, the automatic session shut-off, session history, and the gamified habit data. This is the only system that holds real product-usage data, and it is currently the least integrated with the rest of the stack, a gap noted in Sections 3 and 7. The app is developed and maintained by an outsourced engineering partner, Outcode LLC (Utah), which makes vendor continuity and data-access terms an architectural dependency worth tracking.

**LC Email, LC Phone, Trustpilot, FlexOffers, and payment processing** are supporting systems bound to GHL or Shopify. LC Email sends authenticated mail from mg.enyrgy.com; LC Phone provides the toll-free number and A2P SMS; Trustpilot collects reviews fed by the post-purchase workflow; FlexOffers tracks and reports closed sales attributed to affiliates, supporting the affiliate program managed by the Affiliate Manager; payment processing sits behind Shopify checkout and consumer financing.

## 2.3 How The Systems Connect (Conceptual)

At a conceptual level, the stack has three hubs and a set of spokes. **GoHighLevel is the relationship hub**, nearly every lead, contact, and nurture interaction flows through it. **Shopify is the commerce hub**, every purchase originates there. **The Device App is the product hub**, every session and dosing event lives there. The supporting systems (email, phone, reviews, payments) are spokes bound to one of the hubs.

The critical architectural observation is that the three hubs are only loosely connected today. Lead and nurture data is rich and well-integrated inside GHL. Purchase data lives in Shopify. Usage data lives in the Device App. The connective tissue between them, particularly a reliable Shopify-to-GHL purchase sync and any Device-App-to-GHL usage sync, is the principal architectural gap, addressed in Sections 4 and 7.

---

# SECTION 3, DATA ARCHITECTURE

## 3.1 Systems Of Record

A clear system-of-record map is the foundation of data architecture. Today the map is mostly clear, with one explicitly unresolved boundary.

| Data Domain | System of Record | Notes |
|-------------|------------------|-------|
| Leads & contacts | GoHighLevel | 56 fields, ~92 tags; authoritative for all pre- and post-sale relationship data |
| Funnel/pipeline state | GoHighLevel | Five pipelines, stage history, lead score |
| Marketing consent (email/SMS) | GoHighLevel | Consent tags, opt-in capture, suppression markers |
| Purchases & orders | Shopify | Checkout, payment, transactional order record |
| Product catalog & pricing | Shopify | Storefront source of truth for what is sold |
| Device registration & sessions | Device App (api.enyrgy.com) | MED dosing, session history, usage/habit data |
| Reviews | Trustpilot | Third-party, fed by GHL post-purchase workflow |
| Investor accreditation status | GoHighLevel | accredited_verified tag is the compliance gate |
| Financial / capital records | External (finance/CFO systems) | Outside the marketing stack; not unified here |

## 3.2 The Core Data Flow

The intended end-to-end data flow for a consumer follows the value chain:

1. A lead is generated by a channel (podcast, social, referral) and lands on an entry point, a landing page, a quiz, or a contact form.
2. The entry point fires a capture workflow in GHL, which creates the contact, applies funnel and ICP tags, and enrolls the contact in the correct nurture series. GHL is now the system of record for this person as a lead.
3. The person purchases through Shopify. Shopify becomes the system of record for the transaction.
4. **The purchase fact needs to flow back into GHL** so the contact's pipeline stage advances to Ordered, post-purchase onboarding fires, and the contact stops receiving prospecting nurture. This back-flow is the Shopify-to-GHL sync, and it is the most important missing integration (Sections 4 and 7).
5. The customer registers and uses the device through the Device App. Usage data accumulates at api.enyrgy.com. **Whether and how this usage data should flow into GHL** (for retention, reviews, and reactivation triggers) is an open design question.

## 3.3 Consent And Segmentation Data

Consent data deserves its own treatment because it is both a data-architecture and a compliance concern. Email and SMS consent are captured at the point of opt-in and represented in GHL as tags. SMS consent in particular is captured through a dual-checkbox web form (separate marketing and non-marketing consent, both unchecked by default) and represented so that downstream automation can honor it. The suppression system (the magnet_lead and drip_bypass tags) is a data-architecture mechanism that prevents a contact from being processed by more than one automation path at once; it exists because GHL trigger filters cannot express a negative tag condition, so the exclusion is enforced as in-workflow logic. The full mechanics are in Implementation Guide Section 24.

## 3.4 Data Governance Gaps

Three governance issues are open and are consolidated in Section 7. First, **canonical metric ownership** is unassigned: although the company metrics are now reconciled to a single set of figures (Section 7.5), no single system or document is the designated owner that keeps them consistent as they change. Second, **no master-data process** reconciles a person who exists as both a Shopify customer and a GHL contact; identity resolution across the two hubs is manual. Third, **device usage data is siloed** in the Device App with no defined flow into the relationship or commerce hubs.

---

# SECTION 4, INTEGRATION ARCHITECTURE

## 4.1 Integration Topology Today

Integration in the current stack is webhook- and form-driven rather than built on a central integration bus. The live integration points are:

| Integration | Mechanism | Status |
|-------------|-----------|--------|
| Landing pages to GHL | Inbound webhooks to GHL capture workflows | Live (Synthesis Gap, Recovery) |
| Forms to GHL | Native GHL form submission triggers | Live (contact, accreditation, testimonial, SMS opt-in) |
| Quiz to GHL | Webhook to WF-12 | Pending verification |
| GHL to LC Email | Native within LeadConnector | Live (mg.enyrgy.com authenticated) |
| GHL to LC Phone | Native within LeadConnector | Live; A2P approved & verified |
| GHL to Trustpilot | Review-request workflow | Live |
| DNS / domain to email | GoDaddy Domain Connect | Live (SPF, DKIM, CNAME, MX verified) |
| Shopify to GHL |, | **NOT BUILT** |
| Device App to GHL |, | **NOT BUILT** |
| OEM / Lumanova data boundary | Manual / tag-based | Informal |

## 4.2 Live Webhook Endpoints

Two consumer capture webhooks are live and tested end to end:

- **Synthesis Gap (WF-15):** services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/fd32493c-6ec1-4e55-9edb-75399aa53a34
- **Recovery (WF-18):** services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/3ae538d7-81a9-42a7-9e18-5e7c8b19b84a

Each capture workflow applies its tags (type_consumer, magnet_lead, drip_bypass, and the relevant icp_ tag) in a single add-tags action so the tags land together, which the suppression logic depends on.

## 4.3 The Missing Shopify-To-GHL Sync

This is the highest-priority integration gap in the architecture. Without it, a purchase made in Shopify does not automatically advance the buyer's GHL pipeline stage, does not fire post-purchase onboarding, and does not stop prospecting nurture. The practical consequence is that a customer can continue to receive "why haven't you bought yet" messages after they have bought, a brand and trust risk, not merely an inconvenience.

A correct design needs to decide three things, each an open decision in Section 7: the trigger (Shopify order-created or order-paid webhook), the identity match (email is the likely key, but the master-data gap in Section 3 means duplicates are possible), and the action set in GHL (advance pipeline to Ordered, apply unit_ordered, fire WF-06 onboarding, apply drip_bypass to suppress prospecting). Until this is built, the workaround is manual: a human must mark the purchase in GHL, which violates the top-of-funnel principle that anything benefiting from speed and consistency should be automated.

## 4.4 The Device-App Data Boundary

The Device App at api.enyrgy.com holds the only true product-engagement signal Enyrgy has, who is actually using their device, how often, and how well. Today that signal does not reach the relationship hub. A future integration could use session milestones (for example, sessions_10_complete) to trigger review requests, identify churn risk for reactivation, and give Commercial buyers usage reporting. The boundary is noted as a deliberate Phase 2-plus opportunity rather than an urgent gap, because the business runs without it today, but it is the richest untapped data source in the stack.

## 4.5 OEM / Lumanova Boundary

The Lumanova relationship is a manufacturing and white-label arrangement: Enyrgy manufactures, Lumanova sells Luma D Light under its own brand at the same MSRP. The data boundary today is informal and tag-based (type_partner, source_oem_lumanova). As additional OEM partners are added (the stated goal is one to two more), this boundary should be formalized so that partner-sourced leads and any shared data have a defined, auditable path rather than living as ad hoc tags. This is flagged as an open decision in Section 7.

---

# SECTION 5, SECURITY & COMPLIANCE ARCHITECTURE

Compliance at Enyrgy is not a policy document that sits beside the system; it is enforced inside the system as gates that block non-compliant actions. Three regulatory regimes drive the architecture.

## 5.1 Securities Compliance (Reg D)

The investor funnel carries the strictest controls because it touches securities law. The central mechanism is the **accreditation gate**: the accredited_verified tag in GHL is a hard gate, and no message containing offering details, return percentages, or PPM content is permitted to send to a contact who lacks it. The Audit and Compliance agent scans every investor-bound message before it sends. In the cold investor drip, touches one through six are credibility and traction only; offering content (touch seven, including the PPM) sends only after accreditation. All investor materials are approved by a securities attorney before being loaded into GHL, and the commitment-and-close stage (term sheet, promissory note, KYC/AML, wire) is entirely human-owned. This gate is the single most important compliance control in the stack and must survive any future automation change unbroken.

## 5.2 Messaging Compliance (A2P / CTIA / TCPA)

Outbound SMS is governed by carrier and federal messaging rules. The architecture enforces these through: a dual-checkbox web opt-in (separate marketing and non-marketing consent, both unchecked by default, neither required to submit the form, with sender identity, message-type disclosure, frequency, rate disclosure, and STOP/HELP language); a public privacy policy that states SMS consent is never shared with third parties; and required opt-out and sender-identity language on outbound messages. SMS sends solely from the toll-free number 888-316-1695, approved via Toll-Free Verification (July 28, 2026). There is NO 10DLC / local number on the account (an earlier draft incorrectly referenced a 10DLC registration). SMS sending is now active; outbound messages honor opt-out consent and ramp gradually during the mg.enyrgy.com sending-domain warmup. The consent representation in GHL is what allows downstream automation to honor opt-out reliably.

## 5.3 FDA Wellness Guardrails

The platform is a wellness device, not a medical device, and makes no medical claims. This boundary is enforced in content rather than in code: a prohibited-words list (treat, cure, diagnose, disease, prescription, FDA-approved, and similar) is scanned before content ships, and a compliance workflow (WF-09) flags any contact or content carrying medical-claim risk. All client-facing content is reviewed against the January 2026 FDA guidelines for wellness products before use. The architectural point is that the wellness-versus-medical line is a compliance control with real legal weight, and the prohibited-words scan is its enforcement point.

## 5.4 Data Security And Privacy

Email authentication (SPF, DKIM, DMARC alignment) is in place through the dedicated sending domain, which protects both deliverability and brand integrity against spoofing. Sensitive financial and personal actions, entering payment credentials, executing wires, signing instruments, are deliberately kept human-owned and outside the automation layer. As the Device App holds health-adjacent usage data, any future Device-App-to-GHL integration (Section 4.4) must be designed with that data's sensitivity in mind; this is called out as an open decision rather than assumed solved.

---

# SECTION 6, INFRASTRUCTURE ARCHITECTURE

## 6.1 Domains And DNS

| Domain / Subdomain | Purpose |
|--------------------|---------|
| enyrgy.com | Primary brand site, source of truth for approved terms and framing |
| shop.enyrgy.com | Shopify storefront and checkout |
| go.enyrgy.com | GHL funnels and landing pages (recovery-protocol, synthesis-gap, sms-opt-in) |
| api.enyrgy.com | Device application (registration, dosing, session tracking) |
| mg.enyrgy.com | Dedicated email sending domain (LC Email) |

DNS is managed at the registrar with GoDaddy Domain Connect handling the email-domain records (SPF, DKIM, CNAME, MX) automatically. SSL is issued on the sending domain.

## 6.2 Email Sending Infrastructure

The email layer was rebuilt onto a dedicated sending domain to solve a hard platform constraint: GHL allows only one Gmail connection per sub-account, which had forced the two founders to compete for a single sending identity. The dedicated domain mg.enyrgy.com, authenticated once, can send from any @enyrgy.com address with the per-message From set per workflow. Scott is the sender on all workflows. The domain is in reputation warmup (Stage 1): consumer opt-ins one at a time are a healthy warmup pattern, and the 600-plus existing-customer list must not be bulk-sent during warmup but ramped gradually.

## 6.3 Telephony

The toll-free number is +1 888-316-1695 on LC Phone. Voice integrity has passed and SHAKEN/STIR is approved. A2P SMS is approved and verified (Section 5.2); SMS is now active.

## 6.4 Physical Facility

Manufacturing and fulfillment operate from 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017 (Made in USA), relocated from the prior Scottsdale facility. The facility-address rollout across live customer- and carrier-facing systems (Shopify policies, Google Business Profile, product labels, shipping materials, OEM listings) is substantially complete as of June 2026, with one known exception tracked in the GHL WIP punch list (the Shopify Privacy Policy still shows the prior Scottsdale address and references the wrong policy subdomain). The architectural record notes Phoenix as the canonical facility.

---

# SECTION 7, OPEN ARCHITECTURAL DECISIONS

This section consolidates every unresolved design question so none hides inside a layer. Each item names the decision, why it matters, and where it is referenced.

## 7.1 System-Of-Record Ownership (HIGH)

**Decision needed:** a definitive, documented system-of-record map, ratified rather than inferred, including the rule for resolving a person who is both a Shopify customer and a GHL contact. **Why it matters:** every integration depends on knowing which system wins when two disagree. **Referenced in:** Sections 2.3, 3.1, 3.4.

## 7.2 Shopify-To-GHL Purchase Sync (HIGH)

**Decision needed:** the trigger (order-created vs. order-paid), the identity-match key, and the GHL action set. **Why it matters:** without it, buyers receive prospecting nurture after purchase, and pipeline state is wrong; it is the highest-leverage missing integration. **Referenced in:** Sections 2.3, 3.2, 4.1, 4.3.

## 7.3 Device-App Data Flow (MEDIUM)

**Decision needed:** whether and how api.enyrgy.com usage data flows into GHL, with privacy treatment for health-adjacent data. **Why it matters:** it is the richest untapped engagement signal, useful for reviews, retention, churn, and commercial reporting. **Referenced in:** Sections 2.2, 3.2, 4.4, 5.4.

## 7.4 OEM / Partner Data Boundary (MEDIUM)

**Decision needed:** a formalized, auditable data path for OEM partners as the program grows beyond Lumanova. **Why it matters:** ad hoc tags will not scale to multiple partners. **Referenced in:** Sections 2.2, 4.5.

## 7.5 Metric Governance (MEDIUM)

**Decision needed:** designate which document or system owns canonical company metrics going forward, so they stay consistent as they change. **Resolved (this version):** the canonical figures are a $3.5M capital raise, 25,000-plus treatments completed, and a return rate under 1%. These supersede the earlier variances in source materials (raise previously stated as $2.5M; treatments as 24,000-plus; return rate as 0%). **Why it matters:** these numbers appear in investor, marketing, and partner contexts where inconsistency erodes credibility. **Referenced in:** Section 3.4 and the front matter. For the GHL/CRM layer, the Implementation Guide (now at v3.8.4) reflects these figures; the remaining open item is assigning a single owner above that layer.

## 7.6 Paperclip Activation (operational, not architectural)

The agent layer is designed and its workflows are built and published, but the Paperclip connection itself is a pending Phase 2 task. Until it is live, the workflows run on GHL-native automation and human operation. This is tracked as a roadmap item; the architecture already accommodates it.

---

# SECTION 8, APPENDIX: SYSTEM & ENDPOINT REFERENCE

**GHL sub-account:** GtXjla7Ld1dordsTWrVy

**Key URLs:**
- Brand site: enyrgy.com
- Store / order: shop.enyrgy.com/products/uvb-light-therapy
- Device app: api.enyrgy.com
- Recovery landing: go.enyrgy.com/recovery-protocol
- Synthesis Gap landing: go.enyrgy.com/synthesis-gap
- SMS opt-in: go.enyrgy.com/sms-opt-in

**Live capture webhooks:**
- Synthesis Gap (WF-15): services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/fd32493c-6ec1-4e55-9edb-75399aa53a34
- Recovery (WF-18): services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/3ae538d7-81a9-42a7-9e18-5e7c8b19b84a

**Forms:**
- Consumer inquiry: api.leadconnectorhq.com/widget/form/dclY1TB3jA3eitWEQaCo
- Accreditation: api.leadconnectorhq.com/widget/form/DBQBL51stonmfRcUBsMe
- Testimonial: api.leadconnectorhq.com/widget/form/OjahkWeVDeozQkfG9dW2

**Telephony:** +1 888-316-1695 (LC Phone, toll-free; A2P approved & verified)

**Email:** mg.enyrgy.com (LC Email; SPF/DKIM/CNAME/MX verified; SSL issued; Stage 1 warmup)

**Facility:** 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017 (Made in USA)

**Companion document:** Enyrgy GHL CRM Implementation Guide v3.7, the authoritative reference for the CRM/marketing-automation layer (fields, tags, pipelines, drips, workflows WF-01 through WF-18, ICP-Dartboard).

---

*CONFIDENTIAL, Enyrgy Inc, 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017, enyrgy.com, Sunlight. Evolved., Enterprise Architecture v1.0*
