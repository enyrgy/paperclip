# Outcode to GHL Integration Spec

**Status:** DRAFT, August 1, 2026. Part A is shareable with Outcode. Part B is internal.
**Purpose:** pipe device-app user registrations and completed sessions into GHL so new users get onboarding, inactive users get a nudge, and vitamin D progress is tracked per contact.

---

# PART A: FOR OUTCODE

## Two endpoints, not one

Send **two separate webhooks** to two separate GHL URLs rather than one endpoint with an event-type field.

Reason: a single endpoint means every session ping runs through the same workflow that sends the welcome sequence, and that workflow then needs branching logic to suppress the welcome on all but the first call. Two endpoints means each side does one job with no guard logic and no race conditions.

GHL webhook URLs will be supplied per endpoint. Both are `POST`, `Content-Type: application/json`.

## Endpoint 1: user registered

Fires **once**, when a new user completes registration on a device.

| Field | Type | Notes |
|---|---|---|
| `first_name` | string | |
| `last_name` | string | |
| `email` | string | **Match key.** GHL merges contacts on email. |
| `phone` | string | E.164 preferred (`+16025551234`) |
| `user_id` | string | Outcode's stable user identifier |
| `device_id` | string | |
| `device_type` | string | `home` or `commercial` |
| `facility_name` | string | Commercial only, empty string for home |
| `is_owner` | boolean | See suppression note below |
| `registration_date` | string | `M/D/YYYY` |
| `skin_type` | integer | 1 to 6 |
| `gender` | string | |
| `height` | string | ft/in |
| `weight` | number | lbs |
| `vitamin_d_level` | number | ng/mL, empty if not yet known |
| `email_consent` | boolean | Captured at registration |
| `consent_timestamp` | string | ISO 8601 |
| `tags` | string | Optional, comma-separated. Applied verbatim as GHL tags. |

## Endpoint 2: session completed

Fires on **every completed session**. This is a hard requirement, not a nice-to-have: the inactivity nudge works by resetting a timer on each session, so if this only fired at registration, GHL would have no way to know a user is still active and every user would be flagged inactive on day three forever.

| Field | Type | Notes |
|---|---|---|
| `email` | string | **Match key** |
| `user_id` | string | |
| `device_id` | string | |
| `last_treatment_date` | string | `M/D/YYYY` |
| `vitamin_d_level` | number | Send when it changes, empty string otherwise |
| `session_count_total` | integer | Lifetime sessions for this user |

`session_count_total` is worth including. Enyrgy already has a `sessions_10_complete` tag driving review and referral outreach, currently applied by hand. With this field it becomes automatic.

## Three requirements that matter

**1. Suppress the webhook for account owners.** The owner registers in the app like everyone else. Their contact record already arrives from Shopify with its own onboarding sequence, so an owner registration firing Endpoint 1 would send them a second, wrong welcome. Either omit owner registrations entirely, or set `is_owner: true` so it can be filtered downstream. Omitting is preferred: filtering at the source is more reliable than working around it later.

**2. Send empty strings, never omit keys.** If a field has no value, send `"field": ""`. Do not drop the key from the JSON. GHL's field mapper binds to a fixed payload shape, and a missing key can silently fail to map rather than mapping as blank. This is a known behaviour, not a theory.

**3. Keep field names stable once live.** Each name is bound individually inside GHL workflows. Renaming a field after go-live silently breaks that mapping with no error raised.

---

# PART B: INTERNAL, GHL BUILD

## Prerequisite: WF-01 must be guarded BEFORE the webhook goes live

**WF-01 New Lead Router triggers on Contact Created.** Every device user Outcode creates will hit it and be routed into a lead funnel. These are customers' users, not prospects.

Tags applied by the receiving workflow land *after* WF-01 has already run, so they cannot guard it. This is the same race condition that forced the WF-31 rebuild, where the fix was a 2-minute wait before the condition. WF-01 needs equivalent treatment or a first-step guard on a field that is written during Create Contact.

Also note **WF-31 FlexOffers First Touch** triggers on Contact Created. Harmless here (the refid will be empty, the condition fails, it ends) but every device user will enrol and add execution-log noise.

## New custom fields

| Field | Type | Folder |
|---|---|---|
| Consent Timestamp | Text | Health Profile |
| Device Type | Single Options (Home / Commercial) | Health Profile |
| Facility Name | Text | Health Profile |
| Device ID | Text | Health Profile |
| Last Treatment Date | Date | Health Profile |
| Session Count Total | Number | Health Profile |

Already exist and should be mapped: Registration Date, Skin Type, Gender, Height, Weight, Vitamin D Level.

## WF-32 New Device User Onboarding

Trigger: Inbound Webhook (Endpoint 1)

1. Create Contact: first/last name, email, phone
2. Map custom fields from `{{inboundWebhookRequest.*}}`
3. Standard Add Tag: `source_device_app`, `user_device_registered`, `drip_bypass`
4. Dynamic Add Tag: `{{inboundWebhookRequest.tags}}`
5. Email sequence: app setup and QR scan, four to five sessions a week initially, one session per day maximum, what to expect in the first two weeks, re-test at 90 days

`drip_bypass` keeps these users out of the five lead drips. It does not block WF-32, which is not a drip.

**One workflow, not two.** Home and commercial users share nearly all content: both open the app and scan the QR on the unit, both get the same dosing, frequency, daily limit and re-test cadence. Only the location of the unit differs. Write it device-agnostically and store `device_type` so it can be split later if the copy genuinely diverges. Branching early would mean duplicating the whole sequence inside each branch, because GHL condition branches never rejoin.

## WF-33 Treatment Sync

Trigger: Inbound Webhook (Endpoint 2)

1. Update Contact: Last Treatment Date, Vitamin D Level, Session Count Total
2. **Remove from** WF-34
3. **Add to** WF-34

## WF-34 Inactivity Nudge (INTERIM, retire when the app ships)

Trigger: added by WF-33 only.

1. Wait 3 days
2. Send nudge

**Build it deliberately dumb.** No escalation, no cooldown, no branching. The next version of the device app handles all nudge messaging natively, so this workflow is a stopgap and any cleverness added here is thrown away. One wait, one message.

**Why the timer, not a date condition.** GHL's condition builder handles relative date math poorly, which is what broke the first two attempts at WF-31. Do not build a nudge that asks "is Last Treatment Date more than 3 days ago." Let the timer be the test: every session wipes the pending timer and starts a fresh one, so if three days pass with nothing resetting it, the user has genuinely gone quiet. No date comparison anywhere, and it self-corrects when a session arrives late.

### RETIREMENT TRIGGER

**When the next app version ships with native nudge messaging, unpublish WF-34 and remove the Remove/Add actions from WF-33.** Otherwise users receive two reminders for the same lapse, one push and one from GHL.

Nothing will error when this happens. The only symptom is users being nudged twice and learning to ignore both. This is the same class of failure as the Session 14 double-send, where GHL drips and Paperclip agents were both messaging the same contacts, resolved by narrowing agent triggers and turning Stop-on-Response on.

**Endpoint 2 is NOT retired with the nudge.** Last Treatment Date, Vitamin D Level and Session Count Total continue to drive segmentation, automatic `sessions_10_complete` tagging, milestone messaging, and commercial facility reporting. The "fires on every session" requirement to Outcode stands permanently, independent of WF-34.

## Open decisions

- **Volume.** At 600 users averaging 4 to 5 sessions a week, Endpoint 2 fires roughly 3,000 times a week, around 140,000 workflow executions a year and rising with every unit placed. Confirm the GHL plan's execution limits before go-live; the failure mode is silent throttling, not a visible error. Note this does not reduce when WF-34 retires, since Endpoint 2 continues.
- **Facility member data ownership.** A commercial facility's members flowing into Enyrgy's GHL raises the same question as the open OEM/Lumanova data-boundary item in the EA. Worth settling before the first commercial unit is registering members at scale.
- **Milestone messaging.** With `vitamin_d_level` and `session_count_total` arriving automatically, both a "crossed into optimal range" message and automatic `sessions_10_complete` tagging become possible.

## Why this matters commercially

Vitamin D levels arriving per contact is what makes the Beyond Wellness pitch deliverable rather than aspirational. The Q3 commitment there was to help structure a baseline and a 90-day re-test. Once levels flow into GHL, that is a facility report that can be generated, not a promise.
