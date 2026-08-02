#!/usr/bin/env python3
"""
Resize a photo to the house convention for this site.

  long side 1800px  ·  JPEG quality 82  ·  EXIF rotation applied and stripped

Usage
-----
    python tools/resize-photo.py "C:\\path\\to\\IMG_1234.jpg" denim-cuff

Writes images/denim-cuff.jpg and leaves the original untouched.
Drop the original into originals/ if you want to keep it — that folder is
gitignored, so it never bloats the repo.

Requires Pillow:  pip install Pillow
"""

import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow isn't installed. Run:  pip install Pillow")

MAX_SIDE = 1800
QUALITY = 82

def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)

    src = Path(sys.argv[1])
    name = sys.argv[2].strip().lower().replace(" ", "-").removesuffix(".jpg")

    if not src.exists():
        sys.exit(f"Not found: {src}")

    out_dir = Path(__file__).resolve().parent.parent / "images"
    out_dir.mkdir(exist_ok=True)
    dest = out_dir / f"{name}.jpg"

    if dest.exists():
        reply = input(f"{dest.name} already exists. Overwrite? [y/N] ").strip().lower()
        if reply != "y":
            sys.exit("Cancelled.")

    im = Image.open(src)
    before = im.size

    # Apply EXIF rotation, then drop the flag — otherwise phone photos
    # render sideways in some browsers.
    im = ImageOps.exif_transpose(im)

    # Flatten transparency onto white so JPEG conversion is clean.
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")

    # Never upscale — a small original stays small.
    w, h = im.size
    if max(w, h) > MAX_SIDE:
        scale = MAX_SIDE / max(w, h)
        im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)

    im.save(dest, "JPEG", quality=QUALITY, optimize=True, progressive=True)

    kb = dest.stat().st_size / 1024
    print(f"  {src.name}  {before[0]}x{before[1]}")
    print(f"  -> images/{dest.name}  {im.size[0]}x{im.size[1]}  {kb:.0f} KB")
    print()
    print("  Next: add the piece block to index.html, then commit and push.")
    print(f"  <img src=\"images/{dest.name}\" alt=\"DESCRIBE THE PIECE\" loading=\"lazy\">")

if __name__ == "__main__":
    main()
