# WF-08 Cold Reactivation

**Trigger:** Contact Tag `status_cold`
**Touches:** 4, at Days 60, 67, 74 and 88
**Stop on Response:** On
**Audience:** leads who went quiet, re-approached two months later
**Captured:** 2026-08-03, complete, with six corrections applied.

---

## Touch 1 | Day 60 | Email

**Subject:** A lot has changed since we last spoke

**Body:**

```
{{contact.first_name}},

It has been a while, and I wanted to reach out personally.

A fair bit has changed at Enyrgy since we last spoke. We are at 600 plus users across 5 countries, 25,000 plus sessions with zero adverse events, and a return rate still under 1 percent, against an industry average of 5 to 10 percent. Lumanova also launched Luma D Light, their own brand built on our technology.

The Enyrgy Vitamin D Primal Light Platform is $2,995, and it still does what nothing else does in the time: all three pathways, vitamin D, nitric oxide, and serotonin, in two to four minutes, with the dose calibrated to your skin type and an automatic cutoff.

If the timing was not right before, I get it. Life moves. But if your health goals are still on your mind, I would be glad to reconnect.

Just an open door.

Book a free 15-minute call: Book a call

{{custom_values.standard_signature}}
```

**Links:** `Book a call` -> **Consumer Discovery**
**CORRECTED Aug 3, three times.** The claim, the price wording, and "No pressure". See the change log.

---

## Touch 2 | Day 67 | SMS

**Action name in GHL:** Reactivation

**Body:**

```
Hi {{contact.first_name}}, this is Scott from Enyrgy. A few updates since we last connected, including 600+ users across 5 countries. If your health goals are still on your mind, I would love to reconnect. Book a quick call: https://api.leadconnectorhq.com/widget/booking/C0hV5CFHUhWOIzs4OedC Reply STOP to opt out. Msg & data rates may apply.
```

**CORRECTED Aug 3.** "customers" to "users".

---

## Touch 3 | Day 74 | Email

**Subject:** Someone just like you, and what happened

**Body:**

```
{{contact.first_name}},

A quick story, then the data behind it.

One of our customers came to us at a vitamin D level of 28, deficient, after years of supplements that were not moving the number. Twelve weeks on the Enyrgy Vitamin D Primal Light Platform, he was at 84. Roughly tripled.

That is one person, and his result was well above average. Here is the pattern behind it: in our 12-week study, the five participants raised their vitamin D by an average of 111 percent, and every one of them reached optimal. Small study, no control group, and we say so. 600 plus users across 5 countries are on it now.

Supplements are one lane, vitamin D, and only if your body responds. The platform runs all three, vitamin D, nitric oxide, and serotonin, in two to four minutes.

If your health goals are still on your mind, I would be glad to show you how it could work for you.

Book a free 15-minute call: Book a call

{{custom_values.standard_signature}}
```

**Links:** `Book a call` -> **Consumer Discovery**
**CORRECTED Aug 3, three times.** The typicality disclosure, the study description, and the subject em dash. See the change log.

**The customer is real**, confirmed by Scott, and is not one of the five study participants. Their starting levels were 38.4, 34.0, 37.0, 47.0 and 43.4; nobody began at 28.

**OPEN: consent for this story is unconfirmed.** It is a named individual's health data used in marketing, which is the same standard WF-25 applies to every testimonial. Worth confirming it is on file.

---

## Touch 4 | Day 88 | Email

**Subject:** Is the timing better now?

**Body:**

```
Hi {{contact.first_name}},

I have reached out a few times over the past few months and I do not want to become noise in your inbox.

So this is my last reach out for a while.

One simple question. Is the timing better now?

If your energy is still not where you want it. If your sleep is still inconsistent. If you are still searching for something that actually works. The Enyrgy Vitamin D Primal Light Platform is still here and so are we.

600+ users. 25,000+ sessions. Zero adverse events. Less than 1% return rate.

If you are ready to take the next step:

Order here:
Order Link

Or book a free call first:
Calendar Link

If the timing is still not right, I will check back in a few months. The door is always open.

{{custom_values.standard_signature}}
```

**Links:** `Order Link` -> order page. `Calendar Link` -> **Consumer Discovery**
**CORRECTED Aug 3.** "I completely understand" removed.

**Left as written, deliberately.** The three fragments about energy, sleep and searching do imply the platform addresses those specifically, and the KB requires the serotonin pathway be framed as biology rather than a promise. This version is conditional rather than asserted, which is materially softer than the WF-06 wording corrected the same day. Scott's call to keep it.

---

# Change log, 2026-08-03

| # | Touch | Change |
|---|---|---|
| 1 | 1 | "No supplement or single device does" replaced with the qualified claim; "is now $2,995" became "is $2,995" |
| 2 | 3 | "In our 12-week clinical study" became "in our 12-week study, the five participants"; typicality disclosure added |
| 3 | 1 | "No pressure" removed |
| 4 | 3 | Subject em dash removed |
| 5 | 2 | "customers" to "users" |
| 6 | 4 | "I completely understand" removed |

## The typicality disclosure was the one that mattered

Touch 3 opens with a customer who went from 28 to 84, a 200 percent increase, then cites an average of 111 percent. A story followed by a statistic reads as *here is what happens, and here is the proof*.

The Session 14 audit flagged typicality-screening consumer health testimonials as a standing obligation. **"That is one person, and his result was well above average"** discharges it in one clause, and the story still lands. The honesty makes the 111 percent more credible rather than less.

## Why the price angle was dropped

The unit was $3,445 and is now $2,995, a $450 reduction, which looks like a strong reactivation hook. It was not used because **the change was five months ago**, and WF-08 fires at Day 60. A good share of this audience already saw $2,995, so telling them the price dropped would simply be wrong for them.

"Now" came out for the same reason: it hints at news that is not news.

## "The five participants", not "five participants"

Scott's catch. "Five participants raised their vitamin D by an average of 111 percent" leaves room for a larger cohort in which only five responded. "The five participants" closes it.

**The same ambiguity exists in the WF-06 line corrected earlier the same day** and should be fixed there too.

## "Pilot" is the wrong word, everywhere

Also Scott's catch. The study ran months after full production launch, so "pilot" implies pre-launch or beta testing that did not happen.

It appears in four live emails and, more importantly, twice in KB Section 4, which is what keeps generating it. Tracked as a separate sweep.
