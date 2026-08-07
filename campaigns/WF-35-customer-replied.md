# WF-35 Customer Replied Notification

**Trigger:** Customer Replied, **no filters applied**
**Actions:** If/Else on assigned user, then one internal notification per branch
**Built:** 2026-08-03, Session 16
**Status:** LIVE and fully verified Aug 4, 2026. Two known cosmetic issues remain, see the foot of this file.

**Why it exists.** GHL's built-in Conversation Notification is a doorbell, not a message. It says "You have received a new email from {contact}" and nothing else. Proven by test, not assumed: a reply containing the marker `PURPLE-ELEVEN` produced a notification with no trace of that text. This workflow puts the actual reply in the notification.

---

## Structure

```
Customer Replied (no filters, so every inbound channel)
  -> If/Else "Has Assigned User"   (branches evaluated top to bottom, first match wins)
       |- 1. Call or Voicemail  (Replied message  Is empty)      -> Notify Scott, Inbound Call
       |- 2. Has Owner          (Assigned user  Is not empty)    -> Notify Assigned User
       |- 3. None                                                -> Notify Scott, No Owner
```

**Branch order is the design, not a detail.** GHL takes the first matching branch. If `Call or Voicemail` sat second, a call from a contact who happens to have an owner would fall into `Has Owner` and produce the `undefined` notification again, just rarely enough to be hard to spot.

**The condition field is `Replied message`, operator `Is empty`.** A call or voicemail carries no message text and matches; an email or SMS reply does not.

**Calls and voicemails fire this workflow too, and are handled on their own branch (built Aug 7).** With no trigger filter an inbound call triggers Customer Replied, and `{{message.body}}` renders as the literal string `undefined` because there is no message. Four spam voicemails produced four such notifications.

**Fixing it by filtering the call channel out would have been the wrong move, and the reason is worth keeping.** Those useless notifications are the only thing that surfaced a silenced business line swallowing every inbound call. Filtering would have restored exactly the silence that had to be found by accident. So calls stay in scope and get a branch of their own instead.

**No trigger filter, deliberately.** Unfiltered the trigger covers email, SMS, and any Facebook, Instagram or GMB channel connected later. Every channel a filter excludes becomes a silent loss path, which is the exact failure this workflow was built to end. The July testimonial that went missing was an SMS, so SMS is a proven loss path and not a hypothetical one.

**`Is not empty` rather than naming a user.** Branch 1 follows whoever owns the contact, so when a second sender is added nothing here needs editing. Naming a user works today and breaks silently the first time someone else sends.

---

## Branch 2, Has Owner | Internal Notification

**To User Type:** Assigned owners -> Contact owner
**Subject:** `Reply from {{contact.first_name}} {{contact.last_name}}`

```
{{contact.first_name}} {{contact.last_name}} replied.

Email: {{contact.email}}
Phone: {{contact.phone}}

Open the conversation to answer: {{contact.link}}
Replying to this notification does not reach them.

------- their message -------

{{message.body}}
```

**The link sits directly above the warning on purpose.** "Replying does not reach them" is a dead end on its own. With the link above it, the sentence says where to go instead of only what not to do.

## Branch 1, Call or Voicemail | Internal Notification

**Condition:** `Replied message` `Is empty`
**To User Type:** Particular user -> Scott Hansbury
**Subject:** `Inbound call: {{contact.phone}}`

```
An inbound call was logged on the business line.

Phone: {{contact.phone}}
Name: {{contact.first_name}} {{contact.last_name}}
Email: {{contact.email}}

If you did not take it, there is likely a voicemail waiting.

Open the conversation: {{contact.link}}
Replying to this notification does not reach them.
```

**It says "was logged", not "went to voicemail".** Customer Replied fires on the call event whether or not the call was answered, so asserting voicemail would sometimes be wrong.

**Notifying Scott rather than the assigned owner is deliberate for v1.** The line is named "Scott's number" in GHL and calls to it are his. When a second sender is added this becomes a nested branch.

## Branch 3, None | Internal Notification

**To User Type:** Particular user -> Scott Hansbury
**Subject:** `NO OWNER: Reply from {{contact.first_name}} {{contact.last_name}}`

```
{{contact.first_name}} {{contact.last_name}} replied, and no user is assigned to this contact.

Email: {{contact.email}}
Phone: {{contact.phone}}

Replying to this notification does not reach them.

------- their message -------

{{message.body}}
```

**The `NO OWNER:` prefix earns its place.** Those are the replies nobody is watching, and they should be distinguishable in an inbox at a glance.

**The metadata sits above `{{message.body}}` on purpose.** That field returns the entire raw email including signature and any corporate legal footer, which is unbounded. Anything placed below it gets pushed off the screen. In the first live test the reply arrived carrying a full virus-and-confidentiality disclaimer that buried every line beneath it.

**The line about replying is not boilerplate.** It documents a real trap, see below.

---

# What the build proved

**`{{message.body}}` resolves.** This was the open risk, since the field only exists in the Customer Replied context and had no precedent in the account. Confirmed live.

**The reply path on GHL's built-in notification is a trap, not just a dead end.** The notification is sent as though it came from Scott, so hitting reply addresses `scott@mg.enyrgy.com`, which is Scott's own address on the sending subdomain. It does not reach the contact and nothing errors. Someone would type an answer, send it, and watch it disappear while the client showed a normal sent message. This is exactly the mistake a new sender makes in their first week, which is why the warning is in the copy rather than in a runbook.

**GHL validates merge fields on save, and the editor is what breaks `{{contact.link}}`, not the field.** Resolved Aug 4. The field is valid: WF-02's Day 1 notification uses it and saves clean. What fails is the rich-text editor auto-converting it to a hyperlink when you press space or Enter straight after the closing braces, which wraps the merge field in an `<a>` tag and trips the validator.

**To insert it:** type the line, then click elsewhere in the box rather than pressing space or Enter. Or use the `</>` source view, where nothing is auto-formatted. Black text means it went in clean; blue and underlined means unlink it and try again.

---

# Known issues

**1. There is an unsubscribe link on an internal notification.** "If you no longer wish to receive these emails you may unsubscribe" is appended to a notification going to staff. If Scott or any future sender clicks it, that address may be marked unsubscribed and **reply notifications would stop silently**, presenting as the exact problem this workflow was built to fix. Do not click it. Whether it can be suppressed at the location email-footer level is unresolved.

**2. `{{message.body}}` returns the full raw email.** Signature, quoted history and legal disclaimers all come through. Mitigated by ordering, not solved. GHL exposes no stripped version.

**3. RESOLVED Aug 4: Allow Re-Entry is ON.** Verified by replying twice from the same contact with different markers. Both produced their own enrollment row and their own notification. Had it been off, only a contact's first ever reply would notify anyone, with the workflow appearing to work correctly.

---

# Test log, 2026-08-03

| Time | Event | Result |
|---|---|---|
| 6:59 PM | Reply to a GHL-sent email, built-in notification only | No message body. Marker `PURPLE-ELEVEN` absent. Reply-To pointed at `scott@mg.enyrgy.com`. |
| 8:17 PM | Same test with WF-35 live | `NO OWNER: Reply from ZZ Test` delivered with the message body present. Correct branch, since the test contact had no owner. |
| Aug 4, 7:01 AM | Reply from the contact's own Gmail | Enrolled 7:13:31, `Notify Scott, No Owner`, Finished. Notification carried `ORANGE-SEVEN`. |
| Aug 4, ~7:20 AM | Second reply, same contact, same thread | Second enrollment, second notification carrying `BLUE-TWELVE`. **Allow Re-Entry confirmed.** |
| Aug 7, AM | Four inbound spam voicemails, before the call branch existed | Four notifications reading `NO OWNER: Reply from` with an empty name and `undefined` as the body. Led to the call branch and, indirectly, to the silenced-business-line finding. |
| Aug 7, PM | Live call to 888-316-1695 from Scott's mobile, allowed to reach voicemail | Phone rang showing 888-316-1695, and the notification arrived as `Inbound call:` with the number populated. **Confirms both the branch order and the caller-ID fix in one test.** |

**Two false alarms during testing, both worth knowing about because both looked like workflow failures and neither was.**

**The workflow appeared not to fire, and had.** The inbox was checked at 7:12 and the enrollment ran at 7:13:31. GHL's inbound processing carried a **12-minute lag** between the reply being sent and the trigger firing, so the built-in notification arrived first and looked like the only one. The second round had no such lag, both landing at 7:21, so 12 minutes is an outlier rather than a floor. Wait a full fifteen minutes before concluding a reply did not register.

**GHL tagged the inbound reply `FORWARDED EMAIL` and it made no difference.** The enrollment reason still reads "customer Replied". The display classification and the trigger classification are separate; do not chase that tag as a cause.

**A third false alarm came from the test setup, not the system.** A first attempt used a mistyped Gmail address, which hard-bounced, so nothing was ever received and the "reply" was actually a forward from Scott's own mailbox. Always confirm the outbound email physically arrives before treating anything downstream as a result.

**On `{{message.body}}` noise:** the Aug 3 test arrived carrying a full corporate virus-and-confidentiality disclaimer; the Aug 4 tests from a plain Gmail account arrived clean. The field is only as noisy as the sender's signature, and the metadata-above-message ordering is what makes the bad cases readable.

**Both notifications fire on every reply**, the bare built-in one and this one. **Recommended: switch the built-in from Email to In-App rather than disabling it.** WF-35 triggers on Customer Replied, and every test was a genuine reply to an outbound message. A **cold inbound from someone never emailed first is untested** and may not register as a reply. Keeping In-App on costs nothing, ends the inbox duplication, and leaves a bell that would catch anything WF-35 misses.
