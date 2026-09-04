# Dealer Onboarding

**Applies to:** commercial dealers who resell the $8,950 unit and earn 25 to 16 percent on the final sale price.
**Not for:** facility referral partners on the consumer unit. Different product, different terms, different program.
**Built:** 2026-08-19, alongside the deal registration workflows WF-40 to WF-43.

**Do this in order. Step 3 is the one whose failure is silent.**

---

# STOP: do not onboard a second dealer until this is fixed (found 2026-08-30)

**The per-dealer form does not isolate the dropdown, which was the entire point of it.**

`Dealer Name` is a single Opportunity custom field, `opportunity.dealer_name`, with **one shared option list**. Every form bound to it shows the same options. Duplicating the form gives each dealer their own URL. It does not give them their own dropdown.

**Proven, not theorised.** Onboarding AVETTA Global LLC, the option was set on their form copy alone. It appeared on the shared field without anyone adding it there, and the master form simultaneously lost `Unassigned` and gained `AVETTA Global LLC`.

**Consequences, in order of when they bite:**

  - **Dealer #2 exposes dealer #1 and vice versa.** The moment a second name is added, both forms show both. That is the roster leak this structure exists to prevent.
  - **The master's tripwire is gone.** `Unassigned` is no longer an option anywhere, so an accidental master submission now attributes silently to whichever real dealer is listed, rather than flagging as a fault. Restoring `Unassigned` is not a fix, because it would reappear on live dealer forms where it must never be selectable.
  - **One dealer is safe.** With AVETTA alone there is nothing to leak, which is why their onboarding proceeded.

**The likely fix, not yet built.** Take `Dealer Name` off the form and capture attribution from the link instead: each dealer's URL carries a parameter, the form reads it, WF-40 writes it to the opportunity. No dropdown means no roster. A dealer can only ever see their own name, because it arrived in their own link. **Confirm what the GHL form builder actually supports before committing to that**, rather than assuming, which is how this one was missed.

---

## Why there is a form per dealer

`Dealer Name` is a dropdown on the registration form, because attribution that decides a $2,237 commission cannot be free text with three spellings of the same company.

But a dropdown shows every option to whoever opens it. One shared form would let every dealer read the full roster: who else sells for Enyrgy, and by inference which territories are covered and how large the network is. That is competitive intelligence nobody would hand over on purpose.

GoHighLevel has no hidden-field option on this form type, and its API is `forms.readonly`, so this cannot be automated away inside GHL. One form per dealer was believed to be the way to keep the roster private.

**That belief was wrong, and the reasoning above is why it looked right.** The privacy argument holds. The mechanism does not, because the options live on the shared custom field rather than on the form. See the stop notice at the top of this document.

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

**This edit writes through to the shared field and to every other form.** It is safe with one dealer and is not safe with two. Do not perform this step for a second dealer until the model is rebuilt.

**Step 4 below is therefore already done by this step.** GHL propagates the option to `Settings > Custom Fields > Opportunity > Dealer Registration` on its own. Check it rather than adding it, or you will create a duplicate.

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

**As of 2026-08-30 `Unassigned` no longer exists as an option**, removed by the AVETTA onboarding through the shared-field behavior described at the top. It cannot be restored without putting it back on live dealer forms. Until the model is rebuilt, an accidental master submission attributes to a real dealer instead of flagging, so the protection this section describes is currently absent.

---

## The 90 day expiry date is set by hand, at Conflict Check

**Decided 2026-08-30 after finding that nothing set it.**

WF-41 refuses to send a dealer their confirmation while `Exclusivity Expires` is empty, and nothing in WF-40 or WF-41 populates it. As built, every registration would have stalled unconfirmed.

**GHL cannot compute it.** The Update Opportunity action's date field offers a current date under `Right now` and no offset of any kind. There is no date arithmetic available in that field.

**The rule, until it is automated.** Whoever works the Conflict Check stage sets `Exclusivity Expires` to submission plus 90 days **before** moving the opportunity to Prospect. WF-41's empty check is the enforcement: forget it and the dealer is simply not confirmed, and the internal notification on WF-41's None branch tells you why.

**The permanent fix, when there is time.** WF-40 posts the opportunity to the existing Railway service, which computes the date and writes it back through the GHL API. The infrastructure and credentials already exist for the abandoned-checkout service. Not urgent: one dealer setting one date by hand is not a system under strain.

## Offboarding

When a dealer leaves, unpublish or delete their form and remove it from WF-40's trigger list. Leave their name in the `Dealer Name` field options, because historical opportunities reference it and removing it would orphan the attribution on deals they earned.

Their live registrations keep running their 90 day clocks. Decide deliberately whether to release those early, and tell them either way.

---

## Change log, 2026-08-19

| # | Change |
|---|---|
| 1 | Created alongside the WF-40 to WF-43 deal registration build |

## Change log, 2026-08-30

| # | Change |
|---|---|
| 1 | **Found: the per-dealer form does not isolate the dropdown.** Stop notice added at the top. Do not onboard a second dealer until the model is rebuilt. |
| 2 | **Found: nothing set `Exclusivity Expires`**, so no dealer would ever have been confirmed. Route 1 adopted, set by hand at Conflict Check, with the Railway route recorded as the permanent fix. |
| 3 | **WF-40 hardened.** One minute wait added before the opportunity lookup, against the async-write race that cost this account refids on WF-31. Internal notification added to the `Opportunity Not Found` branch, which previously ended in silence while the dealer believed they held a claim. |
| 4 | W-9 request email added as step 4b, sequenced before the registration link. |
| 5 | `Unassigned` recorded as no longer existing, and why it cannot simply be restored. |

## AVETTA Global LLC, onboarding state at 2026-08-30

Steps 1 to 5 complete: form duplicated and named, dropdown set, form added to WF-40's trigger, shared field populated by GHL's write-through, W-9 requested.

**Steps 6 and 7 outstanding, waiting on the W-9 to arrive.** Step 6 is sending their Integrate link. Step 7 is the test submission that proves the wiring, including the WF-41 confirmation path with Scott's own address in the dealer email field so no test confirmation reaches AVETTA.

## Why this document exists

Everything else in the registration system lives in GoHighLevel and enforces itself. This part does not. It is a sequence somebody has to follow correctly at a moment months from now, when the obvious action is the wrong one: adding a second name to the form that already works.

The whole document exists to prevent that one mistake, and to make step 3 hard to skip.
