# Fix the shop route — step by step

| | |
|---|---|
| **Written** | August 2, 2026 — for a fresh start in the morning |
| **Problem** | The "Shop RESIST!" button on artzy4u.com sends visitors in a circle |
| **Time** | ~5 minutes once you find the right screen |
| **Risk** | Low. You're deleting one redirect rule. Nothing else changes |

---

## What's wrong, in one picture

```
  Visitor on artzy4u.com
        │
        │  clicks "Shop RESIST! →"
        ▼
  artsy4y.com
        │
        │  301 redirect  ← THIS IS THE PROBLEM
        ▼
  www.artzy4u.com   ← back where they started. No shop.
```

The RESIST! catalog — Read Banned Books, No Kings!, Hands Off!!, the penguins —
is **currently unreachable by anyone.** The redirect fires before the site ever
loads.

**Verified 8/2:**

```
artsy4y.com/        →  301  →  https://www.artzy4u.com/
artsy4y.com/shop    →  301  →  https://www.artzy4u.com/shop
Server: Squarespace
```

Note the second line: the path **carries across** (`/shop` → `/shop`). That
detail matters — it tells us this is a **URL Mappings wildcard rule**, not plain
domain forwarding. Plain forwarding would send everything to the root.

**Nothing is wrong with artzy4u.com.** Its button is correct and points where it
should. The problem is entirely at the other end.

---

## Before you start

**Do not change anything on artzy4u.com.** The button is right. If you "fix" it
by repointing it somewhere else, you'll have two problems instead of one.

**Do not touch nameservers or DNS.** This is a redirect rule inside Squarespace,
one layer above DNS. DNS is fine.

---

## Step 1 — Open the site admin

Go to:

```
https://artsy4u.squarespace.com/config/
```

That's the Squarespace site titled **RESIST!** — the one artsy4y.com is
connected to. (It shows in your billing emails as "Artsy4U", later renamed
"RESIST!".)

Log in if prompted. Verification codes go to **dolan.todar@gmail.com**.

> If that URL doesn't load, go to **squarespace.com → log in**, and pick the site
> named **RESIST!** from your sites list.

---

## Step 2 — Find URL Mappings

In the site admin, open **Settings**, then **use the search box** at the top of
the settings panel and type:

```
URL Mappings
```

**Search rather than browsing the menus.** Squarespace has moved this page
between *Settings → Developer Tools* and *Settings → Advanced* depending on
account version, and guessing wastes time. Search finds it either way.

---

## Step 3 — Delete the rule

You're looking for **one line containing `artzy4u.com`**. It'll look something
like:

```
/[name] -> https://www.artzy4u.com/[name] 301
```

or possibly:

```
/ -> https://www.artzy4u.com 301
```

**Delete that line.** Leave any other lines alone — other mappings may be doing
legitimate work.

Save.

> **If the URL Mappings box is empty**, it's domain forwarding instead. Go to
> **Domains → artsy4y.com** and look for a **Forwarding** or **Redirect**
> section with `artzy4u.com` in it. Remove it there. Same outcome.

---

## Step 4 — Check it worked

Open a **private/incognito window** — your normal browser has the 301 cached and
will keep redirecting even after the fix, which looks like failure when it isn't.

Go to:

```
https://artsy4y.com
```

**Success looks like:** the RESIST! catalog — Don't Knock My Peace, Read Banned
Books, No Kings!, Hands Off!!, the penguin ornaments, prices $10–$20.

**Still failing looks like:** you land back on artzy4u.com.

---

## Step 5 — Test the actual route

The point of all this is the visitor path, so walk it:

1. Go to **https://artzy4u.com**
2. Scroll to **Ornaments & Originals**
3. Click **Shop RESIST! →**
4. You should land on the catalog

If that works, you're done. Tell Claude and it'll verify from the outside and
confirm the loop is gone.

---

## If it doesn't work

| Symptom | Likely cause | What to do |
|---|---|---|
| Still redirects in a normal browser | 301s cache hard | Retry in incognito. A 301 can persist for days locally |
| Still redirects in incognito | Rule wasn't saved, or there's a second one | Reopen URL Mappings and confirm it's actually gone |
| artsy4y.com now shows nothing / an error | Domain got disconnected from the site | In the site: Settings → Domains, reconnect artsy4y.com |
| Can't find URL Mappings at all | Wrong site | You may be in a different Squarespace site. Check the site name reads **RESIST!** |
| Can't log in | — | Password recovery goes to dolan.todar@gmail.com — confirmed working |

---

## Context worth having

**This is the second time a redirect like this has bitten.** This morning
artsy4u.com was redirecting to artsy4y.com's parked page — same class of rule,
opposite direction. It was likely created during the domain-connect attempts
while several Squarespace screens were open.

**While you're in there, check artsy4u.com's URL Mappings too.** If these two
rules were created together, there may be a fresh one on that site as well.

**Not urgent, same visit if convenient:** artsy4y.com still has **8 nameservers**
— four Squarespace, four orphaned `dns#.p08.nsone.net`. Both zones currently
serve *identical* records, so nothing is broken. The catch is you can only edit
the Squarespace one, so future changes will drift. Removing the four `nsone`
entries at the registrar makes edits predictable again. Maintenance, not
triage.
