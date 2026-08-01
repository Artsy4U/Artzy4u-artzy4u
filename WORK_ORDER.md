# WORK ORDER — artzy4u.com

| | |
|---|---|
| **Project** | Artzy4u — umbrella brand site |
| **Site** | artzy4u.com (Netlify, personal account) |
| **Repo** | `github.com/Artsy4U/artzy4u` — **public** (not yet created) |
| **Scope** | Stand up the front-door site; 3rdworldart.art becomes a line inside it |
| **Method** | Static HTML, no build step, no framework — same as 3rdworldart |
| **Issued** | August 1, 2026 |

---

## Item 100 — Scaffold ✅ DONE 8/1

Local repo at `C:\Users\stephanie\artzy4u`: `index.html`, `netlify.toml`,
`.gitignore`, `README.md`, `favicon.ico`, `images/` with hero + embroidery
thumbnail. Committed locally on `main`.

---

## Item 200 — Content review — **OPEN, needs Stephanie**

The scaffold ships with only what is already known to be true: the
recycle/reuse/repurpose statement, and 3rd World Art as one line of work.
Nothing else was invented.

Decide and supply:

| # | Question |
|---|---------|
| 201 | Is the wordmark **Artzy4u** correct as displayed — capital A, lowercase rest, "4u" in mulberry? |
| 202 | What other lines belong here besides embroidery and the shop? Each needs a name, one sentence, and a photo |
| 206 | **The Shop card has no product photo** — it renders a styled `.shot--sign` panel as a stand-in. Drop a real product shot into `images/` and replace it |
| 207 | Is "The Shop" the right card title, given the umbrella is Artzy4u and the shop is Artsy4u? Two spellings on one page may confuse visitors |
| 203 | Is the tagline right — "Art made from materials that already had a life"? |
| 204 | Does the statement block read in your voice, or should it be rewritten the way 502 was on the other site? |
| 205 | Hero photo — currently the denim flowers. Better one? |

---

## Item 300 — Create repo + push — **OPEN, needs decision**

Repo does not exist yet. Create under `Artsy4U` (personal GitHub) to match
3rdworldart, public, no template files.

**Do not** create it under `StephanieAtParagonTulsa` or any Paragon org — the
last time that happened on 3rdworldart, Netlify-personal's GitHub identity
didn't match and the deploy key 404'd until the repo was transferred.

---

## Item 400 — Netlify site + domain — **PARTIAL**

### ✅ Project created 8/1

| | |
|---|---|
| Name | `artzy4u` |
| Site ID | `c2e7bc85-b433-492a-8d6d-7fbbaf90bb57` |
| Team | `dolan-todar` ("Stephanie Jones", personal) |
| URL | `https://artzy4u.netlify.app` |

### ⬜ Continuous deployment — needs Stephanie

Requires an interactive GitHub OAuth grant, which an agent cannot complete.

`https://app.netlify.com/projects/artzy4u/configuration/deploys`
→ Link repository → GitHub → `Artsy4U/Artzy4u-artzy4u`
→ branch `main`, build command blank, publish `.` (all already in netlify.toml)

### ✅ Deployed 8/1 (direct CLI deploy, pending CD link)

`netlify deploy --prod --dir . --site c2e7bc85-…` → live.

### ✅ Domain attached 8/1 — artzy4u.com

`netlify api updateSite` → `custom_domain=artzy4u.com`,
`domain_aliases=["www.artzy4u.com"]`. Netlify DNS auto-created both web records
as `NETLIFY`-type ALIAS (they serve **A** records — querying CNAME returns
nothing; that's normal, not a fault).

**Email records verified intact before AND after the attach:**

| Record | Status |
|---|---|
| MX `1 smtp.google.com.` / `5 aspmx.l.google.com.` | ✅ unchanged |
| TXT `v=spf1 include:_spf.google.com ~all` | ✅ unchanged |
| TXT `google-site-verification=bEW8jI92…` | ✅ unchanged |
| TXT `google._domainkey` DKIM | ✅ unchanged |

TLS: Let's Encrypt `CN=artzy4u.com`, issued 8/1, expires 10/30/2026. Cert took
~30s after DNS resolved; `provisionSiteTLSCertificate` returns null and is not
needed — Netlify issues automatically.

**Smoke test passed:** apex 200 · www 301→apex · http 301→https · all assets
200 · netlify.toml cache headers applied.

### ⚠ FOOTGUN FOUND AND FIXED 8/1 — read before any future CLI deploy

`C:\Users\stephanie\.netlify\state.json` held **3rdworldart's** site ID. It sat
in the **home** directory, so every subfolder inherited it — `netlify status`
run inside `artzy4u/` reported "Current project: 3rdworldart". **A
`netlify deploy --prod` from the artzy4u folder would have published Artzy4u
over 3rdworldart.art.**

Fixed: wrote an explicit `3rdworldart/.netlify/state.json`, removed the home
one (backup `~/.netlify/state.json.bak-20260801`), linked artzy4u to its own
site. Both repos now resolve correctly and `.netlify/` is gitignored in each.

This is the second recurrence of this footgun (first was 7/24, holding the
Paragon PROD id). **Always pass `--site <id>` explicitly on CLI deploys.**

Then attach `artzy4u.com` — apex primary, `www` redirecting to it.

> ⚠ **The artzy4u.com zone carries live Google Workspace email.** MX, SPF,
> DKIM and the site-verification TXT are all serving. Attaching the domain
> adds web records alongside them, which is safe. If any wizard or prompt
> offers to *reset* or *replace* the zone's records, stop — that would take out
> the email path. Web records only.

---

## Item 500 — Cross-link — ✅ **DONE 8/1**

3rdworldart.art's statement block now links its "Artzy4u.com" mention to
`https://artzy4u.com` (commit `8e5ef1a`, auto-deployed via CD). Styled mulberry
+ underline so it reads as a link against the calico panel.

Round trip verified live: portfolio → umbrella → portfolio, both 200.

---

## Item 700 — artsy4u.com — ✅ **RESOLVED 8/1**

### ⚠ The original decision was REVERSED — read this before acting

**Superseded:** "once artzy4u.com is live, artsy4u.com redirects to it."

That was decided while the evidence said artsy4u.com fed a parked ad lander with
nothing behind it. **It doesn't.** artsy4u.com is a **live Squarespace
storefront** — "Artsy4u by Desigb", with products, a cart and services:

- **I Resist! Ornament Series** — "Read Banned Books Penguin Ornament", $15.00
- **Originals & Collectibles** shop section
- Custom Commission · Space Curation · Art Installation

**Redirecting it would have taken the store offline.**

**Decided 8/1 (revised):** artsy4u.com **stays as the shop**. artzy4u.com links
to it as a second line of work, alongside 3rd World Art. No redirect.

```
artzy4u.com  (umbrella brand)
├── 3rdworldart.art   — hand embroidery portfolio
└── artsy4u.com       — Artsy4u shop
```

### The redirect fault — FIXED 8/1 by Stephanie

Was: `https://artsy4u.com` → **301 → `https://www.artsy4y.com/`** (a parked
lander). The rule lived in the connected Squarespace **site's URL Mappings**,
not in Domain settings — which is why it wasn't where we first looked. The DNS
gave it away: apex A `198.185.159.145` / `198.49.23.144` + `www` CNAME
`ext-cust.squarespace.com` = a domain connected to a Squarespace *site*.

**Verified fixed:** apex now 301s to its own `www.artsy4u.com`, which returns
200. `Age: 0` on both — fresh, not cached. Store is serving.

| Fact | Value |
|---|---|
| artsy4u.com nameservers | `nsd1-4.squarespacedns.com` — **Squarespace, not Netlify** |
| Redirect served by | `Server: Squarespace` |
| artsy4u.com MX | full Google set (`aspmx.l.google.com` + alts) — **healthy, untouched** |
| Netlify project "artsy4u.com" | **orphaned** — named for the domain but not serving it; April Netlify Drop, unreviewed content |

### Ownership — RESOLVED 8/1

Stephanie **owns artsy4y.com**. Not a stranger's domain. But it is *not* on
Squarespace as she recalled — RDAP says **Tucows**.

### The domain estate (RDAP, verified 8/1/2026)

| Domain | Registrar | Registered | Expires | Nameservers |
|---|---|---|---|---|
| artsy4y.com | Tucows | **2013-07-26** | 2027-07-26 | `ns1/ns2.renewyourname.net` ⚠ |
| artsy4u.com | Squarespace Domains | 2025-04-02 | 2028-04-02 | Squarespace DNS |
| artzy4u.com | Name.com | 2026-07-06 | 2027-07-06 | Netlify DNS (p06) |
| 3rdworldart.art | Name.com | 2026-07-24 | 2027-07-24 | Netlify DNS (p01) |

Four domains, **three registrars, two DNS providers, multiple accounts.**

### Root cause of the parked page — CONFIRMED 8/1 from Gmail history

Not an inference any more. The mail trail in `dolan.todar@gmail.com` proves it:

| Date | Event |
|---|---|
| 2025-08-13 | Squarespace **"Card Billing Failure"** — sites Artsy4U + supply.artsy4y |
| 2025-09-13 | **"Card Billing Failure"** again, both sites |
| 2025-10-21 | **"You've disabled auto-renew"** confirmation |
| 2026-06-27 | "artsy4y.com expires Jul 26, 2026" |
| 2026-07-12 | Same reminder, unread |
| 2026-07-26 | Expired → Tucows parking (`renewyourname.net`) |
| 2026-07-30 | Renewed (RDAP last-changed) — **nameservers never restored** |

Auto-renew was switched off ~10 months prior with a failing card on file, and
four warnings went to an inbox nobody was watching.

### WHERE IT ACTUALLY LIVES — corrected

Earlier note said "Tucows, not Squarespace." **That was wrong in the way that
matters.** Both are true:

- **Tucows** = registrar of record (what RDAP shows)
- **Squarespace** = the **reseller** — the account that bills and notifies

Stephanie's recollection of "a different Squarespace account" was **correct**.

The account is under a different identity, which is why it never surfaced:

| | |
|---|---|
| Addressed to | "Hello **Diana**" |
| Account email | `diwanski@cfl.rr.com` (forwarded to dolan.todar@gmail.com) |
| Squarespace account | `diana-iwanski.squarespace.com` |

### FULL DOMAIN ESTATE — verified 8/1/2026 (RDAP + DNS + mail history)

| Domain | Registrar | Expires | DNS | Web | Email |
|---|---|---|---|---|---|
| artsy4y.com | Tucows *(via Squarespace)* | 2027-07-26 | `renewyourname.net` parking ⚠ | ad lander | — |
| artsy4u.com | Squarespace Domains | 2028-04-02 | Squarespace | 301 → artsy4y ⚠ | Google Workspace (PRIMARY) |
| artzy4u.com | Name.com | 2027-07-06 | Netlify DNS p06 | nothing | Google alias domain (pending) |
| artzy4u.studio | Squarespace Domains II | 2027-03-06 | Google Cloud DNS | 301 → www | **Mailgun** |
| 3rdworldart.art | Name.com | 2027-07-24 | Netlify DNS p01 | ✅ live site | — |

**Five domains · four registrar entities · four DNS providers · three email
systems.** artsy4u.com was transferred INTO Squarespace 5/27–6/2/2026.

### Account access — RESOLVED 8/1

Recovery works. Squarespace sent a **login verification code to
`dolan.todar@gmail.com`** on 2026-05-28. The account email was moved off
`diwanski@cfl.rr.com` before it died. Notices still open "Hello Diana" — stale
contact *name* only, not a routing problem.

### ⚠ CREDENTIALS EXPOSED IN THE GMAIL INBOX — handle first

| Date | Subject | Risk |
|---|---|---|
| 2026-05-28 | "Your Domain Authorization Code" (artzy4u.studio) | Plaintext auth code — permits transfer of the domain to another registrar |
| 2026-05-27 | "Google Workspace Email Invitation" (diana@artsy4u.com) | Plaintext temporary password — possibly an unclaimed mailbox on the primary domain |

Rotate the Workspace password; regenerate/lock the auth code unless a transfer
is actually in flight.

### Squarespace sites also on that billing

| Site | URL | Plan |
|---|---|---|
| "Artsy4U" / later "RESIST!" | `artsy4u.squarespace.com` | $25.00 Basic |
| "supply.artsy4y" | `diana-iwanski.squarespace.com` | Basic |

Both had failed payments in 2025. **Audit before renewing anything** — these may
be paid subscriptions on properties that no longer serve the brand.

### Follow-on risks

- **artsy4y.com is the oldest domain by 12 years** — likely the original brand,
  may carry inbound links and history. Item 700 routes traffic away from it,
  but keep it registered and pointed somewhere sane rather than retiring it.
- **Three domains expire July 2027 across three separate accounts.** One just
  lapsed unnoticed. Put all four on auto-renew; consider consolidating
  registrars to one login.
- **Orphaned Netlify project "artsy4u.com"** — named for the domain but not
  serving it; April Netlify Drop, financial-dashboard thumbnail. Review
  contents before deleting.

### The fix

The redirect lives in **Squarespace**, not Netlify — nothing in the Netlify UI
will change it. Repoint it from `www.artsy4y.com` to `artzy4u.com`.

> ⚠ Change the **web redirect only**. Do not touch artsy4u.com's MX records —
> that domain is the Google Workspace primary, and artzy4u.com is an alias
> *of it*. Breaking artsy4u.com's mail breaks both addresses at once.

---

## Item 600 — Email flip — **OPEN, gated**

When `stephanie@artzy4u.com` is confirmed receiving, flip the contact address
on **both** sites in the same pass:

- `artzy4u/index.html` — contact button href + label
- `3rdworldart/index.html:251` — contact button href + label
