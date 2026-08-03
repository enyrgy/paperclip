# WF-21 Vitamin D Assessment Capture

**Trigger:** Inbound Webhook from the Vitamin D Assessment page (`go.enyrgy.com/vitamin-d-assessment`)
**Touches:** 1 email, the assessment results email, sent Day 1
**Also does:** creates the contact with 11 mapped fields, applies six always-on tags via a Standard Add Tag and the page's conditional tags via a Dynamic Add Tag, and writes Deficiency Risk Score and Deficiency Risk Band
**Hands to:** WF-22 Vitamin D Assessment Nurture
**Captured:** 2026-08-03, with two corrections applied.

---

## Touch 1 | Day 1 | Email

**Subject:** Your vitamin D assessment

**Body:**

```
{{contact.first_name}}

You just answered a few honest questions about your light, your skin, and your labs. Here is what they add up to.

Your deficiency risk came out {{inboundWebhookRequest.deficiency_risk_band}}. That is based on how much real daylight you actually get, your skin type, and what your labs have been telling you.

Your body was built to make vitamin D from light on skin, not from a capsule in your gut. When you come up short on the light, a supplement can only carry part of the load, and the rest of what sunlight does never happens.

Here is the part almost nobody knows. A supplement can feed one road to nitric oxide, the enzyme road. Light opens a second road a pill cannot reach, releasing the nitric oxide your skin has already stored. That road is pure upside. The same few minutes of the right light also drive vitamin D and serotonin. One session, three pathways.

We ran a small 12-week study on the platform that does this. Five people, four to six sessions a week. Average vitamin D went from 39.96 to 84.20 ng/mL, and every one of them reached optimal. Small study, real labs, zero adverse events.

If you want to see how it works and what it would take to close your own gap, start here:
The Enyrgy Platform

Still have questions? Grab a quick call:
Book a call

Prefer to talk it through first? Reply to this email. A real person reads it.

{{custom_values.standard_signature}}
```

**Links:** `The Enyrgy Platform` -> order page. `Book a call` -> **Consumer Discovery**

**CORRECTED Aug 3, twice.** The risk band added, "no pressure" removed. See the change log.

**Checked:** the nitric oxide framing is correct. It grants that a supplement feeds the enzymatic road, then confines the claim to photorelease from preformed skin stores, which is what the KB rule requires. The study is disclosed as five people with "small study" stated.

**Why `inboundWebhookRequest` rather than `contact`.** The payload reference is readable the instant the workflow fires. A `contact.` reference depends on the field write having completed, which is the race condition that broke FlexOffers refid capture and forced the WF-31 rebuild. In a workflow triggered by the webhook itself, always prefer the payload.

---

# Change log, 2026-08-03

| # | Change |
|---|---|
| 1 | Added the reader's Deficiency Risk Band. The email promised a result and never gave one |
| 2 | Removed "no pressure", a Never-list phrase |

## The results email had no results

It opened "Here is what they add up to" and then delivered identical text to everyone, regardless of what they answered.

**The data was already there.** WF-21 writes Deficiency Risk Score and Deficiency Risk Band at capture. Both were sitting unused while the email made a promise it did not keep.

Someone who has just completed an assessment and been told they are about to see their result instead receives a brochure. That gap between the subject line and the body is the widest in the funnel, and it was one merge field away from closing.

## Worth considering, not done

With the band now available in the email, the copy could branch on it. A high-risk reader and a low-risk reader need different next sentences and currently get the same one. That is a bigger change than a merge field, so this was done first to see whether it is enough.

## Minor, left alone

The greeting is `{{contact.first_name}}` with no comma. Every other email in the funnel uses a comma or "Hi". It is the first line the reader sees.
