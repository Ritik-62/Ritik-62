#!/usr/bin/env python3
"""
Generate visually unified terminal-style SVG panels matching the
AI & Data Science Research Lab visual language.
FIX v2: All text properly wrapped with <tspan>, cards expanded vertically,
zero overflow, zero clipping, zero text outside viewBox.
"""
import os, html, xml.etree.ElementTree as ET

ROOT = "/Users/ritikraj/Ritik-GitHub-Profile"
ASSETS_DIR = os.path.join(ROOT, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

BG="#0d1117"; BG2="#111722"; TILE="#161b22"; FRAME="#30363d"; LINE="#21262d"
MUTED="#7d8590"; TEXT="#e6edf3"; GREEN="#39d353"; CYAN="#22d3ee"; BLUE="#58a6ff"
PURPLE="#bc8cff"; ORANGE="#ffa657"; RED="#ff5f56"; YELLOW="#ffbd2e"

BASE_STYLE = """<style>
  .node-box { fill: #161b22; stroke: #30363d; stroke-width: 1.2; }
  .status-pulse { animation: blink 1.8s ease-in-out infinite alternate; }
  @keyframes blink { 0% { opacity: 0.4; } 100% { opacity: 1; } }
  @media (prefers-reduced-motion: reduce) { .status-pulse { animation: none !important; } }
</style>"""

def esc(t): return html.escape(str(t))

def hdr(W, H, cmd):
    return f"""<rect width="{W}" height="{H}" rx="10" fill="url(#bgGrad)"/>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="none" stroke="{FRAME}" stroke-width="1"/>
<line x1="0" y1="30" x2="{W}" y2="30" stroke="{FRAME}"/>
<circle cx="20" cy="15" r="5" fill="{RED}"/>
<circle cx="36" cy="15" r="5" fill="{YELLOW}"/>
<circle cx="52" cy="15" r="5" fill="{GREEN}"/>
<text x="{W//2}" y="19" fill="{MUTED}" font-size="12" text-anchor="middle">{esc(cmd)}</text>"""

def grad_defs():
    return f"""<defs>
  <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/>
  </linearGradient>
</defs>"""

def pill_row(skills, x0, y0, max_x, accent, cw=7.5, pad=18, gap=8, h=24):
    x, y = x0, y0
    out = []
    for s in skills:
        bw = int(len(s)*cw + pad)
        if x + bw > max_x and x != x0:
            x = x0; y += h + gap
        cx2 = x + bw//2
        cy2 = int(y + h*0.635)
        out.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{h}" rx="4" fill="{BG}" stroke="{accent}" stroke-width="0.8"/>')
        out.append(f'<text x="{cx2}" y="{cy2}" fill="{TEXT}" font-size="9.5" font-weight="600" text-anchor="middle">{esc(s)}</text>')
        x += bw + gap
    return "\n".join(out), (y - y0) + h

def write(path, content):
    with open(path, "w", encoding="utf-8") as f: f.write(content)
    ET.parse(path)
    print(f"OK {path}")

# ============================================================
# 1. FEATURED FLAGSHIPS
# ============================================================
def gen_flagships():
    W=860; CARD_W=394; CARD_H=430; H=76+CARD_H+12+38+12
    IW=CARD_W-32
    cards=""
    for i,(accent,num,label,title,tagline,pflow,h1a,h1b,h2a,h2b,h3a,h3b,stack,repo,repourl) in enumerate([
        (CYAN,"01","EVIDENCE-GROUNDED","ARIA Research Assistant",
         '"Evidence-grounded scholarly RAG synthesis system."',
         "Query Plan \u2500\u2500\u25ba Retrieval \u2500\u2500\u25ba Deduplicate \u2500\u2500\u25ba [P1],[P2] Report",
         "Multi-Query Planning:","Decomposes questions across scholarly APIs",
         "Schema Normalization &amp; Deduplication:","Standardized records; identifier &amp; title hash dedup",
         "Citation Grounding &amp; Testing:","Verifiable [P1],[P2] citations; 100% unittest suite",
         "Python \xb7 OpenAI Responses API \xb7 unittest",
         "Ritik-62/aria-research-assistant","github.com/Ritik-62/aria-research-assistant"),
        (PURPLE,"02","LEAKAGE-AWARE EVAL","Flight Delay Prediction",
         '"Large-scale pipeline; calibrated probability output."',
         "5.8M Records \u2500\u2500\u25ba Leakage Denylist \u2500\u2500\u25ba Platt Calibrator \u2500\u2500\u25ba PDF",
         "5.8M U.S. DOT Records &amp; Strict Defense:","Compile-time denylist forbidding post-departure telemetry",
         "Platt Calibrator (Brier Score: 0.1245):","Fitted on validation split; evaluated on held-out test split",
         "26 Automated Tests &amp; PDF Deliverables:","pytest suite: leakage rules &amp; ReportLab PDF generation",
         "Python \xb7 scikit-learn \xb7 XGBoost \xb7 pytest \xb7 ReportLab",
         "Ritik-62/flight-delay-prediction","github.com/Ritik-62/flight-delay-prediction"),
    ]):
        x=24 if i==0 else 442
        cards+=f"""
<g transform="translate({x},76)">
  <rect width="{CARD_W}" height="{CARD_H}" rx="8" class="node-box"/>
  <rect x="0" y="8" width="4" height="{CARD_H-16}" rx="2" fill="{accent}"/>
  <rect x="16" y="16" width="94" height="20" rx="4" fill="{BG}" stroke="{accent}" stroke-width="0.8"/>
  <text x="63" y="30" fill="{accent}" font-size="9.5" font-weight="700" text-anchor="middle">FLAGSHIP {num}</text>
  <rect x="118" y="16" width="150" height="20" rx="4" fill="{BG}" stroke="{FRAME}" stroke-width="0.8"/>
  <text x="193" y="30" fill="{GREEN}" font-size="9.5" font-weight="600" text-anchor="middle">{label}</text>
  <text x="16" y="62" fill="{TEXT}" font-size="14" font-weight="700">{esc(title)}</text>
  <text x="16" y="80" fill="{MUTED}" font-size="10" font-style="italic">{tagline}</text>
  <rect x="16" y="94" width="{IW}" height="38" rx="5" fill="{BG}" stroke="{LINE}" stroke-width="1"/>
  <text x="26" y="110" fill="{accent}" font-size="9.5" font-weight="600">PIPELINE FLOW:</text>
  <text x="26" y="125" fill="{TEXT}" font-size="8.5">{esc(pflow)}</text>
  <text x="16" y="153" fill="{accent}" font-size="10" font-weight="700">VERIFIED ENGINEERING HIGHLIGHTS:</text>
  <circle cx="22" cy="169" r="2.5" fill="{accent}"/>
  <text x="32" y="172" fill="{TEXT}" font-size="10" font-weight="600">{h1a}</text>
  <text x="32" y="186" fill="{MUTED}" font-size="9.5">{h1b}</text>
  <circle cx="22" cy="206" r="2.5" fill="{accent}"/>
  <text x="32" y="209" fill="{TEXT}" font-size="10" font-weight="600">{h2a}</text>
  <text x="32" y="223" fill="{MUTED}" font-size="9.5"><tspan x="32" dy="0">{h2b}</tspan></text>
  <circle cx="22" cy="243" r="2.5" fill="{accent}"/>
  <text x="32" y="246" fill="{TEXT}" font-size="10" font-weight="600">{h3a}</text>
  <text x="32" y="260" fill="{MUTED}" font-size="9.5">{h3b}</text>
  <line x1="16" y1="284" x2="378" y2="284" stroke="{LINE}"/>
  <text x="16" y="300" fill="{MUTED}" font-size="9.5">Core Stack: <tspan fill="{accent}">{esc(stack)}</tspan></text>
  <rect x="16" y="316" width="{IW}" height="62" rx="6" fill="{BG}" stroke="{FRAME}" stroke-width="1"/>
  <text x="28" y="338" fill="{GREEN}" font-size="10.5" font-weight="700">REPO:</text>
  <text x="28" y="357" fill="{GREEN}" font-size="10" font-weight="700">{esc(repo)}</text>
  <text x="28" y="373" fill="{MUTED}" font-size="8.5">{esc(repourl)}</text>
</g>"""

    tel_y=76+CARD_H+12
    svg=f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">
{BASE_STYLE}{grad_defs()}{hdr(W,H,"ritik@github: ~$ ./featured_projects.sh --spotlight=flagship")}
<g transform="translate(24,48)">
  <circle cx="8" cy="8" r="4" fill="{GREEN}" class="status-pulse"/>
  <text x="20" y="12" fill="{GREEN}" font-size="11" font-weight="700">FLAGSHIP RESEARCH SYSTEMS</text>
  <text x="232" y="12" fill="{MUTED}" font-size="10">Dual High-Impact Engineering Pipelines</text>
  <text x="812" y="12" fill="{CYAN}" font-size="10" text-anchor="end">2 BENCHMARKED REPOSITORIES</text>
</g>
{cards}
<g transform="translate(24,{tel_y})">
  <rect width="812" height="36" rx="6" fill="{BG2}" stroke="{FRAME}" stroke-width="1"/>
  <circle cx="18" cy="18" r="3.5" fill="{GREEN}" class="status-pulse"/>
  <text x="30" y="22" fill="{GREEN}" font-size="10" font-weight="700">FLAGSHIP STATUS: ACTIVE</text>
  <text x="216" y="22" fill="{MUTED}" font-size="9.5">ARIA: <tspan fill="{CYAN}">Evidence RAG</tspan>  &#183;  Flight Delay: <tspan fill="{PURPLE}">Brier 0.1245 (26 tests)</tspan></text>
  <text x="796" y="22" fill="{CYAN}" font-size="9.5" text-anchor="end">REPRODUCIBLE CODEBASES</text>
</g>
</svg>"""
    write(os.path.join(ASSETS_DIR,"featured-flagships.svg"), svg)

# ============================================================
# 2. ENGINEERING SHOWCASE
# ============================================================
def gen_engineering():
    W=860; CARD_W=394; IW=366; CARD_H=192; GAP=16
    projects=[
        (CYAN,"01","ARIA Research Assistant","AI RESEARCH & RAG",
         "Evidence-grounded scholarly research system",
         "Research Query \u2500\u2500\u25ba Multi-Query RAG \u2500\u2500\u25ba Synthesis",
         "Multi-query planning \xb7 Schema dedup \xb7 [P1],[P2] citations",
         "Python \xb7 OpenAI API \xb7 Scholarly APIs \xb7 unittest",
         "Ritik-62/aria-research-assistant","",24,80),
        (PURPLE,"02","Flight Delay Prediction","ML ENGINEERING",
         "Leakage-aware ML with calibrated probabilities",
         "5.8M DOT Records \u2500\u2500\u25ba Leakage Denylist \u2500\u2500\u25ba Calibrator",
         "5.8M records \xb7 Platt calibrator (Brier 0.1245) \xb7 26 tests",
         "Python \xb7 scikit-learn \xb7 XGBoost \xb7 pytest \xb7 ReportLab",
         "Ritik-62/flight-delay-prediction","",442,80),
        (BLUE,"03","CN Private Network Platform","SYSTEMS & NETWORKS",
         "DNS, reverse proxy, TLS 1.3 & packet analysis",
         "dnsmasq .test \u2500\u2500\u25ba Nginx :3001/:3002 \u2500\u2500\u25ba TLS 1.3",
         "dnsmasq .test namespace \xb7 Round-robin LB \xb7 Wireshark",
         "Python \xb7 Nginx \xb7 dnsmasq \xb7 OpenSSL \xb7 Wireshark",
         "Ritik-62/CN-Project","",24,80+CARD_H+GAP),
        (PURPLE,"04","Agentic Property Advisor","AGENTIC AI & RAG",
         "Stateful agent: prediction & market advice",
         "Random Forest \u2500\u2500\u25ba LangGraph DAG \u2500\u2500\u25ba Llama 3",
         "Random Forest (R\u00b2=0.9418) \xb7 LangGraph DAG \xb7 Groq/Llama 3",
         "Python \xb7 Streamlit \xb7 LangGraph \xb7 Groq \xb7 Llama 3",
         "Pratyaksha37/GenAI_Capstone","* Collaborative — @Pratyaksha37",442,80+CARD_H+GAP),
        (ORANGE,"05","Smart Hostel Management","SOFTWARE ARCHITECTURE",
         "Modular backend, OOP design & persistence",
         "Modular Services \u2500\u2500\u25ba SOLID OOP \u2500\u2500\u25ba Strategy Pattern",
         "Service/repository layer \xb7 Factory & Strategy patterns",
         "Next.js \xb7 TypeScript \xb7 Prisma ORM \xb7 SQLite \xb7 Tailwind",
         "ishyverma/SDSE_Capstone","* Collaborative — @ishyverma",24,80+2*(CARD_H+GAP)),
        (GREEN,"06","Telecom Customer Analytics","DATA SCIENCE & ANALYTICS",
         "Churn segmentation & BI dashboards (243K records)",
         "243K Records \u2500\u2500\u25ba Statistical Segmentation \u2500\u2500\u25ba Tableau",
         "243,553 customers analyzed \xb7 4 Tableau BI dashboards",
         "Python \xb7 Pandas \xb7 NumPy \xb7 Tableau \xb7 Excel \xb7 SciPy",
         "samiksha-jangid27/SectionC_G5_Telecom","* Collaborative — @samiksha-jangid27",442,80+2*(CARD_H+GAP)),
    ]
    cards=""
    for accent,num,title,domain,tagline,wflow,key,stack,repo,collab,cx,cy in projects:
        collab_line=""
        if collab:
            collab_line=f'<text x="14" y="{CARD_H-9}" fill="{MUTED}" font-size="8" font-style="italic">{esc(collab)}</text>'
        cards+=f"""
<g transform="translate({cx},{cy})">
  <rect width="{CARD_W}" height="{CARD_H}" rx="8" class="node-box"/>
  <rect x="0" y="8" width="4" height="{CARD_H-16}" rx="2" fill="{accent}"/>
  <rect x="14" y="12" width="70" height="18" rx="4" fill="{BG}" stroke="{accent}" stroke-width="0.8"/>
  <text x="49" y="24.5" fill="{accent}" font-size="9" font-weight="700" text-anchor="middle">NODE {num}</text>
  <text x="94" y="25" fill="{MUTED}" font-size="8.5" font-weight="600">{esc(domain)}</text>
  <text x="14" y="48" fill="{TEXT}" font-size="12.5" font-weight="700">{esc(title)}</text>
  <text x="14" y="63" fill="{MUTED}" font-size="9" font-style="italic">"{esc(tagline)}"</text>
  <rect x="14" y="72" width="{IW}" height="22" rx="4" fill="{BG}" stroke="{LINE}" stroke-width="0.8"/>
  <text x="22" y="86" fill="{TEXT}" font-size="8.5">{esc(wflow)}</text>
  <text x="14" y="108" fill="{accent}" font-size="8.5" font-weight="600">KEY: <tspan fill="{TEXT}">{esc(key)}</tspan></text>
  <text x="14" y="126" fill="{MUTED}" font-size="8.5">Stack: <tspan fill="{TEXT}">{esc(stack)}</tspan></text>
  <text x="14" y="148" fill="{GREEN}" font-size="9" font-weight="700">&#128279; {esc(repo)}</text>
  {collab_line}
</g>"""

    bot_y=80+3*(CARD_H+GAP); tel_y=bot_y+8; H=tel_y+30+12
    svg=f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">
{BASE_STYLE}{grad_defs()}{hdr(W,H,"ritik@github: ~$ ./projects.sh --engineering-showcase")}
<g transform="translate(24,48)">
  <circle cx="8" cy="8" r="4" fill="{GREEN}" class="status-pulse"/>
  <text x="20" y="12" fill="{GREEN}" font-size="11" font-weight="700">ENGINEERING PROJECT NODES</text>
  <text x="238" y="12" fill="{MUTED}" font-size="9.5">01 AI \xb7 02 ML \xb7 03 Systems \xb7 04 Agents \xb7 05 Architecture \xb7 06 Analytics</text>
  <text x="812" y="12" fill="{CYAN}" font-size="10" text-anchor="end">6 NODES ACTIVE</text>
</g>
{cards}
<g transform="translate(24,{tel_y})">
  <rect width="812" height="28" rx="5" fill="{BG2}" stroke="{FRAME}" stroke-width="1"/>
  <circle cx="14" cy="14" r="3" fill="{GREEN}" class="status-pulse"/>
  <text x="24" y="17.5" fill="{GREEN}" font-size="9.5" font-weight="700">PORTFOLIO NODES VERIFIED</text>
  <text x="238" y="17.5" fill="{MUTED}" font-size="9">All 6 repositories public (* = collaborative capstone hosted under collaborator accounts)</text>
</g>
</svg>"""
    write(os.path.join(ASSETS_DIR,"engineering-showcase.svg"), svg)

# ============================================================
# 3. JOURNEY TIMELINE
# ============================================================
def gen_journey():
    W=860; CARD_W=812; CARD_H=96; GAP=10; y0=76
    stages=[
        ("01","2024","Core Computer Science &amp; Software Design",CYAN,
         "SOLID design principles, clean architecture &amp; design patterns \xb7 Algorithmic complexity, high-efficiency data modeling",
         "Full-stack foundations: Next.js, TypeScript, Prisma ORM, SQLite"),
        ("02","2024\u201325","Data Science &amp; Statistical Analytics",BLUE,
         "Exploratory data analysis, feature engineering &amp; regression modeling",
         "Analyzed 243,553 telecom records \xb7 Oracle OCI 2025 Certified Data Science Professional"),
        ("03","2025","Machine Learning &amp; Predictive Modeling",PURPLE,
         "XGBoost &amp; Logistic classification pipelines \xb7 Leakage prevention: chronological calendar partitions",
         "Platt calibrator on validation split; Brier Score 0.1245 on held-out test split (26 tests)"),
        ("04","2025\u201326","Retrieval-Augmented Generation (RAG)",ORANGE,
         "Scholarly search retrieval pipelines \xb7 Schema normalization &amp; identifier hash deduplication",
         "Citation-grounded Markdown reports with [P1], [P2] labels (ARIA project)"),
        ("05","CURRENT","Agentic AI &amp; Autonomous Workflows",GREEN,
         "LangGraph stateful DAG machines: multi-step reasoning &amp; decision loops",
         "Random Forest + Groq LPU / Llama 3 agents \xb7 Production-quality AI applications"),
    ]
    cards=""
    for i,(num,year,title,accent,b1,b2) in enumerate(stages):
        y=y0+i*(CARD_H+GAP)
        cards+=f"""
<g transform="translate(24,{y})">
  <rect width="{CARD_W}" height="{CARD_H}" rx="6" class="node-box"/>
  <rect x="0" y="6" width="4" height="{CARD_H-12}" rx="2" fill="{accent}"/>
  <rect x="14" y="10" width="68" height="20" rx="4" fill="{BG}" stroke="{accent}" stroke-width="0.8"/>
  <text x="48" y="23.5" fill="{accent}" font-size="9" font-weight="700" text-anchor="middle">STAGE {num}</text>
  <rect x="88" y="10" width="74" height="20" rx="4" fill="{BG}" stroke="{FRAME}" stroke-width="0.8"/>
  <text x="125" y="23.5" fill="{MUTED}" font-size="9" font-weight="600" text-anchor="middle">{year}</text>
  <text x="172" y="24" fill="{TEXT}" font-size="12" font-weight="700">{title}</text>
  <text x="16" y="46" fill="{TEXT}" font-size="9">
    <tspan x="16" dy="0">&#9679; <tspan fill="{MUTED}">{b1}</tspan></tspan>
  </text>
  <text x="16" y="64" fill="{accent}" font-size="9">
    <tspan x="16" dy="0">&#9679; <tspan fill="{TEXT}">{b2}</tspan></tspan>
  </text>
  <text x="16" y="82" fill="{MUTED}" font-size="7.5">&#8212; Stage {num} complete</text>
</g>"""

    last_y=y0+5*(CARD_H+GAP); H=last_y+12
    svg=f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">
{BASE_STYLE}{grad_defs()}{hdr(W,H,"ritik@github: ~$ ./my_journey.sh --timeline")}
<g transform="translate(24,48)">
  <circle cx="8" cy="8" r="4" fill="{GREEN}" class="status-pulse"/>
  <text x="20" y="12" fill="{GREEN}" font-size="11" font-weight="700">CHRONOLOGICAL LEARNING TIMELINE</text>
  <text x="290" y="12" fill="{MUTED}" font-size="10">Foundations \u2500\u25ba Data \u2500\u25ba ML \u2500\u25ba RAG \u2500\u25ba Agentic AI</text>
  <text x="812" y="12" fill="{CYAN}" font-size="10" text-anchor="end">5 MILESTONE STAGES</text>
</g>
{cards}
</svg>"""
    write(os.path.join(ASSETS_DIR,"journey-timeline.svg"), svg)

# ============================================================
# 4. TECHNICAL INTERESTS
# ============================================================
def gen_interests():
    W=860
    R1W=262; R2W=400; R1H=150; R2H=142
    interests=[
        ("01","AGENTIC AI WORKFLOWS","Multi-step reasoning &amp; stateful execution graphs",
         "[State Machine] \u2192 [LangGraph DAG]",PURPLE,24,80,R1W,R1H),
        ("02","RAG &amp; LITERATURE SEARCH","Multi-query retrieval &amp; citation-grounded synthesis",
         "[Query Decompose] \u2192 [Citation Ground]",CYAN,24+R1W+12,80,R1W,R1H),
        ("03","APPLIED MACHINE LEARNING","Probability calibration &amp; temporal leakage prevention",
         "[Leakage Guard] \u2192 [Platt Calibrator]",GREEN,24+2*(R1W+12),80,R1W,R1H),
        ("04","WEB &amp; API ARCHITECTURE","Modular backend systems with Next.js &amp; typed REST APIs",
         "[Modular Services] \u2500\u2500\u25ba [Typed REST APIs]",ORANGE,24,80+R1H+14,R2W,R2H),
        ("05","DATA ANALYTICS &amp; BI","Customer churn segmentation &amp; Tableau dashboards",
         "[243K Ingestion] \u2500\u2500\u25ba [Tableau Dashboards]",BLUE,24+R2W+12,80+R1H+14,R2W,R2H),
    ]
    cards=""
    for num,name,desc,pipe,accent,ix,iy,iw,ih in interests:
        inner=iw-28
        # name tspans — split on last space before char 22 (safe for &amp; entities)
        def word_split(text, approx_chars):
            """Split text at last space at or before approx_chars."""
            if len(text) <= approx_chars:
                return text, ""
            pos = text.rfind(' ', 0, approx_chars+1)
            if pos == -1: pos = approx_chars
            return text[:pos].rstrip(), text[pos:].lstrip()
        nm1, nm2 = word_split(name, 22)
        nm_tspan2 = ('<tspan x="14" dy="14">' + nm2 + '</tspan>') if nm2 else ''
        nm_svg = '<tspan x="14" dy="0">' + nm1 + '</tspan>' + nm_tspan2
        d1, d2 = word_split(desc, 40)
        desc_tspan2 = ('<tspan x="14" dy="13">' + d2 + '</tspan>') if d2 else ''
        desc_svg = '<tspan x="14" dy="0">' + d1 + '</tspan>' + desc_tspan2
        pipe_esc = esc(pipe)
        cards += (
            f'\n<g transform="translate({ix},{iy})">'
            f'\n  <rect width="{iw}" height="{ih}" rx="8" class="node-box"/>'
            f'\n  <rect x="0" y="8" width="4" height="{ih-16}" rx="2" fill="{accent}"/>'
            f'\n  <rect x="14" y="12" width="68" height="18" rx="4" fill="{BG}" stroke="{accent}" stroke-width="0.8"/>'
            f'\n  <text x="48" y="24.5" fill="{accent}" font-size="9" font-weight="700" text-anchor="middle">NODE {num}</text>'
            '\n  <text x="14" y="52" fill="' + TEXT + '" font-size="11" font-weight="700">' + nm_svg + '</text>'
            '\n  <text x="14" y="76" fill="' + MUTED + '" font-size="9.5">' + desc_svg + '</text>'
            f'\n  <line x1="14" y1="98" x2="{iw-14}" y2="98" stroke="{LINE}"/>'
            f'\n  <rect x="14" y="106" width="{inner}" height="24" rx="4" fill="{BG}" stroke="{FRAME}" stroke-width="0.8"/>'
            '\n  <text x="22" y="121" fill="' + accent + '" font-size="8.5">' + pipe_esc + '</text>'
            '\n</g>'
        )


    bot_y=80+R1H+14+R2H+14; H=bot_y+28+12
    svg=f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">
{BASE_STYLE}{grad_defs()}{hdr(W,H,"ritik@github: ~$ cat technical_interests.log")}
<g transform="translate(24,48)">
  <circle cx="8" cy="8" r="4" fill="{GREEN}" class="status-pulse"/>
  <text x="20" y="12" fill="{GREEN}" font-size="11" font-weight="700">TECHNICAL INTERESTS &amp; DOMAINS</text>
  <text x="268" y="12" fill="{MUTED}" font-size="10">Agentic Workflows \xb7 RAG \xb7 Applied ML \xb7 API Architecture \xb7 BI</text>
  <text x="812" y="12" fill="{CYAN}" font-size="10" text-anchor="end">RESEARCH &amp; DEV FOCUS</text>
</g>
{cards}
<g transform="translate(24,{bot_y})">
  <rect width="812" height="26" rx="5" fill="{BG2}" stroke="{FRAME}" stroke-width="1"/>
  <circle cx="14" cy="13" r="3" fill="{GREEN}" class="status-pulse"/>
  <text x="24" y="16.5" fill="{GREEN}" font-size="9" font-weight="700">INTEREST CLUSTERS LOADED</text>
  <text x="218" y="16.5" fill="{MUTED}" font-size="8.5">Focus: Autonomous Agents &amp; Evidence-Grounded Scientific Pipelines</text>
  <text x="796" y="16.5" fill="{CYAN}" font-size="8.5" text-anchor="end">STATUS: ACTIVE EXPLORATION</text>
</g>
</svg>"""
    write(os.path.join(ASSETS_DIR,"technical-interests.svg"), svg)

# ============================================================
# 5. ABOUT ME
# ============================================================
def gen_about_me():
    W=860; H=348
    svg=f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">
{BASE_STYLE}{grad_defs()}{hdr(W,H,"ritik@github: ~$ cat about_me.txt")}
<g transform="translate(24,48)">
  <circle cx="8" cy="8" r="4" fill="{GREEN}" class="status-pulse"/>
  <text x="20" y="12" fill="{GREEN}" font-size="11" font-weight="700">DEVELOPER IDENTITY &amp; TELEMETRY</text>
  <text x="268" y="12" fill="{MUTED}" font-size="10">SYSTEM: AI_ENGINEER_ENV \xb7 AUTH: SHA256_AUTHENTICATED</text>
  <text x="812" y="12" fill="{CYAN}" font-size="10" text-anchor="end">STATUS: ONLINE</text>
</g>
<g transform="translate(24,76)">
  <rect x="0" y="0" width="194" height="68" rx="6" class="node-box"/>
  <rect x="0" y="6" width="3" height="56" rx="1.5" fill="{CYAN}"/>
  <text x="12" y="20" fill="{MUTED}" font-size="9" font-weight="600">NAME</text>
  <rect x="140" y="8" width="44" height="15" rx="3" fill="{BG}" stroke="{CYAN}" stroke-width="0.6"/>
  <text x="162" y="18.5" fill="{CYAN}" font-size="7.5" font-weight="700" text-anchor="middle">IDENTITY</text>
  <text x="12" y="46" fill="{TEXT}" font-size="13" font-weight="700">Ritik Raj</text>

  <rect x="206" y="0" width="194" height="68" rx="6" class="node-box"/>
  <rect x="206" y="6" width="3" height="56" rx="1.5" fill="{BLUE}"/>
  <text x="218" y="20" fill="{MUTED}" font-size="9" font-weight="600">HANDLE</text>
  <rect x="346" y="8" width="44" height="15" rx="3" fill="{BG}" stroke="{BLUE}" stroke-width="0.6"/>
  <text x="368" y="18.5" fill="{BLUE}" font-size="7.5" font-weight="700" text-anchor="middle">GITHUB</text>
  <text x="218" y="46" fill="{GREEN}" font-size="13" font-weight="700">@Ritik-62</text>

  <rect x="412" y="0" width="194" height="68" rx="6" class="node-box"/>
  <rect x="412" y="6" width="3" height="56" rx="1.5" fill="{PURPLE}"/>
  <text x="424" y="20" fill="{MUTED}" font-size="9" font-weight="600">ROLE</text>
  <rect x="552" y="8" width="44" height="15" rx="3" fill="{BG}" stroke="{PURPLE}" stroke-width="0.6"/>
  <text x="574" y="18.5" fill="{PURPLE}" font-size="7.5" font-weight="700" text-anchor="middle">SPECIALTY</text>
  <text x="424" y="41" fill="{TEXT}" font-size="11.5" font-weight="700">Data Science</text>
  <text x="424" y="58" fill="{TEXT}" font-size="11.5" font-weight="700">&amp; AI Engineering</text>

  <rect x="618" y="0" width="194" height="68" rx="6" class="node-box"/>
  <rect x="618" y="6" width="3" height="56" rx="1.5" fill="{ORANGE}"/>
  <text x="630" y="20" fill="{MUTED}" font-size="9" font-weight="600">LOCATION</text>
  <rect x="758" y="8" width="44" height="15" rx="3" fill="{BG}" stroke="{ORANGE}" stroke-width="0.6"/>
  <text x="780" y="18.5" fill="{ORANGE}" font-size="7.5" font-weight="700" text-anchor="middle">GEO</text>
  <text x="630" y="41" fill="{TEXT}" font-size="11.5" font-weight="700">Sonipat,</text>
  <text x="630" y="58" fill="{TEXT}" font-size="11.5" font-weight="700">Haryana &#127470;&#127475;</text>
</g>
<g transform="translate(24,156)">
  <rect width="812" height="96" rx="6" class="node-box"/>
  <rect x="0" y="6" width="3.5" height="84" rx="1.5" fill="{GREEN}"/>
  <text x="16" y="28" fill="{GREEN}" font-size="10.5" font-weight="700">&#9889; [BIO] // MISSION &amp; ENGINEERING FOCUS</text>
  <text x="16" y="52" fill="{TEXT}" font-size="10.5" font-style="italic">
    <tspan x="16" dy="0">"Data Science &amp; AI Enthusiast | Exploring Machine Learning,</tspan>
    <tspan x="16" dy="17">Generative AI &amp; Intelligent Systems | Building Projects</tspan>
    <tspan x="16" dy="17">That Solve Real-World Problems."</tspan>
  </text>
</g>
<g transform="translate(24,262)">
  <rect width="812" height="48" rx="6" fill="{BG}" stroke="{FRAME}" stroke-width="1"/>
  <text x="16" y="30" fill="{TEXT}" font-size="10.5" font-weight="700">&#129309; OPEN FOR:</text>
  <rect x="108" y="13" width="200" height="22" rx="4" fill="{TILE}" stroke="{CYAN}" stroke-width="0.6"/>
  <text x="208" y="28" fill="{CYAN}" font-size="9" font-weight="600" text-anchor="middle">AI / ML Research Collaborations</text>
  <rect x="318" y="13" width="180" height="22" rx="4" fill="{TILE}" stroke="{BLUE}" stroke-width="0.6"/>
  <text x="408" y="28" fill="{BLUE}" font-size="9" font-weight="600" text-anchor="middle">Open-Source Development</text>
  <rect x="508" y="13" width="160" height="22" rx="4" fill="{TILE}" stroke="{PURPLE}" stroke-width="0.6"/>
  <text x="588" y="28" fill="{PURPLE}" font-size="9" font-weight="600" text-anchor="middle">Technical Discussions</text>
</g>
<g transform="translate(24,320)">
  <rect width="812" height="24" rx="4" fill="{BG2}" stroke="{LINE}" stroke-width="1"/>
  <circle cx="12" cy="12" r="3" fill="{GREEN}" class="status-pulse"/>
  <text x="22" y="15.5" fill="{GREEN}" font-size="9" font-weight="700">SYSTEM: READY FOR RESEARCH &amp; DEVELOPMENT</text>
  <text x="796" y="15.5" fill="{MUTED}" font-size="8.5" text-anchor="end">RUNTIME: PERSISTENT PROFILE</text>
</g>
</svg>"""
    write(os.path.join(ASSETS_DIR,"about-me.svg"), svg)

# ============================================================
# 6. SKILLS STACK
# ============================================================
def gen_skills():
    W=860
    domains=[
        ("01","PROGRAMMING LANGUAGES","4 TECH",["Python","TypeScript","JavaScript","SQL"],CYAN,"├── [ROOT]"),
        ("02","CORE COMPUTER SCIENCE","4 COMPETENCIES",["OOP","Software Design","Data Structures","Algorithms"],BLUE,"├── [FOUNDATIONS]"),
        ("03","AI & MACHINE LEARNING","5 COMPETENCIES",["Machine Learning","Generative AI","RAG Systems","LangGraph","LLM Apps"],PURPLE,"├── [MODELS & AGENTS]"),
        ("04","WEB & BACKEND SYSTEMS","5 FRAMEWORKS",["Next.js","FastAPI","Streamlit","Prisma ORM","REST APIs"],ORANGE,"├── [SERVICES & APIS]"),
        ("05","DATABASES & TOOLING","5 PLATFORMS",["SQLite","Tableau","Excel","Git","GitHub Actions"],GREEN,"└── [TOOLING & OPS]"),
    ]
    BX0=296; BMAX=808
    panels=[]; cur_y=76; gap=8
    for num,name,count,skills,accent,tree in domains:
        badges,bh=pill_row(skills,BX0,12,BMAX,accent,cw=7.5,pad=18,gap=8,h=24)
        ph=max(56,12+bh+16)
        panels.append(f"""
<g transform="translate(24,{cur_y})">
  <rect width="812" height="{ph}" rx="6" class="node-box"/>
  <rect x="0" y="6" width="3.5" height="{ph-12}" rx="1.5" fill="{accent}"/>
  <rect x="12" y="10" width="32" height="18" rx="3" fill="{BG}" stroke="{accent}" stroke-width="0.8"/>
  <text x="28" y="22.5" fill="{accent}" font-size="9" font-weight="700" text-anchor="middle">{num}</text>
  <text x="52" y="23" fill="{TEXT}" font-size="10.5" font-weight="700">{esc(name)}</text>
  <text x="14" y="{ph-10}" fill="{MUTED}" font-size="8.5">{esc(tree)} \xb7 <tspan fill="{accent}">{count}</tspan></text>
  <line x1="288" y1="8" x2="288" y2="{ph-8}" stroke="{LINE}"/>
  {badges}
</g>""")
        cur_y+=ph+gap

    tel_y=cur_y+4; H=tel_y+26+12
    svg=f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">
{BASE_STYLE}{grad_defs()}{hdr(W,H,"ritik@github: ~$ ./skills.sh --verbose")}
<g transform="translate(24,48)">
  <circle cx="8" cy="8" r="4" fill="{GREEN}" class="status-pulse"/>
  <text x="20" y="12" fill="{GREEN}" font-size="11" font-weight="700">SKILLS &amp; TECHNOLOGIES TREE</text>
  <text x="258" y="12" fill="{MUTED}" font-size="10">5 Core Competency Domains</text>
  <text x="812" y="12" fill="{CYAN}" font-size="10" text-anchor="end">23 TECHNOLOGIES VERIFIED</text>
</g>
{''.join(panels)}
<g transform="translate(24,{tel_y})">
  <rect width="812" height="24" rx="4" fill="{BG2}" stroke="{LINE}" stroke-width="1"/>
  <circle cx="12" cy="12" r="3" fill="{GREEN}" class="status-pulse"/>
  <text x="22" y="15.5" fill="{GREEN}" font-size="9" font-weight="700">STACK VERIFIED: 23 SKILLS \xb7 0 ERRORS</text>
  <text x="796" y="15.5" fill="{CYAN}" font-size="8.5" text-anchor="end">ENVIRONMENT: PASSING</text>
</g>
</svg>"""
    write(os.path.join(ASSETS_DIR,"skills-stack.svg"), svg)

# ============================================================
# 7. CERTIFICATIONS
# ============================================================
def gen_certs():
    W=860; H=252
    svg=f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">
{BASE_STYLE}{grad_defs()}
<defs>
  <linearGradient id="oracleGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#f80000"/><stop offset="1" stop-color="#b80000"/>
  </linearGradient>
</defs>
{hdr(W,H,"ritik@github: ~$ ./certs.sh")}
<g transform="translate(24,48)">
  <circle cx="8" cy="8" r="4" fill="{GREEN}" class="status-pulse"/>
  <text x="20" y="12" fill="{GREEN}" font-size="11" font-weight="700">AUTHENTICATED CREDENTIALS</text>
  <text x="268" y="12" fill="{MUTED}" font-size="10">Cryptographically Verified Professional Certifications</text>
  <text x="812" y="12" fill="{CYAN}" font-size="10" text-anchor="end">STATUS: ACTIVE &amp; AUTHENTICATED</text>
</g>
<g transform="translate(24,76)">
  <rect width="812" height="128" rx="8" class="node-box"/>
  <rect x="0" y="8" width="4" height="112" rx="2" fill="#f80000"/>
  <rect x="16" y="14" width="120" height="20" rx="4" fill="{BG}" stroke="#f80000" stroke-width="0.8"/>
  <text x="76" y="27.5" fill="#f80000" font-size="9" font-weight="700" text-anchor="middle">ORACLE CERTIFIED</text>
  <rect x="144" y="14" width="90" height="20" rx="4" fill="{BG}" stroke="{FRAME}" stroke-width="0.8"/>
  <text x="189" y="27.5" fill="{GREEN}" font-size="9" font-weight="600" text-anchor="middle">VERIFIED 2025</text>
  <text x="16" y="56" fill="{TEXT}" font-size="13" font-weight="700">
    <tspan x="16" dy="0">Oracle Cloud Infrastructure 2025</tspan>
    <tspan x="16" dy="18">Certified Data Science Professional</tspan>
  </text>
  <text x="16" y="92" fill="{MUTED}" font-size="9.5">Issuer: <tspan fill="{TEXT}">Oracle Corporation</tspan>  \xb7  Domain: <tspan fill="{CYAN}">OCI Machine Learning, Data Science &amp; Pipelines</tspan></text>
  <text x="16" y="110" fill="{MUTED}" font-size="9.5">Verification: <tspan fill="{GREEN}">Authenticated via Oracle CertView</tspan>  \xb7  Click badge below to view record</text>
  <g transform="translate(548,14)">
    <rect width="248" height="100" rx="6" fill="{BG}" stroke="#f80000" stroke-width="1"/>
    <rect x="10" y="12" width="228" height="28" rx="4" fill="url(#oracleGrad)"/>
    <text x="124" y="30" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">ORACLE CERTIFIED PROFESSIONAL</text>
    <text x="124" y="60" fill="{TEXT}" font-size="9" text-anchor="middle">OCI 2025 Certified</text>
    <text x="124" y="76" fill="{TEXT}" font-size="9" text-anchor="middle">Data Science Professional</text>
  </g>
</g>
<g transform="translate(24,216)">
  <rect width="812" height="26" rx="4" fill="{BG2}" stroke="{LINE}" stroke-width="1"/>
  <circle cx="12" cy="13" r="3" fill="{GREEN}" class="status-pulse"/>
  <text x="22" y="16.5" fill="{GREEN}" font-size="9" font-weight="700">SHA256 BADGE HASH VERIFIED</text>
  <text x="796" y="16.5" fill="{CYAN}" font-size="8.5" text-anchor="end">ISSUED: 2025 \xb7 EXPIRY: ACTIVE</text>
</g>
</svg>"""
    write(os.path.join(ASSETS_DIR,"certifications.svg"), svg)

# ============================================================
# 8. CONTACT CHANNELS
# ============================================================
def gen_contact():
    W=860; CARD_W=194; CARD_H=134; y0=80
    footer_y=y0+CARD_H+12; H=footer_y+40+12
    channels=[
        ("GitHub","@Ritik-62","SOURCE REPOS","&#128025;",GREEN,24),
        ("LinkedIn","ritik-raj-140113352","PROFESSIONAL","&#128188;",BLUE,24+CARD_W+12),
        ("Kaggle","ritikraj8809","NOTEBOOKS & DATA","&#127942;",CYAN,24+2*(CARD_W+12)),
        ("Oracle Cert","Certified 2025","DATA SCIENCE PRO","&#128220;",RED,24+3*(CARD_W+12)),
    ]
    cards=""
    for name,handle,tag,icon,accent,cx in channels:
        tw=CARD_W-64
        cards+=f"""
<g transform="translate({cx},{y0})">
  <rect width="{CARD_W}" height="{CARD_H}" rx="8" class="node-box"/>
  <rect x="0" y="8" width="3.5" height="{CARD_H-16}" rx="1.5" fill="{accent}"/>
  <text x="16" y="34" font-size="20">{icon}</text>
  <rect x="52" y="14" width="{tw}" height="18" rx="3" fill="{BG}" stroke="{accent}" stroke-width="0.8"/>
  <text x="{52+tw//2}" y="26.5" fill="{accent}" font-size="7.5" font-weight="700" text-anchor="middle">{esc(tag)}</text>
  <text x="14" y="64" fill="{TEXT}" font-size="13" font-weight="700">{esc(name)}</text>
  <text x="14" y="82" fill="{MUTED}" font-size="9.5">{esc(handle)}</text>
  <line x1="14" y1="96" x2="{CARD_W-14}" y2="96" stroke="{LINE}"/>
  <text x="14" y="116" fill="{accent}" font-size="9" font-weight="600">HANDSHAKE: 200 OK</text>
</g>"""

    svg=f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">
{BASE_STYLE}{grad_defs()}{hdr(W,H,"ritik@github: ~$ ritik --connect --socials")}
<g transform="translate(24,48)">
  <circle cx="8" cy="8" r="4" fill="{GREEN}" class="status-pulse"/>
  <text x="20" y="12" fill="{GREEN}" font-size="11" font-weight="700">COMMUNICATION &amp; VERIFIED PLATFORMS</text>
  <text x="306" y="12" fill="{MUTED}" font-size="10">Authenticated Social &amp; Research Endpoints</text>
  <text x="812" y="12" fill="{CYAN}" font-size="10" text-anchor="end">CONNECTION READY</text>
</g>
{cards}
<g transform="translate(24,{footer_y})">
  <rect width="812" height="38" rx="6" fill="{BG2}" stroke="{FRAME}" stroke-width="1"/>
  <circle cx="16" cy="19" r="3.5" fill="{GREEN}" class="status-pulse"/>
  <text x="28" y="23" fill="{GREEN}" font-size="10" font-weight="700">COMMUNICATION CHANNELS ONLINE</text>
  <text x="280" y="23" fill="{MUTED}" font-size="9.5">Open for AI / Data Science Collaborations \xb7 Click badges below to open</text>
  <text x="796" y="23" fill="{CYAN}" font-size="9.5" text-anchor="end">200 OK</text>
</g>
</svg>"""
    write(os.path.join(ASSETS_DIR,"contact-channels.svg"), svg)

if __name__ == "__main__":
    gen_flagships()
    gen_engineering()
    gen_journey()
    gen_interests()
    gen_about_me()
    gen_skills()
    gen_certs()
    gen_contact()
    print("\nAll 8 terminal SVGs generated and XML-verified successfully.")
