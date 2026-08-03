# CLAUDE.md — Artzy4u

> Working context for Claude Code. Auto-loaded from `C:\Users\stephanie\artzy4u`.
> **This is Stephanie's personal art business. It is NOT Paragon work.**

If a request is about crew scheduling, WIP, bids, contracts, ODOT, HeavyBid, or
anything Paragon Contractors — **you are in the wrong folder.** That work lives
in `C:\Users\stephanie\paragon-deploy`, which has its own CLAUDE.md and its own
memory. Keeping them apart is deliberate.

---

## What this is

**Artzy4u** is the umbrella brand for the artwork of **Diana Iwanski-Jones**
(Tulsa, OK) — recycle, reuse, repurpose. Stephanie runs the web presence and the
inbox; Diana makes the work.

```
artzy4u.com  — umbrella front door        (Netlify + GitHub CD, this repo)
├── 3rdworldart.art       — hand embroidery portfolio   (Netlify + GitHub CD)
└── artsy4y.com "RESIST!" — the shop catalog            (Squarespace)
```

`artsy4u.com` is a separate live Squarespace landing page, no longer linked from
the umbrella. Don't redirect it — it's a working store, and that decision was
made and reversed once already.

## Read these first

| File | What it holds |
|---|---|
| `NEXT_SESSION.md` | **Paste-ready resume prompt** + content conventions + a "do not re-open" list |
| `STACK_REFERENCE.md` | Full estate: 9 domains, 4 registrars, 4 DNS providers, 3 mail systems |
| `FIX_SHOP_ROUTE.md` | Open defect — the shop chip loops. Step-by-step fix |
| `WORK_ORDER.md` | Build history, Items 100–700 |
| `DOMAIN_PUNCHLIST.md` | DNS/mail punch list, mostly closed |
| `QUEUE.md` | What's next |

## Repos

| Repo | Local | Serves |
|---|---|---|
| `Artsy4U/Artzy4u-artzy4u` | `C:\Users\stephanie\artzy4u` | artzy4u.com |
| `Artsy4U/3rdworldart` | `C:\Users\stephanie\3rdworldart` | 3rdworldart.art |

Edit the sibling repo by absolute path — no need to switch sessions.

**Push to `main` = deploy.** Both are Netlify git-linked, live in ~15 seconds.

## Conventions

- **Static HTML only.** One `index.html` per site, inline `<style>`, no framework,
  no build step, no npm.
- **Photos:** raw drops go in gitignored `originals/`; `python tools/resize-photo.py "originals/IMG.jpg" line-NAME`
  produces `images/line-NAME.jpg` (long side 1800, q82, EXIF applied and stripped).
  **Never** put a raw phone photo in `images/` — that folder ships as-is.
- **Palette:** `--indigo #1E3145` · `--calico #E9E0CC` · `--hoop #F0BE2A` ·
  `--floss #3A7FA6` · `--mulberry #8C3F63` · `--leaf #7FAE3E`
- **Type:** Fraunces (display) + Archivo (body), Google Fonts — the only external dependency.
- **The two sites are deliberately inverted:** artzy4u.com is indigo-on-calico,
  3rdworldart.art is calico-on-indigo. Same family, not duplicates. Keep it.
- **Alt text is required** on every image, describing the actual piece.
- **Verify before pushing:** `python -m http.server 8125`, check console and 375px.
  Every push is live.

## Traps that have already cost time

1. **Four lookalike domains** — artzy4u.com, artsy4u.com, artsy4y.com,
   artzy4u.studio. Most wasted time this project has been acting on the wrong
   one. Confirm which domain a screen refers to before changing anything.
2. **artzy4u.com must never be connected to Squarespace.** Its DNS is on Netlify
   and its Google Workspace MX/SPF/DKIM live in that zone. Squarespace's
   domain-connect screen shows all-red for it — that is *correct*. Following it
   would take the site down and break `stephanie@artzy4u.com`.
3. **Squarespace has no DNS API.** Those edits are always manual console work,
   no credential changes that. Only Netlify DNS zones are automatable.
4. **`.netlify/state.json` inheritance** — a stray one in the home directory made
   `netlify status` report the wrong site from inside a repo. Bit twice. Always
   pass `--site <id>` on CLI deploys.
5. **NS1 lag** — Netlify's API accepts DNS changes instantly; NS1 edge nodes have
   taken 4–40 minutes. Check the authoritative nameserver or the `.com` registry
   before concluding a change failed. Public resolvers cache and will mislead you.
6. **DKIM keys are per-domain.** Publishing one domain's key under another breaks
   signing silently. Never click "Generate new record" unless you intend to
   republish — each generation invalidates the last.

## Git identity

This machine's credential is `StephanieAtParagonTulsa`, **not** `Artsy4U`.
Pushing to an Artsy4U repo needs that account added as a collaborator **and the
invitation accepted** (`gh api user/repository_invitations` → PATCH the id).
Adding without accepting still 403s.
