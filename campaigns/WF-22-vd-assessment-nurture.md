# WF-22 Vitamin D Assessment Nurture

**Trigger:** Contact Tag `magnet_vitamin_d_assessment`, following WF-21
**Touches:** 3 emails, Days 3, 5 and 7
**Ends with:** `nurture_longterm`, which hands the contact to WF-17
**Captured:** 2026-08-03, complete, with three corrections applied.

**Read alongside `WF-21-vd-assessment-capture.md`.** WF-21 sends the results email on Day 1 and WF-22 picks up on Day 3. A reader experiences them as one sequence.

---

## Touch 1 | Day 3 | Email

**Subject:** Your D3 does one job. Light does five.

**Body:**

```
Hi {{contact.first_name}},

Quick follow-up to your assessment.

Vitamin D is the first output of a process your body runs when light hits skin. Sunlight does not stop at D3. One exposure produces five outputs: vitamin D3, vitamin D sulfate, photoproducts, nitric oxide, and serotonin. Five outputs from one trigger.

A capsule gives you the first one. That is the whole reason you can take D3 every day and still read low. You are topping up one of those five and skipping the rest.

The Enyrgy Vitamin D Primal Light Platform gives you that light in a few minutes, dosed to your skin type. Not the whole of midday sun, the part of it your body actually uses.

See how it works: Enyrgy Vitamin D Platform

{{custom_values.standard_signature}}
```

**CORRECTED Aug 3.** The midday sun claim. See the change log.

**Checked:** the five-outputs framing follows the KB rule of thumb exactly. Five outputs describes what sunlight does; the three Triple-Pathway pathways are reserved for what Enyrgy delivers.

---

## Touch 2 | Day 5 | Email

**Subject:** 39.96 to 84.20, and the safety question

**Body:**

```
Hi {{contact.first_name}},

Two questions people ask right after the assessment. Here are straight answers.

Does it work? In a small 12-week study, five people used the platform four to six times a week. Average vitamin D went from 39.96 to 84.20 ng/mL, and every one of them reached optimal. Small study, real labs, zero adverse events.

Is it safe? This is precision phototherapy, not a tanning bed. It doses to your skin type using your MED, the Minimal Erythema Dose, the point where skin would just start to redden. The app keeps your dose safely under that line, triggers synthesis, and ends the session for you. Across 25,000+ sessions the platform has produced zero adverse events, and it allows only one session a day, so you cannot overdo it.

Want to talk it through before you decide? Grab a quick call:
Book a Call

Or see the platform: Enyrgy Vitamin D Platform

{{custom_values.standard_signature}}
```

**CORRECTED Aug 3.** A stray `}` on the line after the signature was deleted. It rendered as a literal closing brace at the bottom of every send.

**Checked:** N=5 disclosed, the 25,000+ session figure and the one-session-a-day limit both match the KB.

---

## Touch 3 | Day 7 | Email

**Subject:** The only test that actually settles this

**Body:**

```
Hi {{contact.first_name}},

You do not have to take my word for any of this. The honest test is your own labs.

Test your level now. Use the platform at least four times a week, then test again at eight to twelve weeks. That is long enough for the number to settle rather than just start moving, and you decide on your own data.

Deciding whether to keep the unit is separate and simpler. It comes with a 30-day money-back guarantee, so if it is not for you, send it back.

You have seen "insufficient" on a lab report before. You can keep seeing it, or you can close the gap the way your body was built to, through light on skin.

Reserve your platform: Shop

Still have questions? Book a quick call: Book a Call

{{custom_values.standard_signature}}
```

**CORRECTED Aug 3.** Retest interval changed from four weeks to eight to twelve. See the change log.

**GUARANTEE LANGUAGE ALREADY CORRECT.** "Deciding whether to keep the unit is separate and simpler" decouples cleanly without needing the standard phrasing. Second workflow running to need no correction here.

---

# Change log, 2026-08-03

| # | Touch | Change |
|---|---|---|
| 1 | 2 | Deleted a stray `}` that rendered after the signature on every send |
| 2 | 3 | Retest interval corrected from four weeks to eight to twelve |
| 3 | 1 | "You get what the midday sun gives you" replaced |

## The four-week retest was the one that mattered

Every other workflow says eight to twelve weeks. The study itself ran twelve. This one said four.

**Four weeks is too early to show the real change.** Levels take roughly two to three months to settle at a new baseline. A reader testing at four weeks sees partial movement, concludes it barely worked, and returns a unit that was doing exactly what it should.

Four weeks probably got chosen because it fits inside the 30-day guarantee, making the two decisions line up. But that is the coupling removed from four other workflows today, and this email already handles it correctly in the next paragraph. The longer interval makes the lab advice honest without breaking anything.

## The midday sun claim contradicted the safety story

Touch 1 said "You get what the midday sun gives you, without the burn."

The platform does the opposite. Consumer Drip touch 7 puts it precisely: *"Sunlight is about 95 percent UVA, the wavelength that ages skin and carries the risk. The platform flips that. It emits over 90 percent UVB and under 10 percent UVA, the opposite of sunlight."*

Claiming parity with midday sun gives away the entire safety argument, which rests on the spectrum being deliberately different. "Without the burn" compounded it by implying the difference is intensity or duration rather than wavelength.

## What was already right

**No shared-template error.** WF-16 and WF-14 both opened their second touch with "Yesterday's idea, made concrete", three days wrong in both. WF-22 does not carry it.

**The guarantee decoupling**, handled in the copy's own words rather than the standard phrasing.
