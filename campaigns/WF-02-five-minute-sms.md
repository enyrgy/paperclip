# WF-02 Five Minute First Response

**Trigger:** consumer lead routed by WF-01 New Lead Router
**Touches:** 1 SMS at 5 minutes, 1 internal notification at Day 1
**Consent:** gated. The workflow checks `sms_consent_given` **before** the SMS action.
**Captured:** 2026-08-03, complete, with one correction applied.

**This is the first thing a consumer lead ever hears from Enyrgy**, and it arrives before any human has seen them.

---

## Touch 1 | 5 minutes | SMS

**Action name in GHL:** 5 Minute First Response SMS

**Body:** (line breaks as they exist in GHL)

```
Hi {{contact.first_name}}, this is Scott from Enyrgy. Most
people find us because they are tired of doing everything right and still not feeling their best. You are in the right place. Check your email, I am sending you something that might finally explain why. Reply STOP to opt out. Msg & data rates may apply.
```

**No changes needed.** Three segments. Carries the STOP opt-out and rate disclosure. Makes no claim requiring KB backing, which is right for a first contact.

**The consent gate is the thing to protect here.** A five-minute SMS to someone who never opted in, on a toll-free number, is real TCPA exposure. WF-12 previously carried `sms_consent_given` in its always-on tag list, so every Tired Test lead was marked as an opt-in whether or not they ticked the box or supplied a phone number. That was fixed in Session 15. **The fix only works because WF-02 checks the tag rather than assuming it.** If anyone ever simplifies this workflow, the condition is the part that must not go.

**Worth knowing about the email reference.** "Check your email, I am sending you something" is true for lead-magnet leads, since WF-12, 15, 18, 19 and 21 all send their guide or results email at capture. For a consumer lead arriving another way, the Consumer Drip's first email is Day 1, so the text points at an inbox that stays empty for up to a day. Fine if magnets carry the bulk of consumer volume, which they currently do.

---

## Touch 2 | Day 1 | Internal Notification

**Subject:** `New Consumer Lead: {{contact.first_name}} {{contact.last_name}}`

**Body:**

```
A new consumer lead has entered the pipeline and received their first SMS response.

Contact details:

Name: {{contact.first_name}} {{contact.last_name}}

Email: {{contact.email}}

Phone: {{contact.phone}}

Source: {{contact.source}}

How Heard: {{contact.how_heard_specific}}

If they arrived through a lead magnet they carry drip_bypass and are in that magnet's nurture rather than the Consumer Drip. If not, the Consumer Drip is running. Monitor for engagement and be ready to take over when lead score reaches 70.

View contact in GHL: {{contact.link}}
```

**CORRECTED Aug 3.** The enrolment line. See the change log.

---

# Change log, 2026-08-03

| # | Where | Change |
|---|---|---|
| 1 | Internal notification | "They have been automatically enrolled in the Consumer Drip Campaign" replaced with the branch-aware version |

## Why the enrolment line was wrong for most leads

The Consumer Drip opens with a **Bypass Check**: contacts carrying `drip_bypass` end immediately. Every lead-magnet capture workflow applies `drip_bypass` at capture, deliberately, so magnet leads run their purpose-built nurture instead of the general drip.

The notification told Scott the Consumer Drip was running. For the bulk of consumer volume it had exited at step one.

**This matters because of what the notification is for.** It exists so a lead can be assessed without opening GHL. If it reports a sequence that is not running, there is no reason to check whether anything is nurturing that person at all. The failure is silent in both directions: nothing errors, and the notification looks correct.

Now it states the rule rather than a conclusion, so it stays accurate whichever path the lead took.

## Checked and correct

**Consent gating.** The SMS is behind an `sms_consent_given` check.

**The subject line.** `New Consumer Lead: {{first}} {{last}}`, informational rather than ACTION REQUIRED, which keeps that prefix meaningful for notifications that genuinely need a response.

**The SMS copy.** Nothing to change. "Tired of doing everything right and still not feeling their best" is the right opening line for a stranger, and it makes no claim at all, which is correct for a message arriving five minutes after a form submission.
