# Enyrgy Device App to CRM Webhook Spec

**Version 1.0 | August 1, 2026 | Enyrgy Inc**
**Contact:** Scott Hansbury, scott@enyrgy.com, 602-321-0322

---

## 1. What this is for

Enyrgy runs its customer communication in a CRM (GoHighLevel). Today the CRM knows about people who **buy** a device, because Shopify tells it. It knows nothing about the **other users registered on that device**, because that happens in the app.

That gap means an additional user on a home unit, or a member using a unit at a commercial facility, receives nothing from us: no welcome, no guidance on how often to run sessions, no reminder when they stop.

This spec covers two webhooks that close it.

## 2. Two endpoints, not one

Please send **two separate webhooks to two separate URLs** rather than a single endpoint with an event-type field.

The registration event and the session event drive completely different behavior on our side. A single endpoint means every session ping runs through the same logic that sends the welcome sequence, and that logic then needs branching to suppress the welcome on all but the first call. Two endpoints means each side does one job.

Both endpoints: `POST`, `Content-Type: application/json`.

---

## 3. Endpoint 1: user registered

**Fires once**, when a new user completes registration on a device.

| Field | Type | Example | Notes |
|---|---|---|---|
| `first_name` | string | `Maria` | |
| `last_name` | string | `Garcia` | |
| `email` | string | `maria@example.com` | **Match key.** The CRM identifies contacts by email. |
| `phone` | string | `+16025551234` | E.164 preferred |
| `user_id` | string | `usr_8f21a` | Your stable user identifier |
| `device_id` | string | `dev_44c1` | |
| `device_type` | string | `home` or `commercial` | |
| `facility_name` | string | `Beyond Wellness` | Commercial only. Empty string for home. |
| `is_owner` | boolean | `false` | See 5.1 |
| `registration_date` | string | `8/1/2026` | `M/D/YYYY` |
| `skin_type` | integer | `3` | 1 to 6 |
| `gender` | string | `Female` | |
| `height` | string | `5ft 6in` | |
| `weight` | number | `140` | lbs |
| `vitamin_d_level` | number | `32` | ng/mL. Empty string if not yet known. |
| `email_consent` | boolean | `true` | As captured at registration |
| `consent_timestamp` | string | `2026-08-01T14:22:07Z` | ISO 8601 |
| `tags` | string | `athlete,facility_member` | Optional, comma-separated. Applied verbatim as CRM tags. |

---

## 4. Endpoint 2: session completed

**Fires on every completed session.**

| Field | Type | Example | Notes |
|---|---|---|---|
| `email` | string | `maria@example.com` | **Match key** |
| `user_id` | string | `usr_8f21a` | |
| `device_id` | string | `dev_44c1` | |
| `last_treatment_date` | string | `8/1/2026` | `M/D/YYYY` |
| `vitamin_d_level` | number | `48` | Send when it changes, empty string otherwise |
| `session_count_total` | integer | `27` | Lifetime sessions for this user |

### 4.1 Please make the firing schedule configurable

Per-session firing is required initially, because the inactivity reminder works by resetting a timer each time a session arrives. If nothing resets it within three days, the user gets a nudge.

A future version of the app will handle that reminder natively. At that point this endpoint drops to a **daily or weekly batch sync**, since nothing on the CRM side will still need per-session resolution.

Please build the schedule as a configuration value rather than hard-wiring it to session completion, so that change is a setting rather than a rebuild.

---

## 5. Three requirements

### 5.1 Suppress the webhook for account owners

The device owner registers in the app like any other user. Their CRM contact already arrives from Shopify with its own onboarding sequence attached.

If an owner registration fires Endpoint 1, that person receives a second welcome sequence written for someone joining an already-installed device, which reads as though we do not know who they are.

**Preferred:** do not fire Endpoint 1 at all for the account owner.
**Acceptable:** always fire, and set `is_owner: true` so we can filter.

Suppressing at the source is more reliable than filtering downstream.

### 5.2 Send empty strings, never omit keys

If a field has no value, send `"vitamin_d_level": ""`. Do not drop the key.

The CRM's field mapper binds to a fixed payload shape. A missing key can silently fail to map rather than mapping as blank, which produces no error and a quietly incomplete contact record. This is known behavior on our side, not a hypothetical.

### 5.3 Keep field names stable after go-live

Each field name is bound individually inside CRM automations. Renaming one after launch breaks that binding silently, with no error raised. If a name needs to change, tell us before you deploy.

---

## 6. Delivery and reliability

- **Timeout:** treat no response within 10 seconds as a failure.
- **Retries:** please retry failed deliveries with exponential backoff, roughly 1 minute, 5 minutes, 30 minutes, then stop. A dropped registration means a user never gets a welcome, and nothing on our side detects the omission.
- **Ordering:** not required. Session events are idempotent on our side.
- **Duplicates:** safe. A repeated session event for the same user is harmless.
- **Auth:** the CRM's inbound webhook URLs carry a secret path segment and require no auth header. Treat the URLs as credentials: do not commit them to a public repository or include them in client-side code.

---

## 7. Testing

We will supply two test URLs alongside the production pair.

Please send one sample payload per endpoint before wiring the live events, so we can confirm field mapping end to end. We will verify each field landed on the contact record and confirm back.

Useful test cases:
1. New user on a home unit, with vitamin D level present
2. New user at a commercial facility, vitamin D level empty
3. An account owner, to confirm suppression
4. A session event for an existing user
5. A session event carrying an updated vitamin D level

---

## 8. What Enyrgy provides

- Production URL, Endpoint 1
- Production URL, Endpoint 2
- Test URL for each

---

## 9. Open questions for Outcode

1. Does the app currently capture explicit email consent at registration, distinct from using email as the login identifier? If so, what is the exact wording the user agrees to?
2. Can the app distinguish the account owner from an added user at registration time?
3. Is `vitamin_d_level` user-entered, imported from lab results, or both? Knowing the provenance matters for how we present it.
4. For commercial units, is `facility_name` already stored, or would that need adding?
5. What is your estimated timeline once this spec is agreed?
