# WF-26 Testimonial Received

**Trigger:** Form Submitted, Customer Testimonial Form (`OjahkWeVDeozQkfG9dW2`)
**Actions:** adds `testimonial_submitted`, adds `gift_card_pending`, sends an internal notification to `scott@enyrgy.com`, sends the thank-you email
**Allow Re-Entry:** Off
**Captured:** 2026-08-03, complete, with one correction applied.

**Pairs with WF-25.** WF-25 makes the ask, this handles the response.

---

## Touch 1 | Email, to the customer

**Subject:** Got it, and thank you

**Body:**

```
Hi {{contact.first_name}},

Got it, and thank you.

It means a lot that you took the time. Your honest take is exactly what helps the next person on the fence stop guessing and decide for themselves.

Your gift card will follow within a week.

{{custom_values.standard_signature}}
```

**CORRECTED Aug 3.** Was "Your gift card is on its way." See the change log.

---

## Internal Notification, to scott@enyrgy.com

**Subject:** `New testimonial from {{contact.first_name}} {{contact.last_name}}`

**Body:**

```
{{contact.first_name}} {{contact.last_name}} just submitted the testimonial form. Email: {{contact.email}}. Open their contact record or the form submission to view the video or written note, then send their gift card.
```

**This is the notification that could not be located on 2026-08-02**, when a cryptic message about a testimonial arrived and there was no record anywhere of what its subject line said. Recorded here now. Searching an inbox for "New testimonial from" will find them.

---

# Change log, 2026-08-03

| # | Where | Change |
|---|---|---|
| 1 | Thank-you email | "Your gift card is on its way" became "Your gift card will follow within a week" |

## Why the gift card wording mattered

`gift_card_pending` is a **manual fulfillment queue**, and the Master TODO still lists working that queue weekly as an open item rather than an established routine.

"On its way" told a customer their gift card had already been sent. In practice it sits in a queue until someone runs it. Someone submitting on a Monday would watch for a card that had not been sent, and if the weekly run had not been happening, would still be waiting.

That lands on the customers who liked the product enough to record a video, which is the worst possible group to leave holding an unmet promise.

"Within a week" is a commitment the process can actually meet, and it stops them looking on day one.

**Still worth confirming: is the weekly fulfillment running?** If it has lapsed, there may be people already holding the old promise.

---

# Two structural gaps, neither fixable in the copy

## 1. The email-reply path never fires this workflow

WF-25 originally invited a reply twice in both branches and offered the form only for large files. **Corrected 2026-08-03:** the form now leads for both formats and reply is the stated fallback, so most people take the tracked path.

WF-26 triggers on **Form Submitted**. A testimonial arriving by reply therefore fires nothing: no `testimonial_submitted`, no `gift_card_pending`, no internal notification, no thank-you, and no gift card.

The customer sends a video, hears nothing, and is never paid the thing they were promised. From their side that is indistinguishable from being ignored.

This is not hypothetical. It is the same gap that made a testimonial impossible to locate on 2026-08-02, before that turned out to be a text message about an intention rather than a submission.

**Anything arriving by reply still has to be tagged by hand** to enter the queue. Nothing in the system will prompt it. The WF-25 reorder reduces how often that happens; it does not remove the path.

## 2. Consent is captured on the form, not on the reply path

The Customer Testimonial Form carries the marketing-permission consent, so form submissions have a consent record.

Replies do not. WF-25 asks for permission in prose, so a reply may or may not contain it, and nothing captures it either way. Publishing a reply-path testimonial means going back to the message and checking what the person actually agreed to.

## 3. Two FTC obligations sit downstream of this workflow

Recorded in the Session 14 audit and still live. Neither is a copy problem, and neither is prompted anywhere in the system:

**Disclose the material connection when publishing.** The gift card creates one.

**Typicality-screen consumer health testimonials.** An unusual result needs context or exclusion, because a reader takes it as representative.

Both depend on whoever works the `gift_card_pending` queue knowing they exist. Today that is one person, from memory.
