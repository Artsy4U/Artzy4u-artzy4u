# Artzy4u — request queue

Updated 8/3/2026. Newest decisions at the top of each section.

---

## 🔴 Blocking — a live defect

**Shop chip on artzy4u.com routes in a circle.** `artsy4y.com` 301s back to
`www.artzy4u.com`, so the RESIST! catalog is unreachable by anyone. Path-preserving,
served by Squarespace ⇒ a **URL Mappings wildcard**, not domain forwarding.

→ **Full walkthrough: `FIX_SHOP_ROUTE.md`.** One line to delete at
`artsy4u.squarespace.com/config/` → Settings → search "URL Mappings".
Verify in **incognito** — a 301 caches hard and will look like the fix failed.

*Owner: Stephanie · Squarespace console · ~5 min*

---

## 🟡 Waiting on you — content

| # | Item | What I need |
|---|---|---|
| 1 | **More product lines** for artzy4u.com | Name · one sentence · does it link anywhere · a photo |
| 2 | **Yellow hoop Fucktastrophy photo** | The original. Only have a Facebook screenshot (405×640, FB chrome) — deliberately not published. Slots straight into the existing gallery |
| 3 | **Contact address** | Site says the artwork is Diana's; the email is `stephanie@artzy4u.com`. Fine if intentional — but a visitor will notice |

---

## 🟢 Maintenance — not urgent

- **artsy4y.com nameservers**: 8 delegated, 4 to an orphaned NS1 zone nobody can
  reach. Both zones currently serve *identical* records, so nothing is broken —
  but only the Squarespace one is editable, so future edits will drift.
  Verify with `Resolve-DnsName artsy4y.com -Type NS -Server a.gtld-servers.net`,
  **not** a public resolver.
- **Check artsy4u.com's URL Mappings** — a rule was deleted there 8/2; if these
  were created together there may be a fresh one.
- **artzy4u.com DKIM** — key was restored 8/2 after one domain's key got
  published under the other. Confirm the two domains' keys differ.
- **artzy4u.studio + artzy4ugroup.com** — decided 8/2 to let expire. Paid through
  **Mar 6 2027**. ⚠ `.studio` carries Mailgun MX and forwards
  `stephanieajones@artzy4u.studio` → dolan.todar@gmail.com; that address dies
  with the domain. Set a reminder before renewal.

---

## ✅ Done — don't re-open

- artzy4u.com built, deployed, TLS, CD linked to GitHub *(8/1–8/2)*
- Mail authentication complete on artzy4u.com **and** artsy4u.com — SPF, DKIM,
  DMARC. The primary was failing SPF on every message and had no DKIM at all
- Contact address flipped to `stephanie@artzy4u.com` on both sites
- Cross-links live both directions
- Fucktastrophy grouped into one entry with a photo gallery
- Artist credited as **Diana Iwanski-Jones**
- Shop card points at RESIST! and carries the real catalog details
- **artsy4u.com is a live store — do not redirect it.** Decided, reversed once,
  settled
