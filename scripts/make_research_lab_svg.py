#!/usr/bin/env python3
"""
Generate an animated AI & Data Science Research Lab workflow SVG:
DATA → MACHINE LEARNING → RAG → AI AGENTS → LLM APPLICATIONS → OUTPUT

Features:
- macOS terminal window chrome with traffic lights
- 6 modular laboratory nodes (Data, ML, RAG, Agents, LLMs, Output)
- Dark research-lab aesthetic (#0d1117, #161b22, #30363d) with terminal green and cyan accents
- Flowing animated connection beams (SVG stroke-dashoffset animation)
- Glowing node borders and pulsing status indicators
- Redesigned, non-overlapping top header and 3-compartment telemetry status bar
- Static fallback via prefers-reduced-motion
- 100% self-contained, valid XML, lightweight (< 20KB)

Usage:
    python scripts/make_research_lab_svg.py [output.svg]
"""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "assets", "ai-research-lab.svg")

W, H = 860, 420
PAD = 20
TITLEBAR_H = 30

BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
TILE = "#161b22"
MUTED = "#7d8590"
INK = "#e6edf3"
GREEN = "#39d353"
CYAN = "#22d3ee"
ORANGE = "#ffa657"
PURPLE = "#bc8cff"


def build_svg(out_path=OUT):
    # 6 Laboratory Nodes (2 rows of 3 nodes)
    # Row 1: Stage 1 (Data) -> Stage 2 (ML) -> Stage 3 (RAG)
    # Row 2: Stage 4 (Agents) -> Stage 5 (LLM Apps) -> Stage 6 (Output)
    # Connecting path flows: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    # Card width = 246, Gap = 37, Padding = 24. Total width = 24*2 + 246*3 + 37*2 = 860.

    stages = [
        # Row 1
        {
            "id": "stage1",
            "num": "01",
            "name": "DATA INGESTION",
            "subtitle": "Raw Data & Feature Pipelines",
            "tech1": "ETL · Normalization",
            "tech2": "Deduplication · Vectors",
            "accent": CYAN,
            "x": 24,
            "y": 80,
            "w": 246,
            "h": 105,
        },
        {
            "id": "stage2",
            "num": "02",
            "name": "MACHINE LEARNING",
            "subtitle": "Statistical & Boosted Baselines",
            "tech1": "XGBoost · Calibration",
            "tech2": "Leakage-Safe · T-60 Protocol",
            "accent": GREEN,
            "x": 307,
            "y": 80,
            "w": 246,
            "h": 105,
        },
        {
            "id": "stage3",
            "num": "03",
            "name": "RAG ARCHITECTURE",
            "subtitle": "Multi-Query Context Retrieval",
            "tech1": "Semantic Search · RAG",
            "tech2": "Filtering · Dense Embeddings",
            "accent": CYAN,
            "x": 590,
            "y": 80,
            "w": 246,
            "h": 105,
        },
        # Row 2
        {
            "id": "stage4",
            "num": "04",
            "name": "AI AGENTS",
            "subtitle": "Autonomous State Machine Loops",
            "tech1": "LangGraph State Loops",
            "tech2": "Decision Flows · Tool Calling",
            "accent": PURPLE,
            "x": 24,
            "y": 225,
            "w": 246,
            "h": 105,
        },
        {
            "id": "stage5",
            "num": "05",
            "name": "LLM APPLICATIONS",
            "subtitle": "Prompt & Synthesis Pipelines",
            "tech1": "Llama 3 · Groq LPU · OpenAI",
            "tech2": "Structured Outputs & Guards",
            "accent": ORANGE,
            "x": 307,
            "y": 225,
            "w": 246,
            "h": 105,
        },
        {
            "id": "stage6",
            "num": "06",
            "name": "SYSTEM OUTPUTS",
            "subtitle": "Evidence-Grounded Deliverables",
            "tech1": "Verified Research Reports",
            "tech2": "Tableau Dashboards · APIs",
            "accent": GREEN,
            "x": 590,
            "y": 225,
            "w": 246,
            "h": 105,
        },
    ]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        "<style>",
        "  .flow-line { stroke: #30363d; stroke-width: 2; fill: none; }",
        "  .flow-pulse { stroke-dasharray: 8 16; stroke-dashoffset: 0; animation: flow 2.5s linear infinite; fill: none; }",
        "  .node-box { fill: #161b22; stroke: #30363d; stroke-width: 1.2; rx: 8px; transition: all 0.3s; }",
        "  .pulse-dot { animation: pulse 2s ease-in-out infinite; }",
        "  .status-pulse { animation: blink 1.8s ease-in-out infinite alternate; }",
        "  @keyframes flow { to { stroke-dashoffset: -48; } }",
        "  @keyframes pulse { 0%, 100% { opacity: 0.3; r: 3; } 50% { opacity: 1; r: 4.5; } }",
        "  @keyframes blink { 0% { opacity: 0.4; } 100% { opacity: 1; } }",
        "  @media (prefers-reduced-motion: reduce) {",
        "    .flow-pulse, .pulse-dot, .status-pulse { animation: none !important; stroke-dashoffset: 0 !important; }",
        "  }",
        "</style>",
        "<defs>",
        f'  <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient>',
        f'  <linearGradient id="cyanLine" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{GREEN}"/></linearGradient>',
        f'  <linearGradient id="greenLine" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GREEN}"/><stop offset="1" stop-color="{CYAN}"/></linearGradient>',
        f'  <linearGradient id="purpleLine" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{PURPLE}"/><stop offset="1" stop-color="{ORANGE}"/></linearGradient>',
        f'  <linearGradient id="orangeLine" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{ORANGE}"/><stop offset="1" stop-color="{GREEN}"/></linearGradient>',
        "</defs>",
        # Window Background & Titlebar
        f'<rect width="{W}" height="{H}" rx="10" fill="url(#bgGrad)"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="none" stroke="{FRAME}" stroke-width="1"/>',
        f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
    ]

    # Traffic light dots
    for i, dot in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dot}"/>')

    # Window title
    parts.append(
        f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" text-anchor="middle">'
        f"ritik@github: ~$ ./ai_research_lab.sh --workflow=overview</text>"
    )

    # Sub-header pipeline banner (Properly balanced, no text collisions)
    parts.append('<g transform="translate(24, 48)">')
    parts.append(f'<circle cx="12" cy="12" r="4" fill="{GREEN}" class="status-pulse"/>')
    parts.append(
        f'<text x="24" y="16" fill="{GREEN}" font-size="11" font-weight="700">AI &amp; DATA SCIENCE WORKFLOW</text>'
    )
    parts.append(
        f'<text x="226" y="16" fill="{MUTED}" font-size="10.5">Data Ingest → ML Baselines → RAG → Agents → LLMs → Outputs</text>'
    )
    parts.append(f'<text x="812" y="16" fill="{CYAN}" font-size="10.5" text-anchor="end">PIPELINE FLOW · 2026</text>')
    parts.append("</g>")

    # Connecting Flow Paths between Stages:
    # 1 -> 2
    parts.append('<line x1="270" y1="132.5" x2="307" y2="132.5" class="flow-line"/>')
    parts.append(f'<line x1="270" y1="132.5" x2="307" y2="132.5" class="flow-pulse" stroke="url(#cyanLine)" stroke-width="2.5"/>')
    parts.append(f'<circle cx="288.5" cy="132.5" r="3" fill="{CYAN}" class="pulse-dot"/>')

    # 2 -> 3
    parts.append('<line x1="553" y1="132.5" x2="590" y2="132.5" class="flow-line"/>')
    parts.append(f'<line x1="553" y1="132.5" x2="590" y2="132.5" class="flow-pulse" stroke="url(#greenLine)" stroke-width="2.5"/>')
    parts.append(f'<circle cx="571.5" cy="132.5" r="3" fill="{GREEN}" class="pulse-dot"/>')

    # 3 -> 4 (Bridge curve: from stage 3 center down and across to stage 4 center)
    bridge_path = "M 713 185 C 713 212, 147 198, 147 225"
    parts.append(f'<path d="{bridge_path}" class="flow-line"/>')
    parts.append(f'<path d="{bridge_path}" class="flow-pulse" stroke="{CYAN}" stroke-width="2"/>')

    # 4 -> 5
    parts.append('<line x1="270" y1="277.5" x2="307" y2="277.5" class="flow-line"/>')
    parts.append(f'<line x1="270" y1="277.5" x2="307" y2="277.5" class="flow-pulse" stroke="url(#purpleLine)" stroke-width="2.5"/>')
    parts.append(f'<circle cx="288.5" cy="277.5" r="3" fill="{PURPLE}" class="pulse-dot"/>')

    # 5 -> 6
    parts.append('<line x1="553" y1="277.5" x2="590" y2="277.5" class="flow-line"/>')
    parts.append(f'<line x1="553" y1="277.5" x2="590" y2="277.5" class="flow-pulse" stroke="url(#orangeLine)" stroke-width="2.5"/>')
    parts.append(f'<circle cx="571.5" cy="277.5" r="3" fill="{GREEN}" class="pulse-dot"/>')

    # Render Node Boxes
    for s in stages:
        bx, by, bw, bh = s["x"], s["y"], s["w"], s["h"]
        accent = s["accent"]

        parts.append(f'<g id="{s["id"]}">')
        # Base tile
        parts.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" class="node-box"/>')
        # Left accent vertical indicator strip
        parts.append(f'<rect x="{bx}" y="{by+8}" width="3.5" height="{bh-16}" rx="1.5" fill="{accent}"/>')

        # Stage number badge
        parts.append(
            f'<rect x="{bx+12}" y="{by+12}" width="38" height="18" rx="4" fill="#0d1117" stroke="{FRAME}" stroke-width="0.8"/>'
        )
        parts.append(
            f'<text x="{bx+31}" y="{by+25}" fill="{accent}" font-size="10" font-weight="700" text-anchor="middle">'
            f'[{s["num"]}]</text>'
        )

        # Stage Name
        parts.append(
            f'<text x="{bx+56}" y="{by+26}" fill="{INK}" font-size="12.5" font-weight="700">{html.escape(s["name"])}</text>'
        )

        # Subtitle
        parts.append(
            f'<text x="{bx+12}" y="{by+49}" fill="{MUTED}" font-size="10.5" font-weight="500">{html.escape(s["subtitle"])}</text>'
        )

        # Divider inside tile
        parts.append(f'<line x1="{bx+12}" y1="{by+60}" x2="{bx+bw-12}" y2="{by+60}" stroke="#21262d"/>')

        # Technologies Line 1 (Accent highlighted)
        parts.append(
            f'<text x="{bx+12}" y="{by+77}" fill="{accent}" font-size="10" font-weight="600">{html.escape(s["tech1"])}</text>'
        )

        # Technologies Line 2 (Secondary details, fully contained within card)
        parts.append(
            f'<text x="{bx+12}" y="{by+93}" fill="#8b949e" font-size="9.5">{html.escape(s["tech2"])}</text>'
        )

        parts.append("</g>")

    # Redesigned 3-Section Telemetry Bottom Bar (Separated compartments, zero overlap)
    bar_y = 356
    bar_w = 812
    parts.append(f'<g id="telemetry-bar">')
    # Background container
    parts.append(f'<rect x="24" y="{bar_y}" width="{bar_w}" height="44" rx="6" fill="#111722" stroke="{FRAME}" stroke-width="1"/>')

    # Compartment Dividers
    parts.append(f'<line x1="195" y1="{bar_y+7}" x2="195" y2="{bar_y+37}" stroke="#30363d"/>')
    parts.append(f'<line x1="645" y1="{bar_y+7}" x2="645" y2="{bar_y+37}" stroke="#30363d"/>')

    # Section 1: Lab Title & Status (Left)
    parts.append(f'<circle cx="42" cy="{bar_y+22}" r="3.5" fill="{GREEN}" class="status-pulse"/>')
    parts.append(f'<text x="54" y="{bar_y+26}" fill="{GREEN}" font-size="11" font-weight="700">AI WORKFLOW LAB</text>')

    # Section 2: Key Tech Stacks (Center - 2-line layout, zero overflow into right compartment)
    parts.append(
        f'<text x="210" y="{bar_y+19}" fill="{MUTED}" font-size="9.5">'
        f'RAG: <tspan fill="{CYAN}">Multi-Query</tspan>'
        f' · ML: <tspan fill="{GREEN}">Platt Calib</tspan>'
        f'</text>'
    )
    parts.append(
        f'<text x="210" y="{bar_y+32}" fill="{MUTED}" font-size="9.5">'
        f'Agents: <tspan fill="{PURPLE}">LangGraph</tspan>'
        f' · LLMs: <tspan fill="{ORANGE}">Groq / Llama 3</tspan>'
        f'</text>'
    )

    # Section 3: Verified Status Badge Pill (Right - strictly contained)
    parts.append(f'<rect x="660" y="{bar_y+10}" width="160" height="24" rx="4" fill="#0d1117" stroke="#238636" stroke-width="0.8"/>')
    parts.append(f'<circle cx="675" cy="{bar_y+22}" r="3" fill="{GREEN}" class="status-pulse"/>')
    parts.append(f'<text x="686" y="{bar_y+26}" fill="{GREEN}" font-size="10" font-weight="700">STATUS: VERIFIED</text>')
    parts.append("</g>")

    parts.append("</svg>")
    svg = "\n".join(parts)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {out_path} ({W}x{H}) - {len(svg)} bytes")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else OUT
    build_svg(target)
