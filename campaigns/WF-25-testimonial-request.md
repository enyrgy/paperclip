# WF-25 Testimonial Request

**Trigger:** Contact Tag `request_testimonial`, applied by hand to a chosen segment. **Not auto-enrolled.**
**Touches:** 1 email, with an If/Else on `seg_facility` routing facility operators and consumers to different versions
**Allow Re-Entry:** Off
**Captured:** 2026-08-03, complete, with two corrections applied.

**Recipients are hand-picked.** Nothing enrols into this workflow automatically. You add `request_testimonial` to the contacts you choose.

**The first batch has already gone out: 15 contacts on Jul 20, 2026, before the Aug 3 correction.** See "The Jul 20 batch" below. Any note elsewhere in the docs saying the first testimonial batch has not happened yet is out of date.

---

## Touch 1, Facility branch | Day 1 | Email

**Condition:** `seg_facility` present

**Subject:** 60 seconds, operator to operator

**Body:**

```
Hi {{contact.first_name}},

Quick ask, one operator to another.

You have had the Enyrgy Vitamin D Primal Light Platform running for your clients for a while now, and I would love to capture how it has gone, for you and for them, in your own words.

The best thing you could send is a short phone video, 30 to 60 seconds, no script, no production, talking the way you would to another owner asking whether it is worth adding. If video is not convenient, a couple of lines typed in a reply work just as well. Either one helps.

A few starters if they help, video or written, pick any:
- Why you brought Enyrgy in, and what your clients say about it
- How it fits into your day and alongside your other modalities
- What setup and support with our team was like
- Whether you would tell another operator to do it

Easiest way to send either one is here: Upload Here. Video or typed note, both go to the same place.

If you would rather just hit reply, that works too and I will pick it up myself.

Why I am asking: other owners weighing this trust a peer who runs a real business far more than they trust a pitch from me. Your honest take could be the thing that tips someone like you off the fence. If you are okay with me sharing what you send with other operators, just say so, and I will always check with you before using your name or video anywhere public.

Grateful for it, and for you.

{{custom_values.standard_signature}}

P.S. Send yours in, a video or a couple of lines, and I will send a gift card to say thanks, whatever your honest take.
```

**Links:** `Upload Here` -> **Customer Testimonial form**

**CORRECTED Aug 3, three times.** Full product name on first reference, bullets changed from `*` to hyphens, and the send options reordered so the form leads. See the change log.

---

## Touch 1, Consumer branch | Day 1 | Email

**Condition:** none of the above, the default branch

**Subject:** A quick favor?

**Body:**

```
Hi {{contact.first_name}},

I will keep this short. You have been using your Enyrgy Vitamin D Primal Light Platform for a while now, and I would love to hear how it is going, in your own words.

Here is the ask, and I have kept it easy. The best thing you could send is a quick phone video, 30 to 60 seconds, filmed selfie-style, talking like you would to a friend. No script, no lighting, no do-overs. But if video is not your thing, do not overthink it. A line or two typed in a reply is just as welcome. Either one helps.

If you want a nudge on what to say, video or written, pick any of these, or say something else entirely:
- What was going on before Enyrgy, and what feels different now
- How easy it has been to actually use, day to day
- The support you have gotten from our team
- Anything you would tell someone who is on the fence

Easiest way to send either one is here: Upload Video Here. Video or a typed note, both go to the same place.

If you would rather just hit reply, that works too and I will pick it up myself.

Here is why I am asking. The people who need this most trust someone like them far more than they trust me. Your 60 seconds could be the thing that helps a stranger stop guessing about their vitamin D and finally do something about it. If you are okay with me sharing what you send, just say so, and I will always check with you before using your name or video anywhere public.

Thank you, truly.

{{custom_values.standard_signature}}

P.S. Send yours in, a video or a couple of lines, and I will send a gift card to say thanks, whatever your honest take.
```

**Links:** `Upload Video Here` -> **Customer Testimonial form**

**CORRECTED Aug 3, three times.** Same three changes as the facility branch.

---

# The Jul 20 batch, found 2026-08-13

**The reply-path gap described in WF-26 is not hypothetical. It happened, to 15 named people.**

## What the enrollment history shows

15 contacts enrolled on **Jul 20, 2026, between 4:38 and 4:42 pm MST** — a hand-tagged batch. Enrollment reason `Request Testimonial`, current action `Email Consumer`, status `Finished` for all of them. The workflow did exactly what it was built to do. Six visible in the audit screenshot: yasushi takayama, victor allison, tom waite, robert allen, brendan witt, randy stoltz.

**The problem is the date.** The Aug 3 correction that made the form lead postdates this send by two weeks, so all 15 received the *original* copy:

> To send a video, **reply with it** or drop it here if it is large: Upload Here
>
> To send a written note, **just hit reply**.

## The consequence

The Customer Testimonial Form has **one lifetime view** as of Aug 13, 2026. Fifteen people were asked for a testimonial and effectively none were pointed at the tracked path.

WF-26 triggers on Form Submitted, so it has correctly never fired: no `testimonial_submitted`, no `gift_card_pending`, no internal notification, no thank-you, **no gift card** — for anyone who did what the email asked and replied. That email promised a gift card explicitly. Nothing in the system recorded the promise or the response.

## Why it then looked like the workflow was broken

**Allow Re-Entry is Off**, so all 15 are permanently burned. Re-applying `request_testimonial` to any of them does nothing, silently. Re-sending the corrected copy to the original batch is impossible without changing that setting first.

## Remediation

1. **Triage first.** Search the inbox for replies from those 15, Jul 20 onward. This matters more than any workflow fix: someone who recorded a video on request and got three weeks of silence is the worst possible outcome for the group most willing to advocate.
2. **Recover each reply by hand.** Personal reply, apply `testimonial_submitted` and `gift_card_pending`, send the gift card. Read the reply for consent — the form carries the consent capture, replies do not, so each one must be checked individually before anything is published.
3. **Then resend to non-repliers only.** Turn Allow Re-Entry on, re-tag the non-repliers, and turn it back off once the resend clears. Excluding repliers is the point: asking someone a second time for something they already sent compounds the original silence.
4. **At publication**, the gift card is a material connection and must be disclosed. Unchanged by any of the above.

---

# FTC handling, and why this workflow is the reference

This is the workflow where the exposure is real, because a gift card is attached to a testimonial request. Both branches handle it correctly and should be the template for anything similar.

**The incentive is not gated on positivity.** "I will send a gift card to say thanks, **whatever your honest take**." An incentive conditioned on a favourable review is the thing FTC guidance is most direct about, and this explicitly removes the condition.

**Consent is asked twice, at different levels.** First permission to share at all, then a separate promise to check again before using a name or video publicly. Most testimonial requests ask once and treat it as blanket.

**The incentive is disclosed to the person giving the testimonial**, in the same email as the ask.

Both were corrected in the Session 14 audit, and both held. That is the only workflow-level fix from that audit found still intact everywhere it was applied.

## Two operational obligations that sit outside this email

Recorded in the Session 14 notes and still live:

**Disclose the material connection when publishing.** The gift card creates one. The obligation is at publication, not at request, so nothing in this email covers it. Any published testimonial obtained through this workflow needs the disclosure attached.

**Typicality-screen consumer health testimonials.** A testimonial describing an unusual result needs either context or exclusion, since a reader will read it as representative.

**A story that arrives outside this form still needs the same consent capture.** This is the one that actually bit. WF-08 touch 3 features a real customer's lab values, 28 to 84 over twelve weeks, and it went live through a drafting session rather than through this workflow. The consent existed, confirmed Aug 3, 2026, but it existed *because someone remembered to get it*, not because a process required it. A customer's results are a testimonial regardless of which door they came through. Before results go into copy, the written consent goes into the testimonial records.

Neither is a copy problem here. All three are things that happen after a testimonial arrives, which means they depend on whoever handles WF-26's `gift_card_pending` queue knowing about them.

**Verified Aug 3, 2026:** a sweep of all 19 captured workflows found WF-08 touch 3 to be the only place in the funnel where an identified individual's results appear in live copy. Everything else cites the five-participant study in aggregate. That is the intended state; treat a second instance as something that needs consent on file before it ships.

---

# Change log, 2026-08-03

| # | Branch | Change |
|---|---|---|
| 1 | Both | Full product name on first reference, per the KB rule |
| 2 | Both | Prompt list bullets changed from `*` to hyphens |
| 3 | Both | Send options reordered so the form leads and reply is the fallback |

## Why the send options were reordered, which is the change that matters

Both branches originally invited a reply twice and offered the form only for large files:

> To send a video, **reply with it** or drop it here if it is large: Upload Here
>
> To send a written note, **just hit reply**.

**WF-26 triggers on Form Submitted.** So the path being presented as easiest was the one that fires nothing: no `testimonial_submitted`, no `gift_card_pending`, no internal notification, no thank-you, no gift card.

A customer following the instructions exactly, hitting reply with a video, disappeared from the system. From their side, having made a video because you asked, it is indistinguishable from being ignored.

The form now leads for both formats, so most people take the tracked path automatically. Reply stays available, because telling people not to reply costs testimonials.

**"I will pick it up myself" is deliberate.** It is true, a reply genuinely needs a human, and it sets the expectation that the reply route is the personal one rather than the instant one. That covers the gap if a reply-path thank-you arrives a day later than a form-path one.

**Still unfixed by this change:** a reply records no consent, since consent lives on the form. Publishing a reply-path testimonial still means going back to the message to check what was agreed.

## On the product name, for the record

The copy originally said "your Enyrgy platform" in both branches. The KB requires the full name on first reference.

There is a real argument that the rule fits prospect-facing copy better than a post-purchase 1:1, where the full name reads like a form letter and this email's whole job is sounding like a person. Scott chose consistency, so both branches now carry the full name.

Worth knowing the tension exists, because it recurs in WF-26 and WF-08, which also address people who already own the device.
