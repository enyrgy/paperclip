# campaigns/

Version-controlled copy of every GHL campaign email and SMS.

## Why this exists

All drip and nurture copy lived only inside GHL: not version-controlled, not searchable, not reliably recoverable. Account Snapshots capture workflow structure but not email bodies in a diffable form. A bad edit or an accidental workflow deletion loses copy that took a full session to compliance-audit (prohibited words, FTC testimonial rules, the guarantee-versus-lab-timeline decoupling, the light-does-five framing).

It also makes the copy greppable. Two separate questions have already gone unanswered for want of this: "which workflow has the email with subject 'One trigger, three outputs'?" and "what is the subject of WF-26's internal notification?"

## One file per workflow

Named `WF-NN-slug.md`, matching the workflow number in GHL.

## Rules

- **GHL is the source of truth, these files are the backup.** When you change copy in GHL, update the file in the same sitting or the backup silently rots.
- Record the **exact** subject and body, including merge fields such as `{{contact.first_name}}`, not a paraphrase.
- No em dashes, per the standing rule. If GHL contains one, fix it in GHL and record the corrected version.
- Note the delay before each touch and any A/B or conditional split.
- Record SMS touches too, not just email.

## Status

See `_INDEX.md` for what has been captured and what has not.
