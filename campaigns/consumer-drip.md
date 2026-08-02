# Consumer Drip

**Trigger:** Contact Tag `type_consumer`
**Touches:** 12 over 21 days
**Gating:** first-step If/Else "Bypass Check". Contacts whose tags do NOT include `drip_bypass` run all 12 touches; contacts carrying it END immediately.
**Stop on Response:** On
**Captured:** 2026-08-02 (partial, see status below)

**Capture status:** Touches 2, 3, 4 recorded. Touch 1 and touches 5 to 12 still outstanding.

---

## Touch 1 | Bypass Check (not an email)

If/Else gate. Tags do NOT include `drip_bypass` -> run the sequence. Tags include it -> END.

---

## Touch 2 | Day 1 | Email

**Subject:** Two minutes of the right light

**Body:**

```
{{contact.first_name}},

You came by enyrgy.com. So you already suspect the supplement route is not quite doing it.

Here is what your body forgot it knew. Given the right light, it makes vitamin D, nitric oxide, and serotonin on its own, all three, in the time it takes to brush your teeth. That light is the Enyrgy Vitamin D Primal Light Platform. Two to four minutes. The same vitamin D from actual sun is two to four hours, plus the burn and the aging you did not sign up for.

What keeps it safe is the app. It reads your skin type, picks your dose, and shuts the session off for you. Nobody stands there guessing. Twenty five thousand sessions, zero burns, zero adverse events.

That is the whole pitch. The unit is here if you want to look: https://shop.enyrgy.com/products/uvb-light-therapy. Reply if you have a question. It lands on my desk, not a queue.

{{custom_values.standard_signature}}
```

---

## Touch 3 | Day 3 | SMS

**Body:** (line breaks are as they exist in GHL, verified by unmodified copy/paste)

```
Hi {{contact.first_name}}, quick question. Have you ever had your
Vitamin D levels checked? Most people are surprised when they see
the number. Reply YES or NO and I'll send you something specific
based on your answer. Reply STOP to opt out. Msg & data rates
may apply.
```

Carries the STOP opt-out and rate disclosure, as required.

**WORTH CHECKING IN GHL:** those four line breaks fall mid-sentence, after "your", "see", "specific" and "rates". That is the signature of a textarea's display wrapping having been baked in as hard newlines rather than deliberate formatting. On a phone the message would render with breaks in odd places, since the handset re-wraps to its own width regardless. Segment cost is barely affected (about 254 characters either way, so two segments), but the rendering is worth eyeballing on a real device before the next send.

---

## Touch 4 | Day 5 | Email

**Subject:** What the pill leaves out

**Body:**

```
{{contact.first_name}},

If you take vitamin D and still feel low, the pill may not be the problem. It might just be doing less than the label implies.

Two things about supplements. They open one lane, vitamin D, and only if your body responds well to it. In the trials, about one in four participants were low responders to vitamin D supplementation. They took it; their body did less with it. And even when it works perfectly, it is still one lane out of three.

Your body was built to get three from sunlight at once. Vitamin D. Nitric oxide, which supports cardiovascular regulation. And serotonin, which supports mood, sleep, and focus. A capsule gives you the first. It cannot give you the other two.

That is the whole reason the Enyrgy Vitamin D Primal Light Platform exists. Two to four minutes, all three, with the app setting your dose by skin type and ending the session for you.

If you want the science behind it, reply and I will send it. Or grab a 15-minute call here: Book Call.

{{custom_values.standard_signature}}
```

**Link note:** "Book Call" is anchor text. All links across the funnel were verified correct in a dedicated session, so the URL behind it is sound; it simply does not survive a plain-text copy. Per the KB the discovery-call booking link is `https://api.leadconnectorhq.com/widget/booking/C0hV5CFHUhWOIzs4OedC`.

**Backup fidelity caveat, applies to every email in `campaigns/`:** plain-text capture preserves wording but drops the URL behind any anchor text. Restoring a workflow from these files alone would rebuild the copy correctly and lose the hyperlinks. See the README for the options.

---

## Touches 5 to 12

**NOT YET CAPTURED.**
