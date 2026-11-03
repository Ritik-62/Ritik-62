#!/usr/bin/env python3
"""
Generate an animated neofetch-style terminal info dashboard SVG
calibrated to 840x880 dimensions to pair alongside ritik-ascii.svg and stats.svg.

Displays genuine profile info (Host, Role, Focus, Languages, Bio, Mission,
Stack, and Project Highlights) with no fabricated computer or hardware specs.

Usage:
    python scripts/make_neofetch_svg.py [output.svg]
"""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "assets", "neofetch.svg")

W, H = 840, 880
PAD = 20
TITLEBAR_H = 30
BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
MUTED = "#7d8590"
INK = "#c9d1d9"
ACCENT = "#58a6ff"
GREEN = "#3fb950"
ORANGE = "#ffa657"
PURPLE = "#bc8cff"
CYAN = "#22d3ee"

# Genuine profile information — no fabricated hardware or OS details
profile_specs = [
    ("Host", "GitHub Profile (Ritik-62)", INK),
    ("Role", "Data Science & AI Enthusiast", ACCENT),
    ("Focus", "Machine Learning, Generative AI, RAG", PURPLE),
    ("Languages", "Python, TypeScript, JavaScript, SQL", ORANGE),
    ("Bio", "Exploring ML, GenAI & Intelligent Systems", INK),
    ("Mission", "Building Projects That Solve Real-World Problems", GREEN),
    ("Location", "Sonipat, Haryana, India 🇮🇳", INK),
    ("Status", "Active · Open to AI / ML Collaborations", GREEN),
]

stack_sections = [
    ("Core CS", "OOP, Design Principles, Data Structures, Algorithms", INK),
    ("AI & ML", "Machine Learning, GenAI, LangGraph, RAG, LLM Apps", PURPLE),
    ("Web & Backend", "Next.js, FastAPI, Streamlit, Prisma ORM, REST APIs", CYAN),
    ("Data & Tools", "SQLite, Tableau, Excel, Git, GitHub Actions", INK),
    ("Certification", "Oracle Cloud 2025 Certified Data Science Pro", GREEN),
]

highlights = [
    ("ARIA", "Academic Research & Innovation Assistant (RAG & Scholar API)", INK),
    ("Flight ML", "Leakage-Safe ML on 5.8M Flights, XGBoost & Platt Calib", INK),
    ("Private Net", "DNS, Dual Backend, Nginx Proxy, TLS & Packet Tracing", INK),
    ("Prop Advisor", "Agentic AI Workflow, Random Forest & Llama 3 via Groq", INK),
]


def render(out_path=OUT):
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        "<style>",
        ".line { opacity: 0; animation: fadeSlide 0.4s ease-out forwards; }",
        "@keyframes fadeSlide { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }",
        "@media (prefers-reduced-motion: reduce) { .line { opacity: 1 !important; transform: none !important; animation: none !important; } }",
        "</style>",
        f'<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>',
        f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}" stroke-width="1"/>',
        f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
    ]

    for i, dot in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dot}"/>')
    parts.append(
        f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" text-anchor="middle">ritik@github: ~$ neofetch</text>'
    )

    curr_y = TITLEBAR_H + 34
    delay = 0.1

    # Header
    parts.append(f'<g class="line" style="animation-delay:{delay:.2f}s">')
    parts.append(
        f'<text x="{PAD+12}" y="{curr_y}" font-size="18" font-weight="700">'
        f'<tspan fill="{GREEN}">ritik</tspan><tspan fill="{MUTED}">@</tspan><tspan fill="{CYAN}">github</tspan></text>'
    )
    parts.append("</g>")
    curr_y += 12
    parts.append(f'<g class="line" style="animation-delay:{delay+0.05:.2f}s">')
    parts.append(
        f'<line x1="{PAD+12}" y1="{curr_y}" x2="{W-PAD-12}" y2="{curr_y}" stroke="{FRAME}" stroke-dasharray="4 4"/>'
    )
    parts.append("</g>")
    curr_y += 24
    delay += 0.08

    # Profile specs
    LABEL_X = PAD + 16
    VAL_X = PAD + 160
    for k, v, col in profile_specs:
        parts.append(f'<g class="line" style="animation-delay:{delay:.2f}s">')
        parts.append(
            f'<text x="{LABEL_X}" y="{curr_y}" fill="{ORANGE}" font-size="13.5" font-weight="600">{html.escape(k)}</text>'
        )
        parts.append(f'<text x="{VAL_X}" y="{curr_y}" fill="{col}" font-size="13.5">{html.escape(v)}</text>')
        parts.append("</g>")
        curr_y += 26
        delay += 0.04

    curr_y += 8
    # Stack divider
    parts.append(f'<g class="line" style="animation-delay:{delay:.2f}s">')
    parts.append(
        f'<text x="{LABEL_X}" y="{curr_y}" fill="{ACCENT}" font-size="14" font-weight="700">— Technical Architecture &amp; Stack</text>'
    )
    parts.append(f'<line x1="{LABEL_X + 270}" y1="{curr_y - 4}" x2="{W-PAD-12}" y2="{curr_y - 4}" stroke="{FRAME}"/>')
    parts.append("</g>")
    curr_y += 26
    delay += 0.05

    for k, v, col in stack_sections:
        parts.append(f'<g class="line" style="animation-delay:{delay:.2f}s">')
        parts.append(
            f'<text x="{LABEL_X}" y="{curr_y}" fill="{ORANGE}" font-size="13.5" font-weight="600">{html.escape(k)}</text>'
        )
        parts.append(f'<text x="{VAL_X}" y="{curr_y}" fill="{col}" font-size="13.5">{html.escape(v)}</text>')
        parts.append("</g>")
        curr_y += 26
        delay += 0.04

    curr_y += 8
    # Highlights divider
    parts.append(f'<g class="line" style="animation-delay:{delay:.2f}s">')
    parts.append(
        f'<text x="{LABEL_X}" y="{curr_y}" fill="{ACCENT}" font-size="14" font-weight="700">— Key Project Highlights</text>'
    )
    parts.append(f'<line x1="{LABEL_X + 200}" y1="{curr_y - 4}" x2="{W-PAD-12}" y2="{curr_y - 4}" stroke="{FRAME}"/>')
    parts.append("</g>")
    curr_y += 26
    delay += 0.05

    for tag, desc, col in highlights:
        parts.append(f'<g class="line" style="animation-delay:{delay:.2f}s">')
        parts.append(f'<circle cx="{LABEL_X + 4}" cy="{curr_y - 4}" r="3" fill="{GREEN}"/>')
        parts.append(
            f'<text x="{LABEL_X + 16}" y="{curr_y}" fill="{ORANGE}" font-size="13" font-weight="600">[{html.escape(tag)}]</text>'
        )
        parts.append(f'<text x="{VAL_X}" y="{curr_y}" fill="{col}" font-size="13">{html.escape(desc)}</text>')
        parts.append("</g>")
        curr_y += 25
        delay += 0.04

    # Terminal prompt line
    curr_y += 18
    parts.append(f'<g class="line" style="animation-delay:{delay:.2f}s">')
    parts.append(
        f'<text x="{LABEL_X}" y="{curr_y}" fill="{MUTED}" font-size="13.5">'
        f'<tspan fill="{GREEN}">ritik@github</tspan>:<tspan fill="{CYAN}">~</tspan>$ '
        f'<tspan fill="{INK}">echo $BIO</tspan></text>'
    )
    parts.append("</g>")
    curr_y += 24
    parts.append(f'<g class="line" style="animation-delay:{delay+0.05:.2f}s">')
    parts.append(
        f'<text x="{LABEL_X + 16}" y="{curr_y}" fill="{MUTED}" font-size="13" font-style="italic">'
        f'&quot;Building Projects That Solve Real-World Problems.&quot;</text>'
    )
    parts.append("</g>")

    # ANSI Color blocks at bottom
    curr_y = H - PAD - 26
    parts.append(f'<g class="line" style="animation-delay:{delay+0.1:.2f}s">')
    colors = ["#484f58", "#ff7b72", "#3fb950", "#d29922", "#58a6ff", "#bc8cff", "#39c5cf", "#e6edf3"]
    for i, c in enumerate(colors):
        bx = LABEL_X + i * 36
        parts.append(f'<rect x="{bx}" y="{curr_y}" width="28" height="16" rx="3" fill="{c}"/>')
        parts.append(f'<rect x="{bx}" y="{curr_y+18}" width="28" height="16" rx="3" fill="{c}" opacity="0.5"/>')
    parts.append("</g>")

    parts.append("</svg>")
    svg = "".join(parts)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {out_path} ({W}x{H})")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else OUT
    render(target)
