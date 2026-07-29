# Enyrgy Master TODO

**Consolidated open-items list. Reconciled against the live state as of July 28, 2026 (Session 15).**
Sourced from the Enterprise Architecture, WIP tracker, Implementation Guide v3.9, and Phase 2 Setup Guide, minus everything already shipped in Sessions 8 to 15. Priority order, top to bottom.

The build is essentially done. What remains is finishing the go-live staging, a few external verifications and WF-07 wiring, investor-readiness prep, a batch of strategic architecture decisions, and documentation updates.

---

## 1. Finish the Paperclip go-live (active)

- [ ] Stage on the remaining heartbeats, one group at a time, watching cost for a day between each. **Set the interval in the same step you enable** (they default to `300s` = every 5 minutes, which is a cost trap):
  - [x] Reactivation, `21600` (6h) — ENABLED (July 28).
  - [ ] Referral and Reviews — HELD for now (volume-gated). Instruction block is trimmed (review + testimonial live; referral paused with the deferred loyalty program). At current volume WF-07 sends the review/testimonial asks GHL-native, so the agent adds little. Enable when new-customer volume is steady; daily (`86400`) is plenty, not 6h.
  - [ ] Sales Scout, `43200` (12h) — when volume justifies it.
  - [ ] Client Success Manager, `43200` (12h) — when volume justifies it.
- [ ] Keep CEO, COO, CRO, CFO, Audit and Compliance, PRD Gatherer, and Onboarding **event-driven (timer heartbeat OFF)**. They wake on escalation/comment, not a timer.
- [ ] Keep Anthropic credit buffered and Paperclip budgets with headroom. Credit starvation multiplies cost (dying runs re-wake and replay growing threads) and causes confabulation. This is a standing operating rule, not a one-time fix.

## 2. Platform / fork fixes

- [ ] **Fix the phantom-completion bug.** A run that dies on "Credit balance is too low" was auto-flipped to `done` (ENY-24) with no execution, masking an unresolved item. Fork fix: runs that die on a credit/budget error must go to `blocked`, never `done`. HIGH — this is a correctness bug in the platform.
- [x] Approval-card context UX: cards now show issue → what approving does → what declining does (deployed).
- [x] Ask-first policy rebalanced: internal CRM writes auto-run; sends/enroll/CFO stay gated.
- [x] Tool-policy toggle bug fixed: metadata-only rule updates no longer re-validate untouched config (deployed).
- [x] QC agent instruction tightened: must cite contact IDs + observed tags, never infer status from stage (repo + live agent updated).

## 3. External verifications & WF-07 completion

- [x] **Toll-free A2P (888) verification** — VALIDATED and approved for SMS (July 28, 2026). SMS can now send from the toll-free number 888-316-1695. Follow-up: activate any SMS touches that were paused waiting on this.
- [x] **Wire the GBP review link into WF-07** — DONE. Google review link is live in the WF-07 Day-14 SMS (https://g.page/r/CfN5Rj0CdmrfEAI/review), Trustpilot offered as secondary, STOP opt-out present, copy compliance-clean.
- [ ] **Referral program (DEFERRED — decided July 28)** — NOT implementing a third-party Shopify referral app (ReferralCandy/Smile.io). The next version of Enyrgy will ship a built-in loyalty/referral program instead. WF-07's referral link stays an intentional placeholder until then. The Referral and Reviews agent's review/testimonial functions are ready now; its referral function waits for the built-in program (see section 6).
- [ ] **Trustpilot** — permanent review URL + post-purchase automation.
- [ ] **Testimonial-form link on enyrgy.com** — add to post-purchase follow-up.
- [ ] **CNAM caller-ID registration** — "Enyrgy" on outbound caller ID. Low priority.

## 4. Investor readiness

- [ ] **Complete the investor contact spreadsheet** (100+ contacts), then import.
- [ ] **Investor Presentation calendar** — verify conflict detection on the collective (Scott + David + Brian) call.
- [ ] **Content assets** — voicemail recordings and the commercial ROI PDF (PPM itself is attorney-approved).
- [ ] **Q2 2026 investor update** — drafted (standalone `Enyrgy_Investor_Update_Q2_2026.docx`). Needs Brian + securities-attorney sign-off before sending; send only to existing/already-introduced investors. Scott chose to omit cash-position and amount-committed lines.

## 5. Strategic architecture decisions (mostly ratify, not build)

- [ ] **Shopify to GHL purchase sync** — the EA flags this as the top gap, but it predates the Session 11 native integration + WF-27/28/29, which largely built it. Reconcile the EA and ratify rather than rebuild.
- [ ] **System-of-record ownership map** — ratify the documented SoR (decision/doc task).
- [ ] **Device App to GHL usage-data flow** — deferred "Phase 2-plus"; decide whether/how usage data flows, with privacy treatment.
- [ ] **OEM / Lumanova data boundary** — formalize an auditable path as the partner program grows.
- [ ] **Metric governance owner** — figures reconciled; assign a single owner.
- [ ] **Facility address exception** — Shopify Privacy Policy still shows the old Scottsdale address / wrong subdomain. Quick fix.
- [ ] **Status-lifecycle representation** (minor) — the account tracks lifecycle two ways: `status_` tags on router/drip contacts, and opportunity stage + `magnet_lead`/`nurture_longterm` on magnet leads. Candidate tidy: make the pipeline stage the single source of truth. NOTE: the QC "systemic lifecycle" escalation (ENY-20) that surfaced this was verified a FALSE POSITIVE against the live account; this remains only a low-priority design tidy, not a live bug.

## 6. Future / optional

- [ ] **Built-in loyalty/referral program** — planned for the next version of Enyrgy, replacing the need for a third-party Shopify referral app. This will supply the referral link/mechanic that WF-07 and the Referral and Reviews agent are waiting on ($150 off referee / $100 store credit referrer are the intended terms).
- [ ] **Reporting dashboards** (GHL KPI views) and the **Reporting Agent** (Phase-2 addition).
- [ ] **The other five Phase-2 agents** — Proposal Writer, OEM Pipeline, Podcast Attribution, Clinical Concierge, Billing. Add only after the core is stable.
- [ ] **Paid acquisition** (Meta/Google) — after domain warmup finishes.
- [ ] **Domain warmup ramp** — mg.enyrgy.com still Stage 1; do NOT bulk-send the 600+ list. Send the first testimonial batch warmup-safe; run weekly gift-card fulfillment from the `gift_card_pending` queue.
- [ ] **Form embeds** — Commercial Inquiry + Partner Application forms onto go.enyrgy.com (developer).
- [ ] **Upgrade the abandoned-checkout Railway service off trial** (may already be on Hobby; confirm).

## 7. Documentation hygiene

- [ ] **Refresh the EA to v1.1** — dated June 29, stale on Shopify, GBP, facility, and the whole Paperclip layer.
- [ ] **IG loose ends** — WF-23/WF-24 numbering gap (confirm not unbuilt), Winter/Tired-Test URLs missing from the Key URLs table, blank team contact fields (Dennis Lan, Dario Pompeii, Millie Carrillo, Thea Cartier).
- [ ] **WIP** — correct the "24-agent" count to "16-agent core (22 with additions)."

## 8. Standing operating discipline (adopted Session 15)

- [ ] **Verify agent audits/verifications against the live GHL account before acting.** Agents confabulate under credit starvation — they produced specific, plausible, false claims (invented tag states, a workflow last-edit date misread as a last-run date, a "confirmed" systemic issue that did not exist). Treat agent escalations as leads to verify, never as facts.
- [ ] **Keep credit buffered and watch the Costs page.** Starvation is more expensive than headroom, not cheaper.
