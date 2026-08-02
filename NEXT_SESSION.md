# Resume point — artzy4u.com content work

Infrastructure is **done**. What's left is content. Paste the prompt below into
a fresh session to pick up.

---

## Paste this to start

```
Working on artzy4u.com content — the umbrella site for Artzy4u, the artwork of
Diana Jones (Tulsa, OK).

Repo: C:\Users\stephanie\artzy4u   (static HTML, no build step, no npm)
Live: https://artzy4u.com          (Netlify + GitHub CD — push to main = deploy)

Read STACK_REFERENCE.md and WORK_ORDER.md first. Infrastructure, DNS, email and
deploys are all finished and verified — do not re-litigate them. This session is
content only.

The site is one page with two "lines of work" cards. I want to work on content.
```

---

## Where things stand

**Live and working — leave alone:**

- artzy4u.com serving on Netlify, valid TLS, CD linked to
  `github.com/Artsy4U/Artzy4u-artzy4u`. Push to `main` deploys in ~15 seconds.
- Mail authentication complete on artzy4u.com and artsy4u.com (SPF/DKIM/DMARC).
- Contact address `stephanie@artzy4u.com` live on both sites.
- Cross-links working both directions with 3rdworldart.art.

**Current page structure:**

```
artzy4u.com  —  "Artwork by Diana Jones — Tulsa, Oklahoma"
├── hero: denim flowers photo + wordmark + tagline
├── The work
│   ├── 3rd World Art          → 3rdworldart.art  (hand embroidery)
│   └── Ornaments & Originals  → artsy4y.com      (RESIST! catalog)
├── statement: "Artzy4u is the artwork of Diana Jones…"
└── contact: stephanie@artzy4u.com
```

---

## Open content items

### 1. More product lines — the main one

Stephanie said there are more lines beyond embroidery and the shop. Each card
needs:

| Needed | Notes |
|---|---|
| **Name** | Becomes the card title |
| **One sentence** | What it is, in her/Diana's voice |
| **Link** | Its own site or page — or none, and the button gets dropped |
| **Photo** | Any size; resize to long-side 1800px, quality 82, into `images/` |
| **3 spec rows** | Optional. Existing cards use Materials/Method/Editions and Series/Also/Prices |

A ready-to-fill `<article class="line">` template is **commented into
`index.html`** inside `<section id="work">`. Copy it out of the comment.

Card title colors alternate via `.line:nth-child(n) .title` — currently indigo
then mulberry. A third card inherits no color rule; add one.

### 2. Contact address vs. artist attribution

The site says the artwork is **Diana Jones's**, but the contact button is
`stephanie@artzy4u.com`. Fine if intentional — Stephanie runs the web and the
inbox — but a visitor will notice. If it should be Diana's address instead,
that's a Google Workspace user away, then flip both sites.

### 3. artsy4u.com is now unreferenced

Since the shop card was pointed at RESIST! (artsy4y.com), `artsy4u.com` isn't
linked from the umbrella at all. It's a Squarespace landing page duplicating one
product teaser. Decide: redirect to RESIST!, repurpose, or retire. Not urgent.

### 4. Possible additions — not requested, just noted

- No **about/bio** for Diana Jones beyond the one statement line
- No individual piece pages — everything links out
- Hero photo is the denim flowers, reused from 3rdworldart's images

---

## Conventions — follow these

| Rule | Detail |
|---|---|
| **One file** | Everything is `index.html` — inline `<style>`, no framework, no build |
| **Images** | Long side 1800px, quality 82, JPEG, into `images/` |
| **Type** | Fraunces (display) + Archivo (body), loaded from Google Fonts — the site's only external dependency |
| **Palette** | `--indigo #1E3145` · `--calico #E9E0CC` · `--hoop #F0BE2A` · `--floss #3A7FA6` · `--mulberry #8C3F63` · `--leaf #7FAE3E` |
| **Design relationship** | artzy4u.com is indigo-on-calico; 3rdworldart.art is calico-on-indigo. Deliberately inverted — same family, not duplicates. Keep it |
| **Accessibility** | Every `<img>` needs real alt text describing the piece. `prefers-reduced-motion` is honored — don't add unconditional animation |
| **Mobile** | Verify no horizontal overflow at 375px before pushing |

### Verify before pushing

Serve locally and check rather than pushing blind:

```bash
cd C:\Users\stephanie\artzy4u && python -m http.server 8125
```

Then load `http://127.0.0.1:8125`, confirm no console errors, and check the
375px viewport. Push only after it renders clean — every push deploys to the
live site.

---

## Do not re-open

These are settled and verified. Re-litigating them wastes the session:

- DNS, nameservers, mail authentication, DKIM keys → `STACK_REFERENCE.md`
- The Netlify/GitHub/CD setup → `WORK_ORDER.md` Items 300/400
- Whether artsy4u.com should redirect to artzy4u.com → **no**, it's a live
  store; decided 8/1 and reversed for good reason
- Whether artzy4u.com belongs on Squarespace → **no.** Its DNS is at Netlify and
  its Workspace MX records live in that zone. Squarespace's domain-connect
  screen shows all-red for it; that is **correct**, not a fault

## Still outstanding on infrastructure (not content)

- **artsy4y.com nameservers** — 8 delegated, 4 to an orphaned NS1 zone. Saved at
  the registrar 8/2 8:44 AM but hadn't reached the `.com` registry. Re-verify:
  `Resolve-DnsName artsy4y.com -Type NS -Server a.gtld-servers.net`
- **artzy4u.com DKIM** — correct key restored to Netlify DNS 8/2; NS1 was still
  serving a stale copy. Re-verify it differs from artsy4u.com's key
