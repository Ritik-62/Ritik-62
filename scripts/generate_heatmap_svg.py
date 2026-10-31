#!/usr/bin/env python3
"""
Generate an animated GitHub contribution heatmap SVG (squares light up with pop + flash).
Works standalone or via GitHub Actions workflow to refresh daily.
Usage: python generate_heatmap_svg.py [username] [output.svg]
"""
import sys
import json
import os
import datetime
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
USER = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GH_PROFILE_USER", "Ritik-62")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "assets", "contrib-heatmap.svg")


def get_data(user):
    snap = os.path.join(HERE, "..", "data", "contributions.json")
    if os.path.exists(snap):
        try:
            d = json.load(open(snap, encoding="utf-8"))
            if d.get("username", "").lower() == user.lower() and all("level" in x for x in d.get("days", [])):
                return {"contributions": d["days"], "total": {"lastYear": d["total_contributions"]}}
        except Exception as e:
            print(f"Warning: Failed to read {snap}: {e}", file=sys.stderr)

    # API fallback
    url = f"https://github-contributions-api.jogruber.de/v4/{user}?y=last"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "profile-heatmap-generator/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        print(f"API fallback failed ({e}); checking for local data", file=sys.stderr)
        if os.path.exists(snap):
            return {"contributions": d["days"], "total": {"lastYear": d["total_contributions"]}}
        raise RuntimeError("No contribution data available.") from e


def render_svg(user, out_path):
    data = get_data(user)
    contribs = data["contributions"]
    total = data["total"]["lastYear"]

    CELL, GAP, RAD, LEFT, TOP = 13, 3, 2.5, 34, 24
    COLORS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
    GRAY = "#7d8590"
    MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    n = len(contribs)
    NW = (n + 6) // 7
    W = LEFT + NW * (CELL + GAP) + 12
    H = TOP + 7 * (CELL + GAP) + 26

    REVEAL, DUR = 3.6, 0.55
    maxorder = max(1, (NW - 1) + 6 * 0.55)

    rects, labels = [], []
    sd = datetime.date.fromisoformat(contribs[0]["date"]) if contribs else datetime.date.today()
    last_m = None
    for wk in range(NW):
        d = sd + datetime.timedelta(days=wk * 7)
        if d.month != last_m:
            last_m = d.month
            labels.append(f'<text class="lbl" x="{LEFT+wk*(CELL+GAP)}" y="{TOP-8}">{MONTHS[d.month-1]}</text>')
    for name, r in [("Mon", 1), ("Wed", 3), ("Fri", 5)]:
        labels.append(f'<text class="lbl" x="2" y="{TOP+r*(CELL+GAP)+CELL-2}">{name}</text>')

    for i, c in enumerate(contribs):
        wk, row, lvl = i // 7, i % 7, c.get("level", 0)
        x = LEFT + wk * (CELL + GAP)
        y = TOP + row * (CELL + GAP)
        delay = round((wk + row * 0.55) / maxorder * REVEAL, 3)
        cls = "c g" if lvl >= 1 else "c e"
        rects.append(
            f'<rect class="{cls}" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="{RAD}" '
            f'fill="{COLORS[lvl]}" style="animation-delay:{delay}s"/>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
<style>
  text.lbl {{ fill: {GRAY}; font-size: 11px; font-weight: 600; }}
  text.total {{ fill: #e6edf3; font-size: 13px; font-weight: 600; }}
  .c {{ transform-box: fill-box; transform-origin: center; opacity: 0; animation: pop {DUR}s ease-out both; }}
  .g {{ animation: pop {DUR}s ease-out both, flash {DUR+0.15}s ease-out both; }}
  @keyframes pop {{ 0% {{ opacity: 0; transform: scale(.2); }} 60% {{ opacity: 1; transform: scale(1.1); }} 100% {{ opacity: 1; transform: scale(1); }} }}
  @keyframes flash {{ 0% {{ filter: brightness(2.4); }} 45% {{ filter: brightness(2.4); }} 100% {{ filter: brightness(1); }} }}
  @media (prefers-reduced-motion: reduce) {{ .c {{ opacity: 1 !important; animation: none !important; }} }}
</style>
<rect width="{W}" height="{H}" rx="10" fill="#0d1117" stroke="#30363d" stroke-width="1"/>
{''.join(labels)}
{''.join(rects)}
<text class="total" x="{LEFT}" y="{H-9}">{total:,} contributions in the last year</text>
</svg>"""

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {out_path}: {n} days, {total:,} contributions, {W} x {H}")


if __name__ == "__main__":
    render_svg(USER, OUT)
