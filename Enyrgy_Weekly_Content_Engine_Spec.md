# Weekly Content Engine ("Maria") - Feature Spec and Build Blueprint

**For:** Enyrgy engineering / Paperclip board
**From:** [source company] outbound marketing build
**Purpose:** Describe the weekly content agent we run (internally nicknamed "Maria") in enough detail that Enyrgy can build the same feature on its existing Paperclip / Railway / GHL stack.
**Status:** Enyrgy does not have this feature yet. This document is the handoff, **verified against the live Enyrgy corpus on August 4, 2026.** See Section 0.5 for what checked out and what did not.

---

## 0. How to read this document

Two kinds of content are mixed here, and they are labelled so nobody guesses:

- **[BUILT]** - what Maria actually does in the source implementation. Treat these as the requirements.
- **[RECOMMENDED]** - how to implement each requirement on the Paperclip / Railway / GHL primitives Enyrgy already runs. These are our suggested mechanics, not a hard contract. Enyrgy can swap the mechanics as long as the [BUILT] behaviour is preserved.

Anything marked **[CONFIRM]** is a decision Enyrgy has to make locally (channel, cadence detail, approval owner) that our setup will not answer for you.

No em-dashes anywhere in this doc, per the standing house rule, so the copy stays paste-safe into GHL.

---

## 0.5 Verification pass, Enyrgy, August 4 2026

This document was written outside Enyrgy and describes Enyrgy from the outside. Every factual claim it makes about Enyrgy was checked against the repo before any of it was built on. **Three did not survive.** They are corrected in place below; this section records what changed so the corrections are not silently reverted by someone reading the original.

### Confirmed accurate

- **The Social Media Manager slot exists and is empty.** Thea Cartier appears in the Implementation Guide team table (Section 7) with blank contact fields, in the Enterprise Architecture personnel table, and in the Q2 2026 investor update as a team addition. **She is a real person, not an agent slot.** An agent here supports her or duplicates her; that is a staffing decision, not a technical one. See Section 10.
- **Brand constants.** Sunrise Orange **#E64C38** and Montserrat are correct, and are Standing Rule 1 in the session handoff.
- **The stack mapping.** Paperclip, Railway and the GHL sub-account are as described.
- **The no-em-dash rule** is real and absolute (Standing Rule 1a).

### CONFIRMED, and a real gap behind it: the January 2026 FDA Guidelines for Wellness Products

**The reference is real and binding.** KB **Section 11** already carries it: "Review all client-facing content against the January 2026 FDA Guidelines for Wellness Products before use." The spec was right to cite it.

**An earlier pass of this verification wrongly reported that no such document existed.** It did not: the grep that would have found it was truncated at the display width, the hit was read as matching on the phrase "FDA-approved" earlier in the same sentence, and the reference was declared a foreign artifact. Recorded because the wrong conclusion was briefly written into this spec and into an agent instruction block, and because the lesson generalises: **a truncated search result is not a search result.**

**The real gap, which stands.** The KB *cites* the guidelines but does not *contain* them. There is no summary, no clause list, no link, and no copy in the repo. So an agent told to "review against the January 2026 FDA Guidelines" has a binding instruction it cannot actually execute. It will either treat the check as passed or reconstruct what it imagines the guidance says, and either way you get a confident compliance claim resting on nothing, on the highest-reach content Enyrgy produces.

**Required before this agent goes live: get the substance into the KB.** A link alone is not enough for an agent that cannot browse. What is needed is the operative content, the specific do-not-say list and the structural claim rules, written into KB Section 11 the way the prohibited-words list already is. **Scott to supply the document or an authoritative summary.**

**The rest of the gate, already in place:** KB **Section 11** prohibited words, KB **Section 8** claim precision, Implementation Guide **Section 14** content rules, and a second pass through the existing **Audit and Compliance** agent.

### RESOLVED BY SCOTT: nothing publishes automatically, so no channel connection is needed

**Scott, August 4: "No content is being posted to social channels automatically. It is for my review and posting outside this platform."**

That removes the whole publishing-integration question. **The GHL Social Planner is not in scope and does not need connecting.** Social output is a review package Scott takes elsewhere and posts by hand.

It also settles the approval model by construction: this is option 1 from Section 4, human-publish, with no gated-agent-publish path to build later for social. The agent physically cannot post.

Worth keeping straight anyway, since the source spec had it wrong: `source_instagram`, `source_facebook` and `source_linkedin` are **lead-source tags** recording where a contact came from, not a list of connected accounts. The only documented active account is **Instagram @enyrgy.light** (Brand Style Guide).

**[CONFIRM] still open:** whether **blog** and **email** stage as GHL drafts, or also come out as review packages. Social is settled; these two are not, and GHL is the natural home for both.

### ADS ARE IN SCOPE, deliberately

**Scott, August 4: the whole point of the raise, stated as such to investors, is to start advertising.** So ads are a v1 content type, not a deferred one.

What still has to happen, and it is a copy task rather than an objection: **"zero paid advertising to date" retires the day the first ad runs.** It is an approved KB talking point (Sections 1 and 6), it appears as a growth proof point in live drip copy, and the Q2 2026 investor update describes Thea Cartier's role as "extending the zero-paid-ads engine."

**Tracked as a sweep, not a blocker.** The claim was true and is a genuine credibility asset while it lasts; it simply cannot outlive the first ad. Retiring it late is the failure mode, because it turns a true differentiator into a false one in copy that is already in the field. Recorded in `Enyrgy_Master_TODO.md`.

Ads still never auto-launch and never auto-spend. Human sign-off before any money moves, unchanged.

---

## 1. What Maria is, in one paragraph

Maria is a single Paperclip agent whose whole job is to produce Enyrgy's outbound marketing content on a fixed weekly cadence. **[BUILT]** Every Monday she generates a full content set for the week:

1. one **blog post**,
2. a set of **email posts** (newsletter / broadcast copy),
3. a set of **ads** (paid social / search ad copy), and
4. a set of **social posts** (organic social).

She does not send anything blind. She stages the whole set, and a human works it through a **dashboard management function**: review, edit, approve, schedule, publish. She is the writer and the scheduler; the dashboard is the control surface; a human keeps the approval gate.

She sits on exactly the same three layers Enyrgy already has:

| Layer | Enyrgy already has | Maria uses it for |
|-------|--------------------|-------------------|
| **Paperclip** (control plane) | Agents, routines, execution issues, approvals, board dashboard | The agent herself, the Monday trigger, the review/approval workflow |
| **Railway** (runtime/host) | Agent runtime container, scheduler | Runs Maria's heartbeat and the weekly job |
| **GHL** (marketing system of record) | Sub-account `GtXjla7Ld1dordsTWrVy`, Blogs, Social Planner, Email builder, contacts/tags | Where the finished content is published and scheduled |

So this is not a new platform. It is one new agent, one recurring routine, one review view, and a set of GHL publishing calls.

---

## 2. The weekly run (the heart of the feature)

### 2.1 Trigger

**[BUILT]** Fires once a week, Monday morning.

**[RECOMMENDED]** Implement as a Paperclip **routine** with a `schedule` (cron) trigger. This is the same routines mechanism documented in `skills/paperclip/references/routines.md`.

```
POST /api/companies/{companyId}/routines
{
  "title": "Weekly Content Engine - Maria",
  "description": "Generate the week's blog, email, ad, and social content set and stage it for review.",
  "assigneeAgentId": "{maria-agent-id}",
  "projectId": "{marketing-project-id}",
  "priority": "high",
  "concurrencyPolicy": "skip_if_active",
  "catchUpPolicy": "skip_missed"
}
```

```
POST /api/routines/{routineId}/triggers
{
  "kind": "schedule",
  "cronExpression": "0 6 * * 1",
  "timezone": "America/Phoenix"
}
```

Notes on the choices:

- `0 6 * * 1` is Monday 06:00. **[CONFIRM]** pick the hour that lands the staged set on the reviewer's desk before they start Monday. Enyrgy runs Phoenix time; `America/Phoenix` avoids daylight-saving drift.
- `concurrencyPolicy: skip_if_active` means if last week's run is somehow still open, the new one is skipped rather than doubling up. Content is not something you want enqueued twice.
- `catchUpPolicy: skip_missed` means a server outage over a weekend does not dump four missed weeks of content into the queue on restart. A missed Monday is just skipped; the human can fire a manual run.
- Add a second trigger of `kind: "api"` (manual) so the board can fire an off-cycle run for a launch week without waiting for Monday.

Each fire creates an **execution issue** assigned to Maria. She picks it up in her normal heartbeat, exactly like every other Paperclip agent. Use `parentIssueId` on the routine so every weekly run issue nests under one standing "Weekly Content" parent, which keeps the board history clean.

### 2.2 What Maria does inside a run

**[BUILT]** produces the four content types for the week. **[RECOMMENDED]** the run issue instructs her to work this sequence:

1. **Read the brief.** Pull the theme/angle for the week. Source of truth in order: (a) any human note left on the run issue or the content calendar, (b) the shared knowledge base (approved talking points, current promo, seasonal angle), (c) last week's performance if available. She never invents a claim, a number, a price, or a date. Facts come only from the KB, same rule every Enyrgy agent already follows.
2. **Draft the blog post** (see 3.1).
3. **Derive the email posts** from the blog angle (see 3.2).
4. **Derive the social posts** from the blog angle (see 3.3).
5. **Draft the ad copy** for the week's offer/angle (see 3.4).
6. **Self-check against compliance and brand** (see Section 5) before anything is staged.
7. **Stage everything into the dashboard** as draft items, grouped under this week's run, each item carrying its target channel, proposed publish time, and a link back to the run issue.
8. **Post a summary comment** on the run issue: what she produced, the through-line, anything she needs a human to decide, and any fact she could not verify (flagged, not guessed).

She stages. She does not publish. Publishing is gated (Section 4).

---

## 3. The four content types

Each type below gives: what she writes, where it lands in GHL, and the per-type rules.

### 3.1 Blog post

- **[BUILT]** One long-form post per week, the anchor piece the rest of the set is derived from.
- **[RECOMMENDED]** Output: title, slug, meta description, body (GHL blog HTML/rich text), suggested category/tags, hero-image prompt or brief for a human/designer.
- **Destination:** GHL **Blogs**. Stage as a draft blog post in the sub-account; the reviewer publishes or schedules it.
- **Rules:** ties to an approved talking point or the current seasonal angle from the KB. Wellness-compliant language only (Section 5). One clear call to action pointing at the correct funnel entry (consumer guide, discovery call, etc.), pulled from the links registry, never a hand-typed URL.

### 3.2 Email posts

- **[BUILT]** A set of email copy for the week (newsletter / broadcast).
- **[RECOMMENDED]** Output per email: subject line (plus one A/B alternate), preview/preheader text, body, single primary CTA. Record merge fields exactly (`{{contact.first_name}}`), not paraphrased, matching the convention in `campaigns/README.md`.
- **Destination:** GHL **Email** (broadcast/campaign builder), staged as a draft. **[CONFIRM]** whether these go out as a true broadcast to a segment, or are queued as the week's touches inside an existing nurture workflow. Keep them clear of the automated drip touches that GHL already sends (WF-11 through WF-20) so you never double-send.
- **Rules:** the standard signature already includes "Carpe Diem," so body copy must not repeat it. No em-dashes. Compliance-scanned before staging.

### 3.3 Social posts

- **[BUILT]** A set of organic social posts for the week.
- **[RECOMMENDED]** Output per post: platform, caption/body, hashtags, image or video brief, proposed date/time. Derive several posts from the one blog angle so the week reads as one campaign, not four unrelated fragments.
- **Destination:** GHL **Social Planner**. Stage each as a draft scheduled post per connected channel. **[CONFIRM]** which channels are connected. **Do not assume any are.** The only documented active account is **Instagram @enyrgy.light** (Brand Style Guide). `source_instagram` and friends are lead-source tags, not publishing channels, see Section 0.5.
- **Rules:** brand voice is peer-to-peer, Sunrise Orange, Montserrat feel, no em-dashes. Narrative / story-style posts should lean on the StorySelling approach (origin stories, testimonials, community proof) rather than hard selling.

### 3.4 Ads

- **[BUILT]** A set of ad copy for the week.
- **[RECOMMENDED]** Output per ad: platform (Meta / Google), objective, primary text variants, headline variants, description, CTA button, and the destination landing page from the links registry. GHL does not run every ad platform natively, so treat ad output as review-ready copy packages that a human (or the connected ad tool) launches. Do not auto-spend.
- **Rules:** paid claims carry the highest compliance risk. Every ad variant runs through the prohibited-words and FDA-wellness check (Section 5) and is flagged for explicit human sign-off before any spend. Ads never auto-publish, full stop.

---

## 4. The dashboard / management function

**[BUILT]** A dashboard that lets a human manage the weekly set: see what Maria produced, edit it, approve it, schedule it, and track what shipped.

**[RECOMMENDED]** You do not need to build a new app. Use the Paperclip **board dashboard** as the control surface, backed by the run issue and one item per content piece. The management view needs to show, per week:

| Column | Meaning |
|--------|---------|
| Week / run | Which Monday run this set belongs to |
| Item | Blog / email / ad / social piece |
| Channel | GHL Blogs, Email, Social Planner, or Ads |
| Status | `draft` -> `in_review` -> `approved` -> `scheduled` -> `published` (or `rejected`) |
| Proposed time | When Maria suggests it goes live |
| Owner | Which human approves this item |
| Link | Deep link to the GHL draft and back to the run issue |

The management actions a human takes:

- **Review and edit** in place, or edit directly in the GHL draft.
- **Approve / reject** each item. Rejecting with a note sends it back to Maria to redraft on the same run issue.
- **Schedule / publish**: on approval, the item is scheduled or published in GHL.

**The approval gate is mandatory and matches Enyrgy's existing governance.** Maria never publishes unreviewed. **[RECOMMENDED]** two ways to enforce it, pick one:

1. **Human-publish (simplest, safest):** Maria only ever stages GHL drafts. A human clicks publish/schedule in GHL. Nothing agent-driven can go live.
2. **Gated agent-publish:** Maria may publish, but only after the item's status flips to `approved` by a board operator, implemented as a Paperclip **approval** on the run issue. Ads stay human-publish regardless.

Start with option 1. It is the same "stage, human ships" posture Enyrgy uses elsewhere and it removes an entire class of go-live risk during domain warmup.

---

## 5. Compliance and brand guardrails (reuse, do not rebuild)

Maria plugs into the guardrails Enyrgy already has. Nothing new to invent here.

- **Prohibited-words, claim-precision and FDA-wellness scan.** Every client-facing string is checked against **KB Section 11** (prohibited words **and** the January 2026 FDA Guidelines for Wellness Products), **KB Section 8** (claim precision) and **Implementation Guide Section 14** (content rules) before it is staged. **BLOCKING: the FDA guidelines are cited in the KB but their substance is not in it.** Until that content is loaded, no agent can perform this check, and it must not claim to have performed it. See Section 0.5. This is the same gate the Audit and Compliance agent enforces on outbound messages. **[RECOMMENDED]** have Maria self-scan, and for ads and blog (the highest-reach items) route through the existing Audit and Compliance agent as a second pass.
- **Approved claims only.** Use only approved talking points and approved product terms (for example BioCalibrated Sunshine, Triple-Pathway Advantage). Never state a number, price, study result, or date not in the KB.
- **Brand voice.** Peer-to-peer, Sunrise Orange, Montserrat, no em-dashes.
- **Links.** Every URL comes from the links registry, never hand-typed, so a funnel URL change does not silently rot the content (same rule as `campaigns/_LINKS.md`).
- **Investor firewall.** Marketing content is consumer/commercial/partner facing. Maria never produces investor financial content and never touches the accreditation-gated material. That stays out of scope for this agent entirely.

---

## 6. The agent itself (hiring Maria)

**[RECOMMENDED]** Hire via the standard `paperclip-create-agent` flow. Key config:

- **Role / title:** Content Marketing Agent. You already have a "Social Media Manager" slot (Thea Cartier) in the personnel table with no instruction block yet; this feature can fill that slot or stand beside it. **[CONFIRM]** name and reporting line (CRO is the natural parent, since this is top-of-funnel demand generation).
- **Adapter:** same local managed-bundle adapter Enyrgy uses for its operational agents.
- **Instruction bundle (`AGENTS.md`):** role charter = "produce the weekly content set, stage for review, never publish unreviewed"; the fact-source rule; the compliance gate; the four output contracts from Section 3; the brand voice block.
- **Skills:** the GHL tool (installed from the agent's Tools tab, since she calls GHL), plus the StorySelling skill for narrative social/blog. Add the campaigns capture habit so staged copy is also written back to version control.
- **Tools:** GHL tool required. No investor-material access.
- **Heartbeat:** this is exactly the "genuinely needs scheduled recurring work" case the create-agent guidance calls out, so `runtimeConfig.heartbeat.enabled=true` is justified, or leave heartbeat off and let the routine's execution issue wake her on demand. Either works; the routine is what guarantees the Monday cadence, not the heartbeat.
- **Governance:** her hire and her publish rights go through the normal approval flow. Capabilities that expand reach (GHL publish) are justified in the hire comment.

---

## 7. Data and knowledge inputs

Maria reads, never invents:

1. **Shared knowledge base** - approved talking points, product terms, pricing, study data, current promo, seasonal angle, prohibited words.
2. **Content calendar / weekly brief** - the theme for the week. **[CONFIRM]** where this lives. Simplest: a note on the run issue or a KB "this week's angle" entry a human sets on Friday.
3. **Links registry** - all funnel URLs.
4. **Performance signal (optional, phase 2)** - last week's opens/clicks/engagement to inform this week's angle.

---

## 8. Reporting

**[RECOMMENDED]** Maria closes each weekly run issue with a short report: items produced per channel, the week's through-line, what was approved vs rejected, and any fact she flagged as unverifiable. Over time this run history is the content audit trail on the board. A phase-2 add is a monthly rollup: what shipped, and (pulled from GHL) how it performed.

---

## 9. Build checklist for Enyrgy

Ordered, smallest-risk-first:

1. **Create the marketing project** in Paperclip (if there is not already one) to hold the routine and run issues.
2. **Hire Maria** (Section 6) with GHL tool + StorySelling skill, publish rights withheld initially.
3. **Confirm GHL surfaces are connected**: Blogs enabled, Social Planner channels connected, Email sender/domain live (it is), ad accounts linked or ad output treated as copy-only.
4. **Write her `AGENTS.md`** with the four output contracts, the fact-source rule, the compliance gate, and the brand block.
5. **Create the routine** with the Monday `schedule` trigger and a manual `api` trigger (Section 2.1).
6. **Wire the compliance second pass** for blog and ads through the existing Audit and Compliance agent.
7. **Set up the dashboard view** on the board (Section 4) and pick the approval model (start with human-publish).
8. **Dry run:** fire the manual trigger, let Maria stage a full set, walk the review flow end to end, publish one item by hand.
9. **Go live** on the Monday schedule once one full cycle has been reviewed cleanly.
10. **Phase 2:** feed performance back in, add the monthly rollup, consider gated agent-publish for the low-risk channels only.

---

## 10. Open decisions for Enyrgy [CONFIRM]

**BLOCKING, must be closed before hire:**

- **Load the January 2026 FDA Guidelines for Wellness Products into KB Section 11.** Cited but not contained, so the check cannot be executed. Scott to supply the document or an authoritative summary. See Section 0.5.

**Settled by Scott, August 4:**

- ~~Which social channels are connected~~ **None needed.** Nothing auto-posts; social output is a review package Scott posts by hand.
- ~~Ads in or out~~ **In.** The raise is explicitly for advertising.
- ~~Approval model~~ **Human-publish**, by construction for social.

**Still open:**

- **Thea Cartier owns organic social and is a real hire named to investors.** Does this agent draft for her to edit and ship, cover what she does not, or is the review gate solely Scott? His "for my review and posting" answers the gate but not her remit.
- Whether **blog and email** stage as GHL drafts or come out as review packages like social.
- Whether GHL Blogs is enabled on the sub-account, if blog is staying in GHL.
- Exact Monday hour.
- Email posts: broadcast to a segment vs. queued touches, and which segment.
- Which social channels are connected in the Social Planner.
- Ad platforms in scope and who owns spend sign-off.
- Where the weekly brief/theme is authored and by whom.
- Reporting line for Maria (recommend under CRO).
- Approval model: human-publish (recommended start) vs. gated agent-publish.

---

## 11. What this doc does not cover

This is the feature shape and the stack mapping. The starter `AGENTS.md` and the four output templates are in Appendix A and Appendix B below. They are a starting point tuned to our brand assumptions; adapt the bracketed fields to Enyrgy before use. What this doc does not ship is our internal dashboard styling and our per-post creative, which are brand-specific and would fight Enyrgy's own.

---

## Appendix A. Starter `AGENTS.md` for Maria

Drop this into `instructionsBundle.files["AGENTS.md"]` at hire time and replace every `[...]` field. It is written to Enyrgy's own conventions (fact-source rule, compliance gate, brand voice, no em-dashes). It deliberately withholds publish rights: Maria stages, humans ship.

```markdown
# Maria - Weekly Content Marketing Agent

You are Maria, the Content Marketing Agent for Enyrgy Inc, operating in GHL
sub-account GtXjla7Ld1dordsTWrVy. You report to the CRO. Your entire job is to
produce Enyrgy's outbound marketing content on a weekly cadence and stage it for
human review. You are the writer and the scheduler. You are not the publisher.

## Charter

Each time you are woken by a "Weekly Content" run issue, produce the full content
set for the week and stage it as drafts for review:
1. One blog post (the anchor piece).
2. A set of email posts (newsletter / broadcast copy).
3. A set of social posts (organic), derived from the blog angle.
4. A set of ad copy packages (paid social / search), review-ready, never launched.

Work the run in this order: read the brief, draft the blog, derive the emails,
derive the social, draft the ads, self-check against compliance and brand, stage
everything into the dashboard as drafts, then post a summary comment on the run
issue.

## Fact discipline (absolute)

Read facts only from the shared knowledge base. Never invent a number, claim,
price, study result, date, or policy. If a fact you need is not in the KB, flag
it in your run summary and leave a placeholder. Do not guess.

Use only approved talking points and approved product terms (for example
BioCalibrated Sunshine, Triple-Pathway Advantage). Every URL comes from the links
registry; never hand-type a funnel URL.

## Compliance gate (must pass before you stage anything)

Scan every client-facing string against KB Section 11 (prohibited words), KB
Section 8 (claim precision) and Implementation Guide Section 14. Never
use: treat, cure, diagnose, disease, prescription, FDA-approved, medical
treatment, heal, fix, medication, illness, clinical diagnosis, therapeutic
treatment. For blog and ad output, route a second compliance pass through the
Audit and Compliance agent before staging.

You never produce investor financial content and never touch accreditation-gated
material. That is out of your scope entirely.

## Brand voice

Peer-to-peer, confident, warm. Sunrise Orange, Montserrat feel. No em-dashes, ever
(use commas, colons, or parentheses). The standard email signature already
contains "Carpe Diem," so do not repeat it in body copy. For narrative social and
blog, use the StorySelling approach: origin stories, testimonials, community
proof, not hard selling.

## Output contracts

Follow the per-type templates in Appendix B of the Weekly Content Engine spec.
Every staged item must carry: target channel, proposed publish time, and a link
back to the run issue.

## Publishing (hard boundary)

Never publish or schedule anything live. Stage GHL drafts only. A human reviews,
approves, and ships from the dashboard. Ads always require explicit human sign-off
before any spend. If asked to publish directly, refuse and escalate to the CRO.

## Close-out

End every run with a comment on the run issue: items produced per channel, the
week's through-line, anything a human must decide, and any fact you could not
verify (flagged, not guessed). Also write the finished copy back to version
control under campaigns/ per the standing capture habit.
```

---

## Appendix B. Output templates (the four contracts)

Maria fills one of these per item and stages it. Merge fields are recorded exactly, not paraphrased.

**Blog post**

```
Title:
Slug:
Meta description (<=155 chars):
Category / tags:
Hero image brief:
Primary CTA (text + destination from links registry):
Body (GHL rich text):
```

**Email post**

```
Segment / audience:
Subject line A:
Subject line B (A/B alternate):
Preheader:
Primary CTA (text + destination):
Body (merge fields exact, e.g. {{contact.first_name}}):
Note: signature auto-includes "Carpe Diem," - do not repeat.
```

**Social post**

```
Platform:
Proposed date/time:
Caption / body:
Hashtags:
Image or video brief:
Link (from links registry, if any):
```

**Ad package**

```
Platform (Meta / Google):
Objective:
Primary text variants (2-3):
Headline variants (2-3):
Description:
CTA button:
Destination landing page (from links registry):
Compliance: prohibited-words + FDA-wellness pass = [pass/flag]
Human spend sign-off: REQUIRED before launch.
```
