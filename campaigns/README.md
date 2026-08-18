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

## Hyperlinks

The GHL email editor has **no source view**, so a plain-text copy carries a link's anchor text but not its URL.

Resolved from `_LINKS.md` rather than re-copied by hand. Every URL in the funnel is already recorded in the KB, the handoff's Key URLs section and the Implementation Guide, and was verified against GHL in a dedicated session, so the repo is the authority and there is no need to extract links a second time.

Each email file preserves the anchor text as the reader sees it and notes the resolved target beneath it:

> `... grab a 15-minute call here: Book Call.`
>
> **Links:** `Book Call` -> Consumer Discovery

**The one risk this creates:** if a link is changed in GHL and `_LINKS.md` is not updated, every file citing it drifts silently. Treat a link change in GHL as a two-step job, same as a copy change.

## Both formats, every file

Standing Rule 1: every deliverable exists as `.md` **and** `.docx`. That applies to every file in this directory, not just the workflow captures.

After editing any `.md` here, regenerate its `.docx`:

```
python3 scripts/md2docx.py campaigns/<name>.md
```

That runs pandoc and then injects table gridlines, which Standing Rule 1b requires on every cell and pandoc does not add. It accepts several files at once, and works on the root-level docs too. Use it rather than calling pandoc directly, or the gridlines get missed. Forgetting to regenerate at all is the more common failure: the `.md` moves and the `.docx` silently keeps the old copy, which is what someone then pastes into GHL.
