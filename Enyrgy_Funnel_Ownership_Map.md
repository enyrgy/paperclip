# Enyrgy Funnel Ownership Map: who sends what

The purpose of this doc: end the confusion about GHL workflows vs Paperclip agents by deciding, per touch, **which engine sends it**, so the two never double-send.

## The rule (autopilot vs brain)

- **GHL workflow = autopilot.** Owns the scheduled, repeatable, pre-written drip touches sent to many contacts. Reliable, runs 24/7, no per-send human approval. This is where the *bulk sending* lives.
- **Paperclip agent = brain.** Owns routing, first-response decisions, replies to real people, judgment/exceptions, lead scoring, and the human-approval-gated sends (investor). Every agent send currently holds at the approval gate, so agents must NOT be the ones firing high-volume routine touches, or every drip email would need a human click.
- **`drip_bypass` = the manual switch.** The moment an agent or human takes a contact into a live conversation, set `drip_bypass` so the GHL drip stops and they do not collide.
- **Stop on Response: ON = the automatic switch.** Turn this GHL setting on for every sending workflow below. When a contact replies, GHL automatically pulls them out of that sequence and the reply wakes the agent to take over. It is the automatic version of `drip_bypass` and the clean autopilot-to-agent handoff. Leave it OFF on router/utility workflows (WF-01, lead scoring, WF-04 Sentinel, WF-05, WF-09, WF-10), which do not send sequences.

**Why the confusion existed:** several funnels trigger BOTH a GHL workflow and an agent on the same tag (e.g., `unit_shipped` fires WF-06 *and* wakes the Onboarding agent). Nobody had drawn the line. This doc draws it.

## Ownership by funnel

### Consumer nurture (general lead, no magnet)
| Touch | Trigger / timing | Owner | Notes |
|---|---|---|---|
| New-lead routing | Contact Created (WF-01) | **Agent** (Dispatcher) | Identifies funnel, sets tags/assigned_agent. No prospect message. |
| 5-minute first response (SMS) | type_consumer (WF-02) | **GHL** | Speed matters; GHL fires instantly. Gated by `drip_bypass`. |
| Consumer Drip touches 2-12 (email/SMS, 21 days) | type_consumer, no drip_bypass | **GHL** | Bulk scheduled drip. Load the voice-fixed copy into these workflow steps. |
| A real reply from the lead | inbound reply | **Agent** (Sales Outreach / SDR) | Composes a response; set `drip_bypass`, hand to human at live conversation. |
| Lead score >= 70 | GHL native lead scoring (Manage Scoring), NOT a discrete workflow | **Agent** (SDR) | Confirm scoring is configured under Settings, Manage Scoring. SDR books the discovery call at threshold. |

**Stop on Response: ON** on the Consumer Drip and the magnet series (WF-11 through WF-20). A reply halts the sequence and hands off to the agent.

### Onboarding (WF-06, `unit_shipped`): your example
| Touch | Trigger / timing | Owner | Notes |
|---|---|---|---|
| 6 scheduled onboarding touches | unit_shipped (WF-06) | **GHL** | WF-06 auto-sends all 6. The 1 template we built = **touch 1 (welcome)**; touches 2-6 still need their copy voice-fixed. |
| Customer question / reply | inbound reply | **Agent** (Onboarding) | Tailored answer, gated. |
| Handoff to Client Success | onboarding complete | **Agent** (Onboarding -> CSM) | |
| **FIX** | | | Narrow the Onboarding agent's `unit_shipped` trigger so it does NOT also send an onboarding email. Right now both WF-06 and the agent fire on the same tag = double-send. Agent wakes for replies/exceptions only. |

**Stop on Response: ON** on WF-06. A reply halts onboarding and hands off to the Onboarding agent.

### Referral / Review (WF-07, `unit_activated`)
| Touch | Trigger / timing | Owner | Notes |
|---|---|---|---|
| Referral ask ($150 / $100) | unit_activated (WF-07) | **GHL** | Scheduled milestone ask. Use the voice-fixed referral template. |
| Review ask | unit_activated | **GHL** | Review links live: GBP + Trustpilot (KB Section 3). Invite every customer neutrally, no review-gating (FTC/Google/Trustpilot). |
| Referral reply / question | inbound | **Agent** (Referral & Reviews) | |
| Ambassador ask | customer milestone | **PAUSED** | Do not send until the ambassador program is finalized (perks confirmed, FTC disclosure requirement in place, documented in the KB). |

**Stop on Response: ON** on WF-07. A single ask, but a reply should still stop any follow-up and hand to the agent.

### Reactivation (WF-08, `status_cold` + 60-day wait)
| Touch | Trigger / timing | Owner | Notes |
|---|---|---|---|
| 4-touch reactivation | status_cold + 60-day (WF-08) | **GHL** | WF-08 auto-sends the 4 touches. Our template = touch 1; 3 more need voice-fixing. |
| Reply | inbound | **Agent** (Reactivation) | Set drip_bypass, hand to human if real intent. |

**Stop on Response: ON** on WF-08. A reply halts the win-back and wakes the Reactivation agent.

### Investor (Investor Drip 8-touch + PPM): the one the AGENT lane genuinely owns
| Touch | Trigger / timing | Owner | Notes |
|---|---|---|---|
| Touches 1-6 (credibility / traction, NO financial content) | type_investor, no drip_bypass | **GHL** | Reg D: credibility only for unverified contacts. Gated so no financial content leaks. |
| Touch 7: PPM delivery | after Intro Meeting complete | **Agent-queued / Human-sent (CFO)** | The template we built. Human-sent, holds at the gate, attorney-approved PPM only. NOT auto-fired. |
| Subscription agreement, accreditation, wire, acceptance | later stages | **Human / CFO** | Gated by `accredited_verified`; every CFO write holds at the gate. |

**Stop on Response: ON** on the cold Investor Drip. An investor reply is exactly when the human takes over, so the cold sequence should stop.

### Always agents (no GHL-workflow equivalent)
Dispatcher (routing) · Sentinel (stale-lead monitoring) · Audit and Compliance (the gate) · Quality Control (data audits) · KB Manager (facts) · Sales Scout (partner prospecting) · lead scoring.

## What has to be fixed to make this real

1. **De-conflict shared triggers.** Any agent whose trigger tag also fires a GHL workflow (Onboarding on `unit_shipped`, Reactivation on `status_cold`, Sales Outreach on `type_consumer`) must be narrowed so it does not re-send what GHL already sends. Agents wake for replies/exceptions, not to duplicate the drip. (Done in the agent instruction pack; deploy to the live agents.)
2. **Load the voice-fixed copy into the GHL workflow steps.** The 5 templates are single messages (mostly touch 1). GHL owns the full sequences, so the remaining touches (onboarding 2-6, reactivation 2-4, consumer drip 2-12) still need their copy brought into voice.
3. **Turn on Stop on Response, and wire `drip_bypass`.** Set Stop on Response: ON for every sending workflow (the automatic reply handoff). Keep `drip_bypass` for the deliberate takeover when a contact has not replied yet.
4. **Confirm lead scoring is actually built.** "WF-03" is GHL native scoring (Settings, Manage Scoring), not a discrete workflow, and may never have been configured. Verify the score model and the 70+ threshold that wakes the SDR.
5. **Keep the investor lane agent/human-owned.** That is the one funnel where the gated agent path owns the critical touches, by design.

*One-line summary: GHL sends the scheduled drip to everyone; agents handle the thinking, the replies, and the gated investor sends. Stop on Response and drip_bypass keep them from stepping on each other.*
