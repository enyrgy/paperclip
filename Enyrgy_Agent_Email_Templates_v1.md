# Enyrgy Agent Email Templates v1 (in-voice, approved-template lane)

Authored against `StorySelling-OS/style-guide.md` (Mode 2: Trusted Advisor) + the Universal Anti-AI Rules, with conversion disciplines matched to each asset's job per KB Section 14. humanize-pro reviewed. The **four consumer emails were tightened to 45-46/50** (max-voice pass, claims re-checked against the KB); the **investor email is held at 39/50 by design** (calm register is the point). These are meant to be loaded as **approved GHL templates the agents SEND**, not freehand. Facts are KB-exact. No em-dashes, no prohibited words, price never anchored.

Voice checklist applied to all: observed opener (not a hedge) · one dry aside · lands on a reframe, not a summary · prose over bullet-stacks · no structure-telegraphing · product full name on first reference · "Carpe Diem, Scott" sign-off.

Deploy: load each as an LC Email template in GHL (sub-account GtXjla7Ld1dordsTWrVy) and point the relevant workflow/agent at it so agents send the template rather than free-writing. Update when KB facts change (KB Manager owns this).

---

## 1. Consumer nurture, first touch  (Sales Outreach)  -- DEPLOYED (edited by Scott)
- **Use:** general consumer lead, fresh website entry, top of funnel.
- **Skill lens:** eugene (match awareness, build desire around the mechanism) + cub.
- **Compliance:** supplement line is the reader's own suspicion, not a quantified claim (stays clear of the "one in four" precision rule); efficiency + safety KB-exact; no price anchor.
- **Note:** live version in GHL. Uses merge fields; signature block supplies the "Carpe Diem," sign-off (do not add separately).

**Subject:** Two minutes of the right light

{{contact.first_name}},

You came by enyrgy.com. So you already suspect the supplement route is not quite doing it.

Here is what your body forgot it knew. Given the right light, it makes vitamin D, nitric oxide, and serotonin on its own, all three, in the time it takes to brush your teeth. That light is the Enyrgy Vitamin D Primal Light Platform. Two to four minutes. The same vitamin D from actual sun is two to four hours, plus the burn and the aging you did not sign up for.

What keeps it safe is the app. It determines your skin type, picks your dose, and shuts the session off for you. Nobody stands there guessing. Twenty five thousand sessions, zero burns, zero adverse events.

That is the whole pitch. The unit is here if you want to look: https://shop.enyrgy.com/products/uvb-light-therapy. Reply if you have a question. It lands on my desk, not a queue.

{{custom_values.standard_signature}}

---

## 2. New customer onboarding, unit shipped  (Onboarding)  -- DEPLOYED (edited by Scott)
- **Use:** unit shipped / WF-06 trigger.
- **Skill lens:** cub + humanize (reduce friction, one clear action).
- **Compliance:** registration URL + dosing/safety KB-exact.
- **Note:** live version in GHL. Uses merge fields; the signature block supplies the "Carpe Diem," sign-off (do not add it separately). Registration step moved up front with device-setup instructions (center button + QR scan).

**Subject:** It shipped. Do this one thing first.

{{contact.first_name}},

Your Enyrgy Vitamin D Primal Light Platform left here today. It is somewhere between Phoenix and your door.

Register your users here: https://api.enyrgy.com/   When it lands, plug it in, turn it on and open the app, click the center button and scan the QR code.

That is the whole game. The app determines your skin type, sets your dose, and ends the session for you, so you are never the one watching a clock or guessing how long is too long.

Then you stand in it for two to four minutes. That is enough to open all three pathways, vitamin D, nitric oxide, and serotonin.

Already running red light? Keep it. The two do different jobs, so this slots into your routine instead of taking anything over.

One number, since it is a light and everyone asks: twenty five thousand sessions, zero burns, zero adverse events. The app earns that on every single one.

Anything looks off when it arrives, reply straight to me.

{{custom_values.standard_signature}}

---

## 3. Referral activation  (Referral & Reviews)  -- DEPLOYED (edited by Scott)
- **Use:** happy customer milestone (activated, 10+ sessions). REFERRAL ONLY.
- **Skill lens:** cub + humanize.
- **Compliance:** referral terms KB-exact ($150 off referee / $100 credit referrer, framed as credit for future purchases). **Review ask deliberately omitted** until the Google Business Profile review link is live in the KB. Add the review ask only after that link ships.
- **Note:** live version in GHL. Uses merge fields; signature block supplies the "Carpe Diem," sign-off (do not add separately).

**Subject:** The people you would tell have not heard of us yet

{{contact.first_name}},

Ten sessions in. That is the point where it stops being a decision and starts being a habit, somewhere between your coffee and your keys.

So, a favor that pays both of us. The Enyrgy Vitamin D Primal Light Platform got to 600 plus customers in five countries on zero paid ads.

The whole engine is people like you saying one sentence to the right person.

If it earned its spot, send it on. They get 150 dollars off. You get 100 in credit for future purchases. Same link you used: https://shop.enyrgy.com/products/uvb-light-therapy.

No pitch required. "This gets me my vitamin D in four minutes" does most of the work.

{{custom_values.standard_signature}}

---

## 4. Reactivation, touch 1  (Reactivation)  -- DEPLOYED (edited by Scott)
- **Use:** lapsed lead, full sequence with no engagement, 60-day pause elapsed / WF-08 eligible.
- **Skill lens:** presell-sandwich (present pain + cost of inaction) + humanize.
- **Compliance:** supplement line kept soft (no "supplements fail one in four"); return-rate + efficiency KB-exact.
- **Note:** live version in GHL. Uses merge fields; signature block supplies the "Carpe Diem," sign-off (do not add separately).

**Subject:** Still low, or did you sort it out?

{{contact.first_name}},

You looked at the Enyrgy Vitamin D Primal Light Platform a while back, then life did what life does.

No judgment. It happens to many people who come through.

One straight question, because it is the only one that matters. Did the vitamin D actually get handled? Or is it still on the someday list, next to the supplements you are not fully sure your body is using?

If it is still open, here is why people come back. Two to four minutes. Three pathways your body runs on, vitamin D, nitric oxide, serotonin.

The app sets your dose by skin type and ends the session for you.

Twenty five thousand sessions, zero adverse events, and under one percent of people send it back. The industry sits at five to ten.

Solved it elsewhere?

Good, genuinely, tell me and I am gone. If not, reply and we pick up where we left off.

{{custom_values.standard_signature}}

---

## 5. Investor PPM delivery cover  (CFO): COMPLIANCE-CRITICAL  -- DEPLOYED (edited by Scott)
- **Use:** investor who has completed the intro meeting.
- **Skill lens:** cub + humanize, investor register (credible, calm, no hype, founder-to-investor peer). Deliberately not pushed for edge; investor/securities context wants calm.
- **SEND PRECONDITIONS (hard):**
  1. Intro meeting is complete.
  2. **The attached PPM is the attorney-approved version.** The PPM is now approved by Enyrgy's securities attorney; confirm you are attaching that approved version, not a draft.
  3. Accreditation is NOT required for PPM delivery (attorney-confirmed). Do not gate this send on `accredited_verified`.
- **Do NOT** bundle wire instructions, the subscription agreement, or the term sheet in this email. Sub-agreement + term sheet are separate pre-acceptance sends (no accreditation needed). Wire instructions / accepting an investment require `accredited_verified` = Yes.
- Every CFO write still holds at the human-approval gate by design. Keep it that way.
- **Signatory:** shown as Scott (the voice profile on file is Scott's). The PPM is human-sent by Scott.
- The email intentionally **defers full terms to the PPM** rather than restating the offer in-channel. Keep it that way.
- **Note (Scott edit):** "next documents" now reads "the subscription agreement and the investor accreditation" (term sheet dropped from the sentence). Still KB-consistent: accreditation is required before funds, and "anything touching funds comes later" keeps the money gate intact. Live version uses merge fields; signature block supplies the sign-off.

**Subject:** The PPM from our conversation

{{contact.first_name}},

Good to sit down properly the other day. The questions you asked were the right ones, which is usually a good sign.

As promised, the PPM is attached. It puts the company, the technology, and the full terms of the current round in one place, so you can read it at your own pace instead of reconstructing it from a call.

The frame, so you know what you are holding: a private credit note on a three year term, with the option to convert to equity later at a discount to an independent valuation if you would rather. The minimum, the rate, and the timing are all laid out in the document.

Nothing here asks you to decide anything. Reading it moves no money and commits you to nothing. When you have been through it and want to go further, the next documents are the subscription agreement and the investor accreditation, and anything touching funds comes later still, once both sides have confirmed.

I am the point of contact on this end of it. Reply with whatever comes up, or grab time on my calendar and we will go through it together.

{{custom_values.standard_signature}}

---

*Authored in-session against style-guide.md Mode 2 + Universal Anti-AI Rules; humanize-pro reviewed (consumer 4 at 45-46, investor 39 by design). CONFIDENTIAL - Enyrgy Inc - Sunlight. Evolved.*
