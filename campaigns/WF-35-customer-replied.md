# WF-35 Customer Replied Notification

**Trigger:** Customer Replied, **no filters applied**
**Actions:** If/Else on assigned user, then one internal notification per branch
**Built:** 2026-08-03, Session 16
**Status:** LIVE, with two known issues and one unverified setting. See the foot of this file.

**Why it exists.** GHL's built-in Conversation Notification is a doorbell, not a message. It says "You have received a new email from {contact}" and nothing else. Proven by test, not assumed: a reply containing the marker `PURPLE-ELEVEN` produced a notification with no trace of that text. This workflow puts the actual reply in the notification.

---

## Structure

```
Customer Replied (no filters, so every inbound channel)
  -> If/Else "Has Assigned User"
       |- Has Owner (Assigned user  Is not empty)  -> Notify Assigned User
       |- None                                     -> Notify Scott, No Owner
```

**No trigger filter, deliberately.** Unfiltered the trigger covers email, SMS, and any Facebook, Instagram or GMB channel connected later. Every channel a filter excludes becomes a silent loss path, which is the exact failure this workflow was built to end. The July testimonial that went missing was an SMS, so SMS is a proven loss path and not a hypothetical one.

**`Is not empty` rather than naming a user.** Branch 1 follows whoever owns the contact, so when a second sender is added nothing here needs editing. Naming a user works today and breaks silently the first time someone else sends.

---

## Branch 1, Has Owner | Internal Notification

**To User Type:** Assigned owners -> Contact owner
**Subject:** `Reply from {{contact.first_name}} {{contact.last_name}}`

```
{{contact.first_name}} {{contact.last_name}} replied.

Email: {{contact.email}}
Phone: {{contact.phone}}

Replying to this notification does not reach them.

------- their message -------

{{message.body}}
```

## Branch 2, None | Internal Notification

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

**GHL validates merge fields on save, and `{{contact.link}}` fails validation.** The editor also auto-converts it to a hyperlink, which may be the cause. **WF-02's Day 1 internal notification carries the same field**, so its "View contact in GHL" line may have been rendering blank or literal in every consumer-lead notification. Unchecked as of this writing.

---

# Known issues

**1. There is an unsubscribe link on an internal notification.** "If you no longer wish to receive these emails you may unsubscribe" is appended to a notification going to staff. If Scott or any future sender clicks it, that address may be marked unsubscribed and **reply notifications would stop silently**, presenting as the exact problem this workflow was built to fix. Do not click it. Whether it can be suppressed at the location email-footer level is unresolved.

**2. `{{message.body}}` returns the full raw email.** Signature, quoted history and legal disclaimers all come through. Mitigated by ordering, not solved. GHL exposes no stripped version.

**3. UNVERIFIED: Allow Re-Entry.** The second-reply test was not run. If the setting is off, **only a contact's first ever reply notifies anyone** and every reply after it is silent, with the workflow appearing to work correctly. Run this before trusting the workflow: reply twice from the same contact with different markers and confirm two notifications arrive.

---

# Test log, 2026-08-03

| Time | Event | Result |
|---|---|---|
| 6:59 PM | Reply to a GHL-sent email, built-in notification only | No message body. Marker `PURPLE-ELEVEN` absent. Reply-To pointed at `scott@mg.enyrgy.com`. |
| 8:17 PM | Same test with WF-35 live | `NO OWNER: Reply from ZZ Test` delivered with the message body present. Correct branch, since the test contact had no owner. |
| pending | Second reply from the same contact | **NOT RUN.** This is what verifies Allow Re-Entry. |

**Both notifications now fire on every reply**, the bare built-in one and this one. Leave the duplication in place until WF-35 has been proven across several real replies. The built-in Conversation Notification can be turned off after that.
