# Investor Drip, Cold

**Trigger:** Contact Tag `type_investor`
**Touches:** 7 over 30 days
**Gating:** first-step Bypass Check. Contacts carrying `drip_bypass` END immediately.
**Captured:** 2026-08-02, complete, with five corrections applied the same day (see the change log at the foot of this file)

**Touch count corrected during capture.** The Implementation Guide recorded 8 touches; the live workflow has 7. The guide was updated to match.

`CALENDAR LINK` resolves to **Investor Intro** (Scott only, see `_LINKS.md`). `ACCREDITATION FORM LINK` resolves to the **Accreditation** form.

---

## Touch 1 | Day 1 | Email

**Subject:** Enyrgy: a health-tech opportunity worth 15 minutes

**Body:**

```
Hi {{contact.first_name}},

We have over 600 users and completed 25,000 sessions without spending a dollar on advertising. Every one of them found us, in five countries, by word of mouth.

That is the part I would want to understand if I were looking at this from your side. Not whether the technology works, the treatment record answers that, but why demand keeps arriving on its own.

The short version: vitamin D runs low in most people who work indoors, the fix everyone reaches for is a supplement, and about one in four participants in research clinical trials were low responders to it.

We built a device that opens the pathway the supplement cannot, in two to four minutes.

Fifteen minutes and I will show you the rest.

CALENDAR LINK

Looking forward to connecting.

{{custom_values.standard_signature}}
```

**Links:** `CALENDAR LINK` -> **Investor Intro**

---

## Touch 2 | Day 3 | Internal Notification, LinkedIn connection

**Subject:** `ACTION REQUIRED: LinkedIn Connect: {{contact.first_name}} {{contact.last_name}}`

**Body:**

```
Investor drip Day 3 action required.

Send a LinkedIn connection request to {{contact.first_name}} {{contact.last_name}} now.

Connection note to use:
"Hi {{contact.first_name}}, I saw your background in health tech and wanted to connect. We are building something at the intersection of health technology and wellness that I think would be right up your alley."

Contact details:
- Company: {{contact.company_name}}
- Email: {{contact.email}}
- Phone: {{contact.phone}}
View contact in GHL: {{contact.link}}
```

**Note:** swap "health tech" per contact as you send. The original read `health tech / wellness / investing`, which was a reminder to choose but was written as the text to paste.

---

## Touch 3 | Day 6 | Email

**Subject:** The traction that made us confident enough to raise

**Body:**

```
Hi {{contact.first_name}},

Before I share any details about our current offering, I want to let the numbers speak.

600+ users.

25,000+ treatments completed.

Zero adverse events across every single session.

Under 1 percent return rate, versus an industry average of 5 to 10 percent.

Five countries, all inbound, zero paid advertising.

OEM pipeline with one signed white-label partner already launched.

This is what organic, word-of-mouth growth looks like when the product actually works.

If you'd like to see the executive summary, I'm happy to send it over.

{{custom_values.standard_signature}}
```

**Checked:** every figure matches the KB. The white-label partner reference is Lumanova, executed.

---

## Touch 4 | Day 10 | Internal Notification, call

**Subject:** `ACTION REQUIRED: Call {{contact.first_name}} {{contact.last_name}} Today`

**Body:**

```
Investor drip Day 10 action required.

Call {{contact.first_name}} {{contact.last_name}} now and leave voicemail if no answer.

Voicemail script:
"Hi {{contact.first_name}}, Scott Hansbury from Enyrgy. I've been reaching out because we have a small number of investment conversations open with health-tech-focused investors and I wanted to see if there's a fit. Would love 15 minutes whenever it works. I'll send an email right after this."

Then send a follow-up email immediately after the call with the calendar booking link.

Contact details:
Company: {{contact.company_name}}
Email: {{contact.email}}
Phone: {{contact.phone}}
View contact in GHL: {{contact.link}}
```

---

## Touch 5 | Day 14 | Email

**Subject:** The team behind Enyrgy

**Body:**

```
Hi {{contact.first_name}},

Investors invest in people first. Here's who is behind Enyrgy.

Scott Hansbury, Co-Founder & CEO
8 startups, 5 exits, $500M+ in value created.

David Letourneau, Co-Founder & President
Scaled Alair Homes from 1 to 100+ locations, $750M+ in sales.

Brian Cameron, CFO
Fractional CFO to public and private companies. Sources and closes our channel relationships directly, and brought us the YourTango partnership.

Our Scientific Advisory Board:

Dr. Bruce Hollis, over 70,000 citations. Widely regarded as the Godfather of Vitamin D Research.

Dr. Samantha Kimball, designer of our MED protocol. Leading researcher in UV therapy safety.

Dr. William Grant, NASA UVB researcher. Pioneer in phototherapy science.

This is the team that built 25,000+ treatments with zero adverse events.

I'd love to show you what we're building next.

CALENDAR LINK

{{custom_values.standard_signature}}
```

**Links:** `CALENDAR LINK` -> **Investor Intro**

---

## Touch 6 | Day 18 | Email

**Subject:** No accreditation needed to review the offering.

**Body:**

```
Hi {{contact.first_name}},

Quick clarification on process, because I want to make this easy, not bureaucratic.

You do not need to be verified as accredited to review our offering. Accreditation matters at exactly one point, before any funds move. So the only step required before you could actually invest is confirming your accredited status, and it takes about 2 minutes.

You are welcome to complete it now so the runway is clear later, or wait until you have seen everything. No pressure either way.

ACCREDITATION FORM LINK

And if you would like to go through the specifics, structure and terms, let's set up a quick call and I will walk you through it.

Looking forward to the next step.

{{custom_values.standard_signature}}
```

**Links:** `ACCREDITATION FORM LINK` -> **Accreditation form**

**COMPLIANCE, VERIFIED CORRECT.** This email matches the attorney-confirmed rule exactly: accreditation gates only the money-moving actions, wire instructions and accepting investment, and is not required to review the offering or receive the PPM, subscription agreement or term sheet. The Session 13 correction and the Session 14 live-workflow fix both reached this touch. Do not re-gate it.

---

## Touch 7 | Day 30 | Email

**Subject:** Closing the loop and leaving the door open

**Body:**

```
Hi {{contact.first_name}},

I've shared everything I can at this stage.

If the timing or fit isn't right for you right now, I completely understand.

I wanted to make sure you'd had a fair shot to evaluate it before I stop reaching out.

Where we stand:

- 600+ users across 5 countries
- 25,000+ treatments, zero adverse events
- Organic, word-of-mouth growth with zero paid advertising

If you have any remaining questions, or if a future round might be a better fit, I'd love to stay connected.

Wishing you and your team continued success.

{{custom_values.standard_signature}}
```

---

# Change log, 2026-08-02

Five corrections applied to the live workflow during capture. The drip was built about two months earlier, and most of what needed changing was drift rather than error.

| # | Touch | Change |
|---|---|---|
| 1 | 7 | Removed "We're closing this round" |
| 2 | 1 | Subject: em dash to colon |
| 3 | 2 | Added a missing subject line; em dash to comma in the connection note; resolved the `health tech / wellness / investing` placeholder |
| 4 | 4 | Added the missing `View contact in GHL` line |
| 5 | 5 | Added Brian Cameron, CFO. Corrected the Hollis bio to the KB-approved wording |

## Why change 1 mattered most

Touch 7 told prospective investors the round was closing. Two days before capture, the Q2 2026 update told 57 current investors: *"The raise is going slower than we would like, and we need at least $100K by end of August."*

Two statements about the same offering, days apart, contradicting each other, with the drip version set to keep sending automatically to every new `type_investor` contact. In ordinary marketing that is a sloppy urgency line. In securities communications it is an inconsistency in what has been represented about the offering.

The replacement keeps the closing-the-loop framing, which is a final touch's actual job, and makes no claim about the round's status.

## Why change 5 mattered

The email opens "Investors invest in people first" and then showed a company with no CFO. Brian Cameron has been in the role for months and featured prominently in the Q2 update sent two days earlier, so an investor receiving both documents would see a CFO in one and not the other.

## Open, not changed

**Voice inconsistency.** This drip uses contractions throughout ("I'm reaching out", "we're building", "I'd love"). The Consumer, Commercial and Partner drips do not, and neither does the Q2 investor update. An investor on this drip may also receive the quarterly update, so the same person gets two documents in different registers. Cosmetic, and a find-and-replace rather than a rewrite, but recorded so the choice is deliberate.

**Optional team additions.** Millie Carrillo, Shanna Schuckman and Thea Cartier all appeared in the Q2 update as team additions and are absent from touch 5. Left out because the email's shape is founders plus advisors, and three commercial hires would change it.
