# ENYRGY GHL - Session Handoff
**Load this at the start of the next session. It is the orientation layer. The WIP tracker and Implementation Guide v3.9 are the source of truth.**

Date of this handoff: July 27, 2026 (end of Session 15)

---

## HOW TO USE THIS
Paste or attach this file at the start of a new chat along with `Enyrgy_GHL_WIP-3.md` and `Enyrgy_GHL_Implementation_Guide_v3_9.md`. Review Standing Rules and Key Constants first. Then read What Was Done This Session and pick up from Remaining Tasks.

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
| Red light co-use | 90% of customers |
| Active OEM partner | Lumanova / Luma D Light (Black Unit exclusivity) |
| Order URL | https://shop.enyrgy.com/products/uvb-light-therapy |
| Phone | +1 888-316-1695 (Toll-Free, LC Phone) |

**Team:** Scott Hansbury (Co-founder & CEO), David Letourneau (President & Co-Founder), Brian Cameron (CFO).

---

## WHAT WAS DONE (Session 15, July 27-28, 2026)

The session took Paperclip from "built" toward "running": the live KB skill was repaired and re-synced, the first heartbeats were brought online and tuned, the two things that made the running system unusable day-to-day (an approval-card flood and cards with no context) were both fixed, a Q2 investor update was drafted, and a QC-raised "systemic" data issue was run to ground and proven a false alarm. That last item surfaced the most important operational lesson of the session: the agent org confabulates when it is credit-starved.

**Approval-card flood stopped (Ask-first policy rebalanced).** The "Ask first" gate was firing a review card on ordinary internal CRM housekeeping (tags, tasks, contact updates, stage moves), so Scott was drowning in low-value approvals and letting them auto-decline. Rebalanced the Rules (Apps > Advanced setup > Rules) so internal-organization writes auto-run while prospect-facing and money-adjacent actions stay gated. Added one rule — **"When any agent uses 13 specific actions -> Allow"** (the read/search actions plus Add/Remove Contact Tags, Create Task, Update Contact, Move Opportunity Stage) — and ordered the rule list so the first match resolves correctly: **row 1 = CFO -> Ask first** (the investor/money agent stays fully gated on every write), **row 2 = the 13-action Allow**, then the per-tool Ask-first rules below. Still gated for everyone: **Send Message, Enroll In Workflow, Remove From Workflow** (all change what a prospect receives). The five per-tool Ask-first rules the Allow rule now supersedes (Add Contact Tags, Create Task, Move Opportunity Stage, Remove Contact Tags, Update Contact) are dead-but-harmless; can be toggled off to declutter. Verified live with Test-a-rule: SDR+Add Contact Tags = Allow, any+Send Message = Ask first, CFO+Add Contact Tags = Ask first. Design note: tagging is auto-allowed even though a tag can trigger a GHL drip, because that drip copy is the human-approved static sequence; the real send risk is the agent composing a fresh 1:1 message, which is `Send Message` and stays gated.

**Approval cards now explain themselves (code, deployed).** The review-queue card ("Waiting for your OK") showed only a generic "we're checking with you first" line plus raw field values, with no indication of what Approve vs Decline actually does — so the cards were unactionable. Restructured the humanized preview in `server/src/services/tool-gateway.ts` (`buildHumanizedActionPreview`) into three parts: what's happening, the specifics, and an explicit **If you approve / If you decline** outcome pair (destructive actions warn the change may be irreversible). Server-side change, so it applies to every pending and future card automatically. Committed `04855fad`, pushed to master, deployed on Railway. This is a fork divergence from upstream Paperclip UI copy.

**Live KB skill repaired and re-synced.** The `enyrgy-knowledge-base` Company Skill had accumulated duplicated/malformed frontmatter and a doubled sentence from prior "select-all paste" syncs; the KB Manager auto-repaired it but that reverted the Session-14 edits. Provided the full clean KB body for a careful single-paste (keep frontmatter, replace body only), which Scott confirmed fixed. **Sync lesson:** never select-all-paste the KB into Skill Studio; replace the body only and verify no duplicate footer.

**Duplicate voice skill removed.** Two `enyrgy-agent-voice-style` skills existed — one attached to 8 agents (the real one) and a bundled 0-agent duplicate created from the repo `skills/enyrgy-agent-voice-style/SKILL.md`. Removed the bundled copy (`git rm -r skills/enyrgy-agent-voice-style/`, committed + pushed); kept the root reference doc `Enyrgy_Agent_Voice_Style_Skill.md`.

**PPM placeholder guardrail lifted (attorney-approved).** The PPM is now attorney-approved, so the "placeholder / do not send" guardrail was removed across the KB (Section 12), the agent instruction blocks, and the guides. PPM may be sent after the intro meeting; accreditation still gates only wire instructions and accepting investment (unchanged attorney rule).

**Anthropic billing fixed -> heartbeats unblocked.** Sentinel and other heartbeats were failing with `acpx_session_init_failed` / "Credit balance is too low." Root cause was two separate caps at console.anthropic.com: the prepaid **credit balance** AND the monthly **spend limit** — topping up credits alone does not override the monthly cap. Scott added credits (settings/billing) and raised the monthly limit (settings/limits); Sentinel then ran successfully. Staged go-live is underway (bring heartbeat groups online one at a time; CEO/COO/CRO heartbeats remain OFF — their earlier spend was a one-time escalation/recovery storm during the KB/credit incident, not heartbeat cost).

**Budget model clarified (no company-wide cap exists).** Paperclip has per-agent and per-project budgets (Costs > Budgets) but **no single org-wide budget field**; the effective ceiling is the sum of per-agent caps (~$59/mo). Heartbeats replay large context on every wake so even no-op wakes cost; GHL drip emails are static (~$0 Anthropic); variable cost tracks agent decisions, not message volume.

**Tool-policy toggle bug fixed (deployed).** Toggling a `require_approval` Rule on/off failed with "Tool policy type require_approval does not support config" because `updatePolicy` re-validated the rule's stored config on every update, and some seeded rules carry a legacy config blob. Fix: validate only what the update actually changes (type always, conditions only when provided, config only when config/type changes). Creates and duplicates stay strict. Commit `0ffb2dd4`.

**Heartbeat intervals tuned and the go-live staging set.** Found the live heartbeats were misconfigured (Dispatcher polling every 30 min, QC weekly, revenue agents off). Corrected the ON set: Dispatcher `28800` (8h, was the 30-min anomaly and largely redundant with WF-01 auto-routing), Quality Control `86400` (daily), Sales Outreach `3600` (1h), SDR `7200` (2h), Sentinel `86400` (24h), KB Manager `2592000` (30d, effectively off). Only ~8 agents should ever run on a timer heartbeat (the proactive monitors + the two revenue agents); the executives (CEO/COO/CRO/CFO), Audit and Compliance, PRD Gatherer, and Onboarding stay **event-driven, timer OFF**. IMPORTANT trap: every OFF agent shows a `300s` (5-minute) default, so whenever you enable one you MUST set its interval in the same step. Remaining rollout, gated on watching cost between each: Reactivation `21600`, Referral and Reviews `21600` (only after WF-07 review link + referral app), Sales Scout `43200`, CSM `43200`.

**Q2 2026 investor update drafted (standalone .docx, not committed).** Built from the KB and session logs only, no invented figures. Includes real Q2 financials (revenue $34,866.86, gross profit $30,834.68, opex $55,822.26, net loss $24,987.58, of which $33,464.79 was non-recurring: $26,897.97 fundraise costs + $6,566.82 annual insurance renewal, so underlying operations ran ~$8,477 positive), the commercial membership reframe (operators use Enyrgy as a member-acquisition and tier-upgrade draw, moving off per-modality pricing), a Team section (Brian Cameron, Millie Carrillo, Shanna Schuckman, Thea Cartier), the operating-platform section (Enterprise Architecture v1.0 + 29 workflows), and YourTango named. Compliance-clean (no em-dashes, no prohibited words, N=5 caveat, offering terms point to the PPM). Needs Brian + attorney sign-off before sending; send only to existing/already-introduced investors.

**QC "systemic lifecycle" escalation (ENY-20) run to ground: FALSE POSITIVE, and the real finding is agent confabulation under credit starvation.** QC's weekly audit escalated a "systemic, most active contacts affected" lifecycle bug (status tags stacking, contacts stuck at New Lead, WF-04 not running). COO then "verified it live" and confirmed it. Both were wrong. Every specific claim was checked by hand against the live sub-account and none held: the New Lead stage had one legitimate same-day lead (Barry Fingerhut via Tired Test); the named magnet leads (Sonya, Engle, Crystal, Celestina, Lynette) carry zero `status_` tags; Preston carries a single clean `status_solicitation`; "Test Calendar" and spam contact Saloni were already deleted; and WF-04 Stale Lead Sentinel has run **every day** (Jul 23 to 28, last run Jul 28 08:02, all Finished) — COO had misread the workflow's last-*edit* date (2026-06-27) as its last-*run* date. Root cause: the agent org was **credit-starved and budget-hard-stopped**, and in that state it did not fail quietly, it produced confident, specific, fabricated claims. A related platform bug: the delegated fix (ENY-24) was auto-flipped to `done` during "credit-balance recovery" with no execution, masking the (non-existent) issue. **Standing lessons adopted:** (1) verify every agent audit/verification against the live GHL account before acting; agent escalations are leads, not facts; (2) keep Anthropic credit buffered and budgets with headroom, because starvation multiplies cost (dying runs re-wake and replay a growing thread) and triggers confabulation; (3) the QC instruction was tightened to require cited contact IDs + observed tags and to forbid inferring status from stage. Cleanup: ENY-20, ENY-30, and the phantom replacement fix ENY-35 were cancelled; ENY-29 and ENY-31 (Saloni reconciliation) were already Done; Saloni was an intentional human spam deletion, not an unapproved action. **Open platform fix:** runs that die on a credit/budget error must go to `blocked`, never `done` (the phantom-completion bug).

**Consolidated open-items list created.** `Enyrgy_Master_TODO.md` reconciles every open item across the EA, WIP, IG, and Phase 2 guide against the live state, in priority order. Use it as the single punch list going forward.

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
| Enyrgy_Paperclip_Knowledge_Base | v2, Session 14 | .md + .docx | Shared agent-read KB, 15 sections, voice-passed. Session 14 additions: founder track record (S1), UVB waveband + sunlight five-outputs/rule-of-thumb (S2), payment options (S3), participant-level pilot data + one-session-a-day (S4). Repo committed (0062ce4e) and re-synced to the live enyrgy-knowledge-base Company Skill. Upload to project. |
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
