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
| 202 | What other lines of work belong here besides embroidery? Each needs a name, one sentence, and a photo |
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

## Item 400 — Netlify site + domain — **OPEN**

New Netlify project on the **personal** team (dolan.todar@gmail), same team as
3rdworldart. Link the repo, branch `main`, build command blank, publish `.`.

Then attach `artzy4u.com` — apex primary, `www` redirecting to it.

> ⚠ **The artzy4u.com zone carries live Google Workspace email.** MX, SPF,
> DKIM and the site-verification TXT are all serving. Attaching the domain
> adds web records alongside them, which is safe. If any wizard or prompt
> offers to *reset* or *replace* the zone's records, stop — that would take out
> the email path. Web records only.

---

## Item 500 — Cross-link ✅ *pending 400*

Once artzy4u.com is live, add a link on 3rdworldart.art pointing back to the
umbrella brand — the statement block already names Artzy4u.com in text but
doesn't link it.

---

## Item 600 — Email flip — **OPEN, gated**

When `stephanie@artzy4u.com` is confirmed receiving, flip the contact address
on **both** sites in the same pass:

- `artzy4u/index.html` — contact button href + label
- `3rdworldart/index.html:251` — contact button href + label
