# DOMAIN PLUMBING — PUNCH LIST

| | |
|---|---|
| **Issued** | August 2, 2026 |
| **Scope** | DNS / nameservers / mail authentication across the domain estate |
| **Not in scope** | Website rebuilds. No site content changes. |
| **Estate** | 9 domains · 4 registrars · 4 DNS providers · 3 mail systems |

---

## Read this first — why you can't hand off the Squarespace parts

**Squarespace has no customer DNS API.** Giving me an account login would not
let me automate those edits — the product simply doesn't expose them. Same for
Google Workspace DKIM generation, which is a console action.

So the split is:

| I can automate | You must click |
|---|---|
| Anything in a **Netlify DNS** zone (artzy4u.com, 3rdworldart.art) | Anything in **Squarespace DNS** (artsy4u.com, artsy4y.com) |
| Verification of every change, from outside | Google Workspace admin console |
| | Registrar nameserver changes |

The only way to move Squarespace items into the automatable column is to
migrate those zones to Netlify DNS — see **Item 6**, which is optional and
deliberately last.

---

## ✅ Item 0 — DMARC on artzy4u.com — **DONE 8/2, automated**

Added to the Netlify zone:

```
_dmarc.artzy4u.com   TXT   v=DMARC1; p=none; rua=mailto:stephanie@artzy4u.com; fo=1
```

`p=none` is monitor-only — it changes no delivery behavior, it just starts
collecting reports. Reports land at `stephanie@artzy4u.com`, so they'll only
arrive once **Item 5** (the alias-domain test) is finished.

---

## ✅ Item 1 — SPF on artsy4u.com — **DONE 8/2, VERIFIED**

Now serving, authoritative and public agree:
`v=spf1 include:_spf.google.com ~all` — **exactly one** SPF record, no
Cloudflare/Zoho remnants.

## ✅ Item 2 — DKIM on artsy4u.com — **DONE 8/2, DNS VERIFIED**

`google._domainkey.artsy4u.com` — 410 chars, `v=DKIM1; k=rsa; p=…`, full
2048-bit key, not truncated. Authoritative and public resolvers agree.

⚠ Unverifiable from outside: whether **Start authentication** was clicked in
Google Admin. The record existing does not make Google sign mail — the toggle
does. Confirm the Authenticate email page reads "Authenticating email".

## ✅ Item 2b — DMARC for artsy4u.com — **DONE 8/2, VERIFIED**

`_dmarc.artsy4u.com` → `v=DMARC1; p=none; rua=mailto:stephanie@artsy4u.com; fo=1`
Exactly one record, `p=none` (monitor-only), authoritative and public agree.

### Mail authentication scorecard

| Domain | SPF | DKIM | DMARC |
|---|---|---|---|
| artsy4u.com (Workspace primary) | ✅ Google | ✅ 2048-bit | ✅ p=none |
| artzy4u.com (alias domain) | ✅ Google | ✅ 2048-bit | ✅ p=none |

Both domains fully authenticated as of 8/2/2026.

---

## ~~🔴 Item 1 — Fix the SPF record on artsy4u.com~~ — SUPERSEDED, see above

**The single highest-value fix in this document.** Two minutes.

### The problem

```
Current MX  : aspmx.l.google.com          ← mail runs on Google Workspace
Current SPF : v=spf1 include:_spf.mx.cloudflare.net include:zohomail.com ~all
```

The SPF record authorizes **Cloudflare and Zoho** — leftovers from a previous
mail provider. It does **not** authorize Google. Every message you send from
`stephanie@artsy4u.com` fails SPF, and has been failing for as long as that
record has been there. That is a spam-folder problem, invisible from your end
because *sending* appears to work fine.

### The fix

1. Go to **Squarespace → Domains → artsy4u.com → DNS Settings**.
2. Find the **TXT** record on `@` whose value starts with `v=spf1`.
3. **Edit** it (don't add a second one — a domain must have exactly **one**
   SPF record; two is an error that fails harder than one wrong record).
4. Replace the entire value with:

```
v=spf1 include:_spf.google.com ~all
```

5. Save.

### Why exactly that value

- `include:_spf.google.com` — authorizes Google Workspace's sending servers
- `~all` — "softfail" anything else. Deliberately not `-all`; softfail is the
  safe choice until DKIM and DMARC are in place, because a hard fail can
  bounce legitimate mail you've forgotten about.

### Accept when

Tell me and I'll verify from outside. Should resolve to exactly one SPF record
naming Google and nothing else.

---

## 🔴 Item 2 — Add DKIM to artsy4u.com

**There is currently no DKIM on your primary domain at all.** I checked the
`google`, `selector1`, `selector2` and `s1` selectors — nothing. Outgoing mail
is unsigned as well as unauthorized.

### Part A — generate the key (Google Admin)

1. Go to **admin.google.com**, signed in as an admin of `artsy4u.com`.
2. **Apps → Google Workspace → Gmail → Authenticate email**.
3. Select **artsy4u.com** in the domain dropdown.
4. Click **Generate new record**. Accept the defaults (2048-bit, selector
   `google`).
5. Google shows you a **TXT record name** (`google._domainkey`) and a long
   **value** starting `v=DKIM1; k=rsa; p=…`. Leave this page open.

> ⚠ If the dropdown also lists `artzy4u.com`, **do not regenerate its key.**
> That one already has a working DKIM record published. Regenerating would
> invalidate it.

### Part B — publish it (Squarespace DNS)

6. In **Squarespace → Domains → artsy4u.com → DNS Settings**, add a **TXT**
   record:
   - **Name / Host:** `google._domainkey`
   - **Value:** the entire string Google gave you
7. Save. The value is long (~400 characters) — paste it whole, don't retype.

### Part C — turn it on

8. Back in Google Admin, wait a few minutes, then click **Start
   authentication**.

### Accept when

Google Admin shows "Authenticating email" for artsy4u.com. Tell me and I'll
confirm the DKIM record resolves publicly and parses correctly.

---

## 🟠 Item 3 — Fix artsy4y.com's split nameserver delegation

### The problem

The domain is delegated to **eight** nameservers across two providers:

```
ns01-04.squarespacedns.com   ← correct, holds the real records
dns1-4.p08.nsone.net         ← an ORPHANED Netlify DNS zone
```

That NS1 zone is not in either of your Netlify accounts — I checked both
logins. It's a leftover Netlify created that outlived whatever site owned it.
Neither you nor I can delete it.

**You don't need to delete it.** It only affects you because your registrar
points at it. Remove the delegation and it becomes inert.

Right now resolvers pick a nameserver at random, so roughly half of all lookups
ask a zone that has no correct answer. The site appears to work — that's luck,
not health.

### The fix

1. **Squarespace → Domains → artsy4y.com → Nameservers**.
2. Set the nameservers to **exactly these four, and nothing else**:

```
ns01.squarespacedns.com
ns02.squarespacedns.com
ns03.squarespacedns.com
ns04.squarespacedns.com
```

3. Remove all four `dns1-4.p08.nsone.net` entries.
4. Save.

### Accept when

Only the four Squarespace nameservers appear. Allow a few hours — nameserver
changes propagate more slowly than record changes, and this registrar has been
slow all week. Tell me and I'll verify the delegation is clean and that
artsy4y.com still serves the RESIST! site.

---

## 🟡 Item 4 — Restore artsy4u.com's missing apex A records

Squarespace expects **four** A records on the apex. Only two are published:

| Should be | Present? |
|---|---|
| `198.185.159.144` | ❌ missing |
| `198.185.159.145` | ✅ |
| `198.49.23.144` | ✅ |
| `198.49.23.145` | ❌ missing |

Not urgent — the site works on two. But you've lost half your redundancy: if
Squarespace takes either of those IPs out of service, half of visitors get
nothing.

**Fix:** in artsy4u.com's DNS Settings, add A records on `@` for
`198.185.159.144` and `198.49.23.145`. Leave the existing two alone.

---

## 🟡 Item 5 — Finish the artzy4u.com alias-domain email test

Carried over — still unfinished, and now **Item 0's DMARC reports depend on it.**

DNS has been verified correct and serving for over a week: MX, SPF, DKIM and
the site-verification TXT are all live. What's missing is the console side.

1. **admin.google.com → Account → Domains → Manage domains.** Confirm
   `artzy4u.com` is listed as a **User alias domain** of `artsy4u.com`. If it
   offers **Verify**, click it — the TXT is live, so it passes immediately.
2. **Apps → Google Workspace → Gmail → Authenticate email** → select
   `artzy4u.com` → **Start authentication**. **Do not generate a new key** —
   the published one is yours and regenerating invalidates it.
3. Send a test message from an outside address to `stephanie@artzy4u.com`. It
   lands in the `artsy4u.com` inbox — same mailbox, no separate login.
4. In Gmail, open **Compose → From**. `stephanie@artzy4u.com` should appear as
   a send-as option automatically.

**Then** I flip the contact address on both sites in one pass:
`artzy4u/index.html` and `3rdworldart/index.html:251`.

---

## 🟢 Item 6 — OPTIONAL: migrate artsy4u.com DNS to Netlify

**Only worth doing if you want these edits automatable in future.** It does not
fix anything Items 1–4 don't already fix.

### ⚠ Read before considering

A Netlify DNS zone for artsy4u.com **already exists** (`69ea84118962f73a8e2f1e0e`)
and is **stale and dangerous**. It contains only:

```
NETLIFY  artsy4u.com      → luxury-hummingbird-8be222.netlify.app
NETLIFY  www.artsy4u.com  → luxury-hummingbird-8be222.netlify.app
```

That's the orphaned April Netlify-drop project, and the zone has **no MX
records**. **If anyone switches artsy4u.com's nameservers to Netlify today, the
store goes dark and all mail stops.**

### If you ever do want it

1. Export or screenshot the **complete** DNS record list from Squarespace for
   artsy4u.com. I can only see records I know to query — a blind migration
   would silently drop any subdomain or verification record I don't know about.
2. Send it to me. I'll rebuild the Netlify zone to match exactly, with the SPF
   already corrected and DMARC added.
3. I verify the staged zone against the live one, record by record.
4. Only then do you change nameservers.

Until step 3 passes, do not touch the nameservers.

---

## Standing rule — artzy4u.com and Squarespace

**artzy4u.com is the one domain Squarespace does not manage.** Registrar
Name.com, DNS at Netlify, site in a GitHub repo, Workspace MX/SPF/DKIM in the
Netlify zone.

Squarespace's domain-connect screen will show **all red / Not found** for it.
**That is correct.** It means the domain isn't pointed at Squarespace, which is
the intent. Your Squarespace domain list already labels it accurately:
*"Not connected · Third-party."*

If any Squarespace wizard offers to connect, verify or fix artzy4u.com — **back
out.** Following through takes down the live site and breaks
`stephanie@artzy4u.com`, because the Workspace MX records would not survive the
nameserver move.

---

## Order of work

| Order | Item | Why |
|---|---|---|
| 1 | **Item 1** — SPF | Biggest real cost, smallest effort |
| 2 | **Item 2** — DKIM | Completes mail authentication |
| 3 | **Item 3** — artsy4y nameservers | Removes an unstable delegation |
| 4 | **Item 5** — alias test | Unblocks the email flip and DMARC reports |
| 5 | **Item 4** — apex A records | Redundancy only |
| — | **Item 6** | Optional, and gated on a full record export |

Items 1, 2 and 4 are all in the same Squarespace DNS panel — do them in one
sitting.

After each item, tell me which one you finished and I'll verify it externally
and confirm nothing else regressed.
