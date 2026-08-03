# WF-06 New Customer Onboarding

**Trigger:** Contact Tag `unit_shipped`, applied by WF-28 Shopify Order Fulfilled
**Touches:** 4 (2 emails, 2 SMS, plus a same-day SMS alongside touch 1)
**Stop on Response:** On
**Audience:** paying customers, post-purchase
**Captured:** 2026-08-03, complete, with five corrections applied.

**Trigger note worth keeping.** WF-06 fires on the `unit_shipped` tag and does not apply it. WF-28 controls that, gated to Home System orders only. That gate exists because an accessory-only reorder, a wall mount, once re-fired this entire onboarding sequence at a customer whose device had arrived days earlier. If onboarding ever misfires again, look at WF-28's product filter, not here.

---

## Touch 1A | Day 1 | Email

**Subject:** Your Enyrgy Vitamin D Primal Light Platform is on its way

**Body:**

```
Hi {{contact.first_name}},

Good news, your Enyrgy Vitamin D Primal Light Platform has shipped and is on its way to you.

Here is how to get ready for your first session.

Step 1. Every person who will use the device needs registering first.
Log in at https://api.enyrgy.com/

Step 2. Click the add button and add each person one at a time. You are already registered as the Owner. Everyone else is added as a User.

Step 3. Download the Enyrgy app.
Search "Enyrgy" in the App Store or Google Play and download the app before your device arrives. This way you are ready to go the moment it lands.

Step 4. Complete your BioCalibrated Sunshine profile.
The app will guide you through your Fitzpatrick skin type assessment. This takes about 2 minutes and sets your personalized MED protocol automatically.

Step 5. Unbox and set up.
When your device arrives follow the simple setup instructions included in the box. Your first session will be guided by the app from start to finish.

Your first session will be 2 to 4 minutes. That is all it takes to activate all three biological pathways.

We cannot wait to hear how your first session goes.

{{custom_values.standard_signature}}
```

**CORRECTED Aug 3, four times.** Two grammar faults, a missing URL, an em dash, and the profile name. See the change log.

---

## Touch 1B | Day 1 | SMS

**Action name in GHL:** Unit Shipping

**Body:** (line breaks as they exist in GHL)

```
Hi {{contact.first_name}}, this is Scott from Enyrgy. Your
Enyrgy Vitamin D Primal Light Platform is on its way. Before
it arrives please register all users at https://api.enyrgy.com/
and download the Enyrgy app so you are ready for your first session. Reply STOP to opt out. Msg & data rates may apply.
```

**Note:** labelled "Touch 1!" in the source capture, which appears to be a typo for 1B. Carries the STOP opt-out and rate disclosure.

---

## Touch 2 | Day 3 | Email

**Subject:** Getting ready for your first session

**Body:**

```
Hi {{contact.first_name}},

Your Enyrgy Vitamin D Primal Light Platform should be arriving very soon. Here is a quick checklist to make sure you are ready for your first session the moment it arrives.

Before your device arrives:

1. Register all users at https://api.enyrgy.com/
You as the owner are already registered. Add any additional users one at a time as "User" accounts.

2. Download the Enyrgy app.
Search "Enyrgy" in the App Store or Google Play. The app is free and takes about 2 minutes to set up.

3. Complete your BioCalibrated Sunshine profile in the app.
The app will walk you through your Fitzpatrick skin type assessment and set your personalized MED protocol automatically. This is what makes every session precise and safe for your specific skin type.

When your device arrives:
Follow the unboxing instructions included in the box. Open the app, select Start Session, and follow the prompts. Your first session will be 2 to 4 minutes.

That is all it takes to activate Vitamin D synthesis, Nitric Oxide release, and Serotonin production simultaneously.

Any questions before your first session?

Reply to this email or call me directly at 602-321-0322.

{{custom_values.standard_signature}}
```

**CORRECTED Aug 3.** Profile name aligned with touch 1A.

---

## Touch 3 | Day 5 | SMS

**Action name in GHL:** First Session Check In

**Body:**

```
Hi {{contact.first_name}}, this is Scott from Enyrgy. Your device should have arrived by now. How was your first session? Any questions I can help with? Reply anytime or call me at 602-321-0322. Reply STOP to opt out. Msg & data rates may apply.
```

**TIMING RISK, not corrected.** This assumes delivery inside four days. If shipping runs longer, the customer reads a check-in about a session they could not have had, which reads as a company not tracking its own orders. Worth setting against the real delivery window. It may be fine.

---

## Touch 4 | Day 10 | Email

**Subject:** Around 10 sessions in, here is what to expect next

**Body:**

```
Hi {{contact.first_name}},

You have been using your Enyrgy Vitamin D Primal Light Platform for about 10 sessions now. Here is what is happening inside your body and what to expect as you continue.

Sessions 1 to 10.
The three pathways are running consistently, most likely for the first time in a long time.

Users report improvements within weeks, and sleep is usually the first thing people mention.

Sessions 11 to 30.
This is the stretch where the pathways are running consistently. Vitamin D synthesis builds with regular exposure. Nitric oxide photorelease supports cardiovascular regulation. Serotonin is the precursor your body converts to melatonin, which is the chemistry behind the sleep cycle.

Sessions 31 to 60.
In our 12-week study, the five participants raised their vitamin D by an average of 111 percent. Small study, no control group, and we say so. Your body is doing what it was designed to do when given the right stimulus.

A few tips to maximize your results.

Session consistency matters more than session length. 4 to 5 sessions per week delivers optimal results. The app tracks everything automatically so you always know where you stand.

If you have not already, this is a great time to get a Vitamin D blood test so you have a baseline to compare against in 12 weeks. The difference will speak for itself.

Keep going. You are exactly on track.

{{custom_values.standard_signature}}
```

**CORRECTED Aug 3, four times.** The study description, the outcome assertions, and the subject em dash. See the change log.

---

# Change log, 2026-08-03

| # | Touch | Change |
|---|---|---|
| 1 | 4 | "Clinical data shows" replaced with the honest study description |
| 2 | 4 | Session-milestone blocks reframed from asserted outcomes to biology |
| 3 | 1A | Two grammar faults, the missing registration URL, and an em dash |
| 4 | 1A, 2 | Profile name unified. Touch 1A said Biosignature, touch 2 said Biocalibration |
| 5 | 4 | Subject em dash |

## "Clinical data shows" was the strongest overstatement in the funnel

Every other email calls the study a small study, an observational cohort, or states N=5. Touch 4 called it clinical data with no qualifier.

**It matters more here because of who receives it.** This goes to someone who has already paid $2,995. Discovering later that the "clinical data" was five people does not produce scepticism about a claim, it produces the feeling of having been handled. That is the customer who returns a working unit and tells people why.

## The milestone blocks promised outcomes to a named individual

The original stated what was happening in the reader's body as fact: *"Your levels are climbing toward optimal range... Serotonin production is stabilizing mood and sleep cycles."*

The KB is explicit for this pathway: present it as how the biology works, **not as a promise the device improves sleep**. Addressed to one person about their own body, the promise version is the one that reads as medical.

Reframed to describe the mechanism. The reassurance survives; the claim does not.

Also narrowed: "Many customers report improved sleep quality and energy levels within the first two weeks" became the KB's "users report improvements within weeks". The original turned a soft observation into a two-week schedule the customer would measure against.

## The first email after purchase had three faults

"All the user of your device must be registered" and "You will be already be registered" were both broken, and step 1 told the customer to log into a portal without giving the address. The URL appears in the SMS an hour later and in touch 2 two days later, so the only email that needed it was the one that omitted it.

On the first message after someone spends $2,995, that reads as carelessness about the thing they just bought.

## Open, needs a decision

**Touch 3's four-day delivery assumption.** See the note on that touch.

**The in-app profile name.** Both emails now say "BioCalibrated Sunshine profile", matching the KB's trademarked term. If the app screen calls it something else, use the app's wording in both and record it in the KB, since the customer is reading the email with the screen in front of them.
