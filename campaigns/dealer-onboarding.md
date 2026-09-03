# Dealer Onboarding

**Applies to:** commercial dealers who resell the $8,950 unit and earn 25 to 16 percent on the final sale price.
**Not for:** facility referral partners on the consumer unit. Different product, different terms, different program.
**Built:** 2026-08-19, alongside the deal registration workflows WF-40 to WF-43.

**Do this in order. Step 3 is the one whose failure is silent.**

---

## Why there is a form per dealer

`Dealer Name` is a dropdown on the registration form, because attribution that decides a $2,237 commission cannot be free text with three spellings of the same company.

But a dropdown shows every option to whoever opens it. One shared form would let every dealer read the full roster: who else sells for Enyrgy, and by inference which territories are covered and how large the network is. That is competitive intelligence nobody would hand over on purpose.

GoHighLevel has no hidden-field option on this form type, and its API is `forms.readonly`, so this cannot be automated away inside GHL. One form per dealer is the way to keep the roster private.

**The master form is a template. Never send it to anyone, and never add a real dealer name to it.**

---

## The five steps

### 1. Duplicate the form

Duplicate `Dealer Deal Registration` and rename the copy:

```
Dealer Registration - <Dealer Company Name>
```

### 2. Set their single dropdown option

On the copy, open the `Dealer Name` field. Remove `Unassigned`, then add one option: their company name exactly as it should appear in reporting and on commission statements.

Their dropdown now contains one entry. They learn nothing about anyone else.

### 3. Add the new form to WF-40's trigger

Open `WF-40 Dealer Registration Received`. The trigger reads `Form is any of "..."`. Add the new form to that list.

**This is the step that gets forgotten, and its failure is invisible.** Without it the dealer submits, an opportunity appears in `Registration Submitted`, and nothing else happens: no tag, no `Source Type`, no alert to Scott. It sits there looking like a real deal until somebody notices the registration nobody actioned.

Two consequences follow. The facility is not protected from consumer drip, because the `no_route` tag never lands. And the dealer believes they hold a claim they do not have.

### 4. Collect the right tax form

US dealers need a **W-9**. Non-US dealers need a **W-8BEN** or **W-8BEN-E** depending on entity type, and treaty status may bring withholding into play.

Determine residency first, then request the matching form. Collect it at onboarding, not in January.

Every dealer clears the US $600 reporting threshold on their first sale, several times over, so there is no volume below which this can be skipped.

### 4b. The W-9 request email

Template. Replace the bracketed fields. **Send it before the registration link**, not after: a dealer who has their link and is already working is much harder to chase for paperwork than one who is waiting on it.

**Subject:** `One piece of paperwork before we switch you on`

```
[First name],

Good to have you on board.

One administrative thing before we can process commissions. I need a completed W-9 from [Dealer Company Name]. It is the standard IRS form for reporting commission payments, and we cannot pay against a sale without one on file.

If you need a blank, the current form is here: https://www.irs.gov/pub/irs-pdf/fw9.pdf

Send it back to me directly at [Scott's address] rather than to a general inbox. It carries your EIN and I would rather it went to one person than sat in a shared mailbox.

As soon as it is in, I will send your registration link and you are live.
```

**Non-US dealers get a W-8BEN or W-8BEN-E instead.** Same email, swap the form and drop the IRS link, which is US-specific.

**On where it goes.** A W-9 carries a taxpayer identification number. Do not route it to `contact@enyrgy.com` or any address that staff or agents can read. It belongs with whoever holds finance records, and nowhere else.

### 5. Send them their link

`Integrate` on their copy of the form, then send that URL and nothing else. Do not send the master form link to a dealer under any circumstances.

---

## Adding them to the field options

Step 2 adds the option to their form. Also add their company to the shared `Dealer Name` field in `Settings > Custom Fields > Opportunity > Dealer Registration`, so the value exists for filtering and reporting across the pipeline.

Adding it there does not expose them, because no dealer sees that screen. What exposes them is putting the name on a form more than one dealer can open.

---

## What `Unassigned` means

`Unassigned` is not a dealer. It is the marker for a registration that lost its attribution, and it should never be selectable on a live dealer form.

An opportunity with `Source Type = Dealer` and `Dealer Name = Unassigned` is a deal nobody can be paid for. Treat any of those as a fault to investigate, not a record to leave.

Worth a saved filter alongside the other dealer views.

---

## Offboarding

When a dealer leaves, unpublish or delete their form and remove it from WF-40's trigger list. Leave their name in the `Dealer Name` field options, because historical opportunities reference it and removing it would orphan the attribution on deals they earned.

Their live registrations keep running their 90 day clocks. Decide deliberately whether to release those early, and tell them either way.

---

## Change log, 2026-08-19

| # | Change |
|---|---|
| 1 | Created alongside the WF-40 to WF-43 deal registration build |

## Why this document exists

Everything else in the registration system lives in GoHighLevel and enforces itself. This part does not. It is a sequence somebody has to follow correctly at a moment months from now, when the obvious action is the wrong one: adding a second name to the form that already works.

The whole document exists to prevent that one mistake, and to make step 3 hard to skip.
