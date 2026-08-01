# artzy4u.com

Umbrella brand site for **Artzy4u** — recycle, reuse, repurpose. One static HTML
file, no framework, no build step, no npm. Deploys to Netlify on push.

Sister site: [3rdworldart.art](https://3rdworldart.art) — the hand-embroidery
portfolio, its own repo (`Artsy4U/3rdworldart`). Artzy4u is the front door;
3rd World Art is one line of work inside it.

## Layout

```
index.html      the whole site
netlify.toml    publish "." , cache headers
favicon.ico     stitched orange flower, 16/32/48
images/         web-sized jpgs, long side 1800px, quality 82
originals/      full-size camera files — gitignored, never committed
```

## Adding a line of work

1. Resize the photo: long side 1800px, quality 82, save into `images/` as
   `line-<name>.jpg`.
2. In `index.html`, find the commented `ADDING A LINE OF WORK` block inside
   `<section id="work">`. Copy it out of the comment, fill it in.
3. If that line has no site of its own yet, **delete the `<a class="go">`
   button** rather than pointing it nowhere.
4. Commit with the line's name as the message. Deploy is automatic.

## Design notes

Same palette and typefaces as 3rdworldart.art, deliberately inverted: the
portfolio is calico-on-indigo, this one is indigo-on-calico. They read as the
same family without looking like a duplicate. Accent colors carry over
unchanged — hoop yellow, floss blue, mulberry, leaf.

Fonts load from Google Fonts. That's the site's only external dependency.

## Contact address

The contact button currently points at `stephanie@artsy4u.com` (s-spelling).
It flips to `stephanie@artzy4u.com` once that alias domain is confirmed
receiving mail — the DNS is live, the Google Workspace side is the open piece.
Both this site and 3rdworldart.art flip together.
