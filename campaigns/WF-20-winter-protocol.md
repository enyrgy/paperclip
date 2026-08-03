# WF-20 Winter Protocol Emails

**Trigger:** Contact Tag `magnet_winter_protocol`, enrolled by WF-19 Winter Protocol Webhook
**Touches:** 3, with a three-way seasonal branch on touch 3
**Ends with:** `nurture_longterm`, which hands the contact to WF-17
**Audience:** SAD and seasonal ICP, `icp_sad`
**Captured:** 2026-08-02, complete, with three corrections applied the same day.

## Structure of touch 3, worth understanding before editing anything

A code action, **Winter Check**, splits three ways:

```
Winter Check
  |- Pre-Winter Check    (current month after June and ...)   -> Touch 3A Pre-Season Close   -> Add Nurture Tag -> END
  |- During Winter Check (current month after October ...)    -> Touch 3B In-Winter Close    -> Add Nurture Tag -> END
  |- None                (neither window)                     -> Add Nurture Tag -> Wait until pre-season -> Email 3C Pre-Season Close (held) -> END
```

**The None branch is a held send, not a third season.** A contact entering outside both windows, in March say, is parked until pre-season rather than being sent a mistimed "October is coming" email. **3C is therefore intentionally identical to 3A.** Do not treat it as a duplicate and delete it.

**3A and 3C must be edited together.** Nothing in GHL enforces that, and they had already drifted by a paragraph break when captured. Any change to one is a change to both.

---

## Touch 1 | Day 1 | Email

**Subject:** Your Winter Protocol guide

**Body:**

```
You know the version of yourself that shows up around November. Lower battery, shorter fuse, quietly saying no to things you would say yes to in June. Here is the guide that explains why that happens, and it has nothing to do with willpower.

I want to be straight about one thing before you open it. I didn't write this to sell you anything. I wrote it because the biology behind the winter version of you is well documented, and almost nobody has had it explained to them plainly. So that is what this does.

Read it. If it lands, there is more where it came from.

Download The Winter Protocol ->

{{custom_values.standard_signature}}
```

**Note:** "quietly saying no to things you would say yes to in June" is the sharpest observation in the workflow. It describes the symptom the reader recognises without naming a condition, which keeps it well clear of the medical-claims line.

---

## Touch 2 | Day 4 | Email

**Subject:** Why your light box isn't enough (and it's not your fault)

**Body:**

```
If you are like most people who dread winter, you have already tried the obvious moves. A light box on the desk. A D3 capsule with breakfast. You did the responsible things.

And from November through February, you still feel like a different person.

That is not you failing to try hard enough. It is two real tools each solving half the problem.

A light box works on your circadian rhythm. It tells your brain it is daytime, which genuinely helps your sleep and your mornings. But it cannot trigger vitamin D synthesis, because that needs UVB at 280 to 315 nanometers, and a visible-light lamp does not emit that wavelength.

A D3 capsule raises the vitamin D number in your blood. Also real. But it does nothing for the serotonin pathway that daytime light drives, a separate mechanism from vitamin D entirely.

Summer feels different because sunlight runs all three pathways at once, something no capsule and no lamp fully copies. The Enyrgy Vitamin D Primal Light Platform runs all three, in a two-to-four-minute session dosed to your skin. In a small 12-week cohort, five people using it four to six times a week moved their vitamin D from an average of 39.96 to 84.20 ng/mL, with zero adverse events. A small pilot, and we say so. But it is the mechanism doing what the lamp and the capsule cannot.

See how it works ->

{{custom_values.standard_signature}}
```

**Checked:** the 280 to 315 nm figure and the statement that visible-light lamps cannot trigger synthesis both match KB Section 2 exactly. The pilot is disclosed as a small cohort of five with the honest qualifier attached.

**The best competitive email in the funnel.** It grants that both the light box and the capsule work, says what each does, and locates the gap between them. Nothing is dismissed, so nothing needs defending.

---

## Touch 3A | Day 6 | Email, Pre-Winter branch

**Subject:** October is coming. You know what that means.

**Body:**

```
The days are about to start getting shorter. The air shifts. And somewhere in the back of your mind, you are already bracing for a few months of running at a lower setting than the rest of the year.

You have done that winter after winter. You know exactly how it goes, and you know roughly when it lifts. That is months of being a smaller version of yourself, every year, on a schedule.

What winter actually takes is the light your body runs on, and that part you can put back.

The Enyrgy Vitamin D Primal Light Platform runs the three light-driven pathways winter cuts off: UVB-triggered vitamin D synthesis, nitric oxide release, and the serotonin pathway that a lamp and a supplement leave untouched. Two to four minutes a day, all year.

Here is how to prove it to yourself, without taking my word for anything. Get a baseline vitamin D lab now, run the protocol, and retest at 8 to 12 weeks. That is a real before and after, on your own body, not ours.

You do not have to wait for those results to decide, though. The unit comes with a 30-day money-back guarantee, so if it is not for you, send it back.

The catch is timing. Start in September and your levels have weeks to climb before the darkest months, instead of starting from empty in December.

Building ahead of the drop beats trying to catch up in the middle of it.

Get the Enyrgy Vitamin D Primal Light Platform ->

{{custom_values.standard_signature}}
```

**CORRECTED Aug 2.** Paragraph break added so 3A and 3C match exactly.

**GUARANTEE LANGUAGE ALREADY CORRECT, do not change.** "You do not have to wait for those results to decide, though" is the reference phrasing from the Session 14 decoupling fix.

---

## Touch 3B | Day 6 | Email, During-Winter branch

**Subject:** You're in it right now. Here's the way out.

**Body:**

```
You are reading this in the middle of it. The short days, the low battery, the version of yourself that takes more effort than it should. So let me skip the part where I explain what is happening, because you are living it.

Here is the part worth knowing. The input your body is missing right now is the same one it will keep missing until spring, unless you give it back. Every week you wait is another week without it.

The Enyrgy Vitamin D Primal Light Platform runs the three pathways winter took from you: the UVB-triggered vitamin D synthesis, the nitric oxide release, and the serotonin pathway that a lamp and a supplement leave untouched. Two to four minutes a day.

I am not going to tell you that you will feel different tomorrow. Vitamin D builds over weeks, not days. Start today and your levels are climbing back through February and March, instead of bottoming out until April and waiting on the sun. The sooner you start, the more of this winter you spend with your levels up instead of empty.

Here is how to prove it to yourself. Pull a baseline vitamin D lab now, run the protocol, and retest at 8 to 12 weeks for your own before and after.

You do not have to wait for those results to decide, though. The unit comes with a 30-day money-back guarantee, so if it is not for you, send it back.

Get the Enyrgy Vitamin D Primal Light Platform ->

{{custom_values.standard_signature}}
```

**Note:** "I am not going to tell you that you will feel different tomorrow. Vitamin D builds over weeks, not days" is the most restrained sentence in any close in the funnel. Written to a reader who is currently suffering, it declines the easy promise.

---

## Touch 3C | Day 6 plus hold | Email, None branch, held until pre-season

**Subject:** October is coming. You know what that means.

**Body:** identical to Touch 3A above. Same subject, same body, word for word.

**Why it exists.** Contacts entering outside both seasonal windows are parked on `Wait until pre-season` and sent this when the season arrives, rather than receiving a mistimed message. It is a scheduling mechanism, not a content variant.

**EDIT IN LOCKSTEP WITH 3A.** They had already drifted by a paragraph break when captured on 2026-08-02. Nothing in GHL keeps them synchronised.

---

# Change log, 2026-08-02

| # | Where | Change |
|---|---|---|
| 1 | 3A | Paragraph break added so 3A and 3C match again |
| 2 | Pre-Winter branch | Action renamed from "Touc 3A" to "Touch 3A" |
| 3 | None branch | `Add Nurture Tag` moved ahead of `Wait until pre-season` |

## The nurture tag was gating on a seasonal wait

Originally the None branch ran **Wait until pre-season -> Email 3C -> Add Nurture Tag.**

The nurture tag is what hands a contact to WF-17 Long-Term Nurture. In the 3A and 3B branches it fires on Day 6. In the None branch it fired only after the hold, so a contact entering in March received touch 1, touch 2, and then **silence until July** before entering the long-term nurture at all.

Up to four months of nothing, starting from the moment a lead is at their most engaged, having just downloaded a guide.

Reordered so the tag fires first. The contact enters WF-17 on Day 6 like everyone else and still receives the seasonal close when the season comes. No conflict: 3C is a single seasonal message and WF-17 is a separate sequence.

## What was already right

**The guarantee decoupling.** All three arms carry "You do not have to wait for those results to decide, though", the reference phrasing from Session 14. **First workflow of five to need no correction on this**, after WF-17 twice, WF-13, WF-16 3A, and WF-14 both arms.

**The seasonal hold itself.** Holding a contact until the right season rather than sending a mistimed message is the correct design, and it is the reason 3C exists. It was initially misread here as an accidental duplicate. It is not. Do not delete it.

## Minor, left alone

Touches 1, 2 and 3B use contractions ("didn't", "isn't", "You're"). WF-13, WF-16 and WF-17 do not. Cosmetic, and the contractions arguably suit this audience, but it is an inconsistency across the funnel if anyone ever wants one voice.
