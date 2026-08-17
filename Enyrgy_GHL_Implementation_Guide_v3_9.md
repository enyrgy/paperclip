**ENYRGY**

*Sunlight. Evolved.*

**GoHighLevel CRM Implementation Guide**

AI-Powered Sales, Marketing & Revenue Automation

Powered by Paperclip Autonomous Agents · Version 3.9.6

**Consumer Unit $2,995 · Commercial Unit $8,950 · 600+ Users · 25,000+ Treatments**

Product Sales · Investor Capital · OEM/White-Label Partners · Vendor Network

scott@enyrgy.com · 602-321-0322 · enyrgy.com

Author: Scott Hansbury, Co-founder & CEO, Enyrgy Inc

Last Updated: August 4, 2026 · Version 3.9.6

**v3.9.6 Changes (Session 16, August 4, 2026):** `no_route` and `source_device_app` added to the tag taxonomy (Section 9); the two bypass switches distinguished in Section 11, since `drip_bypass` stops drips while `no_route` stops WF-01 routing and confusing them has already cost time; WF-01's full guard documented (Section 12); a WF-30 to WF-35 register added. "600+ Customers" corrected to "600+ Users" on the cover and in Section 1, since a home unit supports up to six users and the two are not interchangeable. **Live campaign copy is no longer documented in this guide.** It lives in `campaigns/`, one file per workflow, captured from GHL and version-controlled, so nobody maintains two copies. Also corrected the v3.9.5 phantom-completion claim below.

**v3.9.5 Changes (Session 15):** Paperclip is now operating, not just built. Heartbeats are staged and tuned (Sentinel 24h, Quality Control daily, Dispatcher 8h, Sales Outreach 1h, SDR 2h, KB Manager 30d; remaining agents staged behind a watch-cost gate; executives + Audit and Compliance + PRD Gatherer + Onboarding stay event-driven with timer OFF). Two operating rules added from the ENY-20 incident: (1) **Agents confabulate under credit starvation:** when credit-starved or budget-hard-stopped, the org produces confident, specific, FALSE claims (a QC audit and a COO "live verification" both reported a systemic lifecycle failure that did not exist). Verify every agent audit/verification against the live GHL account before acting; escalations are leads, not facts. (2) **Keep Anthropic credit buffered and Paperclip budgets with headroom:** starvation multiplies cost (dying runs re-wake and replay a growing thread) and is the trigger for confabulation. ~~Open platform bug: a run that dies on a credit/budget error must go to `blocked`, never `done`.~~ **RETRACTED in v3.9.6.** The recovery code was read directly: credit and budget failures route to `blocked` and never to `done`, and the only path to `done` is a legitimate watchdog fold requiring a succeeded run. The "ENY-24 flipped to done" report was itself a COO confabulation, which is to say an instance of rule (1) above rather than evidence for a separate defect. No platform fix is needed or pending. Consolidated open items now live in `Enyrgy_Master_TODO.md`.

**v3.9.4 Changes (Session 14):** Applied the Session 13 accreditation carve-out that was missing here: the subscription agreement and term sheet are PRE-ACCEPTANCE and may be shared before accreditation is confirmed. Accreditation gates ONLY wire instructions and accepting funds. Corrected in Stage 5, the Compliance Gate rules, and the pipeline summary (three locations had wrongly gated the subscription agreement and term sheet behind accreditation). Aligns the Guide with KB Sections 12 and 13.

**v3.9.3 Changes (additive):** Added WF-28 Shopify Order Fulfilled and WF-29 Abandoned Checkout Recovery (fed by a Railway service via Shopify client-credentials), completing the Shopify automation set. v3.9.2 added WF-27, closed the drip bypass-gate gap, removed the Investor Touch 7 accreditation gate, and recorded the Shopify native integration. v3.9.1 added WF-21 to WF-26, the custom fields, and the 617-contact base.

**v3.9 Changes:** Investor funnel accreditation sequencing corrected per securities attorney guidance (PPM sent after intro meeting; accreditation required before accepting investment, not before PPM); SHAKEN/STIR confirmed Approved & Verified; KB Manager updated with attorney guidance.

Facility: 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017

**CONFIDENTIAL**

**Table of Contents**

**Table of Contents** 2

**SECTION 1: ENYRGY COMPANY CONTEXT & UPDATED FACTS** 5

Enyrgy at a Glance 5

Updated Company Metrics 5

The Primal Light Platform, Triple Pathway 5

Revenue Streams & Pricing 6

**SECTION 2: AUTOMATION ARCHITECTURE: PAPERCLIP AGENT SYSTEM + HITL** 7

The Core Philosophy 7

Consumer and Commercial Funnels 7

Stage 1: Lead Capture to First Contact 7

Stage 2: Drip Nurture 7

Stage 3: Qualification and Discovery Call Booking 8

Stage 4: Discovery Call 8

Stage 5: Post-Demo Follow-Up to Order 8

Investor Funnel 9

Stage 1: Identification and Initial Outreach 9

Stage 2: Cold Drip 9

Stage 3: Intro Meeting 9

Stage 4: Accreditation 10

Stage 5: Due Diligence 10

Stage 6: Commitment and Close 10

The HITL Framework 11

Practical Daily Operating Rhythm 12

**SECTION 3: PAPERCLIP AI AGENT ORG CHART** 13

C-Suite Layer, 3 Agents 13

COO Division, 7 Agents 13

CRO Division, 6 Agents 14

Agent-to-Workflow Mapping 14

Compliance Gate, Non-Negotiable Rules 15

Phase 2, Recommended Agent Additions 15

KB Manager, Required Knowledge Base Contents 16

**SECTION 4: FIVE FUNNEL TYPES IN GHL** 17

**SECTION 5: GHL ACCOUNT STRUCTURE** 18

Key URLs 18

Phone System 18

**SECTION 6: CALENDAR REFERENCE** 19

**SECTION 7: TEAM REFERENCE** 20

Funnel Ownership 20

**SECTION 8: GHL CONTACT FIELDS** 21

Folder Structure 21

Universal Fields 21

Consumer Fields 21

Commercial Fields 22

Investor Fields 22

Partner Fields 23

Vendor Fields 23

**SECTION 9: TAG TAXONOMY** 24

**SECTION 10: PIPELINES** 25

**SECTION 11: DRIP CAMPAIGNS** 26

Campaign Overview 26

Bypass Logic 26

Consumer Drip Gating (NEW) 26

Consumer Drip, 12 Touch Sequence 26

Investor Drip, 8 Touch Sequence 27

**SECTION 12: CORE WORKFLOWS** 28

WF-01 through WF-10 28

WF-11 through WF-18 (NEW) 28

Lead Scoring Model 28

**SECTION 13: EMAIL SERVICES (REBUILT)** 29

**SECTION 14: CONTENT RULES (UPDATED)** 30

Content Framework (Corrected) 30

Writing Rules 30

Brand Standards (NEW) 30

Nitric Oxide Framing (NEW) 30

Prohibited Words 30

**SECTION 15: APPROVED TALKING POINTS** 31

**SECTION 16: COMMERCIAL ROI MODEL** 32

Model A, Pay Per Modality 32

Model B, Membership Tier Upgrade 32

**SECTION 17: INVESTOR OFFERING DETAILS** 33

**SECTION 18: KEY REFERENCE DATA** 34

**SECTION 19: OEM / WHITE-LABEL PARTNER PROGRAM** 35

Current Partner, Lumanova / Luma D Light 35

Ideal Next OEM / Distribution Partner Profile 35

**SECTION 20: TOP-OF-FUNNEL LEAD GENERATION STRATEGY** 36

Consumer Lead Magnets, ICP-Dartboard (NEW) 36

Consumer Channels 36

Commercial, Investor, Partner/Vendor Channels 37

**SECTION 21: IMPLEMENTATION PHASES AND ROADMAP** 39

**SECTION 22: CLIENT TYPE PLAYBOOKS** 41

Consumer Playbook 41

Commercial Playbook 42

Investor Playbook 42

**SECTION 23: CONTACT** 44

**SECTION 24: CONSUMER FUNNEL: ICP-DARTBOARD SYSTEM (NEW in v3.7)** 45

The Model 45

End-to-End Routing 45

The Suppression System (drip_bypass) 45

The Magnets 46

Email Series 46

Landing-Page Deploy Recipe 46

# SECTION 1: ENYRGY COMPANY CONTEXT & UPDATED FACTS

## Enyrgy at a Glance

Enyrgy is a health-technology company that has developed the world's first intelligent precision phototherapy platform, the Enyrgy Vitamin D Primal Light Platform. The mission: restore the body's natural ability to respond to sunlight with precision, safety, and measurable benefit.

## Updated Company Metrics

  ------------------------------------------------------------------------------------------------------------------------------------------
  **Metric**                 **Value**                                    **Notes**
  -------------------------- -------------------------------------------- ------------------------------------------------------------------
  Customers                  600+                                         Organic growth, zero paid advertising to date

  Treatments completed       25,000+                                      Zero burns, zero adverse events

  Consumer Unit MSRP         $2,995                                      

  Commercial Unit MSRP       $8,950                                      

  Consumer Gross Margin      66%                                          Exceptional for hardware category

  Commercial Gross Margin    78%                                          Higher margin on commercial volume

  OEM White-Label Partner    Lumanova (Luma D Light)                      Active, same MSRP. Seeking 1-2 more.

  Countries with demand      5                                            USA, UK, Canada, France, New Zealand, all inbound

  Return rate                <1%                                         Industry average 5-10%. Major trust signal.

  Manufacturing / Facility   5115 N 27th Ave, Bld 66, Phoenix, AZ 85017   Made in USA. Relocated from Scottsdale to this Phoenix facility.
  ------------------------------------------------------------------------------------------------------------------------------------------

## The Primal Light Platform, Triple Pathway

-   **PATHWAY 1: Vitamin D Synthesis**, 2.4x more efficient than sunlight. 2-4 minutes = 2-4 hours of mid-day sun.

-   **PATHWAY 2: Nitric Oxide Release**, Triggers cardiovascular regulation, blood pressure support. Cannot be delivered orally.

-   **PATHWAY 3: Serotonin Production**, Sleep, mood, and cognitive function. Users report improvements within weeks.

**SALES ANCHOR:** No other solution delivers all three simultaneously. Supplements = Vitamin D only. Sunlight = 60x more time + cancer risk. Red light = different mechanism entirely (90% of Enyrgy customers use both). Enyrgy is a new category.

## Revenue Streams & Pricing

  -----------------------------------------------------------------------------------------------------------------
  **Revenue Stream**                        **Price**            **Margin**        **Status**
  ----------------------------------------- -------------------- ----------------- --------------------------------
  Consumer Unit (DTC direct)                $2,995              66%               Active, primary revenue driver

  Commercial Unit (B2B wellness)            $8,950              78%               Active, growing

  OEM White-Label (Lumanova/Luma D Light)   Wholesale            Variable          Active, 1 signed partner

  Investor Capital (Private Credit)         $50K min, 12%/3yr   N/A               $3.5M offering, active raise
  -----------------------------------------------------------------------------------------------------------------

# SECTION 2: AUTOMATION ARCHITECTURE: PAPERCLIP AGENT SYSTEM + HUMAN IN THE LOOP (HITL)

## The Core Philosophy: Agents Own the Process, Humans Own the Relationship

The dividing line is a rule: agents do anything that benefits from speed, consistency, and scale. Humans do anything that benefits from judgment, trust, and authority. The moment a prospect signals real intent, booking a call, replying with a real question, committing capital, they become a human conversation. Everything before and after that moment is agent territory.

## Consumer and Commercial Funnels

**Stage 1: Lead Capture to First Contact (100% Agent).** The moment a form is submitted, a DM is sent, or a podcast listener emails in, the Dispatcher agent fires WF-01 within minutes. It reads the incoming data (company field = commercial, investor keyword = investor, everything else = consumer), applies the right type_ tag, source_ tag, status_new, drops the contact into the correct pipeline at Stage 1, and enrolls them in the appropriate drip campaign. For consumer leads, WF-02 fires the 5-minute SMS from the Sales Outreach agent before any human has seen the lead. The only exception: a lead via personal introduction or direct text, create the contact manually in the GHL mobile app immediately and apply drip_bypass if you plan to handle it personally.

**Stage 2: Drip Nurture (95% Agent, 5% Human Awareness).** The Sales Outreach agent executes the full Consumer Drip or Commercial Drip autonomously. Emails send on schedule from the sending domain so they look personal. The agent sends the Day 3 SMS and branches on the reply, logs opens/clicks/replies, updates lead score via WF-03, and applies status tags as engagement progresses. Human role: awareness only, via a GHL view filtered to lead score 50+. If a clear buying signal appears before the score threshold, manually apply drip_bypass + escalate to human and jump in.

**Stage 3: Qualification and Discovery Call Booking (Agent Initiates, Human Confirms).** At lead score 70+, the SDR agent sends a booking message for the Consumer Discovery Call (Scott, 15 min) or Commercial Discovery (Scott, 20 min). The Stale Lead Sentinel (WF-04) runs daily at 8am; any active-pipeline contact with last_agent_touch > 5 days gets flagged requires_human_review and notifies Scott. Human takes over when the call is booked.

**Stage 4: Discovery Call (100% Human).** Scott. Capture the key fields (health goal, current solution, Fitzpatrick skin type, finance preference for consumer; business type, locations, decision maker, units for commercial) and run the demo. After the call, mark Has Seen Demo = Yes, that fires WF-05.

**Stage 5: Post-Demo Follow-Up to Order (Agents Resume).** WF-05 triggers the SDR agent to send the personalized proposal same day. The agent owns the next 12 days (Day 2 SMS, Day 5 objection email, Day 8 first-90-days email, Day 12 human-call flag). If they order before Day 12, WF-06 fires on unit_shipped.

## Investor Funnel

The investor funnel has a stricter agent/human split for legal reasons.

**Stage 1: Identification and Initial Outreach.** Sales Scout runs WF-10 monthly, prospecting investor targets. Warm/personal network contacts: enter manually, apply drip_bypass + investor_warm to skip the cold 8-touch and enroll in the 3-touch Warm Sequence.

**Stage 2: Cold Drip (100% Agent, Compliance-Enforced).** Sales Outreach runs the 8-touch sequence. The Audit and Compliance agent scans every investor-bound message: if accredited_verified is not Yes, zero financial content goes out (Reg D protection). Touches 1-6 are credibility and traction only. Touch 2 and 4 are human tasks (LinkedIn connect, direct call) with agent-provided scripts.

**Stage 3: Intro Meeting (Agent Books, Human Owns).** On reply/booking, SDR moves them to Intro Meeting; Scott runs the 15-minute call (overview, traction, team). At the end of the call or immediately after, Scott sends the PPM directly. The agent has it queued and ready. No accreditation required before sending the PPM - this is confirmed compliant per Enyrgy's securities attorney.

**Stage 4: PPM Sent and Due Diligence (Human-Led, Agent-Supported).** PRD Gatherer sends a follow-up email gathering questions, timeline, and structure preference into the investor fields. Humans own DD calls (PPM walkthrough, financials, IP, exit). Agents track last-touch and fire Sentinel alerts if 5+ days pass without contact.

**Stage 5: Accreditation and Commitment (Human-Led, Agent-Enforced Gate).** When an investor signals intent to invest, the SDR agent sends the accreditation form link. Form completion fires the accredited_verified tag. The Audit and Compliance agent confirms the gate is satisfied before any wire instructions are shared or any investment is accepted. The subscription agreement and term sheet are pre-acceptance documents and may be shared before accreditation is confirmed. ATTORNEY CONFIRMED: accreditation is required before accepting any investment. It is NOT required before sending the PPM, subscription agreement, or term sheet.

**Stage 6: Close (100% Human).** Subscription agreement, promissory note, KYC/AML, wire, all human. On investment_funded, the contact moves to Active Investor and CSM takes over the ongoing relationship.

## The HITL Framework

**Agents own:** all lead capture and routing; replies to real leads and drip exceptions (GHL sends the scheduled drip touches and the 5-minute first response, not the agents); lead scoring and pipeline tracking; task creation for human follow-up; compliance gate enforcement; booking confirmations; onboarding, review/referral, and reactivation replies and handoffs; Sentinel monitoring; monthly partner prospecting.

**Humans own:** every live call; outreach to warm/personal intros before funnel entry; discovery calls (Scott); investor intro and post-PPM due diligence conversations; commercial demo/ROI walkthrough; proposal negotiation; any contract/legal/financial instrument; any conversation with frustration, confusion, or complex objections; Sentinel-flagged judgment calls; escalated contacts.

**The single most important handoff rule:** when a contact crosses into live human conversation, apply drip_bypass so the agent does not send another automated email while a personal dialogue is active.

## Practical Daily Operating Rhythm

-   **Each morning (10-15 min):** check three GHL views, requires_human_review (Sentinel flags), lead score 65+ not yet booked (SDR queue), investors between PPM Sent and Commitment.

-   **After every live call:** update GHL immediately (Has Seen Demo, pipeline stage, notes, tags). Garbage in, garbage out.

-   **Weekly:** review drip engagement stats; decide whether to rewrite weak touches.

-   **Monthly on the 1st:** WF-10 fires; review new partner prospects before drip enrollment.

# SECTION 3: PAPERCLIP AI AGENT ORG CHART

Lead enters GHL -> Dispatcher identifies funnel type -> correct drip auto-enrolls -> GHL sends each scheduled touch, agents handle replies and exceptions -> lead score updates after each interaction -> at threshold, SDR books discovery call -> human closes. No engagement after full sequence -> WF-08 re-enrolls for reactivation after 60-day pause.

## C-Suite Layer (3 Agents)

  ---------------------------------------------------------------------------------------------------------------------------
  **Agent**         **Function**             **Key Decisions**                                             **Escalates To**
  ----------------- ------------------------ ------------------------------------------------------------- ------------------
  CEO Agent         Executive Orchestrator   Cross-division routing, strategic escalation, OEM oversight   Human founders

  COO Agent         Operations Head          Capacity, ops quality, compliance oversight                   CEO Agent

  CRO Agent         Revenue Head             Funnel conversion, drip performance, pipeline health          CEO Agent
  ---------------------------------------------------------------------------------------------------------------------------

## COO Division (7 Agents)

  ----------------------------------------------------------------------------------------------------------
  **Agent**               **Function**                 **Drip Role**
  ----------------------- ---------------------------- -----------------------------------------------------
  Dispatcher              Routes inbound leads         Triggers correct drip on lead entry

  Onboarding              New customer activation      Runs WF-06 post-purchase onboarding

  Quality Control         Data/workflow auditing       Reviews drip engagement weekly

  KB Manager              Knowledge base maintenance   Updates drip templates when facts change

  Sentinel                Stale lead monitoring        Flags contacts who dropped out mid-sequence (WF-04)

  Audit and Compliance    Content/legal review         Reviews every drip message; investor gate (WF-09)

  PRD Gatherer            Requirements collection      Deploys info-gathering emails in B2B sequences
  ----------------------------------------------------------------------------------------------------------

## CRO Division (6 Agents)

  -------------------------------------------------------------------------------------------------------
  **Agent**                **Function**                **Drip Role**
  ------------------------ --------------------------- --------------------------------------------------
  Sales Scout              Lead identification         Identifies ToFu targets; runs WF-10 monthly

  Sales Outreach           Multi-touch nurturing       Executes all drip campaigns autonomously

  SDR                      Qualification and booking   Activates after lead score 70+ or demo request

  Client Success Manager   Post-close retention        Onboarding check-ins; quarterly investor updates

  Referral and Reviews     Growth via existing base    Runs WF-07; re-feeds referrals to Consumer Drip

  Reactivation             Cold lead revival           Runs 4-touch reactivation (WF-08)
  -------------------------------------------------------------------------------------------------------

## Agent-to-Workflow Mapping

  ----------------------------------------------------------------------------------------
  **Workflow**                           **Primary Agent**       **Backup / Escalation**
  -------------------------------------- ----------------------- -------------------------
  WF-01 New Lead Router                  Dispatcher              COO Agent

  WF-02 5-Minute First Response          Sales Outreach          Dispatcher

  WF-03 Lead Score Updater               SDR                     CRO Agent

  WF-04 Stale Lead Sentinel              Sentinel                COO Agent -> CEO Agent

  WF-05 Demo Completion to Proposal      SDR                     Human (Scott/David)

  WF-06 New Customer Onboarding          Onboarding              CSM

  WF-07 Review and Referral Activation   Referral and Reviews    CSM

  WF-08 Reactivation Campaign            Reactivation            CRO Agent

  WF-09 Compliance Guardian              Audit and Compliance    COO Agent -> Human legal

  WF-10 Partner Expansion Trigger        Sales Scout             COO Agent
  ----------------------------------------------------------------------------------------

## Compliance Gate, Non-Negotiable Rules

-   **PPM delivery:** PPM may be sent to any investor after the intro meeting. Accreditation is NOT required before sharing the PPM. Confirmed compliant per Enyrgy's securities attorney.

-   **Commitment gate:** accredited_verified = Yes must be confirmed before any wire instructions or acceptance of investment. The subscription agreement and term sheet are pre-acceptance and are NOT gated by accreditation. No exceptions on the money-moving actions.

-   **Prohibited words scan:** runs before every email/SMS/voicemail across all funnels (see Section 14).

-   **Securities attorney:** all investor materials approved before loading into GHL.

## Phase 2, Recommended Agent Additions

Reporting Agent (HIGH), Proposal Writer (HIGH), OEM Pipeline Agent (HIGH), Podcast Attribution Agent (MEDIUM), Clinical Concierge (MEDIUM), Billing Agent (MEDIUM).

## KB Manager, Required Knowledge Base Contents

Clinical study data (+111% Vitamin D, 100% reached optimal, 12-week study); advisor bios (Dr. Bruce Hollis, Dr. Samantha Kimball, Dr. William Grant); all approved talking points (Section 15); all objection scripts (Section 22); current pricing; per-session cost $2.30; facility 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017; prohibited words (Section 14); referral terms; ROI model (6.0x Year-1); **ATTORNEY CONFIRMED: PPM may be sent after intro meeting without accreditation. Accreditation required before accepting investment. Not before PPM.**

# SECTION 4: FIVE FUNNEL TYPES IN GHL

Every contact must be categorized into one of five funnels.

  ------------------------------------------------------------------------------------------------------------------------------------------------
  **Funnel**        **Who They Are**                                          **Conversion Goal**                **Deal Value**
  ----------------- --------------------------------------------------------- ---------------------------------- ---------------------------------
  Consumer          Individuals seeking Vitamin D, mood, sleep, performance   Purchase Consumer Unit             $2,995 + consumables/referrals

  Commercial        Wellness centers, spas, clinics, gyms                     Purchase Commercial Unit(s)        $8,950-$89,500+

  Investor          Accredited investors, family offices                      Fund promissory note ($50K min)   $50,000-$500,000+

  Partner           OEM white-label buyers                                    Signed partnership agreement       Revenue share / wholesale

  Vendor            Contractors, parts suppliers, service vendors             Active vendor contract             Variable
  ------------------------------------------------------------------------------------------------------------------------------------------------

# SECTION 5: GHL ACCOUNT STRUCTURE

## Key URLs

  ------------------------------------------------------------------------------------------------
  **Item**                      **URL**
  ----------------------------- ------------------------------------------------------------------
  GHL Sub-Account               https://app.gohighlevel.com/v2/location/GtXjla7Ld1dordsTWrVy/

  SMS Opt-In Page               https://go.enyrgy.com/sms-opt-in

  Recovery Landing (NEW)        https://go.enyrgy.com/recovery-protocol

  Synthesis Gap Landing (NEW)   https://go.enyrgy.com/synthesis-gap

  Consumer Inquiry Form         https://api.leadconnectorhq.com/widget/form/dclY1TB3jA3eitWEQaCo

  Accreditation Form            https://api.leadconnectorhq.com/widget/form/DBQBL51stonmfRcUBsMe

  Testimonial Form              https://api.leadconnectorhq.com/widget/form/OjahkWeVDeozQkfG9dW2
  ------------------------------------------------------------------------------------------------

## Phone System

-   Number: +1 888-316-1695 (Toll-Free)

-   **Two numbers exist on purpose, do not "correct" one to the other.** 888-316-1695 is the GHL toll-free line, A2P-verified, and is what sends SMS and places outbound calls. **602-321-0322 is Scott's direct number** and belongs in email signatures and the team reference, where a human contact is what the reader wants. The cover, Section 7 and the signature block all use 602 deliberately.

-   System: LC Phone (LeadConnector)

-   A2P Status: Approved & Verified

-   Voice Integrity: Passed

-   SHAKEN/STIR: Approved & Verified

# SECTION 6: CALENDAR REFERENCE

  --------------------------------------------------------------------------------------
  **Calendar**               **Type**          **Owner**               **Duration**
  -------------------------- ----------------- ----------------------- -----------------
  Investor Intro Call        Personal          Scott                   15 min

  Investor Presentation      Collective        Scott + David + Brian   30 min

  Consumer Discovery Call    Round Robin       Scott           15 min

  Commercial Discovery       Round Robin       Scott           20 min

  Partner Exploratory Call   Personal          Scott                   20 min

  Vendor Meeting             Personal          Scott                   20 min
  --------------------------------------------------------------------------------------

# SECTION 7: TEAM REFERENCE

  ------------------------------------------------------------------------------------------
  **Name**           **Role**                 **Email**                    **Phone**
  ------------------ ------------------------ ---------------------------- -----------------
  Scott Hansbury     Co-founder & CEO         scott@enyrgy.com             602-321-0322

  David Letourneau   President & Co-Founder   david@enyrgy.com             602-625-6607

  Brian Cameron      CFO                      bcameron@brian-cameron.com   602-865-9356

  Dennis Lan         Director, Supply Chain  ,                          ---

  Dario Pompeii      Senior Engineer         ,                          ---

  Millie Carrillo    Affiliate Manager       ,                          ---

  Thea Cartier       Social Media Manager    ,                          ---
  ------------------------------------------------------------------------------------------

## Funnel Ownership

  -------------------------------------------------------------------------------
  **Funnel**                      **Primary**             **Backup**
  ------------------------------- ----------------------- -----------------------
  Consumer                        David                   Scott

  Commercial                      David                   Scott

  Investor (Intro)                Scott                   Scott

  Investor (Presentation/Close)   Scott                   David

  Partner                         Scott                   ---

  Vendor                          Scott                   ---

  Onboarding                      Scott                   ---
  -------------------------------------------------------------------------------

# SECTION 8: GHL CONTACT FIELDS

## Folder Structure

  --------------------------------------------------------------------------
  **Folder**                          **Fields**
  ----------------------------------- --------------------------------------
  Universal                           10 fields

  Consumer                            14 fields (incl. testimonial fields)

  Commercial                          8 fields

  Investor                            9 fields

  Partner                             8 fields

  Vendor                              7 fields
  --------------------------------------------------------------------------

## Universal Fields

Client Type (dropdown), Funnel Stage (dropdown), Assigned Agent (text), Last Agent Touch (date, Sentinel monitors >5 days), Lead Score (0-100 auto), Qualification Status (dropdown), Communication Preference (dropdown), Compliance Reviewed (dropdown), How Heard Specific (text), Referral Source Contact ID (text).

## Consumer Fields

Vitamin D Deficient Self Reported, Current Solution, Health Goal, Skin Type Fitzpatrick (I-VI), Finance Preference (Cash/Financing/Installment/Rent/Not Sure), Use Case, How Heard Podcast, Unit Order Date, Unit Ship Date, Sessions Completed, Time Using Enyrgy, Results Noticed, Would Recommend, Marketing Permission.

## Commercial Fields

Business Type, Number of Locations, Current Wellness Offerings, Decision Maker Name, Estimated Units Needed, Estimated Deal Value, Has Seen Demo, ROI Model Sent.

## Investor Fields

Investor Type, Accredited Verified (COMPLIANCE GATE), Minimum Investment Amount, Investment Structure Preference (Debt/Equity/Convertible/SAFE/Not Sure), Target Return, Has Received PPM, Investment Timeline, Amount Committed, Amount Funded.

## Partner Fields

Partnership Model, Partnership Status, Distribution Reach, Territory, NDA Signed, LOI Signed, Contract Expiry, Monthly Units Capacity.

## Vendor Fields

Vendor Category, Vendor Status, Contract On File, Vendor Contract Expiry, Monthly Spend, Primary Contact Name, Vendor Notes.

# SECTION 9: TAG TAXONOMY

Convention: category_value (lowercase, underscores).

-   **Funnel Type:** type_consumer · type_commercial · type_investor · type_partner · type_vendor

-   **Lead Status:** status_new · status_in_drip · status_engaged · status_qualified · status_demo_scheduled · status_demo_done · status_proposal_sent · status_negotiating · status_won · status_lost · status_cold · status_disqualified · status_reactivation

-   **Lead Source:** source_podcast · source_referral · source_website · source_linkedin · source_cold_email · source_event · source_oem_lumanova · source_oem_partner · source_instagram · source_facebook · source_google_ad · source_meta_ad · source_trade_show · source_clinical_advisor · source_reactivation · source_partner_referral · source_word_of_mouth · source_angel_list · source_lead_magnet

-   **Drip Campaign:** drip_consumer_active · drip_consumer_complete · drip_commercial_active · drip_commercial_complete · drip_investor_active · drip_investor_complete · drip_partner_active · drip_partner_complete

-   **Product & Health Goal:** product_consumer_unit · product_commercial_unit · product_oem · goal_vitamin_d · goal_mood_sleep · goal_cardiovascular · goal_athletic_performance · goal_longevity · goal_seasonal_depression · goal_general_wellness · goal_multiple

-   **Agent Assignment:** agent_dispatcher · agent_sales_scout · agent_outreach · agent_sdr · agent_onboarding · agent_csm · agent_reactivation · escalated_human

-   **Lead Magnet:** source_lead_magnet · magnet_lead · magnet_recovery_protocol · magnet_synthesis_gap · high_deficiency_risk · moderate_deficiency_risk · cart_abandoned · sms_consent_given

-   **ICP (consumer funnel):** icp_stack_optimizer · icp_athlete · icp_energy_sleep · icp_sad

-   **Lifecycle & Compliance:** unit_ordered · unit_shipped · unit_activated · sessions_10_complete · review_requested · review_given · referral_given · referral_rewarded · contract_sent · contract_signed · nda_signed · loi_signed · accredited_verified · ppm_sent · investment_committed · investment_funded · do_not_contact · compliance_reviewed · medical_claim_risk · requires_human_review · reactivation_sequence · unsubscribed · vip · ambassador · investor_warm · **drip_bypass** · **no_route** · **source_device_app**

# SECTION 10: PIPELINES

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Pipeline**                        **Stages**
  ----------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  1 Consumer ($2,995)                New Lead -> Website Visit -> Drip Active -> Discovery Call -> Demo Education -> Order Financing -> Ordered -> Unit Shipped -> User Activated -> Active Customer

  2 Commercial ($8,950/unit)         Prospect -> Drip Active -> Discovery -> Demo -> Proposal -> Negotiation -> Contract Signed -> Unit Shipped -> User Activated -> Installation -> Training Scheduled -> Training Complete -> Active Customer

  3 Investor ($3.5M Raise)           Identified -> Drip Active -> Intro Meeting -> Accreditation -> Due Diligence -> Commitment -> Legal and Close -> Active Investor

  4 Partner                           Identified -> Drip Active -> Exploratory -> NDA Discovery -> LOI Stage -> Vetting -> Contract -> Active Partner

  5 Vendor                            Prospect -> Vetting -> Contract Sent -> Contract Signed -> Active -> Preferred -> Inactive
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SECTION 11: DRIP CAMPAIGNS

## Campaign Overview

  ----------------------------------------------------------------------------------------------------------
  **Campaign**             **Touches**   **Duration**   **Trigger Tag**   **Status**
  ------------------------ ------------- -------------- ----------------- ----------------------------------
  Investor Drip, Cold      7             30 days        type_investor     Published

  Investor Warm Sequence   3             7 days         investor_warm     Published

  Consumer Drip            12            21 days        type_consumer     Published (now gated, see below)

  Commercial Drip          10            28 days        type_commercial   Published

  Partner Drip             9             35 days        type_partner      Published
  ----------------------------------------------------------------------------------------------------------

## Bypass Logic

**Two different switches. Do not confuse them, this has caused confusion once already.**

-   **`drip_bypass` stops DRIPS, not routing.** It is read at the Bypass Check that opens each of the five drips. WF-01 New Lead Router does not check it, so a contact carrying `drip_bypass` is still routed and still receives `type_consumer`.

-   **`no_route` stops WF-01 (added August 4, 2026).** It is the permanent off-switch for imports, tests, staff on other domains, and partners. It replaces the old practice of unpublishing WF-01 during an import and remembering to republish it, which was itself a hazard: a silently unpublished router stops routing everything with nothing erroring.

-   Apply drip_bypass + investor_warm to skip cold drip and enroll in the warm sequence.

-   Apply drip_bypass alone to skip all drip enrollment for manually managed contacts.

-   **NEW (v3.7):** Consumer lead-magnet capture workflows apply magnet_lead + drip_bypass to route leads into purpose-built series and suppress the general Consumer Drip.

## Consumer Drip Gating (NEW in v3.7)

The Consumer Drip now begins with a first-step If/Else "Bypass Check": contacts whose tags do NOT include drip_bypass run all 12 touches; contacts with drip_bypass are routed to END. This prevents the collision where magnet leads received both their purpose-built series and the general drip. The Consumer Drip's correct role is now general consumer leads who did NOT enter through a lead magnet.

## Consumer Drip, 12 Touch Sequence

  -----------------------------------------------------------------------------------------------------------------------------
  **Touch**         **Day**           **Type**          **Content**
  ----------------- ----------------- ----------------- -----------------------------------------------------------------------
  1                 0                 SMS               Instant first response, Scott from Enyrgy

  2                 1                 Email             You're doing everything right. So why don't you feel better?

  3                 3                 SMS               Vitamin D levels question, YES or NO branch

  4                 5                 Email             The supplement industry has a dirty little secret

  5                 7                 Internal          Personal call reminder + voicemail script

  6                 8                 SMS               Story follow up after voicemail

  7                 10                Email             Is it safe?, UV safety deep dive

  8                 12                Email             What would $2,995 cost per session? ($2.30 at 5x/week over 5 years)

  9                 14                SMS               90% of customers use red light too

  10                16                Email             For the person who has done their research

  11                19                SMS               Limited availability, Phoenix, AZ manufacturing

  12                21                Email             Closing the loop, leaving the door open
  -----------------------------------------------------------------------------------------------------------------------------

## Investor Drip, 8 Touch Sequence

  ----------------------------------------------------------------------------------------------------------
  **Touch**         **Day**           **Type**          **Content**
  ----------------- ----------------- ----------------- ----------------------------------------------------
  1                 1                 Email             Company overview, no financial details

  2                 3                 Internal          LinkedIn connect reminder, HUMAN TASK

  3                 6                 Email             Traction email, 600+ customers, 25,000+ treatments

  4                 10                Internal          Direct call attempt + voicemail, HUMAN TASK

  5                 14                Email             Team credibility, scientific advisors

  6                 18                Email             Second follow-up, traction update or proof point

  7                 22                Email             PPM delivery, sent after intro meeting is complete (no accreditation required)

  8                 30                Email             Final outreach, closing the loop
  ----------------------------------------------------------------------------------------------------------

ATTORNEY CONFIRMED: Touch 7 PPM fires after intro meeting is marked complete. No accreditation gate on PPM delivery. Accreditation form is sent when investor signals intent to commit (Stage 5). Per Enyrgy's securities attorney.

# SECTION 12: CORE WORKFLOWS

## WF-01 through WF-10

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Workflow**                           **Trigger**                      **Status**        **v3.7 change**
  -------------------------------------- -------------------------------- ----------------- -----------------------------------------------------------------------
  WF-01 New Lead Router                  Contact Created                  Published         **GUARDED (Aug 1, 4 and 7).** After Wait 1 Minute, a Device User Check continues only when `Tags does NOT include source_device_app AND Email does not contain @enyrgy.com AND Tags does NOT include no_route AND Email is not empty`; otherwise END. The device clause keeps Outcode-created users out of lead nurture. The domain and no_route clauses close the leak where inbound mail to mg.enyrgy.com created contacts that fell through to `Default Consumer` and entered the Consumer Drip. **The `Email is not empty` clause (Aug 7) stops inbound phone calls becoming consumer leads.** GHL creates a contact for every inbound call, and routing one accomplishes nothing: with no email the Consumer Drip cannot send, and with no SMS Consent WF-02's gate blocks the text. The only effects were tags and a spurious Opportunity in the Consumer Product Pipeline. Every genuine lead source captures an email, so email-less contacts are effectively only ever call-created.

  WF-02 5 Minute First Response          type_consumer tag applied        Published         **Gated: If/Else skips contacts with drip_bypass**

  WF-03 Lead Score Updater               Native via Manage Scoring        Active            ---

  WF-04 Stale Lead Sentinel              Daily scheduler 8AM              Published         **"Stale Lead" branch requires status_in_drip AND NOT drip_bypass**

  WF-05 Demo Completion To Proposal      Has Seen Demo = Yes              Published         ---

  WF-06 New Customer Onboarding          unit_shipped tag applied         Published         ---

  WF-07 Review And Referral Activation   unit_activated tag applied       Published         ---

  WF-08 Reactivation Campaign            status_cold + 60 day wait        Published         ---

  WF-09 Compliance Guardian              medical_claim_risk tag applied   Published         ---

  WF-10 Partner Expansion Trigger        Monthly scheduler 1st            Published         ---
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------

## WF-11 through WF-20 (Consumer Funnel, all four magnets live)

  ------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Workflow**                     **Trigger**           **Purpose**                            **Tags applied**
  -------------------------------- --------------------- -------------------------------------- --------------------------------------------------------------
  WF-11 Contact Page Router        Contact-page form     Route general contact-form leads       type_consumer

  WF-12 Tired Test Capture         Quiz webhook          Capture Outer Ring quiz leads          type_consumer, magnet_lead, drip_bypass, icp_energy_sleep

  WF-13 Tired Test Emails          Enrolled by WF-12     5-email series (single version, v2)    nurture_longterm at end

  WF-14 Recovery Protocol Emails   Enrolled by WF-18     A/B, 4 emails Day 0/3/6/10             nurture_longterm at end

  WF-15 Synthesis Gap Webhook      Page webhook          Capture Bullseye leads                 type_consumer, magnet_lead, drip_bypass, icp_stack_optimizer

  WF-16 Synthesis Gap Emails       Enrolled by WF-15     A/B series                             nurture_longterm at end

  WF-17 Long-Term Nurture          nurture_longterm tag  7 emails, shared by all magnet leads   ---

  WF-18 Recovery Webhook           Page webhook          Capture Athlete leads                  type_consumer, magnet_lead, drip_bypass, icp_athlete

  WF-19 Winter Protocol Webhook    Page webhook          Capture SAD leads                      type_consumer, source_lead_magnet, magnet_winter_protocol, status_new, icp_sad, magnet_lead, drip_bypass

  WF-20 Winter Protocol Emails     Contact Tag           3 emails, seasonal 3A/3B split         nurture_longterm at end
                                   (magnet_winter_protocol)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------

## WF-21 through WF-26 (added Sessions 9 and 10, all LIVE)

| Workflow | Trigger | Purpose | Tags / Notes |
|----------|---------|---------|--------------|
| WF-21 Vitamin D Assessment Capture | Inbound Webhook | Capture assessment leads, create contact with 11 fields, results email | type_consumer, source_lead_magnet, status_new, magnet_lead, drip_bypass, magnet_vitamin_d_assessment (Standard) plus Dynamic tags from the quiz payload |
| WF-22 Vitamin D Assessment Nurture | Contact Tag (magnet_vitamin_d_assessment) | 3-email solution-aware series, then Add to WF-17 | nurture_longterm at end |
| WF-25 Testimonial Request | Contact Tag (request_testimonial) | Hand-picked ask. If/Else on seg_facility routes facility vs consumer email | one email per branch, branches terminal. Re-Entry Off |
| WF-26 Testimonial Received | Form Submitted (Customer Testimonial Form) | Handle response: notify Scott, queue gift card, thank-you | applies testimonial_submitted, gift_card_pending. Re-Entry Off |
| WF-27 Shopify New Customer Tagging | Shopify order placed | Shield new buyers from lead nurture, flag as customer | applies drip_bypass, source_shopify, status_customer. Re-Entry On |
| WF-28 Shopify Order Fulfilled | Order fulfilled | Apply unit_shipped to trigger WF-06 onboarding | Re-Entry On |
| WF-29 Abandoned Checkout Recovery | Inbound Webhook (from Railway service) | 3-email reassurance recovery, buyer stop-check | tags abandoned_checkout, drip_bypass, source_shopify. Re-Entry On, Stop on Response On |

## WF-30 through WF-35 (added Sessions 15 and 16)

| Workflow | Trigger | Purpose | Notes |
|----------|---------|---------|-------|
| WF-30 FlexOffers Sale Postback | Shopify Order fulfilled (Home System filter) | Fire the S2S postback that pays the affiliate $600 | `{{order.number}}` and `{{order.subtotal_price}}` remain UNVERIFIED. Check Execution Logs on the first real affiliate sale. |
| WF-31 FlexOffers First Touch | **Contact Created** (unfiltered) | Enforce first-in + new-contacts-only attribution | Wait 2 minutes so custom fields finish writing, then copy `flexoffers_refid_incoming` to `flexoffers_refid` only when the latter is empty. **A second Contact Created trigger, which the Session 10 audit predates. Any import must re-check for Contact Created triggers rather than trusting that audit.** |
| WF-32 / 33 / 34 Device App Integration | Inbound Webhook (Outcode) | New users on existing devices | **NOT BUILT.** Awaiting Outcode. Spec sent, four webhook URLs delivered. WF-01's `source_device_app` guard is already in place ahead of it. |
| WF-35 Customer Replied Notification | **Customer Replied** (no filters) | Put the actual reply text in an email to whoever owns the contact | LIVE and fully verified Aug 4. If/Else on `Assigned user Is not empty`; the None branch notifies Scott with a `NO OWNER:` subject prefix. Allow Re-Entry ON, verified. Full capture in `campaigns/WF-35-customer-replied.md`. |

**Why WF-35 exists.** GHL's built-in Conversation Notification carries no message text, proven with a marker string, and its reply path addresses `scott@mg.enyrgy.com`, Scott's own sending-subdomain address, so replying to it reaches nobody without erroring.

**Live campaign copy is not in this guide.** Every email and SMS across all 19 workflows lives in `campaigns/`, one file per workflow, captured from GHL with a per-workflow change log. GHL remains the source of truth: change GHL first, then update the file.

**Testimonial routing tag:** `seg_facility` is a neutral segmentation tag used only by WF-25's If/Else. It is deliberately NOT a drip trigger, so tagging facilities never enrolls them in the Commercial Drip.

**Drip bypass-gate gap (CLOSED Session 11):** all five drips now open with a `NOT drip_bypass` If/Else gate. The Commercial, Partner, and Investor Warm drips previously lacked it and had it added in Session 11, so `drip_bypass` now reliably suppresses every drip.

**Investor Drip Touch 7 (updated Session 11):** the accreditation gate was removed from PPM delivery. The PPM now sends to all interested investors at Touch 7 (post-intro-meeting) per the attorney rule; the accreditation nudge stays for non-accredited investors. Accreditation remains required before commitment/subscription/wire (pipeline stages, unchanged). Open: confirm the PPM email copy is accreditation-neutral.

**Shopify (connected Session 11):** the GHL LeadConnector native integration is live for store `enyrgy`. Historical orders and products backfilled; contacts merge on email; ongoing Contact/Order/Product sync on with the Order Received trigger enabled. WF-27 tags new buyers `drip_bypass` so they skip lead nurture. Remaining: an Order-fulfilled workflow to apply `unit_shipped` (feeds WF-06 onboarding), and the abandoned-checkout webhook (developer).

## Contact custom fields and base (Session 10)

Seven health-profile custom fields added to the Contact object (folder "Health Profile"): Registration Date (Date), Skin Type (Single Options 1-6), Gender (Single Options Male/Female), Height (Text, ft/in), Weight (Number, lbs), Vitamin D Level (Number, ng/mL). Age was intentionally skipped (derivable from birthdate). Birthdate uses GHL's native Date of Birth field.

Existing customer base imported: 617 contacts, tagged `drip_bypass` and `legacy_customer`, with 24 facility contacts also carrying `seg_facility`. Held in the "Initial Customer Load 7-7-26" Smartlist. Safe-import method: WF-01 (the only Contact Created trigger) unpublished during import; zero `type_`, `status_`, `unit_`, or `investor` tags imported so no drip or workflow enrolled them; GHL merges same-email contacts, so shared-email households were split by blanking the child's email while keeping name and phone.

**Webhook URLs:**

-   WF-12 (Tired Test): https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/6c3a7c6c-f1fa-4c85-a03a-a1c42fdfb13d

-   WF-15 (Synthesis Gap): https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/fd32493c-6ec1-4e55-9edb-75399aa53a34

-   WF-18 (Recovery): https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/3ae538d7-81a9-42a7-9e18-5e7c8b19b84a

-   WF-19 (Winter Protocol): https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/ad11ef02-14c8-4dbc-b1dd-bb5c9f3203bd

-   WF-21 (Vitamin D Assessment): https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/d2692dc6-1e9f-466c-8525-58c466c426bd

**Implementation note:** capture workflows apply drip_bypass in the same Add-Tags action as type_consumer so the tags land together. Because GHL trigger filters do not offer a "does not have tag" condition, the bypass gate is a first-step If/Else inside the Consumer Drip, WF-02, and WF-04. Full detail in Section 24.

## Lead Scoring Model

Email Opened +6 · Appointment Confirmed +21 · Contact Reply +11 · Appointment Booked +21.

# SECTION 13: EMAIL SERVICES (REBUILT in v3.7)

The v3.6 Gmail-SMTP model is retired. GHL allows only one Gmail connection per sub-account, which forced Scott and David to compete for a single slot (David's connection replaced Scott's, so all mail sent from David). Replaced by a dedicated LC Email sending domain.

  ----------------------------------------------------------------------------------------------------------------
  **Element**                         **Value**
  ----------------------------------- ----------------------------------------------------------------------------
  Provider                            LeadConnector Email System (LC Email)

  Dedicated sending domain            mg.enyrgy.com

  DNS                                 Auto-configured via GoDaddy Domain Connect (SPF, DKIM, CNAME, MX verified)

  SSL                                 Issued

  Default sender (Dedicated Header)   Scott Hansbury / scott@enyrgy.com


  Warmup                              Stage 1, ramp volume gradually; no bulk blasts during warmup
  ----------------------------------------------------------------------------------------------------------------

**Why this solves the constraint:** one authenticated domain can send from ANY \@enyrgy.com address. The per-message From is set per workflow; only the sending domain is authenticated. scott@ sends from its own identity, DMARC-aligned, with better deliverability and real delivery stats (Gmail SMTP did not report delivered events).

**Operational caution:** the domain is in reputation warmup. Consumer opt-ins one at a time are a healthy warmup pattern. Do NOT bulk-send to the 600+ existing customer list from this domain on day one, ramp gradually.

# SECTION 14: CONTENT RULES (UPDATED in v3.7)

## Content Framework (CORRECTED, supersedes v3.6 "Story Selling OS on all content")

-   **StorySelling OS** -> NARRATIVE/story content ONLY (origin stories, testimonials, social content pulling traffic to guides).

-   **eugene-skill / cub / copy-chief / humanize-pro** -> conversion and research copy (landing pages, guides, conversion emails).

-   **presell-sandwich** -> Problem-Aware buyer copy.

-   **offer-brief / offer-gravity** -> offer framing.

-   **Rule:** match the skill to the asset's JOB, not its topic. Landing pages and guides require a full skills pass even when derived from already-refined material. Evidence-forward credibility (not narrative) is required on research guides and conversion pages for skeptical buyers.

## Writing Rules

-   No m-dashes ever; use commas, periods, or rewrite.

-   Always "Enyrgy Vitamin D Primal Light Platform" on first reference. Deprecated: "Precision Vitamin D Wellness Platform" and "Primal Light Platform" alone.

-   Treatments completed: 25,000+. Customers: 600+. Red light co-use: 90%.

-   Manufacturing / Facility: 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017, Made in USA (relocated from Scottsdale; all labels, listings, and materials should reflect the new address).

-   Referral: $150 off referee, $100 credit referrer.

-   Per-session cost: $2.30 (1,300 sessions over 5 years).

-   Order URL: https://shop.enyrgy.com/products/uvb-light-therapy · Device Registration: https://api.enyrgy.com/

## Brand Standards (NEW in v3.7, locked)

-   Accent: Sunrise Orange #E64C38 only (NO violet/purple/amber).

-   Typography: Montserrat, all weights (Bely Bold Italic unavailable -> all-Montserrat).

-   Text: Deep Charcoal #1A1A1A. Panels: Warm Off-White #F7F4EE, Calm Beige #ECE4CF. Line #E2DBC9. Muted #6B6B66.

-   Approved terms: BioCalibrated Sunshine™ (personalized-dosing/skin-type angle), Triple-Pathway Advantage™.

## Nitric Oxide Framing (NEW in v3.7, applied across all assets)

Supplements feed the ENZYMATIC route (substrate -> eNOS -> NO). UVA triggers enzyme-independent PHOTORELEASE of NO from preformed skin stores (nitrite/nitrosothiols). The light pathway is additive, one a capsule cannot open. The claim "no supplement produces nitric oxide" is false framing and must not be used.

## Prohibited Words (Compliance)

treat, cure, diagnose, disease, prescription, FDA-approved, medical treatment, heal, fix, medication, illness, clinical diagnosis, therapeutic treatment. Review all client-facing content against the 2026 January FDA Guidelines for Wellness Products before use.

# SECTION 15: APPROVED TALKING POINTS

-   Every human body was meant to thrive on sunlight. We just made it safe, personalized and controllable.

-   Restore your body's natural response to sunlight.

-   Activate three biological pathways in 2-4 minutes.

-   25,000+ sessions with zero adverse events.

-   100% of clinical study participants reached optimal Vitamin D levels.

-   2.4x more efficient than sunlight for Vitamin D synthesis.

-   App-controlled, personalized MED protocol, system shuts off automatically.

-   Less than 1% return rate, 5-10x better than industry average.

-   Manufactured in Phoenix, AZ, Made in USA.

-   600+ customers across 5 countries.

-   Lumanova selected our technology to launch Luma D Light.

-   $2,995 consumer / $8,950 commercial.

-   $2.30 per session at 5 sessions/week over 5 years.

-   90% of our customers also use red light therapy.

-   Sunlight. Evolved.

# SECTION 16: COMMERCIAL ROI MODEL

## Model A, Pay Per Modality

$49/month per client to add as standalone modality.

  -----------------------------------------------------------------------
  **Clients**             **Monthly Revenue**     **Annual Revenue**
  ----------------------- ----------------------- -----------------------
  25                      $1,225                 $14,700

  50                      $2,450                 $29,400

  100                     $4,900                 $58,800
  -----------------------------------------------------------------------

Device cost: $8,950. Payback at 50 clients: under 4 months.

## Model B, Membership Tier Upgrade

Device anchors premium tier. Revenue from clients upgrading tiers.

**Commercial anchor:** at 5 sessions/day at $50/session at 250 operating days = $62,500 gross Year 1; after device cost, $53,550 net = 6.0x ROI on a single unit.

# SECTION 17: INVESTOR OFFERING DETAILS

PPM shared after intro meeting. The subscription agreement and term sheet are pre-acceptance and may be shared before accreditation. Wire instructions and acceptance of any investment shared only after accredited_verified = Yes is confirmed.

  ---------------------------------------------------------------------------------------------------------
  **Item**                            **Detail**
  ----------------------------------- ---------------------------------------------------------------------
  Structure                           Private Credit, Promissory Note

  Total Raise                         $3.5M

  Minimum                             $50,000

  Return                              12% per annum

  Term                                3 years

  Interest                            Paid quarterly (postponed first 3 months)

  Conversion Option                   At investor discretion, 20% discount from independent SEC valuation

  Exit Target                         $100-150M in 5 years
  ---------------------------------------------------------------------------------------------------------

# SECTION 18: KEY REFERENCE DATA

  --------------------------------------------------------------------------------------------------------------------------
  **Data Point**             **Value**                                                    **Use In**
  -------------------------- ------------------------------------------------------------ ----------------------------------
  Consumer Unit MSRP         $2,995                                                      All consumer content

  Commercial Unit MSRP       $8,950                                                      All commercial content

  Per-session cost           $2.30 (5x/week, 5 years)                                    Consumer drip, ROI emails

  Treatments completed       25,000+                                                      Trust/credibility messages

  Return rate                <1%                                                         Consumer objection handling

  Clinical study result      +111% Vitamin D                                              Consumer drip

  Efficiency vs. sunlight    2-4 min = 2-4 hours (60x)                                    Consumer drip

  Gross margin, consumer     66%                                                          Investor conversations

  Gross margin, commercial   78%                                                          Investor conversations

  Active OEM partner         Lumanova / Luma D Light                                      Multiple funnels

  Investor offering          $3.5M at 12%/3yr, $50K min                                 Investor drip Touch 7, PPM sent after intro meeting

  Exit target                $100-150M in 5 years                                        Investor conversations only

  Manufacturing / Facility   5115 N 27th Ave, Bld 66, Phoenix, AZ 85017, Made in USA   Consumer drip + trust

  Red light co-use           90% of customers                                             Consumer + commercial

  Referral discount          $150 off referee / $100 credit referrer                    WF-07
  --------------------------------------------------------------------------------------------------------------------------

# SECTION 19: OEM / WHITE-LABEL PARTNER PROGRAM

## Current Partner, Lumanova / Luma D Light

  ------------------------------------------------------------------------------------------------------------
  **Attribute**                       **Details**
  ----------------------------------- ------------------------------------------------------------------------
  Partner Name                        Lumanova

  Product Brand                       Luma D Light

  Pricing                             Same MSRP as Enyrgy: $2,995 / $8,950

  Status                              Active

  Arrangement                         OEM white-label; Lumanova sells under their brand, Enyrgy manufactures

  Exclusivity                         Black Unit

  GHL Tags                            type_partner + source_oem_lumanova + partnership_status active
  ------------------------------------------------------------------------------------------------------------

## Ideal Next OEM / Distribution Partner Profile

Distribution reach 25,000+ active customers; wellness franchise group, major distributor, or DTC health brand; US + at least 1 of UK/Canada/France/New Zealand; 50+ units/month within 12 months; premium science-backed brand fit.

# SECTION 20: TOP-OF-FUNNEL LEAD GENERATION STRATEGY

**TOP-OF-FUNNEL RULE:** Every lead, regardless of source, must be in GHL within 24 hours. For human-sourced leads, enter the contact in the GHL mobile app before leaving the conversation. Leads not in GHL do not exist.

## Consumer Lead Magnets, ICP-Dartboard (NEW in v3.7)

The consumer lead-magnet strategy is implemented as the ICP-Dartboard system (full detail in Section 24). Live entry points:

  -------------------------------------------------------------------------------------------------------------
  **Ring**        **ICP**           **Magnet**                **Entry**                         **Status**
  --------------- ----------------- ------------------------- --------------------------------- ---------------
  Bullseye        Stack Optimizer   Synthesis Gap Guide       go.enyrgy.com/synthesis-gap       Live

  Inner Ring      Athlete           Recovery Protocol Guide   go.enyrgy.com/recovery-protocol   Live

  Inner Ring      SAD (seasonal)    Winter Protocol Guide     go.enyrgy.com/winter-protocol      Live

  Outer Ring      Energy/Sleep      Tired Test (quiz)         go.enyrgy.com/tired-test          Live

  Everyone else   (all others)      contact-form leads        contact form                      Consumer Drip
  -------------------------------------------------------------------------------------------------------------

## Consumer Channels (feed the entry points above)

Podcast appearances (proven #1 channel), organic social (Vitamin D deficiency, seasonal mood, athletic recovery content), paid Meta/Google ads (Phase 2), referral program (WF-07), word-of-mouth/community, Lumanova/OEM channel.

## Commercial, Investor, Partner/Vendor Channels

-   **Commercial:** LinkedIn prospecting, Google Maps scraping, trade shows (ISPA, A4M), OEM partner referrals, existing-customer referrals, red light studios.

-   **Investor:** podcast inquiries, LinkedIn health-tech investors, existing customer network, AngelList/databases, current-investor referrals, real estate/accredited networks.

-   **Partner/Vendor:** OEM/white-label targets (CRITICAL), large distributors, podcast/influencer affiliates, wellness franchises, clinical advisors, tech/app integration partners.

# SECTION 21: IMPLEMENTATION PHASES AND ROADMAP

**Phase 1, GHL Foundation: COMPLETE.** Sub-account, 56 fields, \~92 tags, 5 pipelines, 6 calendars, SMS number, 6 forms, Trustpilot, Shopify policy updates.

**Phase 2, Paperclip Agent Setup: PENDING.** Connect Paperclip via API; configure CEO orchestrator; build COO + CRO divisions; load KB; configure compliance gate; test each agent on 5 sample contacts before going live.

**Phase 3, Drip Campaigns and Workflows: COMPLETE.** All 5 drips, branching logic, compliance gate, all core workflows. **NEW (v3.7): consumer funnel workflows WF-11-18 built and published; drip_bypass gating wired.**

**Phase 4, Content Loading: IN PROGRESS.** Templates loaded; voicemail recordings and commercial ROI PDF still needed; PPM attorney-approved. **NEW (v3.7): four consumer magnet assets built and skill-refined; two landing pages live.**

**Phase 5, Go Live and Optimization: IN PROGRESS.** Two consumer funnels live and tested end-to-end; reporting dashboards and full agent launch still ahead. **NEW (v3.7): dedicated sending domain live; sender identity solved.**

# SECTION 22: CLIENT TYPE PLAYBOOKS

## Consumer Playbook, Discovery Questions

  ---------------------------------------------------------------------------------------------------------------------------------------------------
  **Question**                     **Field**                           **Routing**
  -------------------------------- ----------------------------------- ------------------------------------------------------------------------------
  Vitamin D tested recently?       vitamin_d_deficient_self_reported   Below 40 ng/mL -> high urgency; Unknown -> test kit link

  Currently using for Vitamin D?   current_solution                    Supplements -> absorption advantage; Red light -> complementary (90% use both)

  Main health goal?                health_goal                         Routes to drip variant; personalizes messaging

  Skin tone (Fitzpatrick I-VI)?    skin_type_fitzpatrick               Sets MED protocol expectations

  Personal, family, or gift?       use_case                            Family -> shared value; Athlete -> recovery angle

  How did you hear about us?       how_heard_podcast                   Attribution; which podcast drives conversion
  ---------------------------------------------------------------------------------------------------------------------------------------------------

## Top Consumer Objections

-   **Is this safe? (UV worry):** >90% UVB / <10% UVA, the opposite of sunlight (95% UVA). App calculates personal MED by skin type and shuts off automatically. 25,000+ sessions, zero burns/adverse events.

-   **I take supplements, why this?:** 1 in 4 cannot effectively absorb oral Vitamin D. Supplements deliver one pathway only; they cannot trigger Nitric Oxide or Serotonin. Enyrgy activates all three in 2-4 minutes.

-   **$2,995 is a lot:** $2.30/session over 5 years at 5x/week. Supplements run $600-$1,200/year with absorption uncertainty. Financing available. <1% return rate.

-   **I'll just go outside:** Therapeutic UVB needs 2-4 hours of mid-day sun (plus UVA aging/cancer risk). Enyrgy does it in 2-4 minutes, 60x efficiency, no downside.

-   **What does the FDA say?:** Wellness device, not medical; makes no medical claims. Results backed by peer-reviewed science; advisory board includes Dr. Bruce Hollis.

## Commercial Playbook

**Anchor:** $8,950 unit; at 5 sessions/day at $50 at 250 days = $62,500 Year 1 gross; $53,550 net = 6.0x ROI.

-   **We already have red light:** 90% of Enyrgy customers use both, different biological purposes. Upsell, not replacement.

-   **Would clients pay?:** About three-quarters of people have vitamin D below 30 ng/mL. Operators charge $40-$75/session.

-   **Staff training?:** Included; the app calculates each client's MED and controls the session.

## Investor Playbook, Pitch Flow

1.  Company & Problem (5 min): about three-quarters of people have vitamin D below 30 ng/mL, about one in four trial participants were low responders to supplementation, no scalable UVB solution.

2.  Solution & Technology (5 min): triple pathway, app-controlled, patented LED card, Made in Phoenix AZ.

3.  Traction (5 min): 600+ customers, 25,000+ treatments, <1% return, 5 countries, $14,700+ MRR, zero paid ads.

4.  Market & Model (5 min): $2,995/$8,950/OEM, 66-78% margins.

5.  The Ask (3 min): $3.5M private credit at 12%/3yr, $50K min, exit $100-150M in 5 years (10-15x).

6.  PPM sent after intro meeting. No accreditation required for PPM delivery. Accreditation form sent when investor signals intent to commit.

**Investor Objections:** equity upside -> conversion option at 20% discount to SEC valuation; crowded market -> category of one (all three pathways); exit -> strategic acquisition $100-150M, buyer profiles Philips/Apple Health/Peloton/AG1/LVMH.

# SECTION 23: CONTACT

  ------------------------------------------------------------------------------------------
  **Name**           **Role**                 **Email**                    **Phone**
  ------------------ ------------------------ ---------------------------- -----------------
  Scott Hansbury     Co-founder & CEO         scott@enyrgy.com             602-321-0322

  David Letourneau   President & Co-Founder   david@enyrgy.com             602-625-6607

  Brian Cameron      CFO                      bcameron@brian-cameron.com   602-865-9356

  Dennis Lan         Director, Supply Chain  ,                          ---

  Dario Pompeii      Senior Engineer         ,                          ---

  Millie Carrillo    Affiliate Manager       ,                          ---

  Thea Cartier       Social Media Manager    ,                          ---
  ------------------------------------------------------------------------------------------

www.enyrgy.com · Facility: 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017

# SECTION 24: CONSUMER FUNNEL: ICP-DARTBOARD SYSTEM (NEW in v3.7)

## The Model

Consumer leads are segmented by Ideal Client Profile and routed to purpose-built lead magnets and email series, rather than into one general drip. Testing priority is weighted by ICP value.

  -----------------------------------------------------------------------------------------------------------------------------------------
  **Ring**        **ICP**                                         **Weight**     **Magnet**                **Format**
  --------------- ----------------------------------------------- -------------- ------------------------- --------------------------------
  Bullseye        Stack Optimizer (skeptical, supplement-savvy)   60%            Synthesis Gap Guide       PDF, evidence-forward

  Inner Ring      Performance Athlete                             35%            Recovery Protocol Guide   PDF, evidence-forward

  Inner Ring      SAD Sufferer (seasonal Aug-Oct)                seasonal       Winter Protocol Guide     PDF, validation-first

  Outer Ring      Energy/Sleep Seeker (Problem-Aware)             5%             Tired Test                Interactive QUIZ (not a guide)

  Everyone else   general contact-form leads                     ,           ,                       Consumer Drip
  -----------------------------------------------------------------------------------------------------------------------------------------

Bullseye and Athlete get full A/B testing. Energy/Sleep gets one strong version. Winter is seasonal. The Tired Test is deliberately a quiz, not a guide, the Problem-Aware tired buyer will not open another PDF.

## End-to-End Routing

  --------------------------------------------------------------------------------------------------------------
  **Ring**                   **Entry**                         **Capture WF**   **Nurture WF**   **Long-term**
  -------------------------- --------------------------------- ---------------- ---------------- ---------------
  Bullseye (Synthesis Gap)   go.enyrgy.com/synthesis-gap       WF-15            WF-16 (A/B)      WF-17

  Inner Ring (Recovery)      go.enyrgy.com/recovery-protocol   WF-18            WF-14 (A/B)      WF-17

  Inner Ring (Winter)        go.enyrgy.com/winter-protocol     WF-19            WF-20 (3A/3B)    WF-17

  Outer Ring (Tired Test)    go.enyrgy.com/tired-test          WF-12            WF-13            WF-17

  Everyone else              contact form                      WF-11/WF-01      (none)          Consumer Drip
  --------------------------------------------------------------------------------------------------------------

All magnet leads converge into WF-17 Long-Term Nurture after their magnet series.

## The Suppression System (drip_bypass)

**Problem:** the original architecture routed ALL consumer leads into the Consumer Drip via type_consumer. When magnet funnels were added, magnet leads carried type_consumer AND got their series, so they received both, including off-brand general-drip emails. That is the collision.

**Fix:** two tags applied at capture gate the general automation:

-   magnet_lead, marks a lead-magnet entrant (suppression marker).

-   drip_bypass, universal "handled by a more specific path; skip general automation" signal.

**Where the gate is wired:**

  ----------------------------------------------------------------------------------------------------------------
  **Workflow**                        **Gate**
  ----------------------------------- ----------------------------------------------------------------------------
  Consumer Drip (12-touch)            First-step If/Else: NOT drip_bypass -> run; else END

  WF-02 5-Minute SMS                  If/Else: NOT drip_bypass -> send; else END

  WF-04 Stale Lead Sentinel           "Stale Lead" branch: status_in_drip AND NOT drip_bypass

  WF-12 / WF-15 / WF-18               Apply magnet_lead + drip_bypass with type_consumer in same Add-Tags action
  ----------------------------------------------------------------------------------------------------------------

In-workflow If/Else is used because GHL trigger filters do not offer "does not have tag." Capture workflows must apply drip_bypass in the same action as type_consumer so the tags land together.

## The Magnets

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Magnet**                **ICP**           **Skills**                          **Notes**
  ------------------------- ----------------- ----------------------------------- -------------------------------------------------------------------------------------------------------------------------------------
  Synthesis Gap Guide       Stack Optimizer   cub + humanize + eugene             "Supplements raise a number. Sunlight runs a process." Cascade signature: D3->sulfate->photoproducts->(gap: nitric oxide->serotonin).

  Recovery Protocol Guide   Athlete           cub + humanize + eugene             Bone/injury differentiator; Bogh 2012 trial; stat boxes 14%/11%/50 ng/mL.

  Winter Protocol Guide     SAD               cub + humanize + presell-sandwich   Validation-first; hard clinical-depression disclaimer; cohort = "a lab measure, not a mood measure."

  Tired Test                Energy/Sleep      cub + presell + humanize            Interactive quiz; no PDF.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Hosted PDFs (assets.cdn.filesafe.space/GtXjla7Ld1dordsTWrVy/media/): Synthesis Gap 6a3eb5fae2763b2eec13afcc.pdf · Recovery 6a3fd90fc408020f97c82b7f.pdf · Winter 6a3f1a46163e40d8627248b1.pdf.

## Email Series

  ------------------------------------------------------------------------------------
  **Series**          **WF**            **Structure**       **Skills**
  ------------------- ----------------- ------------------- --------------------------
  Synthesis Gap       WF-16             A/B                 A=cub, B=eugene

  Recovery            WF-14             A/B, Day 0/3/6/10   A=cub, B=eugene

  Tired Test          WF-13             5 emails, single    cub + presell + humanize

  Winter Protocol     WF-20             3 emails, 3A/3B     cub + humanize + presell-sandwich
                                        seasonal split

  Long-Term Nurture   WF-17             7 emails, shared    conversion skills
  ------------------------------------------------------------------------------------

Signature (all consumer nurture): "Carpe diem, / Scott Hansbury / Enyrgy Inc / Co-founder & CEO / scott@enyrgy.com / 602-321-0322 / enyrgy.com", sent from scott@enyrgy.com to match.

## Landing-Page Deploy Recipe (proven)

7.  Create funnel + step; clean slug from the start.

8.  Custom HTML/JavaScript element on a blank step; paste page HTML.

9.  Section -> Width: Full.

10. "Allow Rows to take entire width" -> ON.

11. Custom Code element -> Styles -> Width: 100% (defaults to "auto," which renders narrow, the key step).

12. Connect domain, Publish.

13. Verify in Chrome incognito (NOT Safari, over-caches).

14. Test with a FRESH email (GHL dedupes).

*CONFIDENTIAL, Enyrgy Inc, 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017, enyrgy.com, Sunlight. Evolved., Implementation Guide v3.9.3*
