# ENYRGY - Paperclip Phase 2 Setup Guide

**AI Agent Organization for GHL Sales, Marketing, and Revenue Automation**

Version 1.0 · July 13, 2026 · Author: Scott Hansbury, Co-founder & CEO, Enyrgy Inc

**Companion to:** Enyrgy GHL Implementation Guide v3.9 (ground truth) and Enyrgy GHL WIP-3 (tracker). This guide is the operational build plan for Phase 2. It does not change any decision in the Implementation Guide; it executes the agent layer that guide already designed.

Brand: Sunlight. Evolved. · Accent Sunrise Orange #E64C38 · Montserrat · No em-dashes anywhere · Peer-to-peer voice.

---

## 1. Purpose and Scope

Phase 1 (GHL foundation) is complete: sub-account, 56 custom fields, roughly 92 tags, 5 pipelines, 6 calendars, SMS number, 6 forms, and the consumer ICP-Dartboard funnel (WF-11 through WF-20) live and tested. Today the workflows run on GHL-native automation and human operation.

Phase 2 stands up the agent layer on top of that foundation. When it is live, autonomous agents own capture, routing, nurture, scoring, monitoring, and compliance enforcement inside GHL, while humans own every moment that needs judgment, trust, or authority. This guide takes you from an empty Paperclip install to a tested, governed, 16-agent organization operating your GHL sub-account.

Scope of this document:

- What Paperclip is and how it connects to GHL
- Prerequisites and key constants
- The reconciled org chart (16 core agents, plus 6 recommended future additions)
- Step-by-step: deploy, connect, load the knowledge base, configure each agent
- The compliance gate as a hard approval gate
- Agent-to-workflow mapping
- Governance (budgets, heartbeats, approval gates, config revisioning, rollback)
- A 5-contact test plan with pass and fail criteria per agent
- Go-live sequence and rollback

Out of scope: any change to the funnels, drips, or workflows themselves. Those are defined and locked in Implementation Guide v3.9.

---

## 2. What Paperclip Is and How It Fits Enyrgy

Paperclip is an open-source, self-hosted platform for orchestrating AI agents as an organization. It gives you an org chart, roles, budgets, heartbeats, tickets, approval gates, config revisioning, and safe rollback. Two properties matter most for Enyrgy:

1. **Bring-your-own-agent.** Paperclip does not build the agents. It orchestrates agents you supply (Claude-based agents, HTTP agents, and adapter-based agents). We supply Claude-based agents and point them at GHL.
2. **Governance is built in.** Task checkout and budget enforcement are atomic (no double-work, no runaway spend). Agents resume the same task context across heartbeats instead of restarting. Approval gates are enforced, config changes are revisioned, and a bad change can be rolled back. This is exactly what a compliance-sensitive investor funnel requires.

How the pieces fit:

```
Paperclip (orchestration: org chart, budgets, heartbeats, approval gates, rollback)
        |
   Enyrgy agents (Claude-based, one per role)
        |
   GHL API (sub-account GtXjla7Ld1dordsTWrVy: contacts, tags, pipelines, workflows, conversations)
        |
   GHL-native workflows WF-01 .. WF-20 (already built and published)
```

Important framing: the agents do not replace the GHL workflows. The workflows remain the execution rails. The agents decide, route, score, monitor, and enforce, then act through the GHL API to move contacts, apply tags, send messages, create tasks, and flag humans. Until Paperclip is live, those same decisions are made by GHL-native logic and by hand. Phase 2 hands them to the agent org.

---

## 3. Prerequisites and Key Constants

Confirm each before you start. Values are locked from Implementation Guide v3.9 and the Session 6 handoff.

| Item | Value |
|------|-------|
| GHL Sub-Account ID | GtXjla7Ld1dordsTWrVy |
| Sending domain | mg.enyrgy.com (LC Email, verified, Stage 1 warmup) |
| Default sender | Scott Hansbury / scott@enyrgy.com (on all workflows) |
| Phone | +1 888-316-1695 (Toll-Free, LC Phone) |
| Facility | 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017 - Made in USA |
| Order URL | https://shop.enyrgy.com/products/uvb-light-therapy |
| Consumer Unit MSRP | $2,995 |
| Commercial Unit MSRP | $8,950 |
| Per-session cost | $2.30 |
| Total raise | $3.5M at 12% / 3yr, $50K minimum |

Technical prerequisites:

- **A host for Paperclip.** Self-host via Docker (a small always-on VPS or a managed host such as Zeabur). Agents run on heartbeats, so the host must stay up.
- **A GHL Private Integration token** scoped to sub-account GtXjla7Ld1dordsTWrVy. Create it in GHL under Settings, Private Integrations. Grant only the scopes the agents need (Section 6).
- **Model access** for the Claude-based agents (API key with sufficient budget).
- **The knowledge base assets** listed in Section 7, exported and ready to load.
- **Attorney sign-off already captured** on the PPM and accreditation rule (Section 11). Do not wire investor financial content until this is loaded.

---

## 4. The Agent Org Chart (Reconciled)

**Count correction.** The built organization is 16 agents: 3 in the C-Suite, 7 in the COO Division, and 6 in the CRO Division. The Session 6 handoff states 16, which is correct. WIP-3 states a 24-agent organization, which is an error and should be corrected to read: "16-agent core organization (22 with all six recommended Phase 2 additions)." The six recommended additions (Section 16) would bring the total to 22 if all are built, never 24.

```
CEO Agent (Executive Orchestrator) -> escalates to: Human founders
|
+-- COO Agent (Operations Head) -> escalates to: CEO Agent
|     COO Division (7):
|       - Dispatcher
|       - Onboarding
|       - Quality Control
|       - KB Manager
|       - Sentinel
|       - Audit and Compliance
|       - PRD Gatherer
|
+-- CRO Agent (Revenue Head) -> escalates to: CEO Agent
      CRO Division (6):
        - Sales Scout
        - Sales Outreach
        - SDR
        - Client Success Manager
        - Referral and Reviews
        - Reactivation
```

Guiding rule for every agent (from the Implementation Guide core philosophy): agents do anything that benefits from speed, consistency, and scale. Humans do anything that benefits from judgment, trust, and authority. The moment a prospect signals real intent (books a call, replies with a real question, commits capital), it becomes a human conversation, and the agent applies `drip_bypass` so no automated message interrupts a live dialogue.

---

## 5. Step 1 - Deploy Paperclip

1. Provision the host (Docker on a persistent VPS or managed host).
2. Deploy Paperclip per its self-host instructions. Confirm the dashboard loads and the scheduler and heartbeat services are running.
3. Create the organization named "Enyrgy Inc." Set the timezone to America/Phoenix so heartbeats and daily jobs (for example the 8am Sentinel sweep) fire on local time.
4. Set an organization-level spend budget and alert threshold so total agent spend cannot run away. Set conservative per-agent budgets in Section 13; you can raise them after the test.
5. Create the three division nodes (C-Suite, COO Division, CRO Division) so agents can be attached to the correct parent for escalation.

Do not create agents yet. Connect GHL and load the knowledge base first, so every agent is born with tools and facts.

---

## 6. Step 2 - Connect GHL

Agents act on GHL through the GHL API using the Private Integration token for the sub-account.

1. In GHL, Settings, Private Integrations, create a token named "Paperclip Agent Layer." Record it as a secret in Paperclip (never paste it into an agent prompt).
2. Grant only these scopes: Contacts (read/write), Conversations and Conversations Messages (read/write), Opportunities and Pipelines (read/write), Tags (read/write), Workflows (read and enroll), Calendars (read), Forms (read), Custom Fields (read). Withhold billing, settings, and user-management scopes.
3. Register a single shared GHL tool (HTTP tool) in Paperclip that all agents can call, pointed at the sub-account with the token. Expose these actions to agents: get and update contact, add and remove tag, get and move opportunity stage, enroll in workflow, send message, create task, read conversation. Every agent uses this one tool; role limits are enforced by each agent's instructions, not by separate credentials.
4. Test the connection: have Paperclip fetch a single known test contact by ID and read its tags. Confirm read works before granting any write action in the test.

Least-privilege note: the compliance posture depends on scope discipline. No agent should be able to change account settings, add users, or touch billing. Only the actions above.

---

## 7. Step 3 - Load the Knowledge Base

The KB Manager agent owns this, but you load the initial set. Every agent reads from the shared KB; none may invent facts. Required contents (from Implementation Guide v3.9, KB Manager section):

- Clinical study data: +111% Vitamin D, 100% of participants reached optimal, 12-week study
- Advisor bios: Dr. Bruce Hollis, Dr. Samantha Kimball, Dr. William Grant
- All approved talking points (Guide Section 15)
- All objection scripts (Guide Section 22)
- Current pricing: Consumer $2,995, Commercial $8,950; per-session cost $2.30; ROI model 6.0x Year-1
- Facility: 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017; Made in USA
- Prohibited words list (Guide Section 14)
- Referral terms
- Approved product name and trademarked terms: Enyrgy Vitamin D Primal Light Platform (first reference), BioCalibrated Sunshine, Triple-Pathway Advantage
- Brand voice constants: Sunrise Orange only, Montserrat, no em-dashes, peer-to-peer voice, signature block
- **Attorney-confirmed compliance rule (verbatim, Section 11)**
- Nitric oxide framing rule (Section 11)

Load the KB as a versioned document set in Paperclip so config revisioning applies. When a fact changes, the KB Manager updates the KB, the change is revisioned, and every agent reads the new version on its next heartbeat.

---

## 8. Step 4 - Configure the CEO Orchestrator

Create the CEO Agent first. It is the top of the org and the only agent that escalates directly to the human founders. Paste this as its instruction block (adjust bracketed host details to your install):

> **Role:** You are the CEO Agent for Enyrgy Inc, the executive orchestrator of a 16-agent organization operating the GHL sub-account GtXjla7Ld1dordsTWrVy. You do not send prospect-facing messages yourself. You route work across the COO and CRO divisions, resolve cross-division conflicts, oversee OEM and partner matters, and decide what escalates to the human founders (Scott Hansbury, David Letourneau, Brian Cameron).
>
> **Own:** cross-division routing, strategic escalation, OEM oversight, and final arbitration when the COO and CRO agents disagree.
>
> **Escalate to humans when:** any legal or securities question is unresolved, any spend exceeds the org threshold, any agent has flagged `requires_human_review` for more than 24 hours, or any event touches an OEM contract (currently Lumanova / Luma D Light).
>
> **Never:** approve investor financial content, override the compliance gate, or change pricing. Those are human or compliance-gate decisions.
>
> **Facts:** read only from the shared knowledge base. Never invent a number, claim, or policy. Brand voice is peer-to-peer, Sunrise Orange, Montserrat, and contains no em-dashes.

Then configure the COO Agent and CRO Agent (division heads). Each has a short instruction block: the COO Agent owns capacity, ops quality, and compliance oversight and escalates to the CEO Agent; the CRO Agent owns funnel conversion, drip performance, and pipeline health and escalates to the CEO Agent. Both read from the KB, neither sends investor financial content, and both enforce `drip_bypass` on any contact in live human conversation.

---

## 9. Step 5 - Build the COO Division (7 Agents)

For each agent below, create it under the COO Division node, attach the shared GHL tool and the KB, set the budget and heartbeat from Section 13, and paste the instruction block. Every block inherits the same standing rules: read facts only from the KB, brand voice with no em-dashes, apply `drip_bypass` when a human conversation is live, and escalate rather than guess.

**9.1 Dispatcher** - Routes inbound leads.
Trigger: a new contact enters GHL (form, webhook, or import). Function: identify the funnel type (Consumer, Commercial, Investor, Partner, or General) from source and tags, then enroll the contact in the correct drip and set `assigned_agent`. GHL scope: read contact and source, add funnel tags, enroll in workflow. Primary on WF-01 (New Lead Router). Escalates to: COO Agent when funnel type is ambiguous.

**9.2 Onboarding** - New customer activation.
Trigger: `unit_shipped` or purchase confirmed. Function: run the post-purchase onboarding sequence, confirm device registration, and hand ongoing care to the Client Success Manager. Primary on WF-06. Escalates to: CSM.

**9.3 Quality Control** - Data and workflow auditing.
Trigger: weekly heartbeat. Function: review drip engagement, find contacts stuck in a stage, find missing or conflicting tags, and open tickets for the responsible agent. GHL scope: read-only across contacts and opportunities; create tasks. Escalates to: COO Agent.

**9.4 KB Manager** - Knowledge base maintenance.
Trigger: a fact change (pricing, facility, clinical data, attorney guidance) or a monthly heartbeat. Function: update the KB, revision the change, and update any drip template whose facts changed. Escalates to: COO Agent, and to human legal for any investor or compliance wording.

**9.5 Sentinel** - Stale lead monitoring.
Trigger: daily 8am heartbeat (America/Phoenix). Function: find any active-pipeline contact with `last_agent_touch` older than 5 days, flag `requires_human_review`, and notify Scott. Primary on WF-04. Escalates to: COO Agent, then CEO Agent if unresolved.

**9.6 Audit and Compliance** - Content and legal review.
Trigger: before any investor-bound message is sent, and continuously as a guardian on WF-09. Function: scan every outbound message against the prohibited-words list and the compliance gate. If a contact is investor-bound and `accredited_verified` is not Yes, block all financial content (Reg D protection); allow only credibility and traction content. Primary on WF-09 (Compliance Guardian). Escalates to: COO Agent, then human legal. This agent has veto power over any send. See Section 11.

**9.7 PRD Gatherer** - Requirements collection.
Trigger: an investor or commercial contact reaches the due-diligence or discovery stage. Function: send info-gathering emails that capture questions, timeline, and structure preference into the investor or commercial fields. GHL scope: send message, update custom fields. Escalates to: CRO Agent for revenue impact, COO Agent for process.

---

## 10. Step 6 - Build the CRO Division (6 Agents)

Create each under the CRO Division node with the same attachments and standing rules.

**10.1 Sales Scout** - Lead identification.
Trigger: monthly heartbeat. Function: identify top-of-funnel targets and partner-expansion candidates; runs WF-10 (Partner Expansion Trigger). GHL scope: read contacts, create tasks, enroll in partner drip. Escalates to: COO Agent.

**10.2 Sales Outreach** - Multi-touch nurturing.
Trigger: a contact is enrolled in a drip. Function: execute all drip campaigns autonomously, sending each scheduled touch on time, updating engagement, and stopping instantly when `drip_bypass` is set. Primary on WF-02 (5-Minute First Response). GHL scope: send message, update tags and fields. Escalates to: Dispatcher for routing errors, CRO Agent for performance.

**10.3 SDR** - Qualification and booking.
Trigger: lead score reaches 70+ or a demo is requested. Function: send the booking message for the correct discovery call (Consumer round-robin or Commercial), update the lead score, and prepare the same-day proposal after a completed demo. Primary on WF-03 (Lead Score Updater) and WF-05 (Demo Completion to Proposal). Escalates to: CRO Agent, and to human (Scott or David) at the point of live conversation.

**10.4 Client Success Manager** - Post-close retention.
Trigger: onboarding complete. Function: run retention check-ins and quarterly investor updates. Backup on WF-06 and WF-07. Escalates to: CRO Agent.

**10.5 Referral and Reviews** - Growth via existing base.
Trigger: a satisfied customer milestone (post-purchase, positive engagement). Function: run the review and referral activation, and re-feed referrals into the Consumer Drip. Primary on WF-07. Blocked by: Google Business Profile review link (open dependency, Section 17). Escalates to: CSM.

**10.6 Reactivation** - Cold lead revival.
Trigger: a contact completes a full sequence with no engagement, after a 60-day pause. Function: run the 4-touch reactivation. Primary on WF-08. Escalates to: CRO Agent.

---

## 11. Step 7 - Configure the Compliance Gate

This is the most important configuration in Phase 2. Build it as a hard Paperclip approval gate that the Audit and Compliance agent enforces and that no other agent, including the CEO Agent, can override.

**Attorney-confirmed rule (load verbatim into the KB and into the gate):**

> The PPM may be sent to any interested investor after the intro meeting. Accreditation is NOT required before sending the PPM.
>
> Accreditation (`accredited_verified` = Yes) IS required before: subscription agreement, term sheet, wire instructions, or accepting any investment. No exceptions.

Gate rules to configure:

- **PPM delivery (allowed after intro meeting):** the SDR or PRD Gatherer may queue and send the PPM once the contact reaches the Intro Meeting stage. No accreditation check blocks this. Scott sends it directly; the agent has it queued and ready.
- **Commitment gate (hard block):** before any subscription agreement, term sheet, wire instructions, or acceptance of investment, the Audit and Compliance agent must confirm `accredited_verified` = Yes. If not verified, the action is blocked and escalated to human legal. No agent may bypass.
- **Cold-drip financial content (hard block):** for any investor-bound contact where `accredited_verified` is not Yes, block all financial content. Touches 1 through 6 are credibility and traction only (Reg D protection).
- **Prohibited-words scan (every send):** runs before every email, SMS, and voicemail across all funnels.
- **Securities attorney approval:** all investor materials must be attorney-approved before they are loaded into the KB. The PPM document itself is still pending attorney approval (open item, Section 17); keep it as a placeholder until approved.

Nitric oxide framing (load into KB, enforce in review): supplements feed the enzymatic route (substrate to eNOS to NO); UVA triggers enzyme-independent photorelease of NO from preformed skin stores. The light pathway is additive. Never say "no supplement produces nitric oxide."

Wire the current open workflow change: in Investor Drip Touch 7, remove the `accredited_verified` gate from PPM delivery so it sends after the intro meeting, and keep the gate on all commitment, offering-terms, and wire content. The accreditation form is sent when the investor signals intent to commit (Stage 5).

---

## 12. Agent-to-Workflow Mapping

Configure each agent as primary owner of its workflow, with the listed backup or escalation path. This mirrors the Implementation Guide exactly.

| Workflow | Primary Agent | Backup / Escalation |
|----------|---------------|---------------------|
| WF-01 New Lead Router | Dispatcher | COO Agent |
| WF-02 5-Minute First Response | Sales Outreach | Dispatcher |
| WF-03 Lead Score Updater | SDR | CRO Agent |
| WF-04 Stale Lead Sentinel | Sentinel | COO Agent, then CEO Agent |
| WF-05 Demo Completion to Proposal | SDR | Human (Scott / David) |
| WF-06 New Customer Onboarding | Onboarding | CSM |
| WF-07 Review and Referral Activation | Referral and Reviews | CSM |
| WF-08 Reactivation Campaign | Reactivation | CRO Agent |
| WF-09 Compliance Guardian | Audit and Compliance | COO Agent, then Human legal |
| WF-10 Partner Expansion Trigger | Sales Scout | COO Agent |

The consumer funnel workflows WF-11 through WF-20 run on GHL-native automation with `magnet_lead` plus `drip_bypass` suppression already wired. The Dispatcher routes into them; Sales Outreach services their nurture touches. No new mapping is required for those beyond routing and touch execution.

---

## 13. Governance - Budgets, Heartbeats, Approval Gates, Rollback

Use Paperclip's native governance so the org is safe by construction.

**Budgets.** Set a conservative per-agent spend cap for the test (for example, enough for a few dozen actions per day), plus an org-level cap with an alert. Atomic budget enforcement means an agent cannot exceed its cap mid-task. Raise caps only after the test passes.

**Heartbeats.** Set cadences to match the workflow rhythm: Sentinel daily at 8am, Quality Control weekly, KB Manager monthly (plus event-triggered), Sales Scout monthly, all prospect-facing agents on a short heartbeat (minutes) so the 5-minute first-response rule holds. Agents resume the same task context across heartbeats, so a multi-step follow-up is not restarted.

**Approval gates.** The compliance gate (Section 11) is the primary hard gate. Add a second gate: any first send to a brand-new segment or template requires one human approval until the template has a track record. This protects domain warmup on mg.enyrgy.com.

**Config revisioning and rollback.** Every KB change and every agent instruction change is revisioned. If an agent starts behaving wrongly after a change, roll back to the prior revision. Keep the CEO Agent and Audit and Compliance instruction blocks under stricter change control (human approval to edit).

**Handoff rule enforcement.** When any contact crosses into live human conversation, the owning agent sets `drip_bypass`. Sales Outreach and every drip agent must check `drip_bypass` before every send and stop if it is set.

---

## 14. Step 8 - 5-Contact Test Plan

Before go-live, test each agent on 5 sample contacts in a controlled way. Create 5 test contacts with clearly fake details and a `test_contact` tag so nothing reaches a real person or the real sending reputation. Where a step would send an external message, route it to an internal address or set the agent to draft-and-hold for human review.

General pass criteria for every agent: correct action taken, correct tags and fields written, correct escalation path used, no fabricated facts, brand voice intact, no em-dashes, and `drip_bypass` respected.

| Agent | Test setup (5 contacts) | Pass criteria | Fail signals |
|-------|-------------------------|---------------|--------------|
| Dispatcher | 5 contacts, one per funnel type | Each enrolled in the correct drip; `assigned_agent` set | Wrong funnel; no enroll; ambiguous case not escalated |
| Sales Outreach | 5 in an active drip, 2 with `drip_bypass` | Sends only to the 3 without bypass; touches on schedule | Sends to a bypassed contact; wrong timing |
| SDR | 5 with scores 60 to 90 | Books only the 70+; proposal drafted post-demo | Books a sub-70; skips a 70+ |
| Onboarding | 5 marked `unit_shipped` | Onboarding sequence runs; handoff to CSM | No handoff; duplicate onboarding |
| Sentinel | 5 with `last_agent_touch` 3 to 8 days old | Flags only the 5-day-plus; notifies Scott | Misses a stale lead; false flag |
| Audit and Compliance | 5 investor contacts, 2 `accredited_verified` = Yes | Blocks financial content for the 3 unverified; allows PPM after intro for all; blocks commitment content for unverified | Any financial content to an unverified contact; blocks a permitted PPM |
| KB Manager | Change one price in the KB | Revisioned; templates updated; agents read new value | Stale value served after change |
| Quality Control | Seed 2 stuck and 1 mistagged contact | Opens tickets for exactly those 3 | Misses an issue; false ticket |
| PRD Gatherer | 2 at due-diligence stage | Info-gathering email drafted; fields captured | Sends financial terms; no capture |
| Sales Scout | Run monthly job once | Produces a target and partner list | Empty or irrelevant list |
| Client Success Manager | 2 post-close | Check-in drafted; quarterly update scheduled | No check-in; wrong cadence |
| Referral and Reviews | 2 satisfied customers | Referral and review ask drafted; referral re-fed to Consumer Drip | Fires without GBP review link ready |
| Reactivation | 2 cold, past 60-day pause | 4-touch reactivation drafted | Fires before 60 days |
| CEO / COO / CRO | Force one cross-division conflict and one over-threshold spend | Correct routing and escalation to humans | Silent override; no escalation |

Run the test with all prospect-facing sends in draft-and-hold. Only after every agent passes do you switch the low-risk agents (Dispatcher, Sentinel, Quality Control, KB Manager) to autonomous send, and keep investor-touching agents in human-approve mode through go-live.

---

## 15. Step 9 - Go-Live Sequence and Rollback

Go live in stages, not all at once, to protect deliverability and compliance.

1. **Monitoring first.** Turn Sentinel, Quality Control, and KB Manager fully autonomous. They read and flag; low risk.
2. **Routing next.** Turn the Dispatcher autonomous. New leads now auto-route.
3. **Consumer nurture.** Turn Sales Outreach and SDR autonomous for consumer funnels only, respecting `drip_bypass` and domain warmup limits. Do not bulk-send to the 600-plus existing customers during warmup; ramp gradually.
4. **Post-close.** Turn Onboarding, CSM, and Referral and Reviews autonomous (Referral and Reviews only after the GBP review link is live).
5. **Investor funnel last, and never fully autonomous on financial content.** Audit and Compliance runs as the enforcing guardian. All investor sends stay human-approve. PPM delivery is agent-queued, human-sent.

Rollback: if any agent misbehaves, set it to draft-and-hold (or pause it), roll its instruction or the KB back to the prior revision, and let the GHL-native workflow carry that step until the agent is fixed. Because the workflows still exist underneath, pausing an agent degrades gracefully to Phase 1 behavior rather than breaking the funnel.

---

## 16. Phase 2 Recommended Agent Additions (Optional, After Core Is Stable)

The Implementation Guide recommends six future agents. Add them only after the 16-agent core is stable. Adding all six brings the total to 22 (this is the correct upper bound; not 24).

- Reporting Agent (HIGH) - builds and refreshes KPI views
- Proposal Writer (HIGH) - generates the same-day proposal for the SDR
- OEM Pipeline Agent (HIGH) - manages Lumanova and future OEM partners
- Podcast Attribution Agent (MEDIUM) - ties podcast traffic to leads
- Clinical Concierge (MEDIUM) - fields clinical questions from the KB
- Billing Agent (MEDIUM) - handles billing and subscription mechanics

---

## 17. Open Items and Dependencies

These block or gate parts of the build. Track them in WIP-3.

- **PPM document** still pending securities attorney approval. Keep the placeholder in Investor Touch 7 until approved. Do not load unapproved investor material into the KB.
- **Investor Drip Touch 7 in GHL** still needs the `accredited_verified` gate removed from PPM delivery to match the attorney rule (Section 11).
- **Google Business Profile** setup and review link are required before Referral and Reviews (WF-07) can run its review ask. Verify enyrgy.com in Search Console first.
- **Vitamin D Assessment lead magnet** needs its GHL webhook inserted and deployment to go.enyrgy.com/vitamin-d-assessment before the Dispatcher can route its leads.
- **Shopify abandoned-checkout webhook and native integration** feed purchase and abandonment signals the Onboarding and Sales Outreach agents rely on.
- **Domain warmup:** mg.enyrgy.com is in Stage 1. Ramp send volume gradually; do not let autonomous agents spike volume.

---

## 18. Appendix - Reference Values

**Agent assignment tag values** (write to the `assigned_agent` field): `agent_dispatcher`, `agent_sales_scout`, `agent_outreach`, `agent_sdr`, `agent_onboarding`, `agent_csm`, `agent_reactivation`, `escalated_human`.

**Webhooks (consumer capture):**

- WF-12 Tired Test: https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/6c3a7c6c-f1fa-4c85-a03a-a1c42fdfb13d
- WF-15 Synthesis Gap: https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/fd32493c-6ec1-4e55-9edb-75399aa53a34
- WF-18 Recovery: https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/3ae538d7-81a9-42a7-9e18-5e7c8b19b84a
- WF-19 Winter Protocol: https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/ad11ef02-14c8-4dbc-b1dd-bb5c9f3203bd

**Forms:** Consumer Inquiry dclY1TB3jA3eitWEQaCo · Accreditation DBQBL51stonmfRcUBsMe · Testimonial OjahkWeVDeozQkfG9dW2

**Team:** Scott Hansbury (Co-founder & CEO), David Letourneau (President and Co-Founder), Brian Cameron (CFO).

---

*CONFIDENTIAL - Enyrgy Inc - 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017 - enyrgy.com - Sunlight. Evolved.*
