# Artzy4u — Tech Stack Reference

| | |
|---|---|
| **Brand** | Artzy4u — the artwork of **Diana Jones**, Tulsa OK |
| **Compiled** | August 2, 2026 — all values verified live from public DNS, RDAP and HTTP |
| **Scope** | Every domain in the estate, plus the adjacent/dormant ones |
| **Maintained by** | Stephanie Jones |

> Verify before trusting. Everything here was read from live sources on the date
> above, not from memory. Registrars and DNS providers change; re-run the checks
> in **Appendix A** rather than assuming this file is current.

---

## 1. Umbrella core

The three properties the brand actually points at.

| Domain | Registrar | Expires | DNS | Web host | Email |
|---|---|---|---|---|---|
| **artzy4u.com** | Name.com | 2027-07-06 | Netlify DNS (p06) | **Netlify** + GitHub CD | Google Workspace *(alias domain)* |
| **artsy4y.com** | Tucows *(via Squarespace reseller)* | 2027-07-26 | ⚠ Netlify **+** Squarespace — **8 NS, split** | **Squarespace** — RESIST! catalog | none |
| **3rdworldart.art** | Name.com | 2027-07-24 | Netlify DNS (p01) | **Netlify** + GitHub CD | none |

```
artzy4u.com  —  "Artwork by Diana Jones"
├── 3rd World Art          → 3rdworldart.art   (hand embroidery)
└── Ornaments & Originals  → artsy4y.com       (RESIST! catalog)
```

---

## 2. Adjacent — live and yours, not linked from the umbrella

| Domain | Registrar | Expires | DNS | Web host | Email |
|---|---|---|---|---|---|
| **artsy4u.com** | Squarespace Domains | 2028-04-02 | Squarespace DNS | **Squarespace** — "Artsy4u by Desigb" landing page | **Google Workspace — PRIMARY DOMAIN** |
| **adopteesherpa.online** | *(no RDAP)* | — | Google Cloud DNS | Squarespace — **401**, password-gated | none |
| **jenifersamort.life** | Name.com | 2027-06-27 | Netlify DNS (p03) | **Netlify** — "Amortization Schedule" | none |

> `artsy4u.com` is the **Google Workspace primary domain**. `artzy4u.com` is an
> alias *of it*. Breaking artsy4u.com's mail breaks both addresses at once.

---

## 3. Dormant or dead

| Domain | Registrar | Expires | DNS | Web host | Email |
|---|---|---|---|---|---|
| **artzy4u.studio** | Squarespace Domains II | 2027-03-06 | Google Cloud DNS | ❌ **404** — site subscription expired | **Mailgun** |
| **artzy4ugroup.com** | Squarespace Domains | 2027-03-06 | Google Cloud DNS | ❌ **404** — redirects into .studio | none |
| **stephanieajones.info** | Tucows | 2027-05-16 | **Hover** (2 NS) | ❌ nothing serving | **Hover hosted email** |

**Decided 8/2:** let `artzy4u.studio` and `artzy4ugroup.com` **expire**. Domains
are paid through Mar 2027; the *site* subscription behind them already lapsed.

> ⚠ `artzy4u.studio` carries **Mailgun MX** and a forward from
> `stephanieajones@artzy4u.studio` → `dolan.todar@gmail.com`. That address dies
> with the domain. Set a reminder before **Mar 6, 2027** to disable auto-renew
> deliberately rather than by surprise.

---

## 4. Stack summary

| Layer | Providers |
|---|---|
| **Registrars** | Name.com (3) · Squarespace (3) · Tucows (2) |
| **DNS** | Netlify DNS (4) · Google Cloud DNS (3) · Squarespace DNS (1) · Hover (1) |
| **Web hosting** | Netlify (3, all git-linked) · Squarespace (4: 1 live, 2 dead, 1 gated) |
| **Email** | Google Workspace (2) · Mailgun (1) · Hover (1) |

**9 domains · 4 registrars · 4 DNS providers · 2 web platforms · 3 mail systems.**

---

## 5. Mail authentication

| Domain | SPF | DKIM | DMARC |
|---|---|---|---|
| **artsy4u.com** *(Workspace primary)* | ✅ `include:_spf.google.com` | ✅ 2048-bit | ✅ `p=none` |
| **artzy4u.com** *(alias domain)* | ✅ `include:_spf.google.com` | ✅ 2048-bit | ✅ `p=none` |
| **artzy4u.studio** *(Mailgun)* | ✅ `include:mailgun.org` | ❌ none | ❌ none |
| stephanieajones.info *(Hover)* | not audited | not audited | not audited |

### Fixed 8/2/2026

`artsy4u.com`'s SPF authorized **Cloudflare and Zoho** while its mail ran on
Google — every outgoing message failed SPF, and there was no DKIM at all.
Both corrected, plus DMARC added to both Workspace domains.

### ⚠ DKIM keys are per-domain — never share one

Each domain gets its own keypair from Google. Publishing domain A's public key
under domain B makes B's signatures fail validation. This happened on 8/2 and
was rolled back.

**Current correct keys:**

| Domain | Key begins |
|---|---|
| artzy4u.com | `…CAQEA141gZnG…` |
| artsy4u.com | *(its own, distinct)* |

**Rollback value for artzy4u.com** if it's ever overwritten again:

```
v=DKIM1;k=rsa;p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA141gZnGAQUhmiLVch2j495znJs5nsEwYujJStCcHI8kPk3uEU/R5nfcS0FcJYeMK7DL9M3kC7IfcEcez8n8w+jmnHyeeL4gdxcktzxRVapzrwiP+T8E0eLINWirZJbVYDipvoDTRMZeESArxPrBYfYoNtyxrXYNHfE5BAkiGnHRDOzgMPCslZsLmCIq3PyaT1yfPY2PNBsA1OE61w0eLnCNkW142DhKeJ9Z7UzwEKm8XfVr9L2Y7C2U7l/1SWVX7OWOkV7ocaJ19UE5rgE6+uzk39u+dGGBdlC2mgIG3Nvv5zFWEnnRnzEvmOfr0R5vhddmwRFVMsAWntAuJr/UjwQIDAQAB
```

> **Never click "Generate new record"** in Google Admin unless you intend to
> republish. Each generation invalidates the previous key. Three keys were
> generated in one sitting on 8/2 chasing this.

---

## 6. Open faults

| # | Fault | Impact | Fix location |
|---|---|---|---|
| 1 | **artsy4y.com — 8 nameservers**, 4 pointing at an orphaned Netlify DNS zone | Resolvers pick at random; half get a zone with no answer. Works by luck | Registrar. Saved 8/2 8:44 AM but hadn't reached the `.com` registry — **re-verify** |
| 2 | artzy4u.studio + artzy4ugroup.com serve **404** | Two dead domains | Squarespace billing — decided to let expire |
| 3 | artzy4u.studio has **Mailgun mail, no DKIM/DMARC** | Unauthenticated mail | Google Cloud DNS |
| 4 | **artsy4u.com unreferenced** by the umbrella since the shop card was pointed at RESIST! | A landing page nobody links to | Decide: redirect, repurpose, or retire |

### The orphaned NS1 zone (fault 1)

A Netlify DNS zone exists on NS1's **p08** pool for `artsy4y.com`. It is **not
visible in either Netlify login** (`stephanie@paragontulsa.com` or
`dolan.todar@gmail.com`) — checked both. It's a leftover that outlived whatever
site owned it, and neither account can delete it.

**It does not need deleting.** It only matters because the registrar delegates
to it. Remove those four nameservers and it becomes inert.

---

## 7. Accounts and access

| System | Account | Notes |
|---|---|---|
| **Netlify** | `stephanie@paragontulsa.com` | Owner of **both** teams: `stephanie-paragontulsa-com` and `dolan-todar` (personal). Artzy4u sites live on **dolan-todar** |
| **Netlify (2nd login)** | `dolan.todar@gmail.com` | Same zones visible. `netlify switch --email` to change |
| **GitHub** | `Artsy4U` owns the repos | ⚠ This machine's git credential is **StephanieAtParagonTulsa**. Pushing to an Artsy4U repo needs that account as **collaborator** *and* the invite **accepted** (`gh api user/repository_invitations` → PATCH id). Adding without accepting still 403s |
| **Squarespace** | account under **"Diana"**, `diana-iwanski.squarespace.com` | Notices addressed "Hello Diana". Login email moved off the dead `diwanski@cfl.rr.com` to `dolan.todar@gmail.com` before it died — verification codes confirmed delivering there |
| **Google Workspace** | admin of `artsy4u.com` | `artzy4u.com` is a verified alias domain |

### ⚠ Squarespace has no customer DNS API

An agent **cannot** automate Squarespace DNS edits with any credential — the
product doesn't expose them. Same for Google Workspace DKIM generation. Those
are always manual console work. Only **Netlify DNS** zones are automatable.

---

## 8. Repositories

| Repo | Serves | Deploy |
|---|---|---|
| `github.com/Artsy4U/Artzy4u-artzy4u` | artzy4u.com | Netlify CD on `main`, publish `.`, no build |
| `github.com/Artsy4U/3rdworldart` | 3rdworldart.art | Netlify CD on `main` |

Local: `C:\Users\stephanie\artzy4u` · `C:\Users\stephanie\3rdworldart`

### ⚠ The `.netlify/state.json` footgun — twice now

A `state.json` at `C:\Users\stephanie\.netlify\` was inherited by **every
subdirectory**, so `netlify status` inside `artzy4u/` reported the wrong site.
A `netlify deploy --prod` from there would have **published one site over
another**. Held the Paragon PROD id on 7/24; held 3rdworldart's id on 8/1.

**Fixed:** each repo now has its own `.netlify/state.json`; home-level file
removed (backup `~/.netlify/state.json.bak-20260801`).

**Always pass `--site <id>` explicitly on CLI deploys.**

### ⚠ NS1 propagation lag on Netlify DNS zones

Netlify's API accepts record changes instantly; NS1's edge nodes lag —
observed **4 minutes** (apex ALIAS), **8+ minutes** (DKIM TXT), and **~40
minutes** (MX RRset, 7/24). Netlify's API is the source of truth. Don't
delete-and-recreate repeatedly to force it — that's how an invalid apex CNAME
got published on 8/1.

---

## Appendix A — re-verify this document

```bash
# registrar + expiry
curl -s -L "https://rdap.org/domain/DOMAIN" | python -m json.tool

# DNS provider / mail / serving
curl -s -H 'accept: application/dns-json' "https://dns.google/resolve?name=DOMAIN&type=NS"
curl -s -H 'accept: application/dns-json' "https://dns.google/resolve?name=DOMAIN&type=MX"
curl -sL -o /dev/null -w "%{http_code}\n" "https://DOMAIN/"

# registry delegation — bypasses resolver caches, use for nameserver changes
# (PowerShell)
Resolve-DnsName DOMAIN -Type NS -Server a.gtld-servers.net
```

Public resolvers cache; the `.com` registry and the authoritative nameservers
do not. When a change "isn't working," check the authoritative source before
concluding it failed.
