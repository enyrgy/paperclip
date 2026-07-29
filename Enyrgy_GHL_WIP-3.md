# ENYRGY GHL - Work In Progress (WIP) Tracker
**Review this at the start of every session**

Last Updated: July 28, 2026 (Session 15). See `Enyrgy_Master_TODO.md` for the consolidated open-items punch list.

---

## QUICK STATUS OVERVIEW

| Area | Status |
|------|--------|
| GHL Foundation | Complete |
| All Drip Campaigns (5) | Published |
| All Core Workflows (10) | Published |
| SMS / A2P | Toll-free SMS APPROVED (888-316-1695, July 28) + Voice Integrity + SHAKEN/STIR. NO 10DLC/local number exists on the account. |
| Contact Import | Complete - 617 existing customers imported (Session 10) |
| Vitamin D Assessment Lead Magnet | LIVE - WF-21 capture + WF-22 nurture (Session 9) |
| Testimonial Collection System | LIVE - form video field, WF-25, WF-26 (Session 10) |
| Shopify / GHL Integration | LIVE (Session 11): native connector + WF-27 + WF-28 fulfillment + WF-29 abandoned-checkout recovery (Railway service). Remaining: upgrade Railway off trial |
| Google Business Profile | Verified and LIVE (Session 15). Review link wired into WF-07 Day-14 SMS (Google + Trustpilot). |
| Paperclip Agent Org (17 agents) | GO-LIVE IN PROGRESS (Session 15): heartbeats staged and tuned. ON: Sentinel 24h, Quality Control daily, Dispatcher 8h, Sales Outreach 1h, SDR 2h, Reactivation 6h, KB Manager 30d. Remaining to stage: Referral and Reviews (review/testimonial ready; referral function deferred with the built-in loyalty program), Sales Scout, CSM. Execs + Audit/PRD/Onboarding stay event-driven (timer OFF). |
| Toll-Free A2P Verification (888) | APPROVED (July 28, 2026) - validated for SMS. SMS can now send from 888-316-1695. |
| Paperclip Agent Setup | Phase 2 build COMPLETE (Sessions 12-13). Now operating: approval-card UX + ask-first policy + toggle-bug fixed (Session 15). Standing rule: keep Anthropic credit buffered and budgets with headroom - starvation multiplies cost and causes agent confabulation. |
| External Tasks | Multiple Pending - see Enyrgy_Master_TODO.md |

---

## SECTION 1 - COMPLETED THIS BUILD

### Foundation
- [x] Enyrgy Inc sub-account created
- [x] LC Phone connected
- [x] go.enyrgy.com domain connected via GoDaddy CNAME
- [x] Scott Gmail SMTP connected (scott@enyrgy.com)
- [x] Voice Integrity registration - Passed
- [x] 6 folders created (Universal, Consumer, Commercial, Investor, Partner, Vendor)
- [x] 56 custom contact fields built
- [x] ~92 tags created
- [x] 5 pipelines built (Consumer, Commercial, Investor, Partner, Vendor)
- [x] 6 forms built (Consumer Inquiry, Commercial Inquiry, Investor Inquiry, Partner Application, Accreditation, Testimonial)
- [x] 6 calendars built (Investor Intro, Investor Presentation, Consumer Discovery, Commercial Discovery, Partner Exploratory, Vendor Meeting)
- [x] Scott + David + Brian added as GHL users
- [x] Scott Google Calendar + Zoom connected
- [x] David Google Calendar + Zoom connected
- [x] Brian Outlook Calendar connected
- [x] Trustpilot business account active (enyrgy.com)
- [x] SMS Opt-In funnel page live at go.enyrgy.com/sms-opt-in
- [x] Shopify Privacy Policy updated with SMS section
- [x] Shopify Terms of Service updated with SMS section

### Drip Campaigns (All Published)
- [x] Investor Drip - 8 Touch 30 Day
- [x] Investor Warm Sequence - 3 Touch 7 Day
- [x] Consumer Drip - 12 Touch 21 Day
- [x] Commercial Drip - 10 Touch 28 Day
- [x] Partner Drip - 9 Touch 35 Day

### Core Workflows (All Published)
- [x] WF-01 New Lead Router
- [x] WF-02 5 Minute First Response
- [x] WF-03 Lead Score Updater (via Manage Scoring)
- [x] WF-04 Stale Lead Sentinel
- [x] WF-05 Demo Completion To Proposal
- [x] WF-06 New Customer Onboarding
- [x] WF-07 Review And Referral Activation
- [x] WF-08 Reactivation Campaign
- [x] WF-09 Compliance Guardian
- [x] WF-10 Partner Expansion Trigger

---

## SECTION 2 - IN PROGRESS

### A2P / SMS Registration
| Item | Status | Notes |
|------|--------|-------|
| Phone Number +1 888-316-1695 | Active & Verified | Toll-free |
| Toll-Free SMS Verification | Approved & Verified | Confirmed working |
| Voice Integrity | Passed & Verified | Confirmed working |
| SHAKEN/STIR Voice | Approved & Verified | Confirmed working |

> **CORRECTION (July 28, 2026):** there is NO 10DLC / local number on this account and one was never approved. Earlier entries that listed an "A2P 10DLC Registration" as approved were wrong. SMS runs solely on the toll-free **888-316-1695** via its Toll-Free Verification (approved July 28, 2026). There is no longer any local number associated with the account.

**A2P History:**
- Error 30909 (CTA verification) - fixed consent text and checkbox placement
- Error 30896 (Opt-in error) - updated Privacy Policy, fixed broken form links, added no-sharing statement, resubmitted
- 4 items approved, verified, and confirmed working: Phone Number (toll-free), Toll-Free SMS, Voice Integrity, SHAKEN/STIR. NO 10DLC/local number exists (corrected July 28).

**A2P Resubmission Fields (save these - GHL resets on every session):**
- Opt-In Form URL: https://go.enyrgy.com/sms-opt-in
- Privacy Policy: https://shop.enyrgy.com/policies/privacy-policy
- Terms of Service: https://shop.enyrgy.com/policies/terms-of-service

### Contact Import
| Item | Status | Notes |
|------|--------|-------|
| Investor Import Template | Built | Excel template with 3 tabs |
| Investor Spreadsheet | In Progress | 100+ contacts being entered |
| Import Process | Ready | Waiting for spreadsheet completion |
| Existing customer import | COMPLETE (Session 10) | 617 imported, tagged drip_bypass + legacy_customer (24 also seg_facility). Safe method: WF-01 unpublished during import, zero type_/status_/unit_ tags imported. Shared-email households split by blanking the child's email. Landed in "Initial Customer Load 7-7-26" Smartlist. |

**Import Instructions:**
1. Complete the Excel spreadsheet using the template
2. Go to GHL -> Contacts -> Import
3. Upload CSV (convert Excel to CSV first)
4. Map columns to GHL fields
5. Assign to Investor Pipeline
6. Apply type_investor tag to trigger drip enrollment

---

## SECTION 3 - PENDING TASKS

### HIGH Priority

| Task | Owner | Notes |
|------|-------|-------|
| Google Business Profile Setup | IN REVIEW (Session 11) | Local store, Wellness center, video submitted; awaiting Google approval, then grab review link for WF-07 |
| Import investor contacts | Scott | Complete spreadsheet first |
| A2P final approval | Complete | Approved and verified by carrier |
| PPM document in Investor Touch 7 | DONE | Attorney-approved; no longer a placeholder, the approved PPM is used in Touch 7. |
| Deploy Vitamin D Assessment Lead Magnet | DONE (Session 9) | LIVE at go.enyrgy.com/vitamin-d-assessment; WF-21 capture + WF-22 nurture live |
| Shopify Abandoned Checkout Recovery | DONE (Session 11) | WF-29 + Railway service (Hobby) + Shopify custom app, all live |
| Shopify -> GHL Native Integration | DONE (Session 11) | Connected; WF-27 + WF-28 + WF-29 built |

### MEDIUM Priority

| Task | Owner | Notes |
|------|-------|-------|
| David Gmail SMTP / per-workflow sender | Complete | Rebuilt as LC Email (mg.enyrgy.com); Scott is per-workflow sender on all workflows |
| Facility address updated in live systems | Complete | 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017 reflected everywhere |
| Winter Protocol workflow + landing page | Complete | WF-19 + WF-20 live; go.enyrgy.com/winter-protocol live |
| Investor Presentation Calendar Fix | Scott/David/Brian | Currently showing all times available - need to verify conflict detection |
| Shopify Referral App | DEFERRED (Jul 28) | Not installing a third-party app; referral/loyalty will be built into the next Enyrgy version |
| Trustpilot connect Shopify | Scott | Automate review invitations post-purchase |
| Commercial form SMS consent | DONE (Session 11) | Consent text + checkbox added to Commercial Inquiry Form |
| Partner form SMS consent | DONE (Session 11) | Consent text + checkbox added to Partner Application Form |
| Testimonial form link on enyrgy.com | Scott | Add link to testimonial form in post-purchase follow up |

### LOW Priority / Future

| Task | Owner | Notes |
|------|-------|-------|
| CNAM Voice registration | Scott | Displays "Enyrgy" on outbound caller ID |
| Paperclip agent setup | IN PROGRESS (Session 12) | 16-agent org (22 with all six Phase 2 additions). Railway (Hobby) ready. Following Enyrgy_Paperclip_Phase2_Setup_Guide |
| Reporting dashboards | Scott | Build KPI views in GHL reporting |
| 600+ existing customer import | DONE (Session 10) | 617 imported, tagged drip_bypass + legacy_customer (24 seg_facility); NOT type_consumer (kept out of drips) |
| Commercial Inquiry Form - add to go.enyrgy.com | Developer | Embed or link to GHL form |
| Partner Application Form - add to go.enyrgy.com | Developer | Embed or link to GHL form |

---

## SECTION 4 - KNOWN ISSUES & BUGS

| Issue | Impact | Status | Notes |
|-------|--------|--------|-------|
| Add Tags in email actions not working | Low | Known GHL bug | Tag dropdowns empty until contacts exist - fix after import |
| Investor Presentation Calendar conflict detection | Medium | Under investigation | Shows all times available despite 3 calendars connected |
| Paperclip phantom-completion | High | Open (fork fix needed) | A run that dies on "Credit balance is too low" was auto-flipped to `done` (ENY-24) with no execution, masking the item. Fix: credit/budget-error deaths must go to `blocked`, never `done`. |
| Accessory reorders triggered device onboarding | Medium | RESOLVED (Jul 28) | WF-28 applied `unit_shipped` on ANY fulfilled Shopify order, so an accessory-only reorder (wall mount) re-fired WF-06 onboarding days after delivery. Fix: gated WF-28's Order-Fulfilled trigger to Home-System orders only. WF-06 triggers on the `unit_shipped` tag, so the single filter fully controls it. |
| Agent confabulation under credit starvation | High | Mitigated by discipline | When credit-starved, agents produce specific, plausible, FALSE claims (ENY-20 false alarm: invented tag states, misread a workflow's last-edit date as last-run). Mitigation: keep credit buffered; verify every agent audit/verification against the live GHL account before acting. |
| David Gmail SMTP not connected | Resolved | LC Email rebuilt | Dedicated sending domain mg.enyrgy.com; Scott is per-workflow sender on all workflows |
| SMS workflows inactive | Resolved | Toll-Free A2P approved Jul 28 | All SMS touches now active |
| From Number field missing in SMS actions | Resolved | Toll-Free A2P approved Jul 28 | From Number confirmed active and working |
| SHAKEN/STIR not configured | Resolved | Approved & Verified | Confirmed working - prevents spam tagging on outbound calls |

---

## SECTION 5 - PLACEHOLDER LINKS TO UPDATE

These placeholders exist in workflows and need real URLs:

| Location | Placeholder | Real URL |
|----------|-------------|---------|
| WF-07 Review SMS | RESOLVED | Google review link live in the Day-14 SMS: https://g.page/r/CfN5Rj0CdmrfEAI/review (Trustpilot offered as secondary) |
| WF-07 Referral Email | DEFERRED (Jul 28) | Referral link intentionally held. No third-party referral app; the next Enyrgy version ships a built-in loyalty/referral program that will supply it. |
| WF-07 Testimonial Email | RESOLVED | Testimonial form link now live in the email: https://api.leadconnectorhq.com/widget/form/OjahkWeVDeozQkfG9dW2?notrack=true |
| All workflows | Order URL | https://www.enyrgy.com/products/uvb-light-therapy |
| Investor Touch 7 | PPM download | Attorney-approved |

---

## SECTION 8 - LEAD MAGNET - VITAMIN D ASSESSMENT

### What Was Built
A fully functional 7-step interactive Vitamin D Deficiency Assessment quiz. Built as a single HTML/JS file deployable as a GHL funnel page or Shopify embed.

**File location:** Saved in this session - request rebuild from Claude if needed. Describe as: "Rebuild the Enyrgy Vitamin D Assessment lead magnet from Section 8 of the WIP tracker."

### How It Works
- 7 steps: Health Goal -> Vitamin D Tested -> Current Solution -> Outdoor Time -> Skin Type -> Finance Preference -> Contact Info
- Calculates a deficiency risk score from answers (tested status, outdoor time, skin type)
- Shows personalized results page: risk badge, score meter, pathway explanation, next steps
- Personalizes CTA based on finance preference (financing vs. purchase outright)
- Includes SMS consent checkbox with compliant language
- Sends all data to GHL via webhook on submit

### GHL Field Mapping (Quiz -> GHL)
| Quiz Answer | GHL Field | Notes |
|-------------|-----------|-------|
| Health Goal | health_goal | Applied as tag + field |
| VD Tested status | vitamin_d_deficient_self_reported | Mapped: optimal=No, low/deficient=Yes, never=Unknown |
| Current Solution | current_solution | Comma-separated string |
| Skin Type | skin_type_fitzpatrick | Exact Fitzpatrick type string |
| Finance Preference | finance_preference | Cash / Financing / Rent / Not Sure |
| First Name | firstName | GHL standard field |
| Last Name | lastName | GHL standard field |
| Email | email | GHL standard field - primary dedup key |
| Phone | phone | GHL standard field |

### Tags Applied Automatically on Submit
- `type_consumer` - always
- `source_lead_magnet` - always
- `status_new` - always
- `goal_[value]` - matches their health goal selection
- `sms_consent_given` - if SMS checkbox checked
- `high_deficiency_risk` - if score 60+
- `moderate_deficiency_risk` - if score 35-59

### Deployment Steps
1. In GHL -> Automation -> Workflows -> create new webhook trigger workflow
2. Copy the inbound webhook URL GHL generates
3. In the lead magnet HTML, replace `YOUR_GHL_WEBHOOK_URL_HERE` with that URL
4. Add workflow actions: Create/Update Contact -> Apply Tags from payload -> Enroll in Consumer Drip -> Fire WF-01
5. Deploy HTML to GHL funnel page at go.enyrgy.com/vitamin-d-assessment
6. Add entry points: Shopify product page soft CTA, podcast bio link, Instagram bio link

### Abandoned Checkout Webhook Spec (Shopify -> GHL)
- Shopify webhook events: `checkouts/create` + `checkouts/update`
- Route through Zapier or Make
- Filter: email present + `completed_at` is null + `abandoned_checkout_url` not null
- Wait 1 hour, then push to GHL: create/update contact, apply `cart_abandoned` tag
- Enroll in 3-touch abandoned cart sequence (same-day SMS, Day 2 financing email, Day 5 ROI email)
- Cancel sequence trigger: Shopify `orders/create` for same email removes `cart_abandoned` tag

### Other Shopify Webhooks to Build
| Shopify Event | GHL Action | Workflow Triggered |
|---------------|------------|-------------------|
| Customer Created | Create contact | WF-01 if no unit_ordered tag |
| Order Created | Apply unit_ordered tag | Pipeline -> Ordered stage |
| Order Fulfilled | Apply unit_shipped tag | WF-06 Onboarding begins |
| Order Refunded | Apply status_lost, flag CSM | Internal alert |
| Device registered at api.enyrgy.com | Apply unit_activated tag | WF-07 Review + Referral begins |

---

## SECTION 9 - PERMANENT DECISIONS & CONTENT CONSTANTS

**These are locked decisions. Do not change without explicit instruction. Load these at the start of every session.**

### Pricing & Math
| Item | Value | Notes |
|------|-------|-------|
| Consumer Unit MSRP | $2,995 | |
| Commercial Unit MSRP | $8,950 | |
| Per-session cost (consumer) | **$2.30** | $2,995 / 5 years / (5x/week x 52 weeks) = $2,995 / 1,300 sessions |
| Usage assumption | 5 sessions per week | Always use this - not 3x/week |
| Sessions per year | 260 | 5 x 52 |
| Sessions over 5 years | 1,300 | |
| Referral discount | $150 off for referee | |
| Referral credit | $100 credit for referrer | |
| Investor minimum | $50,000 | |
| Investor return | 12% per annum | |
| Investor term | 3 years | |
| Total raise | $3.5M | Corrected from $2.5M (Session 7); matches Enterprise Architecture and Implementation Guide v3.9 |

### Content Rules (Permanent)
| Rule | Value |
|------|-------|
| No m-dashes | Never use - in any content. Use commas, periods, or rewrite. |
| Table gridlines | All tables in every .docx use visible gridlines (borders on all cells, not just header underlines). |
| No icons | Do not use icons, checkmarks, emoji, or decorative glyphs. Indicate state with color, fill, borders, or plain text. |
| Brand authority | Enyrgy_Brand_Style_Guide_v2 governs all brand, design, and copy decisions. |
| Minimum age | 18 years or older (resolved Session 7; retires the earlier 21 language). |
| Product name | Always "Enyrgy Vitamin D Primal Light Platform" - never just "Primal Light Platform" |
| Treatments completed | 25,000+ |
| Customers | 600+ |
| Red light co-use | 90% of customers |
| Manufacturing | Phoenix, AZ - Made in USA (never Scottsdale) |
| Framework | Story Selling OS on all client-facing content |

### Funnel Ownership
| Funnel | Primary | Backup |
|--------|---------|--------|
| Consumer calls | Scott | - |
| Commercial calls | Scott | - |
| Investor Intro | Scott | - |
| Investor Presentation / Close | Scott | David |
| Partner / Vendor / Onboarding | Scott | - |

---

## SECTION 10 - NEXT SESSION CHECKLIST

Start each session by reviewing these items:

1. **SMS / A2P** - Toll-free SMS approved and verified (888-316-1695, July 28), plus Voice Integrity and SHAKEN/STIR. NO 10DLC/local number exists on the account.
2. **Toll-Free Status** - Approved & Verified
3. **Import Status** - Existing customer base (617) imported Session 10. Investor spreadsheet still in progress.
4. **David SMTP / Sender** - Complete - LC Email (mg.enyrgy.com); Scott is per-workflow sender
5. **Google Business Profile** - Has this been set up?
6. **Lead Magnet Deployment** - Has the webhook URL been inserted and page deployed?
7. **Shopify Integration** - Has native GHL-Shopify connector been turned on?
8. **Facility Address** - Updated in all live systems (5115 N 27th Ave, Bld 66, Phoenix, AZ 85017)

---

## SECTION 11 - SESSION LOG

### Session 13: July 22-24, 2026
- **GHL-to-MCP bridge built + deployed.** Standalone TypeScript MCP server (repo enyrgy/enyrgy-ghl-mcp), 16 GHL tools (8 read, 8 write), tests passing, deployed to Enyrgy Railway (US West, healthy). Local git set to commit as Enyrgy via an SSH host-alias so Ledgerix work is unaffected. The GHL Private Integration token had leaked into Paperclip logs and was ROTATED (rotate-and-expire-now). Token + GHL_MCP_TOKEN live only in Railway.
- **CFO agent added (17 total).** New CFO reports to CEO and is the single owner of the investor funnel / securities process, so the compliance gate has one clean target. Instruction Blocks pack updated to 17 and the accreditation rule corrected pack-wide.
- **Accreditation rule corrected.** The subscription agreement and term sheet are PRE-ACCEPTANCE and may be sent without accreditation; accreditation gates ONLY wire instructions and accepting funds. Updated in the KB (Sections 12-13), the Instruction Blocks, and the Attorney-Confirmed Rule.
- **Knowledge Base loaded as v2.** Company Skill enyrgy-knowledge-base, all 15 sections, enabled on all agents. Fixed a gotcha where the skill first held only frontmatter (KB body never saved).
- **Compliance gate built AND proven live.** Paperclip Rule "When CFO uses makes-changes -> Ask first," CFO-scoped so other agents scale; plus 8 company-wide require_approval policies on the write tools (all agents' writes are ask-first, safe draft-and-hold). Live test PASSED: a CFO write stopped for approval with skip-permissions on. The system moves no money; the gate protects sends and record changes, not funds.
- **Budgets, permissions, heartbeats.** Per-agent monthly USD caps under the $25/mo account wall; least-privilege permission pass; heartbeats are interval-based (anchor to enable-time) and left OFF until launch, with a go-live enable checklist saved.
- **Bridge flipped to read-write** (GHL_MCP_READONLY=false; GET / -> "mode":"read-write").
- **GHL tools rolled out to all agents (RESOLVED + GO-LIVE PROVEN).** Paperclip's original connection would not re-scan 8->16 (no UI control); a workaround app "ghlv2" scanned all 16 and was installed on the CFO for the gate test. Broadening it via the profile Assign wizard kept erroring ("catalog entry selector must belong to the same company"). A DB inspection (Claude Code + Railway Postgres) showed the DB was healthy: access is driven by tool_connection_installs rows, and the 12 operational agents simply had none. FIX: a reviewed DB transaction mirroring putConnectionInstalls added 1 install + 1 binding per agent (identical to the working execs). Verified (installs 5->17, shape-identical, CFO policy byte-for-byte unchanged, reversible via saved rollback.sql), and a live SDR read task confirmed. All 12 operational agents are now live on the 16 read-write tools.
- **Status: Paperclip agent org is GO-LIVE READY.** Remaining is launch-day only: optional least-privilege tidy (remove GHL from CEO/COO/CRO/KB Manager), the 5-contact draft-and-hold test, enabling heartbeats per the checklist, and optionally relaxing the 8 company-wide write approvals later for non-CFO scale.
- Paperclip lessons: "delete" a connection = soft archive (leaves catalog rows); a working catalog-refresh endpoint (POST /api/tool-connections/:id/catalog/refresh) exists but is not wired to any UI button; agent tool access is by installs, not profiles.

### Session 12: July 20-21, 2026
- **Paperclip deployed LIVE** on Enyrgy's own Railway account (entity-separate from Ledgerix). Public URL https://enyrgy-paperclip-production.up.railway.app. Docker single-service deploy (avoided Railway Agent's 110-service monorepo split by using Empty Project + one service). Postgres attached; persistent /paperclip volume; fixed the root-owned-volume EACCES by making docker-entrypoint.sh chown /paperclip to node unconditionally. Bootstrapped first admin via interactive `pnpm paperclipai onboard` (not --yes) then claimed CEO/owner (scott@enyrgy.com).
- **Enyrgy Anthropic account** created for billing separation; $25 credits. Hard cap: $25/mo monthly spend limit AND auto-reload OFF (prepaid balance is a second hard floor). ~$8 used on setup this session; resets Aug 1.
- **Org + CEO Agent** created via the setup wizard (mission set; Claude Code adapter; env check passed). Cancelled Paperclip's auto-fired demo task subtree ("Hire your first engineer" + Founding Engineer agent + 6 sub-tasks) so the workspace is clean.
- **GHL Private Integration token** "Paperclip Agent Layer" created with 15 least-privilege scopes (contacts r/w, conversations r/w, conversations/message r/w, opportunities r/w, locations/tags r/w, workflows.readonly, calendars.readonly, calendars/events.readonly, forms.readonly, locations/customFields.readonly). Withheld billing/users/oauth/payments/settings.
- **KEY FINDING:** this Paperclip build has NO native GHL connector. Its Apps area supports only Zapier or bring-your-own MCP (via URL). Connecting GHL requires a small MCP bridge service (Node, deploy to Enyrgy Railway) that holds the token and exposes the shared GHL actions, connected via the BYO MCP URL. This is the first task next session and unblocks the 15-agent build.
- Build status vs Phase 2 Guide: Step 1 Deploy DONE; Step 2 Connect GHL in progress (token done, bridge pending); Steps 3-9 (KB, agents, compliance gate, test, go-live) not started.

### Session 11: July 19, 2026
**Completed:**
- Connected the GHL LeadConnector Shopify native integration (store handle enyrgy). Historical Order + Product import ON, Contact import OFF (617 already imported; GHL merges on email). Ongoing Contact/Order/Product sync ON with the Order Received trigger enabled. Ran it with WF-01/06/07 unpublished during the backfill, then re-published. Extra contacts the sync created (partners/staff/older buyers) are untagged and inert; Paul Barattiero (OEM partner) tagged drip_bypass + source_oem_partner.
- Built WF-27 Shopify New Customer Tagging: trigger Shopify order placed, applies drip_bypass + source_shopify + status_customer, Re-Entry ON. Shields new buyers from lead nurture.
- Added the first-step drip_bypass gate (Bypass Check: NOT drip_bypass to run, else END) to the Commercial, Partner, and Investor Warm drips, which lacked it. All five drips now honor drip_bypass.
- Removed the accreditation gate on Investor Drip Touch 7: PPM now sends to all interested investors post-intro-meeting (added PPM email to the Not-Yet-Accredited branch; nudge retained). Accreditation still required before commitment/wire (pipeline, untouched). OPEN: confirm PPM email copy is accreditation-neutral.
- Toll-free A2P: the 888 Toll-Free Verification was Rejected (30496, use-case/summary inconsistency), corrected to a marketing-consistent description with go.enyrgy.com/sms-opt-in as opt-in proof, resubmitted, and APPROVED July 28, 2026. SMS now sends from the toll-free. (Correction: an earlier note here referenced a "10DLC (approved)" number; that was wrong. There is no 10DLC/local number on the account.)
- Google Business Profile: set up as Local store (eligible via on-site treatments for registered users), category Wellness center. Google required video verification (Search Console instant overridden, likely shared GCU address); Scott records the walkthrough video next.
- Abandoned Checkout Recovery built LIVE end to end. Shopify custom app "Enyrgy Abandoned Checkout Sync" (Dev Dashboard, client-credentials auth, read_checkouts + read_orders, legacy install flow OFF, installed). Railway service (Enyrgy account, trial) deployed from GitHub repo enyrgy/enyrgy-abandoned-checkout, self-scheduling every 20 min, validated live (scanned=0 clean). WF-29 Abandoned Checkout Recovery published: inbound webhook -> create contact -> tags (abandoned_checkout, drip_bypass, source_shopify) -> Email 1 -> wait 1d -> Purchased Check (status_customer -> END) -> Email 2 -> wait 2d -> Email 3, Re-Entry On, Stop on Response On, reassurance copy (no discount). WF-27 updated to also apply status_customer.

**Still pending:**
- Railway upgraded to Hobby plan (Session 11); the abandoned-checkout service is always-on. Done.
- Shopify fulfillment: WF-28 built (Order fulfilled -> unit_shipped -> WF-06). Abandoned checkout: DONE (WF-29 + Railway live).
- Optional: custom fields for cart value + checkout id (high-value escalation); real end-to-end abandoned-cart test.
- GBP video verification, then wire the review link into WF-07.
- Toll-free TFV carrier decision.

- Send first testimonial batch; weekly gift-card fulfillment.

### Session 10: July 18, 2026
**Completed:**
- Testimonial collection system built and tested LIVE in GHL. Added a video File Upload field to the Customer Testimonial Form (File Types = All so it accepts video; reply-by-email fallback for large files); reused the existing "Results Noticed" field as the written lane. Built WF-25 Testimonial Request (trigger tag request_testimonial; If/Else on seg_facility routing facility vs consumer email; single email per branch; Re-Entry Off) and WF-26 Testimonial Received (trigger Form Submitted; adds testimonial_submitted, internal notification to Scott, gift_card_pending queue, thank-you email). Both branches and the form-to-workflow loop tested successfully.
- Testimonial emails (consumer + facility) finalized with a gift-card P.S. (no amount named). All new copy (P.S. lines, thank-you email) run through CUB + humanize-pro. Saved as Enyrgy_Testimonial_Request_Emails (.md + .docx).
- Added 7 contact custom fields in a Health Profile folder: Registration Date (Date), Skin Type (Single Options 1-6), Gender (Single Options), Height (Text), Weight (Number), Vitamin D Level (Number); Age intentionally skipped; Birthdate uses native Date of Birth field.
- Imported 617 existing customers. Ran a full 27-workflow trigger audit: only WF-01 (Contact Created) is an import risk; the 5 drips all trigger on type_* tags. Safe method used: unpublish WF-01 during import, import only drip_bypass + legacy_customer (+ seg_facility on 24 facilities), no type_/status_/unit_ tags. Cleaned the data (NULLs blanked, dates to M/D/YYYY, phones to +1). Proved via a 5-row test that GHL merges same-email contacts, so shared-email households were split by blanking the child's email (kept name + phone). WF-01 re-published after import.
- Note found (not blocking): Commercial, Partner, and Investor Warm drips lack a drip_bypass first-step gate; add one later for consistency.

**Still pending for Scott:**
- Hand-pick and send the first testimonial batch (add request_testimonial to chosen contacts from "Initial Customer Load 7-7-26"), warmup-safe batches; facilities consider owners only.
- Weekly gift-card fulfillment from the gift_card_pending queue.
- Re-upload the cleaned .md files into the project.

### Session 7: July 13, 2026
**Completed:**
- Paperclip Phase 2 Setup Guide created (.md + .docx): full build plan for the 16-agent organization covering deploy, GHL connection with least-privilege scopes, KB load, per-agent instruction blocks for the CEO orchestrator and all COO + CRO division agents, compliance gate as a hard approval gate, agent-to-workflow mapping, governance (budgets, heartbeats, config revisioning, rollback), a 5-contact test plan with pass and fail criteria, and a staged go-live with rollback
- Agent count corrected: the built organization is 16 agents (3 C-Suite + 7 COO + 6 CRO). The prior "24-agent" figure was an error; correct upper bound is 22 (16 core plus all six recommended Phase 2 additions)
- Standing rule reinforced: no em-dashes ever, in this session and all sessions. All five docs that contained em-dashes (Implementation Guide v3.9, WIP-3, Session Handoff, Consumer ICP Dartboard, B2B ICP Dartboard) regenerated with zero em-dashes in both .md and .docx
- All regenerated .docx rebuilt to match the locked brand style (branded cover page, Sunrise Orange running header per document, centered footer with page numbers, Montserrat, orange headings, properly rendering tables), using the prior Implementation Guide .docx as the exact style reference
- Em-dash in the source cover author line ("Co-Founder - Enyrgy Inc") corrected across all covers
- Brand Style Guide v2.0 saved into the project as Enyrgy_Brand_Style_Guide_v2 (.md + .docx) and set as the governing brand authority; minimum age resolved to 18
- Vitamin D Assessment lead magnet built (7-step quiz, GHL webhook payload, results copy routed through presell-sandwich in founder voice) and aligned to Brand Guide v2.0 (legal disclosures added, WCAG AA fixes, phone made optional)

**Still pending for Scott:**
- Deploy Paperclip and execute the Phase 2 guide (connection, KB load, agent config, 5-contact test, staged go-live)
- Update Investor Drip Touch 7 in GHL to remove the accredited_verified gate from PPM delivery (per attorney rule)
- Re-upload the cleaned .md files into the project to replace the em-dash versions

### Session 3: July 13, 2026
**Completed:**
- Implementation Guide updated v3.8.4 -> v3.9 (applied attorney guidance on accreditation sequencing; SHAKEN/STIR confirmed; raise updated to $3.5M)
- v3.9 produced in both .md and .docx
- WIP Tracker corrections applied:
  - A2P reference URLs corrected to shop.enyrgy.com
  - SHAKEN/STIR confirmed Approved & Verified
  - Facility address confirmed complete in all live systems
  - Winter Protocol workflow (WF-19/WF-20) + landing page confirmed complete
  - David SMTP / per-workflow sender confirmed complete (LC Email mg.enyrgy.com; Scott is sender)
  - Checklist items 2, 3, 4 & 8 marked complete

### Session 2: May 26, 2026
**Completed:**
- GHL Implementation Guide updated from v3.3 to v3.4 (added Paperclip agent org chart, lead gen strategy, implementation phases, client playbooks)
- v3.4 Word document (.docx) generated from markdown with full TOC, branded headers/footers, all tables
- Detailed Paperclip agent automation map created (agent vs. HITL by funnel stage)
- Shopify / GHL integration architecture documented (native connector + webhook specs)
- Vitamin D Deficiency Assessment lead magnet built (full 7-step interactive HTML/JS quiz)
- Lead magnet GHL webhook payload spec documented
- Abandoned checkout webhook spec documented

**End of Session Updates (same day):**
- Accreditation Form fixed: www.example.com links replaced with correct enyrgy.com policy URLs, HELP instruction added, no-sharing statement added
- SMS Opt-In Page and Consumer Inquiry Form updated: no-sharing statement added to both consent blocks
- A2P resubmitted with updated evidence package
- Usage assumption locked at 5 sessions per week for all content and sales materials
- Lead magnet deploy target: go.enyrgy.com/vitamin-d-assessment
- Lead magnet entry points: Shopify product page, podcast bio, Instagram bio, abandoned cart recovery

### Session 1: May 16-22, 2026
**Completed:**
- Full GHL clean slate - deleted 3 old sub-accounts
- Created Enyrgy Inc sub-account
- LC Phone connected
- Phone number +1 888-316-1695 purchased
- A2P registration submitted (multiple attempts)
- All 56 custom fields built
- All ~92 tags created
- All 5 pipelines built
- All 6 forms built
- All 6 calendars built
- go.enyrgy.com domain connected
- All 5 drip campaigns built and published
- All 10 core workflows built and published
- Scott Gmail SMTP connected
- Voice Integrity passed
- Trustpilot account activated
- Investor import Excel template created
- Shopify Privacy Policy and Terms of Service updated for SMS compliance

**Decisions Made:**
- Partner and Vendor treated as separate funnel types (not combined)
- Finance Preference includes "Rent" as option
- Investment Structure includes "SAFE" as option
- Consumer/Commercial calls handled by Scott
- Partner/Vendor/Investor Presentation handled by Scott
- Onboarding handled by Scott
- Toll-free number 888-316-1695 used instead of local Phoenix area code (unavailable)
- Manufacturing location is Phoenix, AZ (not Scottsdale)
- Treatments completed is 25,000+ (not 30,000+)
- 90% of customers use red light (not 40-60%)
- Referral discount is $150 off (not $200)
- No m-dashes ever in any content
- All tables in every .docx use visible gridlines (borders on all cells)
- Always say "Enyrgy Vitamin D Primal Light Platform"
- Story Selling OS framework applied to all client-facing content

---

*CONFIDENTIAL - Enyrgy Inc - Phoenix, AZ - Sunlight. Evolved.*
