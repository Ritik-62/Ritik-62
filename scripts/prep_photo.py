#!/usr/bin/env python3
"""
Prepare portrait photo for clean monochrome ASCII conversion:
  1. Remove background so subject is isolated.
  2. Bilateral smoothing to remove noise/texture while preserving drawn outlines.
  3. Tone stretch over subject only.
  4. Line work enhancement (difference of Gaussians).
  5. Square crop and export grayscale prepped image.

Usage:
    python scripts/prep_photo.py [input.png] [output.png]
"""
import os
import sys
import cv2
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "ritik-photo.png")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "ritik-prepped.png")

LINE_WEIGHT = 0.6

# 1. Background cutout using rembg (u2netp) or fallback thresholding
try:
    from rembg import remove, new_session
    session = new_session("u2netp")
    cut = remove(Image.open(INP).convert("RGBA"), session=session)
except Exception as e:
    print(f"rembg unavailable ({e}), using color distance cutout...", file=sys.stderr)
    src_img = Image.open(INP).convert("RGBA")
    arr = np.array(src_img)
    # Background in ritik-photo is cream (~[242, 238, 230])
    bg_diff = np.sqrt(np.sum((arr[:, :, :3].astype(float) - [242, 238, 230]) ** 2, axis=2))
    alpha = np.where(bg_diff < 28, 0, 255).astype(np.uint8)
    arr[:, :, 3] = alpha
    cut = Image.fromarray(arr)

rgb = np.array(cut.convert("RGB"))
alpha = np.array(cut.split()[-1])
gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

# 2. Smooth texture, preserve sharp edges
smooth = gray
for _ in range(3):
    smooth = cv2.bilateralFilter(smooth, 9, 40, 9)

# 3. Tone stretch over subject
subj_pixels = smooth[alpha > 128]
if len(subj_pixels) > 0:
    lo, hi = np.percentile(subj_pixels, [2, 92])
    tone = np.clip((smooth.astype(np.float32) - lo) / max(1.0, hi - lo), 0, 1)
else:
    tone = smooth.astype(np.float32) / 255.0

# 4. Difference-of-Gaussians ridges for line enhancement
fine = cv2.GaussianBlur(smooth, (0, 0), 1.5).astype(np.float32)
coarse = cv2.GaussianBlur(smooth, (0, 0), 6).astype(np.float32)
lines = np.clip((coarse - fine) / 40.0, 0, 1)
out = np.clip(tone - LINE_WEIGHT * lines, 0, 1) * 255.0

# 5. Composite onto white with feathered alpha mask and square crop
mask = cv2.GaussianBlur(alpha.astype(np.float32) / 255.0, (0, 0), 1.0)
out = out * mask + 255.0 * (1.0 - mask)

ys, xs = np.where(alpha > 20)
if len(xs) > 0 and len(ys) > 0:
    side = max(xs.max() - xs.min(), ys.max() - ys.min()) + 60
    cx, cy = (xs.min() + xs.max()) // 2, (ys.min() + ys.max()) // 2
    canvas = np.full((side, side), 255, np.uint8)
    x0, y0 = cx - side // 2, cy - side // 2
    sx0, sy0 = max(x0, 0), max(y0, 0)
    sx1, sy1 = min(x0 + side, out.shape[1]), min(y0 + side, out.shape[0])
    canvas[sy0 - y0:sy1 - y0, sx0 - x0:sx1 - x0] = out[sy0:sy1, sx0:sx1].astype(np.uint8)
else:
    canvas = out.astype(np.uint8)

os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
Image.fromarray(canvas, mode="L").save(OUT)
print(f"Wrote prepped image to {OUT} (shape: {canvas.shape})")
