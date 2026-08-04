# WF-02 Five Minute First Response

**Trigger:** `Consumer Tag Applied`, Tag Added includes `type_consumer` (applied by WF-01 New Lead Router)

**Live structure, read off the canvas Aug 4, 2026:**

```
Consumer Tag Applied (type_consumer)
  -> Condition
       |- Not Bypassed - Send Drip   (Tags does not include drip_bypass
       |                              AND SMS Consent Is not empty)
       |    -> Wait 5 Minutes -> 5 Minute First Response SMS
       |    -> Wait 1 Day -> Alert Team, New Consumer Lead -> END
       |- None -> END
```

**OPEN ISSUE: the internal alert is behind both conditions.** A lead carrying `drip_bypass`, which every lead-magnet capture applies deliberately, ends at the first condition. So does any lead without SMS consent. Neither generates an internal notification, and an internal email has no business depending on either. See the foot of this file.
**Touches:** 1 SMS at 5 minutes, 1 internal notification at Day 1
**Consent:** gated, but **not** by the `sms_consent_given` tag. The gate is a **custom field named `SMS Consent`**, a checkbox, tested with `Is not empty`. Unchecked leaves the field empty, so `Is not empty` is a genuine affirmative test rather than a loose one. Verified against the live workflow Aug 4, 2026.
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

**The consent gate is the thing to protect here.** A five-minute SMS to someone who never opted in, on a toll-free number, is real TCPA exposure, and statutory damages run per message. WF-12 previously carried `sms_consent_given` in its always-on tag list, so every Tired Test lead was marked as an opt-in whether or not they ticked the box or supplied a phone number. That was fixed in Session 15. **If anyone ever simplifies this workflow, the `SMS Consent` condition is the part that must not go.**

**Read the operator before assuming the gate is loose.** `Is not empty` looks weaker than an affirmative test and is not. It only holds because the field is a checkbox, which writes nothing when unticked. Were it ever changed to a dropdown or text field that stores `No`, the same condition would pass for someone who declined and the gate would fail silently while still appearing to be there.

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

**Consent gating.** The SMS is behind an `SMS Consent` custom-field check. See the note above on why the `Is not empty` operator is sound here.

**The subject line.** `New Consumer Lead: {{first}} {{last}}`, informational rather than ACTION REQUIRED, which keeps that prefix meaningful for notifications that genuinely need a response.

**The SMS copy.** Nothing to change. "Tired of doing everything right and still not feeling their best" is the right opening line for a stranger, and it makes no claim at all, which is correct for a message arriving five minutes after a form submission.

---

# OPEN, found Aug 4, 2026: the bypass gate is in the wrong workflow

**How it surfaced.** Scott had never received a single "New Consumer Lead" email. Enrollment History showed roughly thirty enrollments since July 17, almost all with Current Action "No Action" and status Finished: enrolled, hit the condition, exited, no actions run.

**`drip_bypass` exists to keep magnet leads out of the general Consumer Drip**, and the Consumer Drip enforces that itself at its own Bypass Check, independently. **WF-02 enrols nobody in anything.** The branch is named "Not Bypassed - Send Drip" but contains no drip action, which is probably how the gate ended up here: the name describes a job this workflow does not do.

**The contradiction that makes it clear.** The SMS reads "Check your email, I am sending you something that might finally explain why." That is only true for someone who just requested a guide, since WF-12, 15, 18, 19 and 21 all send theirs at capture. **The message is aimed precisely at the audience the gate excludes.** For a general consumer lead the first email is Day 1, so the line points at an empty inbox.

**And the notification corrected on Aug 3 can never reach the people it describes.** Its body now reads "If they arrived through a lead magnet they carry drip_bypass and are in that magnet's nurture rather than the Consumer Drip." A `drip_bypass` lead cannot receive that sentence. The wording of a notification was fixed for a case in which it never fires.

**Proposed:**

```
Consumer Tag Applied (type_consumer)
  -> Condition "Has SMS Consent"
       |- Has Consent (SMS Consent Is not empty)
       |    -> Wait 5 Minutes -> SMS -> Wait 1 Day -> Alert Team
       |- None
            -> Wait 1 Day -> Alert Team
```

`drip_bypass` comes out of WF-02 entirely. Consent gates the SMS and only the SMS. The alert fires for every consumer lead, on both paths, which is the whole reason it exists.

**Awaiting Scott's decision**, because removing `drip_bypass` means magnet leads start receiving the 5-minute SMS where they have consented. The conservative alternative is to keep the SMS gated on `drip_bypass` and move only the alert.

**Not urgent in the way it first appeared.** Scott is BCC'd on all outbound drip email, so these leads were never invisible and are still in their nurture. What is missing is the consolidated alert: source, how_heard_specific, phone, email and a link, in one message at one time. That is a convenience gap, not lost leads.
