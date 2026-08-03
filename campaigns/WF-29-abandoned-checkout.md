# WF-29 Abandoned Checkout Recovery

**Trigger:** Inbound Webhook, fired by the Railway service "Enyrgy Abandoned Checkout Sync" which scans Shopify every 20 minutes
**Touches:** 3 emails at Days 1, 2 and 4
**Structure:** Email 1 immediate -> Wait 1 day -> If/Else "Purchased Check" (`status_customer` present -> END) -> Email 2 -> Wait 2 days -> Email 3
**Tags applied at capture:** `abandoned_checkout`, `drip_bypass`, `source_shopify`
**Re-Entry:** On. **Stop on Response:** On.
**Captured:** 2026-08-03, complete, with two corrections applied.

**The Purchased Check matters.** Anyone who completes the order after Email 1 carries `status_customer` and exits before Email 2. Without it, a buyer would keep receiving cart-recovery emails for something already paid for.

**Recovery link:** `{{inboundWebhookRequest.recovery_url}}`, Shopify's own cart-restore URL, passed through by the Railway service. All three emails use it.

---

## Touch 1 | Day 1 | Email

**Subject:** You were one step away, {{contact.first_name}}

**Body:**

```
Hi {{contact.first_name}},

You were right at the finish line on the Enyrgy Vitamin D Primal Light Platform and then stepped away. That is normal. This is a real decision, not an impulse buy.

Your cart is still saved. If you were ready, you can pick up exactly where you left off here:

{{inboundWebhookRequest.recovery_url}}

And if something gave you pause, just reply and tell me what it was. I read these myself.

{{custom_values.standard_signature}}
```

**Note:** "That is normal. This is a real decision, not an impulse buy" is the right opening for a $2,995 cart. It removes the implication that the reader did something wrong, which is what most abandoned-cart copy leads with.

---

## Touch 2 | Day 2 | Email

**Subject:** The two things that usually stop people here

**Body:**

```
Hi {{contact.first_name}},

When people pause at this exact step, it is almost always one of two things. Let me take both off the table.

The first is cost. It is a real investment, which is why you do not have to pay for it all at once. You can finance or rent it so it fits a monthly budget instead of a lump sum, and it is backed by a 30-day money-back guarantee. The decision is not permanent.

The second is whether it will actually work for you. The honest test is your own labs. Check your vitamin D now, use the platform four to five days a week, and check again at eight to twelve weeks. That is long enough for the number to settle rather than just start moving.

Your cart is still here: {{inboundWebhookRequest.recovery_url}}

{{custom_values.standard_signature}}
```

**CORRECTED Aug 3.** Retest interval changed from four weeks to eight to twelve. See the change log.

**Checked:** the study is disclosed as a small study of five with "small study, real numbers" attached. Financing and rental are both described as real options without quoting rates, which matches the KB constraint.

**On the guarantee and the labs:** these do not need decoupling here. The guarantee answers the cost objection in one paragraph and the labs answer the does-it-work objection in the next, so they are separated by topic rather than presented as one timeline. That is why lengthening the retest created no coupling problem.

---

## Touch 3 | Day 4 | Email

**Subject:** Just the honest version

**Body:**

```
Hi {{contact.first_name}},

Last note from me.

You have seen "insufficient" or "low" on a lab report before, or you would not have gotten this far. You can keep topping up with a capsule and keep reading low, or you can close the gap the way your body was built to, through light on skin. That is the whole idea behind the platform.

If now is not the time, that is genuinely fine. If it is, your cart is saved here:
{{inboundWebhookRequest.recovery_url}}

Either way, I appreciate you looking.

{{custom_values.standard_signature}}
```

**CORRECTED Aug 3.** "No pressure" removed from the subject and the opening line. See the change log.

---

# Change log, 2026-08-03

| # | Touch | Change |
|---|---|---|
| 1 | 2 | Retest interval corrected from four weeks to eight to twelve |
| 2 | 3 | "No pressure" removed from the subject and the first line |

## The four-week retest, second instance

WF-22 touch 3 carried the same figure and was corrected earlier the same day. Every other workflow says eight to twelve weeks, and the study itself ran twelve.

Four weeks shows partial movement at best. A reader who follows the instruction exactly tests too early, sees a modest number, and concludes it barely worked.

In both workflows the four-week figure lines up neatly with the 30-day guarantee, which is presumably why it was chosen. In WF-22 that created a real coupling. Here it did not, because the guarantee and the labs sit in separate paragraphs answering separate objections.

## "No pressure" appeared twice in six words

Subject line and opening sentence. It is on the voice spec's Never list, and it was removed from WF-21 and the Investor Drip earlier today.

It also works against itself. Announcing an absence of pressure twice at the top of a final email introduces the idea that there might be some. The email already earns its calm ending with "If now is not the time, that is genuinely fine", which is the same reassurance shown rather than declared.

"Just the honest version" is also a stronger subject. It promises something; "No pressure" only promises the absence of something.

## Corrected during capture, not a copy change

The touches were initially given as Days 1, 12 and 4, which would have sent "Last note from me" on Day 4 and then another email eight days later. Confirmed as a typo: touch 2 is Day 2. The live sequence is 1, 2, 4 and matches the Session 14 structure.

Worth keeping in mind that a twelve-day gap would have been wrong for this workflow regardless of the ordering. Most of an abandoned cart's intent is gone inside 72 hours.
