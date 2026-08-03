# WF-07 Review and Referral Activation

**Trigger:** Contact Tag `unit_activated`
**Touches:** 3, at Days 14, 21 and 28
**Audience:** customers a few weeks into using the device
**Captured:** 2026-08-03, complete.

**No copy changes were needed.** First workflow of fourteen to come through clean. What it did surface was two stale entries in the documentation, both corrected the same day.

---

## Touch 1 | Day 14 | Email

**Subject:** A few weeks in. How are you feeling?

**Body:**

```
{{contact.first_name}},

It has been a few weeks since your Enyrgy Vitamin D Primal Light Platform arrived, and I wanted to check in personally.

How are you feeling? Noticing anything in your sleep, mood, or energy?

If you have a minute, I would love to hear how it is going. Your experience, in your own words, helps the next person who found us the same way you did, unsure whether it would do anything.

Share your experience here

Whatever you write, thank you for being part of this.

{{custom_values.standard_signature}}
```

**Links:** `Share your experience here` -> **Customer Testimonial form**

**The best testimonial ask in the account.** It asks how they are before it asks for anything, and gives a reason that is about the next customer rather than about Enyrgy. "Whatever you write" keeps it off any positivity gate, which is the FTC exposure that matters when a gift card is attached downstream in WF-26.

---

## Touch 2 | Day 21 | SMS

**Action name in GHL:** Review Request

**Body:**

```
Hi {{contact.first_name}}, this is Scott from Enyrgy. Would you take 2 minutes to leave an honest review of your Enyrgy Vitamin D Primal Light Platform? Google: https://g.page/r/CfN5Rj0CdmrfEAI/review or Trustpilot: https://www.trustpilot.com/evaluate/enyrgy.com Reply STOP to opt out. Msg & data rates may apply.
```

**FTC-clean.** "An honest review", both platforms offered, no positivity gate, no incentive attached to a favourable outcome. Carries the STOP opt-out and rate disclosure.

---

## Touch 3 | Day 28 | Email

**Subject:** Share Enyrgy and save: our referral program

**Body:**

```
{{contact.first_name}},

If the Enyrgy Vitamin D Primal Light Platform has earned a spot in your routine, there is a good chance someone you know would want in too. Here is how the referral works.

You share your referral link. When someone buys through it, they get $150 off, and $100 in credit lands with you toward accessories or a future purchase.

Send it to whoever comes to mind. Want your link? Reply here or email contact@enyrgy.com and we will set it up for you.

Thanks for helping the right people find us.

{{custom_values.standard_signature}}
```

**Checked:** $150 off the referee and $100 credit to the referrer match KB Section 3 exactly.

**How this actually works, which the docs had wrong.** The referral program is **live and operating manually**. A customer asks, and a **custom Shopify discount code specific to that user** is created by hand. The Master TODO previously described WF-07's referral link as "an intentional placeholder", which was incorrect and would have led someone to pause a working email. Corrected 2026-08-03.

What waits on the built-in loyalty program in the next app version is the **automation**, not the offer.

---

# Findings, 2026-08-03

No copy changes. Two documentation corrections and one addition.

| Where | Correction |
|---|---|
| Master TODO | "WF-07's referral link stays an intentional placeholder" was wrong. The program runs manually via per-customer Shopify discount codes |
| KB Section 3 | Referral entry now records the manual mechanism, so agents know the offer is live and quotable |
| KB Section 3 | `contact@enyrgy.com` added. Monitored and used across the funnel but recorded nowhere, so agents had no way to know it was safe to give out |

## Why the stale TODO entry mattered

It did not break anything today. It would have broken something later.

A future session reading "intentional placeholder" next to a live email offering a referral link would reasonably conclude the email was promising something undeliverable, and either pause it or rewrite it to remove the offer. That would have taken a working referral channel offline to fix a problem that did not exist.

**Same shape as the accreditation gate in the Investor Warm drip and the guarantee coupling across four nurtures**, in reverse: there the documentation said fixed and the copy was wrong; here the copy was right and the documentation said broken. Both directions cost the same thing, which is trust in the docs.

## Three things that were checked and were fine

**The two Day-21 asks.** Initially read as a review request and a referral request landing the same day. Touch 3 is Day 28. No stacking.

**`contact@enyrgy.com`.** Monitored, and used in many places.

**The testimonial and review asks against FTC rules.** Touch 1 invites "whatever you write". Touch 2 asks for "an honest review" and offers both platforms. Neither gates on positivity, which is what the Session 14 audit corrected in WF-25 and WF-26 and what matters once a gift card enters the flow.
