# Investor Drip, Warm

**Trigger:** Contact Tag `investor_warm` (applied manually alongside `drip_bypass` so the contact skips the cold 8-touch sequence)
**Touches:** 3 over 7 days
**Audience:** personal network and warm introductions who have already had a conversation
**Captured:** 2026-08-02, complete, with eight corrections applied the same day (see the change log at the foot of this file)

`CALENDAR LINK` resolves to **Investor Intro** (Scott only). `ACCREDITATION LINK` resolves to the **Accreditation** form. See `_LINKS.md`.

---

## Touch 1 | Day 1 | Email

**Subject:** Great connecting with you, a few things I wanted to share

**Body:**

```
Hi {{contact.first_name}},

Really enjoyed our conversation. You asked the questions I would have asked.

As promised, here is what is worth looking at.

Where we are:

- 600+ users across 5 countries
- 25,000+ treatments completed
- Zero adverse events
- Return rate under 1 percent, against an industry average of 5 to 10 percent
- One signed white-label partner already launched

Who is behind it:

- Scott Hansbury, 8 startups, 5 exits, $500M+ in value created
- David Letourneau, scaled Alair Homes from 1 to 100+ locations, $750M+ in sales
- Brian Cameron, CFO, and a former securities regulator

On the science side, our advisory board includes Dr. Bruce Hollis, who has over 70,000 citations and is widely regarded as the Godfather of Vitamin D Research.

When you are ready to go deeper I would like to set up a proper presentation with the full investment details.

CALENDAR LINK

Looking forward to continuing the conversation.

{{custom_values.standard_signature}}
```

**Links:** `CALENDAR LINK` -> **Investor Intro**
**Note:** Brian Cameron's former securities regulator background is confirmed by Scott and appears nowhere else in the docs. Worth adding to the KB so agents can use it.

---

## Touch 2 | Day 3 | Internal Notification, follow up call

**Subject:** `ACTION REQUIRED: Follow Up Call: {{contact.first_name}} {{contact.last_name}}`

**Body:**

```
Warm investor follow up, Day 3 action required.

Call {{contact.first_name}} {{contact.last_name}} today for a personal follow up on your recent conversation.

Talking points:

- Did they read what went over on Day 1?
- Any questions on the traction numbers or the team?
- Offer to send the PPM. They do NOT need to be accredited to receive it, or the term sheet, or the subscription agreement. Accreditation gates wire instructions and accepting funds, nothing earlier.
- Ready to put the full investor presentation on the calendar?

If no answer leave this voicemail:

"Hi {{contact.first_name}}, Scott Hansbury from Enyrgy. Following up on our conversation. I wanted to make sure what I sent landed, and see whether you have any questions. Happy to get a proper presentation on the calendar whenever suits. Call me at 602-321-0322 or book directly at enyrgy.com."

Contact details:

Company: {{contact.company_name}}
Email: {{contact.email}}
Phone: {{contact.phone}}
View contact in GHL: {{contact.link}}
```

**This touch carries the attorney rule deliberately.** The original talking points asked "Have they confirmed accredited investor status?", which coached gating on the call itself. Emails can be corrected; a habit formed on the phone cannot. The rule now sits in front of Scott at the moment it is used.

---

## Touch 3 | Day 7 | Email

**Subject:** Clearing the runway

**Body:**

```
Hi {{contact.first_name}},

One piece of housekeeping, because it trips people up more than it should.

Accreditation is not a gate on information. You can read the PPM, the term sheet and the subscription agreement without it. It matters at the point funds would move, which is the last step rather than the first.

You are welcome to complete it now so nothing is waiting on paperwork later, or leave it until you have decided.

ACCREDITATION LINK

Either way, the presentation is the better use of your time. Happy to get it on the calendar.

CALENDAR LINK

{{custom_values.standard_signature}}
```

**Links:** `ACCREDITATION LINK` -> **Accreditation form**. `CALENDAR LINK` -> **Investor Intro**

**COMPLIANCE, THE REASON THIS DRIP MATTERED.** The original read: *"Before I can share the specifics of our current offering I need to confirm your accreditation status."* That is the attorney-corrected error, and it survived here. Do not re-gate. See below.

---

# Change log, 2026-08-02

Eight corrections. One of them is the most consequential compliance find across all five drips.

| # | Touch | Change |
|---|---|---|
| 1 | 3 | **Accreditation gate removed.** Rewritten as housekeeping that states the rule correctly |
| 2 | 2 | "Have they confirmed accredited investor status?" replaced with the attorney rule in full, plus an explicit prompt to offer the PPM |
| 3 | 1 | "Zero returns" corrected to "return rate under 1 percent". The KB says under 1 percent; zero is a stronger and different claim |
| 4 | 1 | "600+ customers" to "600+ users", per the same-day standardisation |
| 5 | 1 | Brian Cameron's former securities regulator background added |
| 6 | 1 | Dr. Hollis moved out of "The team" into the advisory board, which the KB keeps separate |
| 7 | 3 | "Projected returns" removed. The note carries a stated 12 percent rate, which is a term, not a projection |
| 8 | 1, 2, 3 | Eleven em dashes removed |

## The accreditation gate, and why it survived

The attorney-confirmed rule is unambiguous:

> **PPM may be sent to any interested investor after the intro meeting. Accreditation is NOT required before sending the PPM.** The subscription agreement and term sheet are PRE-ACCEPTANCE documents and may also be sent BEFORE accreditation is confirmed. **Accreditation IS required ONLY before wire instructions, or accepting any investment. No exceptions.**

The Session 14 notes record that the pre-Session-13 version of this error "had persisted in three places the KB correction never reached" and lists all three as fixed: the live Investor Drip gate, the Implementation Guide in three locations, and the Audit and Compliance and CFO agent instructions.

**The Warm drip was a fourth place, and nobody looked.** The correction reached the cold drip, the guide and the agents. It never reached here.

The result was two investor sequences saying opposite things about the same process. Cold Touch 6: *"You do not need to be verified as accredited to review our offering."* Warm Touch 3: *"Before I can share the specifics of our current offering I need to confirm your accreditation status."*

Warm contacts are personal network and introductions, so they are the population most likely to compare notes with each other and with existing investors.

**The lesson worth carrying:** a correction declared "fixed everywhere" was verified against the places someone thought to check. This drip is small, quiet, manually triggered and rarely opened, which is exactly why it was missed. When a compliance fix is applied, enumerate every asset that could carry the claim rather than the ones that come to mind.

## Still open

**Brian Cameron's regulator background is not in the KB.** It is now live in investor copy and confirmed by Scott, but agents have no access to it and cannot use or corroborate it. Worth adding to Section 1 alongside the other founder track records.
