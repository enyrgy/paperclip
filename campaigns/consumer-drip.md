# Consumer Drip

**Trigger:** Contact Tag `type_consumer`
**Touches:** 12 over 21 days
**Gating:** first-step If/Else "Bypass Check". Contacts whose tags do NOT include `drip_bypass` run all 12 touches; contacts carrying it END immediately.
**Stop on Response:** On
**Captured:** 2026-08-02, complete. All 12 touches recorded, then a CUB spot-check the same day produced three changes: touch 10, touch 12 and a full rewrite of touch 11.

---

## Touch 1 | Bypass Check (not an email)

If/Else gate. Tags do NOT include `drip_bypass` -> run the sequence. Tags include it -> END.

---

## Touch 2 | Day 1 | Email

**Subject:** Two minutes of the right light

**Body:**

```
{{contact.first_name}},

You came by enyrgy.com. So you already suspect the supplement route is not quite doing it.

Here is what your body forgot it knew. Given the right light, it makes vitamin D, nitric oxide, and serotonin on its own, all three, in the time it takes to brush your teeth. That light is the Enyrgy Vitamin D Primal Light Platform. Two to four minutes. The same vitamin D from actual sun is two to four hours, plus the burn and the aging you did not sign up for.

What keeps it safe is the app. It reads your skin type, picks your dose, and shuts the session off for you. Nobody stands there guessing. Twenty five thousand sessions, zero burns, zero adverse events.

That is the whole pitch. The unit is here if you want to look: https://shop.enyrgy.com/products/uvb-light-therapy. Reply if you have a question. It lands on my desk, not a queue.

{{custom_values.standard_signature}}
```

---

## Touch 3 | Day 3 | SMS

**Body:** (line breaks are as they exist in GHL, verified by unmodified copy/paste)

```
Hi {{contact.first_name}}, quick question. Have you ever had your
Vitamin D levels checked? Most people are surprised when they see
the number. Reply YES or NO and I'll send you something specific
based on your answer. Reply STOP to opt out. Msg & data rates
may apply.
```

Carries the STOP opt-out and rate disclosure, as required.

**WORTH CHECKING IN GHL:** those four line breaks fall mid-sentence, after "your", "see", "specific" and "rates". That is the signature of a textarea's display wrapping having been baked in as hard newlines rather than deliberate formatting. On a phone the message would render with breaks in odd places, since the handset re-wraps to its own width regardless. Segment cost is barely affected (about 254 characters either way, so two segments), but the rendering is worth eyeballing on a real device before the next send.

---

## Touch 4 | Day 5 | Email

**Subject:** What the pill leaves out

**Body:**

```
{{contact.first_name}},

If you take vitamin D and still feel low, the pill may not be the problem. It might just be doing less than the label implies.

Two things about supplements. They open one lane, vitamin D, and only if your body responds well to it. In the trials, about one in four participants were low responders to vitamin D supplementation. They took it; their body did less with it. And even when it works perfectly, it is still one lane out of three.

Your body was built to get three from sunlight at once. Vitamin D. Nitric oxide, which supports cardiovascular regulation. And serotonin, which supports mood, sleep, and focus. A capsule gives you the first. It cannot give you the other two.

That is the whole reason the Enyrgy Vitamin D Primal Light Platform exists. Two to four minutes, all three, with the app setting your dose by skin type and ending the session for you.

If you want the science behind it, reply and I will send it. Or grab a 15-minute call here: Book Call.

{{custom_values.standard_signature}}
```

**Links:** `Book Call` -> **Consumer Discovery** (see `_LINKS.md`). Inline order URL is written out in the body and needs no entry.

---

## Touch 5 | Day 7 | Internal Notification (not customer-facing)

**Subject:** `ACTION REQUIRED - Personal Call: {{contact.first_name}} {{contact.last_name}}`

**Em dash in the live subject corrected in GHL, Aug 2.** GHL and this file now match.

**Body:**

```
Consumer drip Day 7 action required.

Call {{contact.first_name}} {{contact.last_name}} and leave this voicemail if no answer:

"Hi {{contact.first_name}}, this is Scott Hansbury from Enyrgy. I noticed you were curious about what we do and I wanted to reach out personally.

We have had 600+ users complete 25,000+ sessions

with zero adverse events. I would love 15 minutes to show you

exactly how the Enyrgy Vitamin D Primal Light Platform works for someone like you.

Book a call at enyrgy.com or call me back at

602-321-0322."

Contact details:

Company: {{contact.company_name}}

Email: {{contact.email}}

Phone: {{contact.phone}}

View contact in GHL: {{contact.link}}
```

---

## Touch 6 | Day 8 | SMS

**Body:** (line breaks as they exist in GHL)

```
Hi {{contact.first_name}}, I left you a voicemail. Quick version: in our
 12-week study, participants raised their vitamin D an average of
111 percent, and every one of them reached optimal levels. Want to see
how it could work for you? Book a free call: https://api.leadconnectorhq.com/widget/booking/C0hV5CFHUhWOIzs4OedC
Reply STOP to opt out. Msg & data rates may apply.
```

**COMPLIANCE:** cites the 111 percent and all-reached-optimal figures with no N=5 pilot caveat. See the compliance note at the foot of this file.

---

## Touch 7 | Day 10 | Email

**Subject:** Is it safe?

**Body:**

```
{{contact.first_name}},

The first question people ask about the Enyrgy Vitamin D Primal Light Platform is almost always the same one: is it safe.

Fair question. Here is the honest version.

Sunlight is about 95 percent UVA, the wavelength that ages skin and carries the risk. The platform flips that. It emits over 90 percent UVB and under 10 percent UVA, the opposite of sunlight, weighted to the wavelength your body actually uses.

The app is the other half. It reads your Fitzpatrick skin type, sets your personal dose (your MED, the point where skin would start to redden), and ends the session there on its own. You are not the one watching a clock or guessing.

The record backs it up. Twenty five thousand sessions, zero burns, zero adverse events.

If you want to see how the dose works for your skin type, reply and I will walk you through it. Or grab a 15-minute call here: Book Call.

{{custom_values.standard_signature}}
```

**Links:** `Book Call` -> **Consumer Discovery**

---

## Touch 8 | Day 12 | Email

**Subject:** What $2,995 works out to per session

**Body:**

```
{{contact.first_name}},

$2,995 for the Enyrgy Vitamin D Primal Light Platform reads big. It reads a lot smaller once you run it per use.

Five sessions a week for five years is about 1,300 sessions. That puts it at $2.30 a session. Less than your coffee.

Set that next to what the supplement route already costs. Vitamin D pills run $600 to $1,200 a year, with no promise your body does much with them (in the trials, about one in four people were low responders). Five years of that is real money for one pathway with an open question attached.

The platform opens all three pathways in two to four minutes, at $2.30 a session. If the up-front number is a stretch, financing is there.

If you want to talk it through for your situation, reply, or grab a 15-minute call here: Book a call.

{{custom_values.standard_signature}}
```

**Links:** `Book a call` -> **Consumer Discovery**
**Checked:** the $600 to $1,200 supplement figure and the $2.30 per session maths both match KB approved talking points.

---

## Touch 9 | Day 14 | SMS

**Body:** (line breaks as they exist in GHL)

```
Hi {{contact.first_name}}, one thing I have not mentioned yet.
About 90% of our customers also use red light. The two do different
biological jobs, so this sits alongside your red light and fills the
vitamin D gap it cannot. Worth a 15-minute call? Book here:
https://api.leadconnectorhq.com/widget/booking/C0hV5CFHUhWOIzs4OedC
Reply STOP to opt out. Msg & data rates may apply.
```

---

## Touch 10 | Day 16 | Email

**Subject:** For the person who reads the studies first

**Body:**

```
{{contact.first_name}},

If you want the data before anything else, here it is.

In a 12-week study on the Enyrgy Vitamin D Primal Light Platform, participants raised their vitamin D an average of 111 percent, from 39.96 to 84.20 ng/mL. 100 percent of them reached optimal levels. Not most. All of them.

The board behind it carries real weight. Dr. Bruce Hollis, who has over 70,000 citations and is widely regarded as the Godfather of Vitamin D research, has reviewed and endorsed the platform. Dr. Samantha Kimball, a leading UV-safety researcher, designed the MED protocol that sets your dose every session. Dr. William Grant is a NASA UVB researcher and phototherapy pioneer.

One thing research-minded people always ask: where does red light fit. About 90 percent of our customers use both. They do different biological jobs, so this sits alongside red light rather than replacing it.

If you have questions about the study or the mechanism, reply and I will answer them myself, or grab a 15-minute call here: Book a call.

{{custom_values.standard_signature}}
```

**Links:** `Book a call` -> **Consumer Discovery**
**Checked:** advisor bios match the KB approved wording exactly, including "reviewed and endorsed". See the FTC note at the foot of this file.
**COMPLIANCE:** cites the 111 percent and 100-percent-optimal figures with no N=5 pilot caveat, and "Not most. All of them." actively invites the inference of a large trial. See the compliance note below.

---

## Touch 11 | Day 19 | SMS

**Body:**

```
Hi {{contact.first_name}}, the part most people ask about last: there is a 30 day money back guarantee. Try it, and if it is not for you, send it back. Under 1 percent of people do. Happy to answer anything before you decide. Book here: https://api.leadconnectorhq.com/widget/booking/C0hV5CFHUhWOIzs4OedC Reply STOP to opt out. Msg & data rates may apply.
```

**REWRITTEN Aug 2 (CUB spot-check).** The original led with limited batches and a few weeks' ship time. It was the only touch in the sequence that handed the reader pressure rather than something useful, and arriving on Day 19 it undercut the low-pressure Day 21 close two days later.

Replaced with the objection nothing else in the drip answers: what if it does not work for me. The guarantee and the under-1-percent return rate work as one move, risk reversal plus the evidence almost nobody needs it.

The manufacturing fact is true and stays available for a reply to someone actually deciding. It does not need broadcasting to everyone on Day 19.

**Deliberately keeps the guarantee decoupled from lab timing.** The Session 14 audit found several emails tying the 30-day window to an 8-to-12-week lab retest, which is impossible inside 30 days. This is a standalone keep-or-return decision with no mention of labs.

Three segments, the same as the copy it replaces.

---

## Touch 12 | Day 21 | Email

**Subject:** Closing the loop, door open

**Body:**

```
{{contact.first_name}},

I have sent a fair bit over the last few weeks, and I would rather not turn into inbox noise. So this is the last one from the sequence.

Here is where things stand. 600 plus people have come to the Enyrgy Vitamin D Primal Light Platform the same way you did, most of them tired of guessing whether their routine was actually doing anything. They are not guessing anymore.

If the timing is not right today, that is genuinely fine. Life moves and priorities shift. Keep this in your back pocket. If you find yourself wondering again why your energy is low or your sleep is off, you know where we are.

If you would rather just find out whether it fits, that is a 15-minute call, free, and the information is yours to keep either way.

Book whenever you are ready: Book a call.

Wishing you good health either way.

{{custom_values.standard_signature}}
```

**Links:** `Book a call` -> **Consumer Discovery**

---

# Compliance notes on this workflow

All three items below were raised during capture on 2026-08-02 and **resolved by Scott the same day**. They are recorded as settled so they are not re-raised on every future read.

## 1. N=5 caveat omitted from the pilot figures (touches 6 and 10): DELIBERATE, RESOLVED

Touches 6 and 10 cite the 111 percent and 100-percent-optimal figures without the pilot context that KB Section 4 otherwise requires.

**Scott's call, and the reasoning:** the science page states the N=5 design plainly, and touch 10 is aimed at the reader who goes and reads it. The substantiation lives one click away in the place that reader will actually look, so the email carries the finding and the page carries the design.

Note this is the same decision made for the Q2 2026 investor update, taken separately rather than by precedent.

## 2. FTC consent for the Hollis endorsement (touch 10): ON FILE, RESOLVED

The KB requires documented consent for any public "reviewed and endorsed" claim. **Consent is on file.** Settled, do not raise again.

## 3. "Limited batches" in touch 11: TRUE, but the touch was rewritten anyway

The scarcity and lead-time language was a literal description of manufacturing, not manufactured urgency. Confirmed by Scott at capture, 2026-08-02.

It came out of touch 11 for a separate reason found in the CUB spot-check the same day: it was the only touch handing the reader pressure rather than something useful. See touch 11 above.

**Batch size is deliberately NOT a KB fact.** It moves with funding and production capacity, so a number written down becomes a claim agents state confidently after it stopped being true, with nothing to catch the drift. KB Section 3 records the policy instead: never quote a batch size or lead time, escalate to Scott.
