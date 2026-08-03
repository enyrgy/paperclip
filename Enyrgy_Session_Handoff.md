# ENYRGY GHL - Session Handoff
**Load this at the start of the next session. It is the orientation layer. The WIP tracker and Implementation Guide v3.9 are the source of truth.**

Date of this handoff: July 28, 2026 (end of Session 15)

---

## HOW TO USE THIS
Paste or attach this file at the start of a new chat along with `Enyrgy_GHL_WIP-3.md` and `Enyrgy_GHL_Implementation_Guide_v3_9.md`. Review Standing Rules and Key Constants first. Then read What Was Done This Session and pick up from Remaining Tasks.

---

## OPERATING MODE: PRODUCTION (as of August 1, 2026)

**Enyrgy exited build mode and entered production mode on August 1, 2026.** Everything before this date was construction against test contacts and unpublished workflows. From here, every workflow, agent, drip, and send touches real customers, real investors, and real partners.

What changes in practice:

- **Nothing is a rehearsal.** A published workflow fires on real people. Before publishing or editing any live workflow, know who is currently enrolled in it.
- **The live audiences are real and sizeable:** 617 legacy customers, 57 current investors, plus ongoing lead-magnet capture. A mis-tagged import or a workflow edit that changes a trigger now has immediate outbound consequences.
- **Domain warmup is now a binding constraint, not a theoretical one.** mg.enyrgy.com is Stage 1. Use GHL's native batch mode for any multi-recipient send, keep Track clicks and UTM tracking OFF, and do not bulk-send the 600+ list.
- **Agent approval gates are now protecting real relationships**, not test records. The CFO/investor commitment gate stays absolute. Anything customer-facing or investor-facing keeps human approval.
- **Verify agent claims against the live account before acting.** This mattered in build mode; in production, acting on a confabulated agent audit changes real contact records.
- **KB accuracy is now customer-facing latency.** A stale fact in the KB is a wrong number quoted to a live prospect within hours, not a note in a doc. Sync the live `enyrgy-knowledge-base` skill whenever the repo KB changes, and record the synced commit hash.
- **Back up on the stated cadence.** See BACKUP PROCEDURE below. Snapshot plus contact CSV after every meaningful change session; there is no undo in production.

---

## STANDING RULES (always apply, every session)

1. **Both formats every time.** Every deliverable in `.md` AND `.docx`, with download buttons, no exceptions (updated Session 7: the WIP tracker and handoff are now produced in both formats too).
1a. **No em-dashes ever.** This session and all sessions. Use a hyphen, comma, or colon instead. Applies to every `.md`, `.docx`, and any other output.
1b. **Table gridlines in every `.docx`.** All tables use visible gridlines (borders on all cells, not just header underlines).
1c. **Brand Style Guide v2.0 is the governing authority.** `Enyrgy_Brand_Style_Guide_v2` governs product name, tagline, color, typography, voice, imagery, trademark usage, legal disclosures, and digital rules. Minimum age is 18. Route copy through the copy skills to match the founder-to-peer voice.
1d. **No icons.** Do not use icons, checkmarks, emoji, or decorative glyphs in any asset. Indicate state with color, fill, borders, or plain text.
2. **Options require full analysis.** Whenever options are presented (including via any input tool), provide: description of each option, pros and cons for each, a clear recommendation, and the reason. Full analysis in the message text before any selection.
3. **Route ALL copy through the right skill by default** (do not wait to be reminded):
   - StorySelling OS -> narrative/story content ONLY (origin stories, testimonials, social content pulling traffic to guides)
   - eugene-skill / cub / copy-chief / humanize-pro -> conversion and research copy (landing pages, guides, conversion emails)
   - presell-sandwich -> Problem-Aware buyer copy
   - offer-brief / offer-gravity -> offer framing
   - Match the skill to the asset's JOB, not its topic. The skills pass is part of building the asset, not a separate step.
4. **Brand constants (locked):**
   - Accent: Sunrise Orange #E64C38 ONLY (no violet, purple, or amber)
   - Typography: Montserrat, all weights
   - Text: Deep Charcoal #1A1A1A. Panels: Warm Off-White #F7F4EE, Calm Beige #ECE4CF. Line #E2DBC9. Muted #6B6B66.
   - Tagline: "Sunlight. Evolved." No em-dashes anywhere. Peer-to-peer voice throughout.
5. **Approved terms:** BioCalibrated Sunshine™, Triple-Pathway Advantage™. Product name: "Enyrgy Vitamin D Primal Light Platform" on first reference. Deprecated: "Precision Vitamin D Wellness Platform" and "Primal Light Platform" alone.
6. **Nitric oxide framing:** supplements feed the enzymatic route (substrate -> eNOS -> NO); UVA triggers enzyme-independent photorelease of NO from preformed skin stores (nitrite/nitrosothiols). The light pathway is additive - one a capsule cannot open. Never say "no supplement produces nitric oxide."
7. **Claim precision is non-negotiable.** Every claim must be exactly as verifiable as stated. No superlatives, no inflation, no unverifiable characterizations.
8. **Answer only what was asked.** Do not volunteer unrequested depth (e.g., Gen4 pricing, subscription mechanics) unless the forum specifically calls for it.
9. **SAVE THE ARTIFACT, NOT A DESCRIPTION OF IT.** Any customer-facing copy drafted in a session (email, SMS, landing page, script, one-pager) gets written to a repo file **in that same session**, before it is pasted into GHL or anywhere else. Pasting into GHL is the second step, never the only one.
   - **Why this rule exists.** Every drip and nurture email across WF-11 to WF-29 was drafted in sessions, pasted into GHL, and never written to a file. An entire session went into compliance-auditing that copy. The handoff faithfully recorded that the work happened ("copy handed back for paste into GHL", "all live funnel copy compliance-audited") while the copy itself was recorded nowhere. Sessions carry no memory, only the repo persists, and prior transcripts are not on disk. The result was a three to four hour manual re-extraction from GHL, in August 2026, of copy that had already passed through twice.
   - **The failure mode is subtle:** documenting the work *about* an artifact feels like documenting the artifact. It is not. If the deliverable is text, the text goes in a file.
   - Campaign copy lives in `campaigns/`, one file per workflow. See `campaigns/README.md`.
   - Costs nothing at the time. The copy already exists in the response; it only needs writing down.

---

## KEY CONSTANTS

| Item | Value |
|------|-------|
| GHL Sub-Account ID | GtXjla7Ld1dordsTWrVy |
| Facility | 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017 - Made in USA |
| Sending domain | mg.enyrgy.com (LC Email, verified, SSL issued, Stage 1 warmup) |
| Default sender | Scott Hansbury / scott@enyrgy.com (on all workflows) |
| Consumer Unit MSRP | $2,995 |
| Commercial Unit MSRP | $8,950 |
| Per-session cost | $2.30 ($2,995 / 1,300 sessions - 5x/week x 52 weeks x 5 years) |
| Total raise | $3.5M at 12%/3yr, $50K minimum |
| Treatments completed | 25,000+ |
| Customers | 600+ (617 imported into GHL, Session 10, tagged drip_bypass + legacy_customer; 24 facility contacts also carry seg_facility) |
| Current investors | 57 in GHL (Session 16, tagged seg_investor_current + drip_bypass + source_investor_import; NEVER type_investor, that triggers the cold 8-touch drip). Smart list "Investors - Current". $10,373,000 funded. 10 are also legacy_customer. |
| Red light co-use | 90% of customers |
| Active OEM partner | Lumanova / Luma D Light (Black Unit exclusivity) |
| Order URL | https://shop.enyrgy.com/products/uvb-light-therapy |
| Phone | +1 888-316-1695 (Toll-Free, LC Phone) |

**Team:** Scott Hansbury (Co-founder & CEO), David Letourneau (President & Co-Founder), Brian Cameron (CFO).

---

## BACKUP PROCEDURE (run after every meaningful build session)

GHL has no one-click "export everything" and no automated backups, so back up manually in three parts. Cadence: **snapshot + contact CSV after every meaningful change session.**

1. **GHL config -> Account Snapshot.** Agency view -> Account Snapshots -> Create Snapshot -> source = the Enyrgy Inc sub-account -> name it dated (e.g., "Enyrgy Backup 2026-07-28"). Captures workflows, funnels, forms, pipelines, custom fields, triggers, campaigns, email/SMS templates, and calendars. To restore, deploy the snapshot to a fresh sub-account. Keep the last few snapshots.
2. **GHL data -> CSV exports.** Contacts -> Smart Lists/All -> Export -> CSV (current count ~637; the avatar "+N" bubble is cosmetic, the header count is the real total). Opportunities -> List view -> Export. Download when ready (push notification / Bulk Actions page). IMPORTANT: export files expire in 30 days, so download and store them in a secure local or cloud folder. Do NOT leave them only in GHL, and do NOT commit contact PII to the GitHub repo.
3. **Already backed up (Git).** All agent instruction blocks, the KB, workflow specs, the implementation guide, this handoff, the ROI one-pager, and every session doc live in the GitHub repo (enyrgy/paperclip) with full history. The bridge and abandoned-checkout services are in their own repos.

**Gaps a snapshot does NOT cover** (these are re-established on restore, not copied): phone numbers, A2P/toll-free registration, CNAM, integration tokens, the media library, and conversation history.

---

## WHAT WAS DONE (Session 16, July 31, 2026)

### Current investors imported (57) and the Q2 2026 update SENT

**The list.** 57 current investors imported into GHL. Total funded across the list: **$10,373,000**. Seven rows carry blank amounts by design (co-investors on a spouse's or entity's tranche: Zurawski, Brooke Coughlan, Gordon Ross, Jennifer Scharf, Monroe Gang, Paul Will, Wendy Weathers).

**Tags imported:** `seg_investor_current`, `drip_bypass`, `source_investor_import`. **Deliberately NOT `type_investor`** - that tag is the trigger for the Investor Drip, Cold 8-touch/30-day sequence, and these are people who have already funded. Two independent protections: no trigger tag, plus `drip_bypass`.

**NEW IMPORT RISK, not in the older docs.** The Session 10 audit concluded WF-01 New Lead Router was the *only* Contact Created trigger. That is now false: **WF-31 FlexOffers First Touch** (built Session 15) also triggers on Contact Created. Both were unpublished for the import and re-published after. Any future import must check for Contact Created triggers fresh rather than trusting the Session 10 finding.

**GHL's newer 4-step import wizard** (Start / Upload / Map / Verify) replaces the old flow. Notes:
- Mapping requirements state **"Update contacts: Either of Contact ID / Phone / Email."** Phone is a valid match key and there is **no email-only override**. Two spouse pairs shared a phone (Brian/Jennifer Scharf, Mark/Wendy Weathers). Rather than gamble on match precedence, the phone was blanked on one of each pair so every phone in the file was unique and no phone-based merge was possible. Add those numbers back by hand if wanted.
- The Verify step holds the three dangerous preferences: **Add to workflow**, **Add tags**, **Create a Smartlist**. All three left OFF. The auto-Smartlist only captures contacts *created* by the import, so it silently excludes updated ones and must not be used as a mailing list.
- A consent attestation checkbox gates the Start import button.

**Result: 46 created + 10 updated = 56, but the file had 57.** One row, **Scott Chaverri**, failed silently with no error anywhere in the wizard. Added by hand.
- **LESSON: the smart-list count is the only reliable verification of an import.** The wizard's own counts did not surface the failure, and the Bulk Actions "show imported" count (46) measures creates only, which looks like a discrepancy but is not one.

**The 10 updated contacts** are dual-role investor/legacy-customers from the Session 10 617-import. All retained `legacy_customer`; three retained `request_testimonial`. Nothing was clobbered. Note: re-applying `drip_bypass` to them was a **no-op** - Session 10 already applied it to all 617, and no legacy customer carries a `type_` tag, so no drip was ever enrollable on them.

**Data cleaning required before the file was importable** (all real, all silent if missed):
- A duplicate row (same investor twice, second with a trailing space in the email) that would have **overwritten** the first rather than summing
- `25K` in a numeric amount field
- Two `Acrredited Individual` spelling variants, which would have created a permanent second dropdown option
- Trailing whitespace in a first name and an email; a whitespace-only cell
- `Source_referral` vs `source_referral` casing split
- A **UTF-8 BOM** on byte 0, which makes the first header `﻿First Name` and breaks its auto-map. Excel adds this when saving as "CSV UTF-8"; plain "CSV (Comma delimited)" does not.
- A `✦` character inside a header name, same auto-map failure
- A column headed `Accredited Verified` whose values were actually Investor Type values

**Smart list `Investors - Current`** built on a single filter: `Tag` / `Is` / `seg_investor_current`. Dynamic, so any future investor tagged that way joins automatically. Do not filter on the other two tags; they are protective and provenance markers, not membership criteria.

**Email template `Investor Quarterly Update - MASTER`** built in the **plain text editor**, chosen over the Design editor for two reasons: an investor update should read as a personal email rather than a marketing blast, and simple text is the best-performing format from a Stage 1 sending domain. Never send the MASTER; duplicate it each quarter.

**Q2 2026 investor update SENT July 31, 2026**, meeting the standing commitment to send by the end of the month following quarter close.
- **48 via GHL bulk email in batch mode** (12 per batch, 15-minute interval). Track clicks and UTM tracking left OFF deliberately: link rewriting is a negative deliverability signal from an unproven domain, and the email contains no hyperlinks to track.
- **9 AOL/Yahoo recipients sent individually from `scott@enyrgy.com`**, one email each, no BCC. Rationale: those mailboxes weight sender reputation hardest, and Google Workspace authenticating as `enyrgy.com` is far stronger than a weeks-old `mg.enyrgy.com`. No-BCC is both a deliverability and a confidentiality rule - a CC slip would disclose the investor list to everyone on it.
- Copy corrections applied before send: "added to **principle**" -> **principal** (in the note's own terms), `K1's` -> `K-1s`, "in regards to" -> "regarding", `$100 to 150M` -> `$100M to $150M`, and two sentences broken mid-line. The N=5 pilot caveat on the +111% / 100%-optimal figures was **deliberately omitted at Scott's direction**.

**DELIVERABILITY RESULT (checked Aug 1, clean).** Delivered **100%** (48/48), opened **75%**, and **0% on every failure metric**: hard bounce, soft bounce, unsubscribed, skipped, spam. Clicked 0% is expected (no links, Track clicks off).
- **Spam at 0% was the number that mattered.** One complaint out of 48 is a 2 percent rate, well past the level that damages a warming domain. Combined with 75% opens, this was a **net positive warmup event** for mg.enyrgy.com rather than a risk taken.
- **The corporate-domain worry did not materialise.** All 20 corporate-domain investors delivered. The `scott@ledgerixpro.com` test that vanished without a bounce is therefore tenant-side quarantine (likely M365) on that one account: not the sending domain, not GHL suppression (Skipped was 0%), and not a signal about the investor list. Worth remembering as a diagnosis pattern - a message that vanishes with no bounce and no spam-folder entry is usually recipient-side quarantine, which is invisible to the sender.
- **Zero unsubscribes**, so all 57 remain eligible for Q3.
- Open rate caveat for future comparison: Apple Mail Privacy Protection auto-loads tracking pixels and some corporate scanners pre-fetch images, so opens skew high. Treat 75% as directional, and compare quarter over quarter rather than against an absolute benchmark.

### Live KB skill re-synced (Aug 1, 2026)

The `enyrgy-knowledge-base` Company Skill now matches repo commit `95f41a40`. Six targeted edits, done as individual find/replace operations rather than a select-all paste (the Session 14 method that corrupted the skill). All six confirmed present after save.

Two of them were more than cosmetic and had been actively misleading agents:
- **S12** told every agent the PPM was an unapproved placeholder. It has been attorney-approved since July 28, so agents may have been declining to send a cleared document for several days.
- **S3** had agents quoting a flat $49/month into premium markets that support $125. The range is now $49 to $125 with the rule that it is **set by location and local clientele**, plus named reference markets (Orange County = $125).

New in S3 and worth knowing it exists: **credit-based membership guidance.** Where a facility sells prepaid service credits, Enyrgy must NOT be priced per session against those credits (at 4 to 5 sessions a week it would consume a whole membership and crowd out the operator's higher-margin services). Price it as a flat monthly add-on outside credits, or fold it into a top tier as the upgrade trigger. This came out of the Beyond Wellness call prep and now lives in the KB rather than only in that call sheet.

**Sync method for future KB changes:** `git log <last-synced-commit>..HEAD -- Enyrgy_Paperclip_Knowledge_Base.md` to see what actually changed, then apply only those hunks as find/replace in Skill Studio. Never select-all-paste. Always reopen after saving and confirm the body has content and the frontmatter appears exactly once.

### Inbound replies were invisible, fixed Aug 2

**The gap.** Every email GHL sends goes out over `mg.enyrgy.com`, and replies come back to that domain so GHL can log them onto the contact record. That part works as designed. What was missing was any notification. Conversation Notifications had **In-App ticked and Email unticked**, and In-App only renders inside GHL, so a reply pinged a bell nobody saw unless already logged in.

**Found the hard way.** A reply to the Q2 investor update landed in Conversations only. It was caught solely because the contact happened to be open during the import work. A testimonial reply from the same period has still not been located.

**Fixed.** Settings, My Staff, the user, Notification Settings. All six Conversation Notification rows now have **Email** ticked. SMS deliberately left off on all six: email reaches the same phone and watch without per-segment toll-free cost, and "all new conversations and messages" would get noisy as lead volume grows.

**DO NOT repoint Reply-To to `scott@enyrgy.com` to solve this.** It is the obvious fix and it breaks something worse. Stop-on-Response is ON across WF-06, WF-08 and the consumer drip (Session 14 Fix #1), and it works by GHL seeing the reply. Route replies around GHL and **a contact who replies keeps receiving drip emails**. The conversation history on the contact and the agents' ability to act on replies both go too.

**Still open.** The notification tells you a reply exists; the reply itself still lives in GHL. If the requirement is reading and answering from the inbox rather than being alerted to go and look, a workflow on the **Customer Replied** trigger sending an internal notification with the message body and contact link is the answer, the same pattern WF-26 uses. Test what GHL's built-in notification actually contains before deciding whether to build it.

### Quarterly runbook (from Q3 onward)

1. Duplicate `Investor Quarterly Update - MASTER`, swap the numbers, keep the `{{contact.first_name}}` greeting
2. Subject `Enyrgy Q<N> <YEAR> Investor Update`; fill the **pre-header** (it does not carry over from the test dialog and is blank by default)
3. From name **Scott Hansbury**, not the raw email address - GHL auto-fills the address and it reads as automated mail
4. Select all 57 in `Investors - Current`, send once. No batching and no separate AOL/Yahoo handling once the domain is warm
5. Roughly ten minutes

### CAMPAIGN CAPTURE COMPLETE, Aug 2-3, 2026

**All 19 workflows are now in `campaigns/`, 94 touches, 83 corrections applied.** Every live email and SMS in the GHL account exists as `.md` + `.docx` in the repo, with a per-workflow change log recording what was corrected and why. This closes the gap that produced Standing Rule 9.

**GHL remains the source of truth.** These files are a backup and a review surface, not a deployment source. Change GHL first, then update the file.

**Three systemic findings, worth carrying forward:**

1. **"Fixed everywhere" was never everywhere.** The accreditation gate was attorney-corrected in Sessions 11, 13 and 14 and declared fixed in three places; it survived in the Investor Warm drip, a fourth place nobody had checked. The guarantee/lab-timeline decoupling was found still coupled in six instances across four consecutive workflows after being declared fixed. **A correction is not done until it has been grepped across every workflow, not just the one that surfaced it.**

2. **A/B workflows need both arms checked.** WF-16's touch 3B was corrected and 3A was not. A fix applied to one variant is indistinguishable, from the outside, from a fix applied to the workflow.

3. **Silent failures were the most valuable finds, and none of them errored.** WF-25 steered testimonials toward a reply while WF-26 triggered only on Form Submitted, so a customer following instructions vanished. WF-20's None branch applied the nurture tag *after* a seasonal wait, producing up to four months of silence. WF-21 promised a result and never delivered it while the Risk Band field sat unused. Nothing in GHL reports any of these.

**Testimonial consent: the process has one door and stories keep arriving through the wall.** WF-25 routes every testimonial through a form that captures consent. WF-08 touch 3 features a real customer's lab values, 28 to 84 over twelve weeks, and it reached live copy through a drafting session instead. Consent was confirmed with the customer on Aug 3, 2026 and the copy stands, but it existed because someone remembered to get it, not because anything required it. He is unnamed and not anonymous: within Enyrgy's own customer base those two numbers identify exactly one person, which is an FTC endorsement whether or not he is named or paid, and health data under the Washington, California, Colorado and Connecticut privacy statutes. **A sweep of all 19 workflows on Aug 3 found this to be the only instance in the funnel.** Treat a second one as needing written consent on file before it ships.

**WF-20 Touch 3C is NOT a duplicate.** It is a held send for contacts outside both seasonal windows. It was misread as a duplicate during capture. Do not delete it.

---

## WHAT WAS DONE (Session 15, July 27-28, 2026)

The session took Paperclip from "built" toward "running": the live KB skill was repaired and re-synced, the first heartbeats were brought online and tuned, the two things that made the running system unusable day-to-day (an approval-card flood and cards with no context) were both fixed, a Q2 investor update was drafted, and a QC-raised "systemic" data issue was run to ground and proven a false alarm. That last item surfaced the most important operational lesson of the session: the agent org confabulates when it is credit-starved.

**Approval-card flood stopped (Ask-first policy rebalanced).** The "Ask first" gate was firing a review card on ordinary internal CRM housekeeping (tags, tasks, contact updates, stage moves), so Scott was drowning in low-value approvals and letting them auto-decline. Rebalanced the Rules (Apps > Advanced setup > Rules) so internal-organization writes auto-run while prospect-facing and money-adjacent actions stay gated. Added one rule: **"When any agent uses 13 specific actions -> Allow"** (the read/search actions plus Add/Remove Contact Tags, Create Task, Update Contact, Move Opportunity Stage): and ordered the rule list so the first match resolves correctly: **row 1 = CFO -> Ask first** (the investor/money agent stays fully gated on every write), **row 2 = the 13-action Allow**, then the per-tool Ask-first rules below. Still gated for everyone: **Send Message, Enroll In Workflow, Remove From Workflow** (all change what a prospect receives). The five per-tool Ask-first rules the Allow rule now supersedes (Add Contact Tags, Create Task, Move Opportunity Stage, Remove Contact Tags, Update Contact) are dead-but-harmless; can be toggled off to declutter. Verified live with Test-a-rule: SDR+Add Contact Tags = Allow, any+Send Message = Ask first, CFO+Add Contact Tags = Ask first. Design note: tagging is auto-allowed even though a tag can trigger a GHL drip, because that drip copy is the human-approved static sequence; the real send risk is the agent composing a fresh 1:1 message, which is `Send Message` and stays gated.

**Approval cards now explain themselves (code, deployed).** The review-queue card ("Waiting for your OK") showed only a generic "we're checking with you first" line plus raw field values, with no indication of what Approve vs Decline actually does, so the cards were unactionable. Restructured the humanized preview in `server/src/services/tool-gateway.ts` (`buildHumanizedActionPreview`) into three parts: what's happening, the specifics, and an explicit **If you approve / If you decline** outcome pair (destructive actions warn the change may be irreversible). Server-side change, so it applies to every pending and future card automatically. Committed `04855fad`, pushed to master, deployed on Railway. This is a fork divergence from upstream Paperclip UI copy.

**Live KB skill repaired and re-synced.** The `enyrgy-knowledge-base` Company Skill had accumulated duplicated/malformed frontmatter and a doubled sentence from prior "select-all paste" syncs; the KB Manager auto-repaired it but that reverted the Session-14 edits. Provided the full clean KB body for a careful single-paste (keep frontmatter, replace body only), which Scott confirmed fixed. **Sync lesson:** never select-all-paste the KB into Skill Studio; replace the body only and verify no duplicate footer.

**Duplicate voice skill removed.** Two `enyrgy-agent-voice-style` skills existed: one attached to 8 agents (the real one) and a bundled 0-agent duplicate created from the repo `skills/enyrgy-agent-voice-style/SKILL.md`. Removed the bundled copy (`git rm -r skills/enyrgy-agent-voice-style/`, committed + pushed); kept the root reference doc `Enyrgy_Agent_Voice_Style_Skill.md`.

**PPM placeholder guardrail lifted (attorney-approved).** The PPM is now attorney-approved, so the "placeholder / do not send" guardrail was removed across the KB (Section 12), the agent instruction blocks, and the guides. PPM may be sent after the intro meeting; accreditation still gates only wire instructions and accepting investment (unchanged attorney rule).

**Anthropic billing fixed -> heartbeats unblocked.** Sentinel and other heartbeats were failing with `acpx_session_init_failed` / "Credit balance is too low." Root cause was two separate caps at console.anthropic.com: the prepaid **credit balance** AND the monthly **spend limit:** topping up credits alone does not override the monthly cap. Scott added credits (settings/billing) and raised the monthly limit (settings/limits); Sentinel then ran successfully. Staged go-live is underway (bring heartbeat groups online one at a time; CEO/COO/CRO heartbeats remain OFF. Their earlier spend was a one-time escalation/recovery storm during the KB/credit incident, not heartbeat cost).

**Budget model clarified (no company-wide cap exists).** Paperclip has per-agent and per-project budgets (Costs > Budgets) but **no single org-wide budget field**; the effective ceiling is the sum of per-agent caps (~$59/mo). Heartbeats replay large context on every wake so even no-op wakes cost; GHL drip emails are static (~$0 Anthropic); variable cost tracks agent decisions, not message volume.

**Tool-policy toggle bug fixed (deployed).** Toggling a `require_approval` Rule on/off failed with "Tool policy type require_approval does not support config" because `updatePolicy` re-validated the rule's stored config on every update, and some seeded rules carry a legacy config blob. Fix: validate only what the update actually changes (type always, conditions only when provided, config only when config/type changes). Creates and duplicates stay strict. Commit `0ffb2dd4`.

**Heartbeat intervals tuned and the go-live staging set.** Found the live heartbeats were misconfigured (Dispatcher polling every 30 min, QC weekly, revenue agents off). Corrected the ON set: Dispatcher `28800` (8h, was the 30-min anomaly and largely redundant with WF-01 auto-routing), Quality Control `86400` (daily), Sales Outreach `3600` (1h), SDR `7200` (2h), Sentinel `86400` (24h), KB Manager `2592000` (30d, effectively off). Only ~8 agents should ever run on a timer heartbeat (the proactive monitors + the two revenue agents); the executives (CEO/COO/CRO/CFO), Audit and Compliance, PRD Gatherer, and Onboarding stay **event-driven, timer OFF**. IMPORTANT trap: every OFF agent shows a `300s` (5-minute) default, so whenever you enable one you MUST set its interval in the same step. Remaining rollout, gated on watching cost between each: Reactivation `21600`, Referral and Reviews `21600` (only after WF-07 review link + referral app), Sales Scout `43200`, CSM `43200`.

**Q2 2026 investor update drafted (standalone .docx, not committed).** Built from the KB and session logs only, no invented figures. Includes real Q2 financials (revenue $34,866.86, gross profit $30,834.68, opex $55,822.26, net loss $24,987.58, of which $33,464.79 was non-recurring: $26,897.97 fundraise costs + $6,566.82 annual insurance renewal, so underlying operations ran ~$8,477 positive), the commercial membership reframe (operators use Enyrgy as a member-acquisition and tier-upgrade draw, moving off per-modality pricing), a Team section (Brian Cameron, Millie Carrillo, Shanna Schuckman, Thea Cartier), the operating-platform section (Enterprise Architecture v1.0 + 29 workflows), and YourTango named. Compliance-clean (no em-dashes, no prohibited words, N=5 caveat, offering terms point to the PPM). Needs Brian + attorney sign-off before sending; send only to existing/already-introduced investors.

**QC "systemic lifecycle" escalation (ENY-20) run to ground: FALSE POSITIVE, and the real finding is agent confabulation under credit starvation.** QC's weekly audit escalated a "systemic, most active contacts affected" lifecycle bug (status tags stacking, contacts stuck at New Lead, WF-04 not running). COO then "verified it live" and confirmed it. Both were wrong. Every specific claim was checked by hand against the live sub-account and none held: the New Lead stage had one legitimate same-day lead (Barry Fingerhut via Tired Test); the named magnet leads (Sonya, Engle, Crystal, Celestina, Lynette) carry zero `status_` tags; Preston carries a single clean `status_solicitation`; "Test Calendar" and spam contact Saloni were already deleted; and WF-04 Stale Lead Sentinel has run **every day** (Jul 23 to 28, last run Jul 28 08:02, all Finished): COO had misread the workflow's last-*edit* date (2026-06-27) as its last-*run* date. Root cause: the agent org was **credit-starved and budget-hard-stopped**, and in that state it did not fail quietly, it produced confident, specific, fabricated claims. A related claim (that the delegated fix ENY-24 was auto-flipped to `done` during "credit-balance recovery" with no execution) was later investigated in code and debunked: credit/budget failures route to `blocked`, never `done`, so there is no such platform bug. It was another confabulation. **Standing lessons adopted:** (1) verify every agent audit/verification against the live GHL account before acting; agent escalations are leads, not facts; (2) keep Anthropic credit buffered and budgets with headroom, because starvation multiplies cost (dying runs re-wake and replay a growing thread) and triggers confabulation; (3) the QC instruction was tightened to require cited contact IDs + observed tags and to forbid inferring status from stage. Cleanup: ENY-20, ENY-30, and the phantom replacement fix ENY-35 were cancelled; ENY-29 and ENY-31 (Saloni reconciliation) were already Done; Saloni was an intentional human spam deletion, not an unapproved action. **Phantom-completion "bug": investigated and debunked (July 28).** The recovery code (`server/src/services/recovery/service.ts`) already routes credit/budget failures to `blocked`, never `done` (the only `done` transition is a legitimate watchdog fold requiring a succeeded run). No code change; the claim was another COO confabulation.

**Consolidated open-items list created.** `Enyrgy_Master_TODO.md` reconciles every open item across the EA, WIP, IG, and Phase 2 guide against the live state, in priority order. Use it as the single punch list going forward.

**FlexOffers affiliate attribution built end to end (July 29).** Affiliates drive traffic to the free Tired Test, but the sale happens weeks later on a different domain (shop.enyrgy.com), so cookie/pixel tracking cannot attribute it. Built a **capture-and-postback** chain instead, which is cookie-free and time-independent:
1. **FlexOffers program:** "Enyrgy - Tired Test (S2S)" **#250377** (default campaign #144482449, creative #6673704 "Take the free Tired Test..."). Payout **$600 fixed amount, CPA** (~20 percent of the $2,995 unit; leaves ~$1,377 gross profit per affiliate sale after the ~34 percent product cost). **Return Days 365** (FlexOffers allows up to 999, which solves the multi-week nurture cycle). **Manual Review** publisher approval, chosen deliberately over Automated: automated only manages refund risk, while manual review lets Scott vet publishers before they can make health claims that become Enyrgy's FTC problem. Deep Linking OFF (it requires FlexOffers tracking code on every page; we track via S2S). Unchecked promotional methods: the three coupon types (Enyrgy does not discount), Sub-Network (unvetted sub-affiliates), Browser Extension (last-click hijacking).
2. **Program default URL** points at `https://go.enyrgy.com/tired-test`. NOTE: the S2S program's campaign is flagged DEFAULT, so its Destination URL is locked to the program default; that is why the program default, not the campaign, carries the quiz URL. Campaigns cannot be moved between programs (the Program field is disabled on edit).
3. **Capture:** the Tired Test page reads `refid` from the landing URL and persists it to `localStorage`, so it survives refreshes and a visitor returning later without the affiliate link. It is sent to the WF-12 webhook as `flexoffers_refid` on every submission (empty string when there is no affiliate, keeping the payload shape stable for GHL's field mapper). Also pushes a `source_flexoffers` tag for segmentation. Page committed to the repo at `lead-magnets/tired-test.html`.
4. **Storage:** new contact custom field **FlexOffers Refid** (key `flexoffers_refid`), mapped in **WF-12** from `{{inboundWebhookRequest.flexoffers_refid}}`. VERIFIED live: a test submission with `refid=24.TESTFLEX002` stored correctly on the contact.
5. **Postback:** **WF-30 FlexOffers Sale Postback**. Trigger **Order fulfilled** filtered to `Fulfilled Products contains the Home System`, then a condition `FlexOffers Refid is not empty`, then a Webhook POST. GHL's webhook action has no query-params section (only Custom Data, which goes in the JSON body), and FlexOffers' `da.ashx` reads the query string, so **all parameters live in the URL**: `advertiserid`, `clickid={{contact.flexoffers_refid}}`, `ordernumber={{order.number}}`, `orderamount={{order.subtotal_price}}` (subtotal, not total, because FlexOffers defines orderamount as before tax and shipping), plus `currency=USD&geo=USA&platform=S2S`.
**Two bugs caught during the build, both by Scott.** (a) The trigger was originally *Shopify order placed* with no product filter, which combined with the flat $600 CPA would have paid **$600 on a $297 wall-mount reorder** (a $303 loss) and again on every future accessory reorder by any affiliate-referred customer. Fixed by switching to *Order fulfilled*, the only trigger exposing a **Fulfilled Products** filter, and gating on the Home System. (b) Scott correctly questioned whether the Shopify `Number` merge field meant quantity rather than order number (it is the order number; quantity lives under the `Products` submenu).
**Known gaps, recorded honestly:** the `{{order.number}}` and `{{order.subtotal_price}}` tokens were selected while a different trigger was active and are UNVERIFIED, because testing required a real Shopify order and Shopify's payment/refund cycle made that too costly (a "mark as pending" unpaid order was offered but Scott judged the charge risk too high). Verify on the first real affiliate sale via WF-30 Execution Logs. Also inherent to any setup like this: attribution depends on the buyer using the **same email** at Shopify checkout as on the quiz; a different email creates a new contact with no refid and that sale will not credit.
**Waiting on the FlexOffers rep:** a test tracking link for 250377 (to verify the click-to-capture path for free), surfacing 250377 to the network, and migrating the 124 publishers approved on the OLD program (#247334) since approvals are per-program and 250377 currently has zero. Only after they migrate should old creative **#6673701** be disabled (it has no S2S tracking, so anyone promoting it earns nothing). Also note the old program shows **4,233 clicks in 30 days with 0 tracked sales**, which is the signature of conversion tracking never having worked there; that audience is a warm list of publishers already willing to promote.
**All five lead magnets wired for affiliate attribution (July 30).** The capture chain now runs on every magnet, not just the Tired Test: **Tired Test** (`/tired-test`, WF-12), **Vitamin D Assessment** (`/vitamin-d-assessment`, WF-21, webhook `d2692dc6-1e9f-466c-8525-58c466c426bd`), **Synthesis Gap** (`/synthesis-gap`, WF-15), **Recovery Protocol** (`/recovery-protocol`, WF-18), **Winter Protocol** (`/winter-protocol`, WF-19). Each page reads `refid` from the landing URL, persists it to localStorage, and sends it to its capture webhook; each capture workflow maps `{{inboundWebhookRequest.flexoffers_refid}}` to the contact's FlexOffers Refid field. Every one was verified live end to end. All five pages are now version-controlled in `lead-magnets/`. **WF-30 is magnet-agnostic** (it fires on the sale, not the entry point), so one postback workflow covers all five.
**Structure that makes this work:** ONE FlexOffers program (250377) with a **campaign per lead magnet**. The destination URL lives at the campaign level while tracking, payout, and publisher approvals sit at the program level, so a publisher applies once and can then promote whichever magnet fits their audience. Do NOT make each magnet its own program (publishers would have to apply five times, and there would be five postback configs). Non-default campaigns have an editable Destination URL on their LINK tab; the program's DEFAULT campaign does not, which is why the program default URL carries the Tired Test link. Campaigns cannot be moved between programs (the Program field is disabled on edit).
**Attribution behavior, by design:** the URL `refid` always wins, with localStorage as the fallback, so a visitor who clicks an affiliate link, wanders off, and returns later without the link still credits that affiliate. Last click wins if they later arrive via a different affiliate. TESTING GOTCHA that produced one confusing result: reusing an incognito session carries localStorage over and can mask a new refid, making it look like the wrong value was captured. Always close all incognito windows before a capture test, and confirm the URL bar still shows `?refid=` before submitting.
**Attribution set to FIRST-IN and NEW-CONTACTS-ONLY (July 30, final architecture in WF-31).** Scott raised the scenario: a prospect clicks affiliate A's Tired Test link, enters nurture, then a month later clicks affiliate B's Recovery Protocol link and buys. No double-payment was ever possible (one refid field, one postback, one publisher credited), but which affiliate is a real question. Decision, and Scott pushed the rule further than the first proposal: **an affiliate earns the $600 only for introducing someone NEW to the database.** If a contact record already exists, Enyrgy had the relationship first, organic or via a prior affiliate, so a later affiliate does not collect. **Architecture, after two approaches failed:** GHL's condition builder exposes no contact-creation date (searched "created" and "date"; only DOB and custom date fields), so "is this contact new" cannot be tested inside a capture workflow, and tags cannot substitute because the capture workflow's own Add Tag actions run before any guard. The working solution uses GHL's **Contact Created** trigger, which fires only on genuine creation. Each of the five capture workflows (WF-12/15/18/19/21) now just maps the click ID to a staging field in Create Contact, **FlexOffers Refid Incoming** (`flexoffers_refid_incoming`) = `{{inboundWebhookRequest.flexoffers_refid}}`, with no conditions or branching. **WF-31 FlexOffers First Touch** then does the attribution: trigger Contact Created (unfiltered) -> Wait 2 minutes (lets custom fields finish writing; a trigger-level filter would silently drop refids that had not landed yet) -> Condition `FlexOffers Refid Incoming is not empty AND FlexOffers Refid is empty` -> Update Contact Field `FlexOffers Refid` = `{{contact.flexoffers_refid_incoming}}`. WF-31 reads from `contact.`, the capture workflows read from `inboundWebhookRequest.`. One rule, one workflow, five magnets inherit it. (Superseded note: an earlier per-workflow guard approach was built and then removed.) Scott raised the scenario: a prospect clicks affiliate A's Tired Test link, enters nurture, then a month later clicks affiliate B's Recovery Protocol link and buys. Technically no double-payment was ever possible (one refid field, one postback, one publisher credited), but the question of WHICH affiliate is real. Decision: **first-in wins**, because Enyrgy does the selling, so the affiliate's genuine contribution is the introduction. Implementation on WF-12, WF-15, WF-18, WF-19, WF-21: the refid is NO LONGER mapped in Create Contact (an unconditional write there would overwrite before the guard runs and make it a no-op); instead each workflow ends with `If FlexOffers Refid is empty -> Update contact field -> FlexOffers Refid = {{inboundWebhookRequest.flexoffers_refid}}`.
**CRITICAL GHL PLACEMENT RULE (learned the hard way):** condition branches never rejoin, so the guard MUST be the last thing in a workflow. Inserting it mid-flow swallows everything below into the Yes branch. This happened on WF-12: the tags and seasonal logic ended up inside the branch, meaning any contact who already had a refid would have received no tags and therefore no emails. Caught, reverted, rebuilt. To make the guard placement clean, two redundant conditions were removed (each verified redundant by inspection first, not assumed): WF-21's risk-band Condition and WF-12's seasonal Condition, both of which re-applied tags the page already sends and a Dynamic Add Tag already applies.
**MUST TELL PUBLISHERS:** last-click is the industry default, so first-in has to be stated explicitly in the program terms and the Message Center newsletter, or the dispute just gets pointed at Enyrgy instead of between two affiliates. Open decision not addressed: an existing customer or long-time organic lead who clicks an affiliate link has an empty refid, so that affiliate would earn $600 on someone already in the database (a known affiliate leak).
**COMPLIANCE BUG FOUND AND FIXED: false SMS consent on every Tired Test lead (July 30).** While inspecting WF-12 for the guard work, its static Add Tag was found to include **`sms_consent_given` in the always-on list**, so every Tired Test lead was tagged as an SMS opt-in regardless of whether they checked the consent box or gave a phone number. The page only sets that tag conditionally (`if(smsConsent && phone)`). Real TCPA/A2P exposure, and newly material now that the toll-free is live for SMS. FIX: removed it from the static list and added a **Dynamic Add Tag** reading `{{inboundWebhookRequest.tags}}`, so consent lands only when actually given. That also closed a second gap: WF-12 had **no dynamic tag action at all**, so the page's other conditional tags (`low_sun_exposure`, `tired_test_seasonal`, `source_flexoffers`) were never landing either. STILL TO VERIFY: WF-21's static list (the Vitamin D Assessment page also collects phone and SMS consent conditionally) for the same bug.
**Caution learned:** the FlexOffers "Advertiser Assistant" AI fabricated a postback URL (wrong domain `flexlinks.com` instead of `flexlinkspro.com`, and a made-up `advertiserid` built from the program number with `XXXX` placeholders). The real GUID came from the human rep. Same lesson as the agent confabulation above: verify AI-supplied identifiers against the authoritative source.

**Fixed: accessory reorders were triggering device onboarding.** A customer who reordered a wall mount (a Shopify accessory) received the WF-06 New Customer Onboarding "your unit is on its way, register before it arrives" sequence, days after the device had already been delivered and after Scott had spoken with them. Root cause: WF-28 Shopify Order Fulfilled applied the `unit_shipped` tag on ANY fulfilled order, and WF-06 triggers on that tag. Fix: added a product filter to WF-28's Order-Fulfilled trigger so it applies `unit_shipped` only when the fulfilled order contains the Home System device (the sole product sold through Shopify; the Commercial unit is sold off-Shopify, so no additional product needed in the filter). WF-06's trigger is the `unit_shipped` tag (a Contact-tag trigger that fires when the tag is added; it does not add the tag), so the single WF-28 filter fully controls onboarding. The mistimed SMS to the affected customer had failed to send (toll-free SMS was not yet live), so only a harmless "register your device" email reached them.

**Decision: referral program deferred to the next Enyrgy version.** Scott decided not to implement a third-party Shopify referral app (ReferralCandy/Smile.io) now; the next version of Enyrgy will have a built-in loyalty/referral program. So WF-07's referral link stays an intentional placeholder until then, and the Referral and Reviews agent's referral function waits for that program (its review and testimonial functions are ready now). Intended terms when it ships: $150 off referee / $100 store credit referrer.

**July 28 wrap (marketing-ops cleanup + go-live tuning).**
- **Heartbeat lineup settled for early stage.** ON: Sentinel 24h, Quality Control daily, Dispatcher 8h, Sales Outreach 1h, SDR 2h, Reactivation 6h, KB Manager 30d. HELD until volume ramps (daily is plenty when enabled): Referral and Reviews (block trimmed, referral function paused), Sales Scout, CSM. Event-driven / timer OFF: CEO/COO/CRO/CFO, Audit and Compliance, PRD Gatherer, Onboarding.
- **WF-07 fully wired.** Day-14 review SMS carries the Google (g.page/r/CfN5Rj0CdmrfEAI/review) + Trustpilot links; the testimonial-form link is live in the WF-07 email and on the enyrgy.com website.
- **Toll-free 888 approved for SMS.** IMPORTANT: the account has NO 10DLC / local number and never did (an earlier "A2P 10DLC approved" claim was wrong; corrected across all docs). SMS runs solely on 888-316-1695.
- **CNAM caller-ID** confirmed Approved in LC Phone with Friendly Name "Enyrgy Inc".
- **Content assets complete.** Commercial ROI one-pager (`Enyrgy_Commercial_ROI.pdf` + editable `.html` in repo; one placeholder = commercial booking link). Inbound 888 voicemail greeting recorded in Scott's voice. Outbound investor-drip voicemail script drafted (optional, record only if that touch is activated).
- **WF-28 fix.** Accessory-only Shopify reorders (e.g., wall mount) were triggering WF-06 device onboarding because WF-28 applied `unit_shipped` on any fulfilled order. Gated WF-28's trigger to the Home System product (the only device sold via Shopify; commercial is off-Shopify). WF-06 triggers on the `unit_shipped` tag, so the single filter fully controls it.
- **GHL agency corrections.** Agency mailing address corrected to Phoenix; Business Category fixed Medical -> Health & Wellness (Self Service Health Station niche; no A2P impact, separate TCR filing).
- **OPEN, employee-facing:** Enyrgy agency system emails send with the sender display name "Ledgerix Pro LLC" (Scott's SEPARATE GHL agency, Relationship 0-783-665, vs the Enyrgy agency's 0-167-470). Both agencies were verified internally correct (each Company Name matches its own brand; Enyrgy templates use {{agency.name}} = Enyrgy Inc so email bodies are right). Therefore it is a HighLevel PLATFORM cross-agency sender-identity issue, not an editable field in either agency. A support ticket is drafted in `Enyrgy_Master_TODO.md`; that is the fix path.
- Also resolved July 28: investor-presentation calendar conflict; Q2 investor update sent to Brian for review; GBP verified/live.

## WHAT WAS DONE (Session 14, July 25-26, 2026)

The whole session was a compliance and deployment pass: a full delta audit of every live funnel's copy, six KB additions, correction of a stale investor accreditation gate in the live workflow, deployment of the agent-trigger narrowing (Fix #1), and a Railway false-alarm fix. Nothing here changed the org architecture; it hardened what already exists.

**Full compliance delta audit of ALL live funnel copy.** Reviewed every live GHL email and SMS, one touch at a time, across Recovery (WF-14), Synthesis Gap (WF-16), Long-Term Nurture (WF-17), Winter (WF-19/20), VD Assessment (WF-21/22), Testimonial (WF-25/26), Abandoned Checkout (WF-29), the Investor Drip, and the Commercial Drip. Corrected copy was handed back for paste into GHL (Scott confirmed all pasted). Systemic fixes found and applied:
- **Prohibited words / em-dashes:** removed `fix`, `heal`, `treating`, and every em-dash (the Investor and Commercial drips were full of em-dashes and needed a sweep).
- **Guarantee vs lab-timeline contradiction:** several emails tied the 30-day money-back window to an 8-to-12-week lab retest ("risk only a lab fee"), which is impossible inside 30 days. Decoupled into two separate beats everywhere: labs are your own long-term proof, the 30-day guarantee is an independent keep-or-return decision ("you do not have to wait for those results to decide").
- **Light-does-five vs three pathways (unified frame, now in the KB):** sunlight produces FIVE outputs; Enyrgy delivers the THREE Triple-Pathway benefits. Fixed the biologically wrong linear cascade to parallel outputs, and corrected wavelength misattribution (nitric oxide = UVA photorelease, serotonin = daytime light, not downstream of vitamin D).
- **Study-caveat discipline:** the 100%-optimal and 39.96-to-84.20 figures are always cited with the small N=5 pilot context.
- **FTC testimonials (WF-25/26):** gift-card incentive reframed so it is not positivity-gated ("whatever your honest take"), consent line added for the reply path, and two operational flags recorded (disclose the material connection when publishing; typicality-screen consumer health testimonials).
- **Commercial economics (recurring number errors):** deficiency stat `89.9%` corrected to **77 percent of indoor adults** (appeared in 3 touches); treatments `30,000+` to **25,000+**; return rate never "zero"/"0%" to **under 1 percent**; payback always tied to **50 clients** (not "modest volume"); advisor bio reverted to the approved "Godfather of Vitamin D Research" wording (dropped the unverifiable "most cited"); "clinical/scientifically validated" softened to "clinical study"/"science-backed"; and the fabricated "$50,000 to $187,500" revenue range replaced with the KB figures ($14,700 / $29,400 / $58,800 at 25/50/100 clients).

**Six KB additions (committed and synced to the live skill).** Repo now at commit `0062ce4e`; the live `enyrgy-knowledge-base` Company Skill was re-pasted to match.
- Section 1: founder track record (Scott Hansbury, 8 startups, 5 exits, $500M+ created; David Letourneau, Alair Homes 1 to 100+ locations, $750M+ in sales).
- Section 2: vitamin D synthesis requires UVB in the 280 to 315 nm band (lamps do not emit it); sunlight photochemistry (five parallel outputs) plus the "light does five, Enyrgy delivers three" rule of thumb.
- Section 3: payment options (pay in full, finance, or rent monthly; specific rates not yet in the KB, confirm before quoting).
- Section 4: participant-level pilot results (P1-P5, reconcile exactly to the 39.96 / 84.20 averages); one-session-per-day cap (so "2 to 4 minutes a day" is accurate).

**Investor accreditation gate corrected in the LIVE workflow.** The live GHL "Accreditation Gate - PPM Check" branch still gated the PPM on `accredited_verified = Yes`, contradicting the attorney rule (accreditation is NOT required to share the PPM or terms; it gates only wire/acceptance). Scott removed the branches. The gate email was redrafted to state accreditation is not required to review the offering, and the final touch reverted to credibility-only for un-met investors (no offering terms in a cold broadcast, Reg D general-solicitation protection). Also caught a material term error in the final touch: `$2.5M` corrected to **$3.5M** raise. Follow-through: the same stale sub-agreement/term-sheet-behind-accreditation error was then found and fixed in the **Implementation Guide** (corrected to v3.9.4, three locations) and the **live Audit and Compliance and CFO agent blocks** (plus a build-pack Never-line fix). The accreditation carve-out is now consistent everywhere.

**Fix #1 deployed: agent triggers narrowed + Stop-on-Response ON.** Updated the top instruction block on five live agents so GHL owns the scheduled drip and the agents wake only for replies/exceptions (ending the double-send): **Onboarding**, **Sales Outreach**, **Reactivation** (narrowed off the shared trigger tags), **Sentinel** (notify Scott, not David), and **Referral and Reviews** (review ask unblocked with both GBP + Trustpilot links, invite everyone neutrally, ambassador ask paused). IMPORTANT for future edits: each live agent's instruction has a standard **Execution Contract** block that the build pack (`Enyrgy_Paperclip_Agent_Instruction_Blocks.md`) does not contain; only swap the `Role:` through `Facts:` top block and leave the Execution Contract intact. Paired GHL step also done: **Stop on Response = ON** on WF-06, WF-08, and the consumer drip (WF-11 to WF-20).

**Outbound and booking identity is Scott.** All outbound (sender, notifications, PPM delivery) is Scott, and the booking calendars route to Scott: Consumer, Commercial, and Investor Intro each host with Scott, meeting location set to a phone approach ("Scott will call you at the number you provided"), phone required on the forms. Founder roster, org, history, and internal escalation are unchanged.

**Funnel Ownership Map built.** New doc (`Enyrgy_Funnel_Ownership_Map`, .md + .docx) that ends the GHL-vs-agent confusion per touch: GHL workflow = autopilot (owns the scheduled bulk drip), Paperclip agent = brain (routing, replies, judgment, gated investor sends). Documents `drip_bypass` (manual switch) and Stop-on-Response (automatic switch) as the two clean handoff mechanisms.

**Railway false "Deploy failed" emails fixed.** Root cause was NOT the app: an orphaned duplicate service named `paperclip` (no domain, no volume) auto-deploys from the same repo/branch and fails its `/api/health` healthcheck on every push, while the real app `enyrgy-paperclip` deploys fine. Disabled the orphan's GitHub auto-deploy (its Settings > Source); failure emails stopped (confirmed). The orphan is not yet deleted (optional cleanup; delete via its Settings > Danger). Recorded in project memory (`railway-orphan-paperclip-service.md`). Its canvas tile does not render; open it via command palette or direct service URL.

## WHAT WAS DONE (Session 13, July 22, 2026)

The Paperclip agent org went from infrastructure to a working, compliance-gated system. The headline: the human-approval compliance gate is built AND proven live. The one open item is a Paperclip product bug blocking the final tool rollout to 12 agents, not anything in our design.

**GHL-to-MCP bridge, built and deployed.** Standalone TypeScript MCP server (`enyrgy-ghl-mcp`, GitHub `enyrgy/enyrgy-ghl-mcp`, also on device at `~/Projects/enyrgy-ghl-mcp`). 16 GHL tools (8 read, 8 write), zod schemas, tests passing, Docker + railway.toml, StreamableHTTP at POST /mcp with Bearer auth, `/healthz` and a `/` info endpoint that reports `mode`. Deployed to the Enyrgy Railway account, US West, healthy. Local git set to commit as Enyrgy via an SSH host-alias so Ledgerix work is unaffected. The GHL Private Integration token leaked into Paperclip logs earlier and was ROTATED (rotate-and-expire-now); token and `GHL_MCP_TOKEN` live only in Railway, never in chat.

**Ledgerix needs no bridge:** Ledgerix's architecture routes its top-of-funnel through a different stack, so it does not require a parallel GHL-to-MCP bridge the way Enyrgy does. Confirmed from the uploaded Ledgerix architecture doc.

**All 16 base agents built + CFO added (17 total).** Names carry NO "Agent" suffix (CEO, COO, CRO, Dispatcher, etc.). Reports-to hierarchy: CEO on top; COO, CRO, and the new CFO report to CEO; 7 COO-division agents; 6 CRO-division agents. Each agent's `AGENTS.md` holds its role block from the Instruction Blocks pack. The 17th agent, **CFO (reports to CEO)**, was created this session as the single owner of the investor funnel and securities process, so the compliance gate has one clean target.

**Knowledge Base corrected and actually loaded (v2).** Built as Company Skill `enyrgy-knowledge-base` (Skill Studio; frontmatter name must be the slug; Tagline capped at 120 chars). GOTCHA fixed: the skill first held ONLY frontmatter, the KB body was never saved, so agents had the description but none of the facts. Rebuilt the full `SKILL.md` (frontmatter + all 15 sections) and pasted it in = v2, shared to all agents. Lesson recorded: after creating any skill, confirm its SKILL.md body has content, not just frontmatter.

**Accreditation rule corrected (see the updated Attorney-Confirmed Rule section).** Scott corrected it: the subscription agreement and term sheet are PRE-ACCEPTANCE and may be sent without accreditation; accreditation gates ONLY wire instructions and accepting funds. KB Section 12 and 13 updated; `.md` + `.docx` rebuilt and saved.

**Compliance gate built AND proven live.** Framing corrected first: the system moves NO money (it sends messages and changes records); the risk is a wrong send, not funds moving. Built one Paperclip Rule (Apps > Advanced setup > Rules): "When CFO uses actions that make changes -> Ask first." Scoped to the CFO ALONE so the other agents scale freely, rather than a blanket gate that would bottleneck everything. **Live test PASSED:** assigned the CFO a write (add a tag), and the run STOPPED for human approval instead of executing, even with skip-permissions ON. This proves Paperclip's server-side rules engine is the real enforcement layer. Approvals live at Apps > Review; NEVER use "always-allow" for CFO money-stage actions.

**Budgets, permissions, heartbeats set.** Per-agent monthly USD caps on all 17 (Sentinel $3, most operational $2, heads/CFO/specialists $1-2), under the $25/mo Anthropic account wall. Least-privilege permissions pass: create-new-agents OFF on all (it and assign-tasks are an XOR pair; the floor is assign-only, harmless), create/import-skills ON only for KB Manager. Heartbeats are INTERVAL-based (no per-agent clock scheduler); they anchor to enable-time, so "8am Phoenix" = enable at 8am. ALL heartbeats left OFF until go-live; the enable checklist is in project memory.

**Bridge flipped to read-write.** Set `GHL_MCP_READONLY=false` in Railway; confirmed live via `GET /` -> `"mode":"read-write"`. (A stale 15-min fetch cache briefly misreported read-only; a cache-busted re-read confirmed read-write.)

**GHL rollout - RESOLVED + GO-LIVE PROVEN (July 24).** After the write-flip, Paperclip's original `ghl` connection would not refresh from 8 to 16 tools (the UI exposes no re-scan; toggles, runs, redeploy all failed). Workaround: a new app `ghlv2` scanned all 16 and was installed on the CFO for the gate test. Broadening `ghlv2` to the other agents via the profile Assign wizard kept erroring ("Tool profile catalog entry selector must belong to the same company"). Root cause turned out to be different: a DB inspection (via Claude Code + Railway Postgres) showed the database was healthy with NO dangling reference. Agent tool access is driven by `tool_connection_installs` rows, and the 12 operational agents simply had none. FIX: a single reviewed DB transaction mirroring the app's `putConnectionInstalls` added one install row + one profile binding for each of the 12, identical to the working execs (pure DB writes, no side effects). Verify passed (installs 5->17, shape-identical to a working agent, CFO policy byte-for-byte unchanged, fully reversible via a saved rollback.sql), and a live SDR read task returned correct data. All 12 operational agents are now live on the 16 read-write tools. The 8 write tools are ask-first company-wide, and the CFO's investor gate is untouched. Full detail in project memory (`paperclip-ghl-connection.md`). Lessons: Paperclip "delete" = soft archive; a working catalog-refresh endpoint (`POST /api/tool-connections/:id/catalog/refresh`) exists but is not wired to any button; access is by installs, not profiles.

**Status: GHL rollout complete and go-live proven.** All 17 agents can read GHL; all writes are held for human approval (8 company-wide ask-first policies plus the CFO's own gate). No heartbeats run yet, so nothing fires on a schedule until launch. The org is go-live ready.

## WHAT WAS DONE (Session 12, July 20-21, 2026)

### Paperclip deployed LIVE on Enyrgy's own Railway (Phase 2 infrastructure complete)
The Paperclip agent-orchestration platform is deployed, running, and stable on Enyrgy's own Railway account (entity-separate from Ledgerix). This is the foundation the 16-agent org will run on.
- **Repo:** forked paperclipai/paperclip to github.com/enyrgy/paperclip; cloned locally to ~/Projects/enyrgy-paperclip-core.
- **Deploy method:** Railway Empty Project + a single Docker service. Do NOT use "New Project from repo," which triggers Railway's Agent to split the monorepo into ~110 services (hit and deleted once). Postgres plugin attached. Public URL: https://enyrgy-paperclip-production.up.railway.app
- **Env vars:** PAPERCLIP_DEPLOYMENT_MODE=authenticated, PAPERCLIP_DEPLOYMENT_EXPOSURE=public, PAPERCLIP_PUBLIC_URL=the Railway URL, DATABASE_URL=${{Postgres.DATABASE_URL}}, ANTHROPIC_API_KEY (Enyrgy account). railway.toml pins the Docker build and the /api/health check.
- **Persistent volume** mounted at /paperclip (holds config.json, the secrets key, agent data). Fixed the volume-permission bug: Railway mounts the volume as root but the app runs as the non-root node user, so scripts/docker-entrypoint.sh now chowns /paperclip to node unconditionally on every start (previously gated, which caused EACCES).
- **First-admin bootstrap:** ran interactive `pnpm paperclipai onboard` (NOT --yes) in the Railway Console so it read the env vars and wrote config.json to the volume; onboard generated the bootstrap-CEO invite URL; opened it and claimed CEO/owner with scott@enyrgy.com.

### Enyrgy Anthropic (Claude) account created, billing separated, hard-capped
- A separate Anthropic Console org for Enyrgy (scott@enyrgy.com) so Ledgerix never pays for Enyrgy agent spend. $25 credits loaded.
- **Hard spend cap in place:** Monthly spend limit = $25 (the API stops serving at $25 in a calendar month). Auto-reload turned OFF, so the prepaid credit balance is a second hard floor - nothing can charge the card without a deliberate top-up. About $8 was spent this session on setup, environment-check probes, and the brief agent runs before cleanup; the counter resets Aug 1.

### Org created + runaway starter task cleaned up
- The first-run wizard created org "Enyrgy Inc," a mission (run Enyrgy's customer growth engine for the Vitamin D Primal Light Platform), and the lead agent renamed to CEO Agent on the Claude Code adapter (environment check passed; ANTHROPIC_API_KEY drives API-key auth, which is what we want for a business deployment).
- Paperclip auto-fired a canned demo task ("Hire your first engineer"), which spawned a Founding Engineer agent and 6 sub-tasks. Stopped and cancelled the entire subtree; the workspace is clean (0 tasks, 0 running agents). No net spend damage.
- The two paused built-in helper agents (Reflection Coach, Summarizer) are Paperclip defaults; left as-is.

### GHL Private Integration token created (least-privilege) for the agent layer
Created the "Paperclip Agent Layer" Private Integration in GHL with exactly 15 scopes: contacts (r/w), conversations (r/w), conversations/message (r/w), opportunities (r/w), locations/tags (r/w), workflows.readonly, calendars.readonly, calendars/events.readonly, forms.readonly, locations/customFields.readonly. Deliberately withheld billing, users, oauth, payments, and settings scopes. Token copied and held by Scott (not stored in chat).

### KEY FINDING: no native GHL connector in Paperclip, so a bridge is required
This Paperclip build has NO ready-made GoHighLevel connector. Its "Apps" area supports only Zapier or a bring-your-own MCP server (via URL). So the GHL token cannot simply be pasted into a connector. Connecting GHL requires a small bridge: a lightweight MCP server (Node, to deploy on the Enyrgy Railway account) that holds the token and exposes the shared GHL actions (get/update contact, add/remove tag, get/move opportunity stage, enroll in workflow, send message, create task, read conversation), connected to Paperclip via the bring-your-own MCP URL flow. This matches the Phase 2 Guide's "single shared GHL tool." Building this bridge is the first task next session and unblocks the rest of the agent-org build.

### Where the Paperclip build stands against the Phase 2 Setup Guide
- DONE: Step 1 Deploy (Section 5), admin claimed, org + CEO lead created, budget cap set.
- IN PROGRESS: Step 2 Connect GHL (Section 6) - token created, bridge pending.
- NOT STARTED: Step 3 Load KB; Steps 4-6 build the remaining 15 agents (CEO already exists); Step 7 compliance gate; Step 8 5-contact test; Step 9 staged go-live.

### Paperclip access details (for next session)
- Dashboard: https://enyrgy-paperclip-production.up.railway.app (owner: scott@enyrgy.com)
- Railway: the Enyrgy Railway account, one Paperclip service + Postgres + /paperclip volume
- Local clone: ~/Projects/enyrgy-paperclip-core. Note: local git is authed as LedgerixPro, so pushing to enyrgy/paperclip needs the auth fixed or a commit via GitHub web.
- GHL Private Integration token: held by Scott; it will live in the bridge service's Railway env vars, not in Paperclip.

---

## WHAT WAS DONE (Session 11, July 19, 2026)

### Shopify native integration connected (controlled, no re-triggering)
Connected GHL's LeadConnector Shopify app for store handle `enyrgy` (enyrgy.myshopify.com). Same safe method as the CSV import: unpublished WF-01 (Contact Created), WF-06 (unit_shipped), and WF-07 (unit_activated) during the initial sync so the historical backfill could not re-fire onboarding or the router, verified, then re-published all three.
- **Import Elements (historical backfill):** Order Import ON, Product Import ON, Contact Import OFF (the 617 were already imported manually; GHL merges on email so no duplication), Collection Import OFF, Transaction Import OFF.
- **Sync Settings (ongoing):** Contact Sync ON, Order Sync ON with the Order Received trigger enabled, Product Sync ON, Transaction Sync OFF, Collection Sync OFF.
- The sync created some contacts beyond the 617 (partners, staff, older buyers), all untagged, so no `type_` tag means no drip can touch them. Paul Barattiero (OEM white-label partner) was tagged `drip_bypass` + `source_oem_partner`. Rule for any non-customer the sync pulls in: `drip_bypass` plus a marker, never a `type_` tag.

### WF-27 Shopify New Customer Tagging built and LIVE
Trigger: Shopify order placed. Action: add `drip_bypass`, `source_shopify`, `status_customer`. Allow Re-Entry ON. This shields every new Shopify buyer from lead nurture (they already purchased) while flagging them as a customer. Closes the going-forward gap created by Contact Sync (new buyers auto-create contacts that would otherwise hit WF-01).

### Remaining Shopify (not done today)
- Fulfillment workflow: use the "Order fulfilled" trigger to apply `unit_shipped`, which feeds WF-06 onboarding. (There is also a deprecating "Shopify order fulfilled" trigger; use the newer "Order fulfilled".)
- Abandoned-checkout webhook: developer build, highest-ROI recovery piece.

### All five drips now have the drip_bypass gate
Added the first-step If/Else "Bypass Check" (NOT drip_bypass to run, else END) to the Commercial, Partner, and Investor Warm drips, which previously lacked it. The Consumer and Investor drips already had it. So `drip_bypass` now reliably suppresses all five drips.

### Investor Drip Touch 7 accreditation gate removed (per attorney rule)
The PPM now sends to everyone at Touch 7 (post-intro-meeting), not just accredited investors. Added a PPM email send to the "Not Yet Accredited" branch and renamed the gate to a router; the accreditation nudge stays for non-accredited. Accreditation is still required later, before commitment/subscription/wire (handled in the pipeline, untouched). The PPM email copy was confirmed accreditation-neutral (Session 11).

### Toll-free A2P Verification (TFV) corrected and resubmitted
**CORRECTION (July 28, 2026): the claim below that a 10DLC/local-number registration was "A2P Fully Approved" was WRONG. No 10DLC/local number was ever approved and none is associated with the account. SMS runs solely on the toll-free 888-316-1695, whose Toll-Free Verification was approved July 28, 2026. The original (incorrect) Session 11 note is preserved below for history.** Original note: the toll-free number **+1 888-316-1695 has its own separate Toll-Free Verification**, which was **Rejected** (error 30496, Use Case and Use Case Summary Inconsistent: the Marketing category did not match a description that mixed in transactional content). Fixed by rewriting the use-case description to be marketing-consistent, using go.enyrgy.com/sms-opt-in as the opt-in proof URL, removing an em-dash from the sample message, and resubmitting. Status now: **Verification in progress** (carrier queue, typically a few business days). SMS cannot send from the toll-free until this passes.

### Google Business Profile in progress (video verification pending)
Eligibility resolved: Enyrgy qualifies for a Business Profile because registered users physically come to the GCU Innovation Center location to take treatments on the demo unit (real in-person customer contact). The pure "online retail" path was abandoned because it routes to Merchant Center (which kept throwing "try again later") and does not produce a Google review link. Set up as a Local store, category **Wellness center**, address 5115 N 27th Ave Bld 66, phone 888-316-1695. Google required **video verification** (instant/Search Console was overridden, likely due to the shared GCU address). Scott records the live walkthrough video at the office next (a pre-existing Instagram clip cannot be used; must be a fresh, unedited recording through Google's tool showing signage, the demo unit, and proof of management). Once verified, grab the review link and wire into WF-07.

### Abandoned Checkout Recovery built LIVE end to end (WF-29 + Railway)
The full cart-recovery system is live. Reassurance approach, no discount (a coupon would cheapen a premium platform and train buyers to bail for discounts).
- **Shopify custom app "Enyrgy Abandoned Checkout Sync"** created in the Dev Dashboard (the new dev-dashboard model, not the legacy static-token flow). Scopes read_checkouts + read_orders. Legacy install flow OFF (that setting had blocked the install; unchecking it fixed it). Installed on the store. Auth uses the **client credentials grant**: the service exchanges Client ID + Secret for a 24-hour token, refreshed automatically. Client ID `13afeaf3ecd9fe2d1190244dfd240f6d` (Secret lives only in Railway).
- **Railway service** (new Enyrgy-owned Railway account, currently on TRIAL). Deployed from GitHub repo `enyrgy/enyrgy-abandoned-checkout` (`server.js`, self-scheduling every 20 min, no cron, in-memory dedup). Env vars: SHOPIFY_STORE=enyrgy, SHOPIFY_CLIENT_ID, SHOPIFY_CLIENT_SECRET, SHOPIFY_API_VERSION, GHL_WEBHOOK_URL (WF-29), ABANDON_GRACE_MINUTES=60, LOOKBACK_MINUTES=1440, RUN_EVERY_MINUTES=20, DRY_RUN=false. Validated live: logs show `scanned=0 eligible=0 forwarded=0` (clean auth + fetch; 0 = no abandoned carts in the window right now).
- **WF-29 Abandoned Checkout Recovery** (LIVE): Inbound Webhook trigger (URL below) -> Create Contact (maps first/last name, email, phone from the webhook) -> Add Tags abandoned_checkout + drip_bypass + source_shopify -> Email 1 (immediate) -> Wait 1 day -> If/Else "Purchased Check" (Tags includes status_customer -> END; buyers get no more emails) -> Email 2 (None branch) -> Wait 2 days -> Email 3. Re-Entry On, Stop on Response On. All copy through CUB + humanize-pro; the recovery link is `{{inboundWebhookRequest.recovery_url}}`.
- **WF-27 updated:** added `status_customer` to its tag action (it was missing), so a Shopify order now tags the buyer status_customer, which is what WF-29's Purchased Check reads.
- Deliverables: `server.js`, `abandoned-checkout-sync.js` (one-shot local variant), `package.json`, `README-abandoned-checkout.md`, `.env.example`, and `Enyrgy_Abandoned_Checkout_Recovery` (.md + .docx, WF-29 spec + the three reassurance emails).

### Remaining on Abandoned Checkout (not blocking, system is live)
- Railway upgraded to the Hobby plan (Session 11), so the service is always-on. No action needed.
- NOT built, and dropped as unnecessary. The website sells one fixed-price consumer product ($2,995), so cart value never varies and a value-threshold escalation has nothing to trigger on. Optional micro-adds only if wanted: keep Abandoned Checkout ID as a WF-29 de-dupe backstop, and/or a simple notify-Scott-on-every-abandoned-cart (no threshold, since every cart is worth a personal look at this price).
- Optional: a real end-to-end test (start a checkout on shop.enyrgy.com, abandon it, wait past the 60-min grace, confirm it lands in WF-29).

---

## WHAT WAS DONE (Session 10, July 18, 2026)

### Testimonial collection system built LIVE in GHL
A complete video-or-written testimonial engine, all copy routed through CUB and humanize-pro.
- **Customer Testimonial Form** (form ID OjahkWeVDeozQkfG9dW2): added a File Upload field ("Your video (optional)," File Types = All so it accepts video; helper text points large videos to reply-by-email), reusing the form's existing "Results Noticed" free-text field as the written lane. The form already carried the marketing-permission consent, left as is. On submit it applies `testimonial_submitted`.
- **WF-25 Testimonial Request** (the ask): trigger Contact Tag `request_testimonial`; an If/Else on `seg_facility` routes facilities to the operator-voiced email ("60 seconds, operator to operator?") and everyone else to the consumer email ("A quick favor, {{first_name}}?"). Both branches send one email and end. Allow Re-Entry Off. Tested both branches live. NOT auto-enrolled: you hand-pick recipients by adding `request_testimonial` to a chosen segment.
- **WF-26 Testimonial Received** (the response): trigger Form Submitted = Customer Testimonial Form; actions add `testimonial_submitted`, send an internal notification to scott@enyrgy.com, add `gift_card_pending` (the manual fulfillment queue), and send the tightened thank-you email. Allow Re-Entry Off. Tested live.
- **Gift-card thank-you:** both request emails close with a P.S. offering a gift card, no dollar amount named on purpose so the amount can start modest and rise without changing copy. Fulfillment is manual: weekly, pull the `gift_card_pending` list, send a Visa or Amazon e-card, swap the tag to `gift_card_sent`.
- Emails live in `Enyrgy_Testimonial_Request_Emails` (.md + .docx). The form's share URL (https://api.leadconnectorhq.com/widget/form/OjahkWeVDeozQkfG9dW2) is the video upload link in both emails.

### 7 contact custom fields added (Health Profile folder)
Registration Date (Date), Skin Type (Single Options 1-6), Gender (Single Options Male/Female), Height (Text, ft/in), Weight (Number, lbs), Vitamin D Level (Number, ng/mL), plus Age was intentionally skipped (derivable from birthdate and goes stale). Birthdate uses GHL's native Date of Birth field, not a custom field.

### 617 existing customers imported into GHL (safe, no workflow enrollment)
- **Full workflow trigger audit first.** All 27 workflows were checked. Only **WF-01 New Lead Router** triggers on Contact Created, so it was the only import risk. Every other workflow triggers on a tag, webhook, form, schedule, or parent enrollment. The five drip campaigns (Commercial, Consumer, Investor, Investor Warm, Partner) all trigger on a `type_*` tag. So the safe-import rule: unpublish WF-01 during import, and import zero `type_`, `status_`, `unit_`, or `investor` tags.
- **Data cleaned:** literal "NULL" strings blanked, Registration Date and Date of Birth reformatted to M/D/YYYY, phones to +1 E.164, Skin Type kept as 1-6 (blanks left truly blank per Scott).
- **Shared-email handling:** GHL enforces email as a unique key and merges same-email contacts (proven in the 5-row test: Aki and Yas Takayama collapsed to one). 14 emails were shared by 31 household members. Scott decided per household who keeps the email (parent) and blanked the email on the others (child), keeping their name and phone so GHL creates them as separate phone-keyed contacts. Final file: 617 rows, 17 blank-email children, zero remaining duplicate emails.
- **Import settings used:** Create contacts (create-only), Add-to-workflow left OFF, Add-tags left OFF (tags came from the file's Tags column). Tags survived the CSV conversion intact. Landed in the "Initial Customer Load 7-7-26" Smartlist. WF-01 re-published after.
- Import file: `Enyrgy_Production_Users_FINAL_for_GHL.csv` (617 rows).

### Note found during the audit (not blocking)
The Commercial, Partner, and Investor Warm drips have no `drip_bypass` first-step gate (Consumer and Investor drips do). So `drip_bypass` does NOT protect a contact from the Commercial or Partner drip; only not applying their `type_` tag does. Worth adding a bypass gate to those three later for consistency.

### Next up (testimonials)
Hand-pick the first testimonial batch from the "Initial Customer Load" list (start with happiest users; for facilities, consider asking owners only, since the 24 seg_facility contacts include both owners and operators), add `request_testimonial` to just those, and send in warmup-safe batches from mg.enyrgy.com.

---

## WHAT WAS DONE (Session 9, July 17, 2026)

### Vitamin D Assessment built LIVE in GHL, end to end
Walked through the full GHL integration for the Vitamin D Assessment (Lead Magnet 5) and took it live and tested. WF-21 Vitamin D Assessment Capture: Inbound Webhook trigger, Create Contact with all 11 fields mapped, a Standard Add Tag with the six always-on tags (type_consumer, source_lead_magnet, status_new, magnet_lead, drip_bypass, magnet_vitamin_d_assessment), a Dynamic Add Tag that reads the quiz's tags list, the CUB-refined results email, and (redundant now) a risk-band Condition. Two custom fields added (Deficiency Risk Score, Deficiency Risk Band). Page deployed to go.enyrgy.com/vitamin-d-assessment. Live end-to-end test passed: contact created with fields and tags, results email delivered.

### Segmentation solved in one action
The quiz computes goal, SMS consent, and the risk band client-side and sends them in the payload's `tags` field. A single Dynamic Add Tag action in WF-21 inserting `{{inboundWebhookRequest.tags}}` applies them all. This replaced the planned SMS Consent field plus separate goal and SMS workflows. GHL requires one action per mode (Standard vs Dynamic), so WF-21 has both.

### WF-22 Vitamin D Assessment Nurture is LIVE
A 3-email solution-aware series. Trigger on the magnet tag, 2-day wait, Email 1 (Your D3 does one job. Light does five.), 2-day wait, Email 2 (study and safety), 3-day wait, Email 3 (own-labs close), then Add to WF-17 Long-Term Nurture. Emails routed through CUB, eugene-skill, and humanize-pro.

### Key fixes found during go-live
- The browser send had to be form-encoded (application/x-www-form-urlencoded); GHL did not parse the earlier JSON or plain-text attempts, so contacts came through empty.
- GHL condition branches do not rejoin, so unconditional actions (the email) sit above any branch.
- Results and email CTAs re-routed by readiness: ready buyers to the platform or order page, unsure people to the Consumer Discovery booking calendar, not straight to checkout.
- Disclosures: removed the annual skin-exam line from all emails, the page footer, and the Brand Guide, per Scott.

### Website CTAs added
Published a "take the assessment" CTA on five pages, all linking to go.enyrgy.com/vitamin-d-assessment: The Science and FAQ (primary orange), Home, The Platform, and Our Story (secondary outline).

### Follow-ons
- DONE: goal and SMS segmentation (the Dynamic Add Tag action above).
- DONE: WF-22 nurture series.
- Optional: a clean go.enyrgy.com/book vanity redirect to the Consumer Discovery calendar (the widget URL works today).
- Later: an optional high-risk accelerator variant of the nurture series, keyed off the high_deficiency_risk tag.

---

## WHAT WAS DONE (Session 8, July 17, 2026)

### YourTango partnership assets
Reviewed Millie's first draft of the branded content ("9 Signs Your Body Is Running Low On Sunlight") and produced: the revised article for Tom (7 signs, 729 words, single CTA to the Tired Test), an internal editorial record, and Scott's response to Millie. Article and CTA were run through humanize-pro and CUB rather than hand-edited; CUB found a vague antecedent and a buried lede that a manual read missed.

### lead-magnets.md repaired, v2.0 to v2.1
The Tired Test section contained the Vitamin D Assessment's questions (Fitzpatrick skin type, latitude, an ICP router) filed under the wrong heading. Those were moved to a new Lead Magnet 5 section. The Tired Test section now matches its source spec and the live quiz: four Problem-Aware questions, one result for everyone. The single-path design is now documented as intentional so it is not mistaken for a gap again.

### Vitamin D Assessment documented
Lead Magnet 5 existed as built HTML but was never documented in lead-magnets.md. It now has a full section: fields, tags, scoring, build steps outstanding, and its place in the funnel relative to the Tired Test.

### 1-in-4 claim corrected
Millie flagged that "1 in 4 cannot absorb oral vitamin D" on the consumer objections sheet had no source. Correct: the underlying research is real (Carlberg, VitDmet and VitDbol trials, ~25% low responders, Nutrients 2023 15(15):3382) but the claim is about RESPONSE, not absorption. Low responders absorb the pill fine; their cells do less with it. Approved wording: "in these trials, about one in four participants were low responders to vitamin D supplementation." Never "one in four Americans" (trials were 71, 35, and 25 participants). The objections sheet needs this correction.

### about-me.md cleaned
Corrected stale items: Co-founder & CEO (not Founder), Phoenix (not Scottsdale), 25,000+ treatments (file contradicted itself), ten direct commercial placements for external use (16 total), Brian described by function not title, Millie and Shanna added, 37 em-dashes removed. Added a Claim Discipline section and a Current Commercial Context section.

**Known stale (RESOLVED in Session 9):** the `Enyrgy_Session_Handoff.docx` cover previously carried 602-321-0322 and "End of Session 6." The cover now shows the toll-free +1 888-316-1695, the session label matches the body, and the Vitamin D Assessment and Google Business Profile task entries are present.

---

## WHAT WAS DONE THIS SESSION (Session 7, July 13, 2026)

### Paperclip Phase 2 Setup Guide created (new)
Authored the full Phase 2 build plan as `Enyrgy_Paperclip_Phase2_Setup_Guide` (.md + .docx). It takes Scott from an empty Paperclip install to a tested, governed 16-agent organization operating the GHL sub-account. Contents: what Paperclip is and how it connects to GHL (open-source, self-hosted, bring-your-own-agent, acting on GHL via API); prerequisites and key constants; the reconciled org chart; deploy and connect steps with least-privilege scopes; KB load checklist; ready-to-paste instruction blocks for the CEO orchestrator and every COO and CRO division agent; the compliance gate wired as a hard approval gate with the attorney-confirmed PPM and accreditation rule; the agent-to-workflow mapping (WF-01 through WF-10); governance (budgets, heartbeats, config revisioning, rollback); a 5-contact test plan with pass and fail criteria per agent; and a staged go-live with graceful fallback to Phase 1.

### Agent count reconciled
The built organization is 16 agents (3 C-Suite + 7 COO + 6 CRO). The prior "24-agent" figure in WIP-3 was an error; the correct upper bound is 22 (16 core plus all six recommended Phase 2 additions). Corrected in WIP-3 and stated in the Phase 2 guide.

### Em-dash rule enforced across all docs
Standing rule reinforced: no em-dashes ever, this session and all sessions. The five docs that contained em-dashes (Implementation Guide v3.9, WIP-3, Session Handoff, Consumer ICP Dartboard, B2B ICP Dartboard) were regenerated with zero em-dashes in both `.md` and `.docx`. The em-dash in the cover author line ("Co-Founder - Enyrgy Inc") was also corrected.

### Brand style rebuilt on all .docx
All regenerated `.docx` were rebuilt to match the locked brand style (branded cover page, Sunrise Orange running header per document, centered footer with page numbers, Montserrat, orange headings, properly rendering tables), using the prior Implementation Guide `.docx` as the exact style reference.

**Still pending for Scott:** deploy Paperclip and execute the Phase 2 guide; update Investor Drip Touch 7 in GHL to remove the accredited_verified gate from PPM delivery; re-upload the cleaned `.md` files into the project.

---

## WHAT WAS DONE (Session 6, July 13, 2026)

### Implementation Guide: v3.8.4 -> v3.9
The uploaded v3.8.4 was the correct ground truth (not v3.7 as previously thought). Applied attorney-confirmed corrections to produce v3.9. Both `.md` and `.docx` generated and validated.

**7 locations corrected across the investor funnel:**
- Section 2, Stage 3: PPM sent at end of intro meeting - no accreditation required before PPM
- Section 2, Stage 4: Renamed to "PPM Sent and Due Diligence" - accreditation gate removed from this stage
- Section 2, Stage 5: Renamed to "Accreditation and Commitment" - gate correctly placed here with COMPLIANCE GATE callout
- Section 2, Daily Rhythm: "between Accreditation and Commitment" -> "between PPM Sent and Commitment"
- Section 3, Compliance Gate rules: Replaced "Investor gate" and "PPM gate" with correctly framed "PPM delivery" and "Commitment gate"
- Section 11, Investor Drip Touch 6 + 7: Touch 6 changed to traction follow-up; Touch 7 to PPM delivery after intro meeting
- Section 22, Investor Pitch Flow Step 6: Removed "AFTER accreditation"; corrected to PPM after intro meeting

**Three attorney/compliance callout boxes added** (amber = ATTORNEY CONFIRMED, red = COMPLIANCE GATE) in Sections 2, 3, and 11.

**Other v3.9 fixes:**
- SHAKEN/STIR: "Approved" -> "Approved & Verified"
- KB Manager: attorney guidance on PPM/accreditation added explicitly
- Pipeline 3: stage order corrected (PPM Sent before Accreditation)
- Section 17 header note: corrected
- Section 18: "post-accreditation" -> "PPM sent after intro meeting"; new row for accreditation timing
- Brand fonts updated to Montserrat throughout the Word doc

### WIP Tracker Updated (Enyrgy_GHL_WIP-3)
- A2P reference URLs corrected: `www.enyrgy.com` -> `shop.enyrgy.com` (both Privacy Policy and Terms of Service)
- SHAKEN/STIR marked Approved & Verified
- Facility address update marked Complete
- Winter Protocol workflow + landing page marked Complete
- David SMTP / per-workflow sender marked Complete (LC Email, Scott is sender on all workflows)
- Checklist items 2, 3, 4, and 8 marked Complete
- Total raise corrected: $2.5M -> $3.5M in Section 9 Permanent Decisions
- Content framework rule corrected in Section 9 (Story Selling OS is not for all content)
- Session 3 log entry added

---

## ATTORNEY-CONFIRMED RULE (load into KB Manager, wire into all investor workflows)

> **PPM may be sent to any interested investor after the intro meeting. Accreditation is NOT required before sending the PPM.**
>
> **The subscription agreement and term sheet are PRE-ACCEPTANCE documents and may also be sent BEFORE accreditation is confirmed. Accreditation is NOT required to send them.**
>
> **Accreditation (accredited_verified = Yes) IS required ONLY before: wire instructions, or accepting any investment (the points where funds change hands). No exceptions.**

This was confirmed by Enyrgy's securities attorney. CORRECTED Session 13 (July 22): an earlier draft wrongly gated the subscription agreement and term sheet behind accreditation. They are pre-acceptance (the subscription agreement carries the accreditation questionnaire itself, so it must reach the investor before verification can happen). Accreditation gates only the two money-moving actions: wire instructions and accepting funds. The workflow change: remove the accredited_verified gate from Touch 7 PPM delivery AND from subscription-agreement / term-sheet delivery. Keep the gate on wire instructions and acceptance of funds.

**Status: corrected in the Implementation Guide and the GHL workflow (Session 11), re-corrected in the KB (Section 12 and 13) Session 13, and a residual live-workflow gate was found and removed in Session 14.** Session 14 note: the pre-Session-13 error (gating the subscription agreement and term sheet behind accreditation) had persisted in three places the KB correction never reached. All now fixed: (1) the live Investor Drip "Accreditation Gate - PPM Check" branch was removed by Scott (gate email + final touch redrafted, credibility-only for un-met investors); (2) the Implementation Guide was corrected to v3.9.4 in three locations (Stage 5, Compliance Gate rules, pipeline summary); (3) the live Audit and Compliance and CFO agent instructions were updated to the corrected carve-out (build-pack Never-line also fixed). The carve-out is now consistent across the KB, the Implementation Guide, the GHL workflow, and every agent block. In Paperclip, the rule is enforced by the CFO-scoped ask-first gate plus the KB rule the agents read.

---

## REMAINING OPEN TASKS

### HIGH Priority

| Task | Owner | Notes |
|------|-------|-------|
| Verify LIVE investor/compliance agent blocks | DONE (Session 14) | The live Audit and Compliance and CFO agent instructions were updated to the corrected accreditation carve-out (subscription agreement + term sheet pre-acceptance; accreditation only before wire/acceptance). The build-pack Audit and Compliance Never-line was also fixed. Carve-out is now consistent across KB S12/13, Implementation Guide v3.9.4, the GHL workflow, and all agent blocks. |
| Fix #1 agent narrowing + Stop-on-Response | DONE (Session 14) | Onboarding, Sales Outreach, Reactivation narrowed off shared triggers; Sentinel notifies Scott; Referral and Reviews review-ask unblocked (GBP + Trustpilot, no gating), ambassador paused. Stop on Response ON on WF-06, WF-08, and the consumer drip (WF-11 to WF-20). Double-send resolved. |
| Full compliance delta audit of live copy | DONE (Session 14) | Every live email/SMS across all funnels reviewed and corrected (prohibited words, em-dashes, KB-claim drift, guarantee/timeline decouple, light-does-five/three frame, FTC testimonials, investor Reg D, commercial economics). Scott pasted all corrections into GHL. |
| Delete orphaned Railway `paperclip` service | Optional (Session 14) | Auto-deploy already disabled (stopped the false "Deploy failed" emails). Deleting the duplicate service is optional final cleanup: its Settings > Danger > Delete, confirm by typing `paperclip`. Do NOT touch `enyrgy-paperclip` (the real app). |
| Google Business Profile - Enyrgy setup | IN PROGRESS (Session 11) | Set up as Local store (eligible: users take treatments on-site), category Wellness center. Google requires VIDEO verification (Search Console instant was overridden, likely shared GCU address). Scott records the live walkthrough video at the office next. Then grab review link, wire into WF-07. |
| Toll-free A2P Verification (888-316-1695) | APPROVED July 28, 2026 | The ONLY SMS number on the account (no 10DLC/local number exists). Was Rejected (30496 use-case inconsistency), corrected to marketing-consistent, resubmitted, and approved. SMS now sends from the toll-free. |
| Ledgerix Pro LLC GBP transfer | Scott | Transfer to scott@ledgerixpro.com - blocked by Google 7-day hold (should have cleared ~July 5) |
| PPM document in Investor Touch 7 | DONE (Session 14) | Attorney-approved. No longer a placeholder; the approved PPM is used in Touch 7. |
| Update Investor Drip Touch 7 in GHL | DONE (Session 11) | Accreditation gate removed; PPM now sends to all at Touch 7. PPM email copy confirmed accreditation-neutral. |
| Deploy Vitamin D Assessment Lead Magnet | DONE (Session 9) | LIVE at go.enyrgy.com/vitamin-d-assessment. WF-21 capture + WF-22 nurture live; results email sending. Lead Magnet 5, the Solution-Aware sorting magnet. NOT a replacement for the Tired Test. |
| Shopify Abandoned Checkout Recovery | LIVE (Session 11) | WF-29 + Railway service (Hobby plan, always-on) + Shopify custom app, all live and running. |
| Enyrgy Railway account | DONE (Session 11-12) | On Hobby plan, always-on. Now hosts BOTH the abandoned-checkout service AND the Paperclip deploy (single service + Postgres + /paperclip volume). |
| Shopify -> GHL Native Integration | DONE (Session 11) | Connected (handle enyrgy). Orders + products backfilled, contacts merged on email, WF-27 shields buyers. Remaining: fulfillment -> unit_shipped workflow (use "Order fulfilled" trigger, feeds WF-06). |
| Build GHL-to-MCP bridge service | DONE (Session 13) | Built, deployed to Enyrgy Railway, healthy, token rotated. Now READ-WRITE (`GHL_MCP_READONLY=false`). 16 tools (8 read, 8 write). Repo `enyrgy/enyrgy-ghl-mcp`. |
| Paperclip Phase 2 deploy | DONE (Session 12) | Live at https://enyrgy-paperclip-production.up.railway.app, owner scott@enyrgy.com, budget hard-capped. |
| GHL tools rollout to all agents | DONE (July 24) | RESOLVED via a reviewed DB transaction (Claude Code + Railway Postgres) that added `tool_connection_installs` + profile bindings for the 12 operational agents on ghlv2. Verified (5->17 installs, shape-identical to working agents, CFO policy unchanged, reversible), and a live SDR read task confirmed. Root cause was missing install rows, not the profile-assign error. |

### MEDIUM Priority

| Task | Owner | Notes |
|------|-------|-------|
| Calendar conflict detection | RESOLVED (Session 14) | Root cause: the calendar was connected but "check for conflicts" was OFF, so GHL never read the real schedule (connected does NOT equal conflict-checking). Turned conflict-checking ON at the user level, which fixed availability across all of Scott's host calendars. Gotcha for the collective Investor Presentation calendar: enable conflict-checking for each host. Second gotcha: an all-day event marked "Busy" blocks the entire day (zero slots) - set such events to "Free" if they should not block bookings. |
| Shopify Referral App | Scott | Install Referral Candy or Smile.io |
| Trustpilot connect Shopify | Scott | Automate review invitations post-purchase |
| Commercial form SMS consent | DONE (Session 11) | Consent text + checkbox added to Commercial Inquiry Form. |
| Partner form SMS consent | DONE (Session 11) | Consent text + checkbox added to Partner Application Form. |
| Send first testimonial batch | Scott | System LIVE (WF-25/WF-26). Hand-pick from "Initial Customer Load" list, add request_testimonial to just those, send in warmup-safe batches. Facilities: consider owners only (seg_facility includes operators too). |
| Gift-card fulfillment | Scott | Weekly, pull gift_card_pending list, send Visa/Amazon e-card, swap tag to gift_card_sent. |
| Testimonial form link on enyrgy.com | Scott | Add to post-purchase follow-up |
| Website punch list | Scott | See detail below |

### Website Punch List (enyrgy.com)
- The Platform page: add Synthesis Gap CTA; verify "how the platform works" CTA links to /the-platform
- Our Story page: verify two CTA link targets
- FAQ page: repoint "Read the Clinical Data" link from /home to /the-science
- The Science page: delete "This is a Paragraph Font" placeholder text
- Shopify Privacy Policy: confirm shop.enyrgy.com subdomain address is current everywhere (A2P-relevant)
- **SEASONAL REMINDER (act ~late August 2026):** add the Winter Protocol CTA to enyrgy.com for the SAD Aug-Oct purchase window. It is deliberately OFF the site now (mid-summer, off-season), NOT missing by mistake. Add a "FOR THE SEASONAL SUFFERER" segment block to the homepage "Who gets the most from Enyrgy" row linking to go.enyrgy.com/winter-protocol (NOT enyrgy.com/winter-protocol, which is blank). Funnel WF-19/WF-20 is already live; this is website surfacing only. Optional: seasonal hero band Aug-Mar, hidden Apr-Jul. A scheduled reminder is also set for late August.

### LOW Priority / Future

| Task | Owner | Notes |
|------|-------|-------|
| VD Assessment high-risk accelerator | Scott | Optional. A sharper nurture variant keyed off high_deficiency_risk. Core nurture (WF-22) and segmentation are already live. |
| Update live page footer disclosure | Scott | The deployed assessment page still shows the old footer with the skin-exam line until it is re-pasted (low priority). |
| CNAM Voice registration | Scott | Displays "Enyrgy" on outbound caller ID |
| Paperclip agent setup | GO-LIVE READY (July 24) | DONE: bridge built + read-write; all 17 agents built; KB v2; compliance gate proven live (CFO-scoped ask-first + 8 company-wide write approvals, held with skip-permissions on); budgets, permissions, heartbeat checklist set; all 12 operational agents live on the 16 read-write tools (DB-install fix + live SDR proof). REMAINING (all optional / launch, none blocking): (1) optional least-privilege tidy - remove GHL from CEO/COO/CRO/KB Manager; (2) 5-contact draft-and-hold test (test_contact tag); (3) staged go-live: enable heartbeats per the checklist; (4) optionally relax the 8 company-wide write approvals for non-CFO scale later; (5) remove the test_cfo_gate tag if that write was approved. |
| Reporting dashboards | Scott | Build KPI views in GHL |
| 600+ existing customer import | DONE (Session 10) | 617 imported into GHL, tagged drip_bypass + legacy_customer (24 also seg_facility), landed in "Initial Customer Load 7-7-26" Smartlist. Still do NOT bulk-send from mg.enyrgy.com during warmup - ramp gradually. |
| Commercial/Partner forms on go.enyrgy.com | Developer | Embed or link to GHL forms |

---

## ICP-DARTBOARD CONSUMER FUNNEL - CURRENT STATE (all live)

| Ring | ICP | Magnet | Entry URL | Capture WF | Nurture WF | Long-term |
|------|-----|--------|-----------|-----------|------------|-----------|
| Bullseye | Stack Optimizer | Synthesis Gap Guide | go.enyrgy.com/synthesis-gap | WF-15 | WF-16 (A/B) | WF-17 |
| Inner Ring | Athlete | Recovery Protocol Guide | go.enyrgy.com/recovery-protocol | WF-18 | WF-14 (A/B) | WF-17 |
| Inner Ring | SAD (seasonal) | Winter Protocol Guide | go.enyrgy.com/winter-protocol | WF-19 | WF-20 (3A/3B) | WF-17 |
| Outer Ring | Energy/Sleep | Tired Test (quiz) | go.enyrgy.com/tired-test | WF-12 | WF-13 | WF-17 |
| Cross-ring | Solution Aware | Vitamin D Assessment | go.enyrgy.com/vitamin-d-assessment | WF-21 | WF-22 | WF-17 |
| Everyone else | General | Contact form | contact form | WF-11/WF-01 | (none) | Consumer Drip |

**Suppression:** magnet_lead + drip_bypass applied at capture. Consumer Drip, WF-02, and WF-04 all begin with If/Else gate: NOT drip_bypass -> run; else END.

---

## KEY URLS & WEBHOOKS

**Pages:**
- SMS Opt-In: https://go.enyrgy.com/sms-opt-in
- Synthesis Gap: https://go.enyrgy.com/synthesis-gap
- Recovery: https://go.enyrgy.com/recovery-protocol
- Winter Protocol: https://go.enyrgy.com/winter-protocol
- Tired Test: https://go.enyrgy.com/tired-test
- Vitamin D Assessment: https://go.enyrgy.com/vitamin-d-assessment
- Order: https://shop.enyrgy.com/products/uvb-light-therapy

**Webhooks:**
- WF-12 (Tired Test): https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/6c3a7c6c-f1fa-4c85-a03a-a1c42fdfb13d
- WF-15 (Synthesis Gap): https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/fd32493c-6ec1-4e55-9edb-75399aa53a34
- WF-18 (Recovery): https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/3ae538d7-81a9-42a7-9e18-5e7c8b19b84a
- WF-19 (Winter Protocol): https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/ad11ef02-14c8-4dbc-b1dd-bb5c9f3203bd
- WF-21 (Vitamin D Assessment): https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/d2692dc6-1e9f-466c-8525-58c466c426bd
- WF-29 (Abandoned Checkout Recovery, fed by the Railway service): https://services.leadconnectorhq.com/hooks/GtXjla7Ld1dordsTWrVy/webhook-trigger/8087b56e-c304-488d-a7a0-c828800f39f8

**Forms:**
- Consumer Inquiry: https://api.leadconnectorhq.com/widget/form/dclY1TB3jA3eitWEQaCo
- Accreditation: https://api.leadconnectorhq.com/widget/form/DBQBL51stonmfRcUBsMe
- Testimonial: https://api.leadconnectorhq.com/widget/form/OjahkWeVDeozQkfG9dW2

**Calendars:**
- Investor Intro (Scott): https://api.leadconnectorhq.com/widget/booking/JtYjGrq6vF7aBiM3IZiG
- Investor Presentation (collective): https://api.leadconnectorhq.com/widget/booking/UpEku45jOQdYpj9qXlM5
- Consumer Discovery (round-robin): https://api.leadconnectorhq.com/widget/booking/C0hV5CFHUhWOIzs4OedC
- Commercial Discovery (round-robin): https://api.leadconnectorhq.com/widget/booking/VJ3PDGQsxhiSXhkzUwND

**Hosted PDFs** (assets.cdn.filesafe.space/GtXjla7Ld1dordsTWrVy/media/):
- Synthesis Gap: 6a3eb5fae2763b2eec13afcc.pdf
- Recovery: 6a3fd90fc408020f97c82b7f.pdf
- Winter Protocol: 6a3f1a46163e40d8627248b1.pdf

**A2P Registration URLs (save - GHL resets on every session):**
- Opt-In Form: https://go.enyrgy.com/sms-opt-in
- Privacy Policy: https://shop.enyrgy.com/policies/privacy-policy
- Terms of Service: https://shop.enyrgy.com/policies/terms-of-service

---

## DOCUMENTS CURRENT AS OF THIS SESSION

| Document | Version | Format | Notes |
|----------|---------|--------|-------|
| Enyrgy_VitaminD_Assessment_LeadMagnet.html | v1.0 | .html | LIVE at go.enyrgy.com/vitamin-d-assessment. Webhook wired, brand-aligned, humanized. |
| Enyrgy_VitaminD_Assessment_Deployment_Runbook | v1.0 | .md + .docx | Deploy plan, reflects the live build. Upload to project. |
| Enyrgy_VD_Assessment_Nurture_and_Segmentation | v1.0 | .md + .docx | WF-22 nurture copy plus the one-action segmentation. Upload to project. |
| lead-magnets.md | v2.1 | .md + .docx | Four-ring magnet strategy plus Lead Magnet 5. Upload to project. |
| Enyrgy_Brand_Style_Guide_v2 | v2.0 | .md + .docx | Governing brand authority. Age minimum 18. Skin-exam disclosure removed. Upload to project. |
| Enyrgy_Testimonial_Request_Emails | v1.0 | .md + .docx | Consumer + facility ask emails, gift-card P.S., and the full GHL build spec (form field, WF-25, WF-26). Copy through CUB + humanize-pro. LIVE. Upload to project. |
| Enyrgy_Production_Users_FINAL_for_GHL | current | .csv | The 617-customer import file, imported Session 10. Reference only. |
| Enyrgy_Paperclip_Phase2_Setup_Guide | v1.0 | .md + .docx | The Phase 2 build plan. Upload to project. |
| Enyrgy_GHL_Implementation_Guide | v3.9.4 | .md + .docx | Ground truth. Session 14: applied the Session 13 accreditation carve-out (subscription agreement + term sheet pre-acceptance) in three locations, bumped to v3.9.4, and generated the .docx (was md-only in repo). Upload to project. |
| Enyrgy_GHL_WIP-3 | Session 12 | .md + .docx | Session 12 log added (Paperclip deploy, budget cap, GHL token, no-native-connector finding). Upload to project. |
| Enyrgy_Paperclip_Agent_Instruction_Blocks | Session 14 | .md + .docx | All 16 role blocks + CFO + compliance gate + workflow map. Session 14: the narrowed blocks (Onboarding, Sales Outreach, Reactivation, Sentinel, Referral and Reviews) were DEPLOYED to the live agents (top block only; each live agent also has a standard Execution Contract not in this pack). On device at ~/Projects/enyrgy-paperclip-core. Upload to project. |
| Enyrgy_Funnel_Ownership_Map | Session 14 | .md + .docx | Per-touch GHL-vs-agent ownership (autopilot vs brain), drip_bypass + Stop-on-Response handoff, Fix #1 rationale. On device. Upload to project. |
| Enyrgy_Paperclip_Knowledge_Base | v2, Session 16 | .md + .docx | Shared agent-read KB, 15 sections, voice-passed. **Live `enyrgy-knowledge-base` Company Skill re-synced Aug 3, 2026 and confirmed at repo commit `42090226`.** That sync carried nine targeted edits: S1 users-not-customers (a home unit supports six users, so "600+ customers" overstates unit sales), S1 Brian Cameron CFO as a former securities regulator, S1 referral operated manually via a hand-built Shopify code, S1 contact@enyrgy.com as the monitored inbound address, S4 pilot-to-study plus the two new rules behind it (never call it a pilot, since the study ran months after full production launch; write "the five participants" so the article does not imply a larger cohort in which only five responded), S4 participant-level line aligned, S5 the three advisor bios with publication and tenure figures plus the guidance paragraph, S6/S7 users and "in research clinical trials", and S8 the approved one-in-four wording. **S8 was the one that mattered:** "in these trials" is only unambiguous while it sits beside the citation, and an agent lifting the phrase into an email leaves the citation behind, so the reader parses it as Enyrgy's own trials. Prior sync Aug 2 at `17c553b7`, which carried: S2 sales anchor qualified (the unqualified "no other solution delivers all three" is knockable down by a tanning bed, which does trigger all three pathways badly and with no dosing control; the calibration-and-cutoff qualifier is what nothing else clears), S3 commercial unit footprint 4ft by 4ft, and S3 manufacturing lead-time policy with no figures recorded since batch size moves with funding. Earlier syncs: Aug 2 at `2f4fb933`, Aug 1 at `95f41a40`. Six targeted edits applied (NOT a select-all paste): founder track record (S1), commercial pricing $49-$125 range + membership/credit-model guidance (S3), objection line $49-$125 (S11), PPM placeholder guardrail lifted (S12), distribution alongside white-label (S14), quick-lookup table row (S15). Earlier Session 14 additions (UVB waveband, sunlight five-outputs, payment options, participant-level pilot data, one-session-a-day) synced at `0062ce4e`. Upload to project. |
| Enyrgy_ICP_Dartboard | current | .md + .docx | Em-dashes and icons removed; brand .docx built. Upload to project. |
| Enyrgy_B2B_ICP_Dartboard | current | .md + .docx | Em-dashes and icons removed; brand .docx built. Upload to project. |
| Enyrgy_Session_Handoff | Session 14 | .md + .docx | This document. Upload to project, replace prior handoff. |

**Action for Scott:** upload the cleaned `.md` files (VD Assessment Deployment Runbook, VD Assessment Nurture and Segmentation, lead-magnets, Brand Style Guide v2, Phase 2 Setup Guide, v3.9 Implementation Guide, WIP-3, both ICP Dartboards, and this handoff) plus the lead-magnet `.html` into the project to replace the prior versions. Project files are read-only in Claude, so uploads are required for the next session to have current context.

---

## PRE-LAUNCH DRAFT-AND-HOLD TEST (2026-07-24, in progress)

Five clearly-fake test contacts created in GHL sub-account GtXjla7Ld1dordsTWrVy to verify agents draft normal outreach and that every write holds at the human-approval gate. All identities route to Scott (scott+testN@enyrgy.com) so a mistaken send only reaches Scott. Nothing was approved, declined, or sent; no policy or gate was modified.

**Safety design:** all five carry `drip_bypass` so no GHL-native drip auto-sends (the Paperclip approval gate does NOT hold GHL-native drips). The three sending-workflow trigger tags (`unit_shipped` WF-06, `unit_activated` WF-07, `status_cold` WF-08) were deliberately OMITTED because `drip_bypass` does not gate those non-drip workflows; those persona states are conveyed in the agent task prompt instead. Drafts are driven by explicit task assignment; the gated `send_message` tool holds each at the approval queue.

| Persona | Agent | Contact | Email | GHL contact id | Tags |
|---------|-------|---------|-------|----------------|------|
| a Consumer nurture | Sales Outreach | Test One | scott+test1@enyrgy.com | `TluJ7Ip0muEWPKLHm1AS` | test_contact, drip_bypass, type_consumer, status_new, source_website, agent_outreach |
| b Onboarding | Onboarding | Test Two | scott+test2@enyrgy.com | `DDNLSYtGdTkIWTYDrKAT` | test_contact, drip_bypass, type_consumer, product_consumer_unit, status_won, agent_onboarding |
| c Review/referral | Referral and Reviews | Test Three | scott+test3@enyrgy.com | `XQY4FrHctRpKx5TCji8L` | test_contact, drip_bypass, type_consumer, product_consumer_unit, sessions_10_complete, status_won, agent_csm |
| d Reactivation | Reactivation | Test Four | scott+test4@enyrgy.com | `qWitg3dEQuJLHTOpWLJV` | test_contact, drip_bypass, type_consumer, status_reactivation, agent_reactivation |
| e Investor (holds at gate) | CFO | Test Five | scott+test5@enyrgy.com | `3Sn50wLhDeNdP25oyIbX` | test_contact, drip_bypass, type_investor, status_qualified |

Task prompts (paste-ready, one per agent's Assign Task box): held in scratchpad `agent_task_prompts.md` this session.

**Status (updated):** All 5 agents ran and drafted; all 5 writes are HELD at the human-approval gate (ghlv2 `send-message`, `awaiting_approval`). Nothing sent, no queue item cleared, no policy/gate touched. Consolidated review captured in scratchpad `DRAFT_REVIEW_REPORT.md`.

**Findings:** Copy is compliance-clean and KB-accurate, but off-voice: the live agents carry the KB (facts) and brand rules but NOT the personal voice profile (`StorySelling-OS/style-guide.md`, `about-me.md`) and NOT a skills pass, so drafts break Scott's own style guide (telegraphing, list scaffolding, no signature moves, wrong sign-off). One material compliance flag: the investor PPM draft asserted sharing the PPM without noting it is a placeholder pending securities-attorney approval (KB Section 12). (Since resolved: the PPM was attorney-approved in Session 14.)

**Voice fix (Option 2, done):** All 5 funnel emails rewritten in Scott's Mode 2 voice as approved templates the agents SEND (not freehand), humanize-pro reviewed (39-42/50), compliance locked incl. the investor send-preconditions. See `Enyrgy_Agent_Email_Templates_v1.md` (this repo). Architecture note: the consumer nurture lane should run these approved templates, not agent freehand; agent-composed copy is for genuine 1:1s (investor Q&A, replies).

**Voice fix (Option 1, done):** `Enyrgy_Agent_Voice_Style_Skill.md` (this repo) wires Scott's voice (style-guide.md Mode 2) + the anti-AI rules + KB Section 14 skill-to-job map + compliance guardrails into the writing agents, for the 1:1/ad-hoc lane. Encodes the template-lane-vs-1:1-lane rule so agents send approved templates for standard funnel messages and compose only for genuine 1:1s. Includes a condensed instruction-block insert and install steps (load as a company skill and assign to writing agents, or paste the insert into each agent's instruction block; UI install, no API push from this workspace).

**Remaining:** cleanup (delete the 5 test contacts + their held requests) once Scott approves. Test contact ids and held-request ids recorded in scratchpad. Deploy Option 1 + Option 2 into GHL/Paperclip via the UI.

---

*CONFIDENTIAL - Enyrgy Inc - 5115 N 27th Ave, Bld 66, Phoenix, AZ 85017 - enyrgy.com - Sunlight. Evolved.*
