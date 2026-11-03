#!/usr/bin/env python3
"""
Generate preview.html from README.md styled with GitHub Dark theme
so Ritik can preview his complete profile locally in any web browser.
"""
import os
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
README_PATH = os.path.join(ROOT, "README.md")
PREVIEW_PATH = os.path.join(ROOT, "preview.html")

def build_preview():
    with open(README_PATH, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html_body = markdown.markdown(
        md_content,
        extensions=["extra", "tables", "fenced_code", "nl2br"]
    )

    template = f"""<!DOCTYPE html>
<html lang="en" data-color-mode="dark" data-dark-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>GitHub Profile Preview — Ritik Raj (Ritik-62)</title>
  <style>
    * {{
      box-sizing: border-box;
    }}
    body {{
      background-color: #0d1117;
      color: #e6edf3;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
      font-size: 14px;
      line-height: 1.6;
      word-wrap: break-word;
      margin: 0;
      padding: 40px 16px 80px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .preview-banner {{
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 10px 20px;
      margin-bottom: 28px;
      max-width: 900px;
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 12px;
      color: #7d8590;
    }}
    .preview-banner strong {{
      color: #39d353;
    }}
    .markdown-body {{
      max-width: 900px;
      width: 100%;
    }}
    h1, h2, h3, h4, h5, h6 {{
      margin-top: 24px;
      margin-bottom: 16px;
      font-weight: 600;
      line-height: 1.25;
      color: #e6edf3;
    }}
    h3 code {{
      color: #58a6ff;
      background: #161b22;
      padding: 6px 14px;
      border-radius: 6px;
      border: 1px solid #30363d;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 14px;
      display: inline-block;
    }}
    p {{
      margin-top: 0;
      margin-bottom: 16px;
    }}
    a {{
      color: #58a6ff;
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 85%;
      background: rgba(110, 118, 129, 0.4);
      padding: 0.2em 0.4em;
      border-radius: 6px;
    }}
    pre {{
      background-color: #161b22;
      border: 1px solid #30363d;
      border-radius: 6px;
      padding: 16px;
      overflow-x: auto;
      overflow-y: visible;
      font-size: 85%;
      line-height: 1.45;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      color: #e6edf3;
      margin-top: 0;
      margin-bottom: 16px;
      max-width: 100%;
      box-sizing: border-box;
      text-align: left;
    }}
    pre code {{
      background-color: transparent;
      padding: 0;
      font-size: 100%;
      color: inherit;
    }}
    table {{
      border-spacing: 0;
      border-collapse: collapse;
      margin-top: 0;
      margin-bottom: 16px;
      display: block;
      max-width: 100%;
      overflow-x: auto;
      border: 1px solid #30363d;
      border-radius: 6px;
      background: #0d1117;
    }}
    table table {{
      display: table;
      width: 100%;
      margin: 12px 0 16px;
      border: 1px solid #30363d;
      background: #161b22;
      border-radius: 6px;
    }}
    table table th {{
      background: #21262d;
      color: #7d8590;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 8px 12px;
    }}
    table table td {{
      padding: 8px 12px;
      font-size: 13px;
    }}
    td, th {{
      padding: 12px;
      border: 1px solid #21262d;
    }}
    hr {{
      height: 1px;
      background-color: #30363d;
      border: 0;
      margin: 16px 0;
    }}
    img {{
      max-width: 100%;
      box-sizing: content-box;
      background-color: transparent;
    }}
    sub {{
      font-size: 75%;
      line-height: 0;
      position: relative;
      vertical-align: baseline;
    }}
    .vp-btn {{
      background: #21262d;
      color: #c9d1d9;
      border: 1px solid #30363d;
      border-radius: 4px;
      padding: 4px 10px;
      font-size: 11px;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.15s ease;
    }}
    .vp-btn:hover {{
      background: #30363d;
      color: #f0f6fc;
    }}
    .vp-btn.active {{
      background: #1f6feb;
      color: #ffffff;
      border-color: #388bfd;
      font-weight: 600;
    }}
    .markdown-body.wide-view {{
      max-width: 1440px !important;
      transition: max-width 0.3s ease;
    }}
    .markdown-body.mobile-view {{
      max-width: 412px !important;
      border: 1px solid #30363d;
      padding: 16px 12px;
      border-radius: 12px;
      background: #0d1117;
      box-shadow: 0 12px 32px rgba(0,0,0,0.6);
      transition: max-width 0.3s ease;
    }}

    /* Terminal Showcase & 2x2 Engineering Grid */
    .terminal-showcase {{
      background: linear-gradient(180deg, #111722 0%, #0d1117 100%);
      border: 1px solid #30363d;
      border-radius: 10px;
      overflow: clip;
      margin-top: 16px;
      margin-bottom: 24px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
      width: 100%;
      box-sizing: border-box;
    }}
    .terminal-showcase-header {{
      background: #161b22;
      border-bottom: 1px solid #30363d;
      padding: 10px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 12px;
      box-sizing: border-box;
    }}
    .terminal-traffic-lights {{
      display: flex;
      gap: 6px;
    }}
    .dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      display: inline-block;
    }}
    .dot-red {{ background: #ff5f56; }}
    .dot-yellow {{ background: #ffbd2e; }}
    .dot-green {{ background: #27c93f; }}
    .terminal-showcase-title {{
      color: #7d8590;
      font-size: 12px;
    }}
    .terminal-showcase-meta {{
      color: #39d353;
      font-weight: 600;
      font-size: 11px;
      letter-spacing: 0.5px;
    }}
    .workflow-sequence-banner {{
      background: #0d1117;
      border-bottom: 1px solid #21262d;
      padding: 10px 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 11px;
      box-sizing: border-box;
    }}
    .node-pill {{
      padding: 3px 8px;
      border-radius: 4px;
      font-weight: 600;
      font-size: 11px;
    }}
    .pill-cyan {{ background: rgba(34, 211, 238, 0.15); color: #22d3ee; border: 1px solid rgba(34, 211, 238, 0.4); }}
    .pill-purple {{ background: rgba(188, 140, 255, 0.15); color: #bc8cff; border: 1px solid rgba(188, 140, 255, 0.4); }}
    .pill-orange {{ background: rgba(255, 166, 87, 0.15); color: #ffa657; border: 1px solid rgba(255, 166, 87, 0.4); }}
    .pill-green {{ background: rgba(57, 211, 83, 0.15); color: #39d353; border: 1px solid rgba(57, 211, 83, 0.4); }}
    .connector-arrow {{ color: #484f58; font-weight: bold; }}
    
    /* 2x2 Project Grid */
    .project-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
      padding: 20px;
      box-sizing: border-box;
      width: 100%;
    }}
    .project-card {{
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
      position: relative;
      min-width: 0;
      box-sizing: border-box;
      word-wrap: break-word;
      overflow-wrap: break-word;
    }}
    .project-card:hover {{
      border-color: #58a6ff;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5);
    }}
    .card-cyan {{ border-top: 3px solid #22d3ee; }}
    .card-purple {{ border-top: 3px solid #bc8cff; }}
    .card-orange {{ border-top: 3px solid #ffa657; }}
    .card-green {{ border-top: 3px solid #39d353; }}

    .card-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
      flex-wrap: wrap;
    }}
    .card-badge {{
      font-size: 10px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .badge-cyan {{ background: rgba(34, 211, 238, 0.2); color: #22d3ee; border: 1px solid #22d3ee; }}
    .badge-purple {{ background: rgba(188, 140, 255, 0.2); color: #bc8cff; border: 1px solid #bc8cff; }}
    .badge-orange {{ background: rgba(255, 166, 87, 0.2); color: #ffa657; border: 1px solid #ffa657; }}
    .badge-green {{ background: rgba(57, 211, 83, 0.2); color: #39d353; border: 1px solid #39d353; }}

    .card-category {{
      font-size: 10px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-weight: 600;
      letter-spacing: 0.5px;
      word-break: break-word;
    }}
    .category-cyan {{ color: #22d3ee; }}
    .category-purple {{ color: #bc8cff; }}
    .category-orange {{ color: #ffa657; }}
    .category-green {{ color: #39d353; }}

    .card-title {{
      margin-top: 0;
      margin-bottom: 8px;
      font-size: 14.5px;
      font-weight: 600;
      word-break: break-word;
      overflow-wrap: break-word;
      line-height: 1.35;
    }}
    .card-summary {{
      font-size: 12.5px;
      color: #8b949e;
      margin-top: 0;
      margin-bottom: 12px;
      line-height: 1.5;
      word-break: break-word;
      overflow-wrap: break-word;
    }}
    .card-workflow {{
      background: #0d1117;
      border: 1px solid #21262d;
      border-radius: 6px;
      padding: 8px 10px;
      margin-bottom: 12px;
      overflow-x: auto;
      max-width: 100%;
      box-sizing: border-box;
      min-width: 0;
    }}
    .card-workflow code {{
      background: transparent;
      padding: 0;
      color: #e6edf3;
      font-size: 10.5px;
      white-space: normal;
      word-break: normal;
      overflow-wrap: break-word;
      line-height: 1.5;
      display: inline-block;
    }}
    .card-highlights ul {{
      margin-top: 0;
      margin-bottom: 12px;
      padding-left: 18px;
      font-size: 12.5px;
      line-height: 1.55;
    }}
    .card-highlights li {{
      margin-bottom: 6px;
      color: #c9d1d9;
      word-break: break-word;
      overflow-wrap: break-word;
    }}
    .card-footer {{
      border-top: 1px solid #21262d;
      padding-top: 10px;
      margin-top: auto;
      font-size: 12px;
      word-break: break-word;
      overflow-wrap: break-word;
    }}
    .card-footer p {{
      margin-bottom: 6px;
      word-break: break-word;
      overflow-wrap: break-word;
    }}
    .card-footer a {{
      word-break: break-all;
      overflow-wrap: break-word;
    }}

    /* Journey Timeline */
    .timeline-container {{
      padding: 20px;
      box-sizing: border-box;
      width: 100%;
    }}
    .timeline-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      box-sizing: border-box;
      width: 100%;
    }}
    .timeline-card {{
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      min-width: 0;
      box-sizing: border-box;
      word-wrap: break-word;
      overflow-wrap: break-word;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }}
    .timeline-card:hover {{
      border-color: #58a6ff;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5);
    }}
    .card-blue {{ border-top: 3px solid #58a6ff; }}
    .stage-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .stage-badge {{
      font-size: 10px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .stage-date {{
      font-size: 11px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-weight: 600;
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .badge-blue {{ background: rgba(88, 166, 255, 0.2); color: #58a6ff; border: 1px solid #58a6ff; }}
    .date-cyan {{ background: rgba(34, 211, 238, 0.15); color: #22d3ee; border: 1px solid rgba(34, 211, 238, 0.4); }}
    .date-blue {{ background: rgba(88, 166, 255, 0.15); color: #58a6ff; border: 1px solid rgba(88, 166, 255, 0.4); }}
    .date-purple {{ background: rgba(188, 140, 255, 0.15); color: #bc8cff; border: 1px solid rgba(188, 140, 255, 0.4); }}
    .date-orange {{ background: rgba(255, 166, 87, 0.15); color: #ffa657; border: 1px solid rgba(255, 166, 87, 0.4); }}
    .date-green {{ background: rgba(57, 211, 83, 0.15); color: #39d353; border: 1px solid rgba(57, 211, 83, 0.4); }}
    .pill-blue {{ background: rgba(88, 166, 255, 0.15); color: #58a6ff; border: 1px solid rgba(88, 166, 255, 0.4); }}
    .stage-title {{
      font-size: 13.5px;
      font-weight: 600;
      margin: 0 0 10px 0;
      color: #e6edf3;
      line-height: 1.35;
      word-break: break-word;
      overflow-wrap: break-word;
    }}
    .stage-highlights ul {{
      margin: 0;
      padding-left: 16px;
      font-size: 12px;
      line-height: 1.5;
      color: #c9d1d9;
    }}
    .stage-highlights li {{
      margin-bottom: 6px;
      word-break: break-word;
      overflow-wrap: break-word;
    }}

    /* Technical Interests Dashboard */
    .interests-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      padding: 20px;
      box-sizing: border-box;
      width: 100%;
    }}
    .interest-card {{
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-width: 0;
      box-sizing: border-box;
      word-wrap: break-word;
      overflow-wrap: break-word;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }}
    .interest-card:hover {{
      border-color: #58a6ff;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5);
    }}
    .interest-badge {{
      font-size: 10px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .interest-category {{
      font-size: 10px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-weight: 600;
      letter-spacing: 0.5px;
      word-break: break-word;
    }}
    .category-blue {{ color: #58a6ff; }}
    .interest-title {{
      font-size: 14px;
      font-weight: 600;
      margin: 0 0 8px 0;
      color: #e6edf3;
      line-height: 1.35;
      word-break: break-word;
      overflow-wrap: break-word;
    }}
    .interest-desc {{
      font-size: 12.5px;
      color: #8b949e;
      line-height: 1.5;
      margin: 0 0 12px 0;
      flex-grow: 1;
      word-break: break-word;
      overflow-wrap: break-word;
    }}
    .interest-connector {{
      background: #0d1117;
      border: 1px solid #21262d;
      border-radius: 6px;
      padding: 6px 10px;
      margin-top: auto;
      overflow-x: auto;
      max-width: 100%;
      box-sizing: border-box;
      min-width: 0;
    }}
    .interest-connector code {{
      background: transparent;
      padding: 0;
      color: #e6edf3;
      font-size: 10.5px;
      white-space: normal;
      word-break: normal;
      overflow-wrap: break-word;
      line-height: 1.5;
      display: inline-block;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }}

    /* Connect & Profile Terminal Dashboard */
    .connect-dashboard {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
      padding: 20px;
      box-sizing: border-box;
      width: 100%;
    }}
    .connect-panel {{
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 18px;
      min-width: 0;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
    }}
    .panel-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 14px;
      border-bottom: 1px solid #21262d;
      padding-bottom: 8px;
    }}
    .panel-tag {{
      font-size: 10px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .tag-cyan {{ background: rgba(34, 211, 238, 0.2); color: #22d3ee; border: 1px solid #22d3ee; }}
    .tag-purple {{ background: rgba(188, 140, 255, 0.2); color: #bc8cff; border: 1px solid #bc8cff; }}
    .panel-terminal-label {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 11px;
      color: #7d8590;
    }}
    .identity-name-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
      flex-wrap: wrap;
    }}
    .developer-name {{
      font-size: 18px;
      font-weight: 700;
      color: #e6edf3;
      margin: 0;
    }}
    .handle-badge {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 12px;
      color: #58a6ff;
      background: rgba(88, 166, 255, 0.15);
      border: 1px solid rgba(88, 166, 255, 0.4);
      padding: 2px 8px;
      border-radius: 4px;
      font-weight: 600;
    }}
    .identity-role, .identity-location, .identity-status {{
      font-size: 12.5px;
      margin: 0 0 6px 0;
      color: #c9d1d9;
    }}
    .identity-bio-box {{
      background: #0d1117;
      border: 1px solid #21262d;
      border-radius: 6px;
      padding: 10px 12px;
      margin: 12px 0;
    }}
    .bio-label {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 10.5px;
      color: #7d8590;
      margin-bottom: 4px;
    }}
    .bio-text {{
      font-size: 12px;
      color: #8b949e;
      line-height: 1.5;
      margin: 0;
    }}
    .identity-collab-box {{
      font-size: 12px;
      color: #c9d1d9;
      margin-top: auto;
    }}
    .collab-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 6px;
    }}
    .collab-pill {{
      background: #0d1117;
      border: 1px solid #21262d;
      border-radius: 4px;
      padding: 3px 8px;
      font-size: 11px;
      color: #8b949e;
    }}
    .channels-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      height: 100%;
      justify-content: space-between;
    }}
    .channel-link-card {{
      display: flex;
      align-items: center;
      gap: 12px;
      background: #0d1117;
      border: 1px solid #21262d;
      border-radius: 6px;
      padding: 10px 14px;
      text-decoration: none;
      transition: all 0.15s ease;
      min-width: 0;
      box-sizing: border-box;
    }}
    .channel-link-card:hover {{
      border-color: #58a6ff;
      background: #1a2230;
      text-decoration: none;
    }}
    .channel-icon-col {{
      font-size: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 28px;
      flex-shrink: 0;
    }}
    .channel-content-col {{
      display: flex;
      flex-direction: column;
      min-width: 0;
      flex-grow: 1;
    }}
    .channel-title-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 2px;
    }}
    .channel-name {{
      font-size: 13px;
      font-weight: 600;
      color: #e6edf3;
    }}
    .channel-badge {{
      font-size: 9.5px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      padding: 1px 5px;
      border-radius: 3px;
      font-weight: 700;
    }}
    .channel-url {{
      font-size: 11.5px;
      color: #7d8590;
      word-break: break-all;
    }}

    /* Kaggle Dashboard Section */
    .kaggle-dashboard-section {{
      border-top: 1px solid #21262d;
      background: #0d1117;
      padding: 16px 20px;
      box-sizing: border-box;
      width: 100%;
    }}
    .kaggle-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .kaggle-title {{
      font-size: 13px;
      color: #e6edf3;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .kaggle-badge-sync {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 10.5px;
      color: #39d353;
      font-weight: 600;
    }}
    .kaggle-badges-grid {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      align-items: center;
      justify-items: center;
      width: 100%;
      box-sizing: border-box;
    }}
    .kaggle-badge-item {{
      width: 100%;
      display: flex;
      justify-content: center;
      min-width: 0;
      box-sizing: border-box;
    }}
    .kaggle-badge-item a {{
      display: block;
      max-width: 100%;
    }}
    .kaggle-badge-item img {{
      max-width: 100%;
      height: auto;
      display: block;
      border-radius: 6px;
    }}

    /* Flagship Showcases */
    .flagship-showcase {{
      margin-top: 16px;
      margin-bottom: 24px;
    }}
    .flagship-inner {{
      padding: 20px;
      box-sizing: border-box;
      width: 100%;
    }}
    .flagship-badge-row {{
      display: flex;
      gap: 8px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }}
    .flagship-title {{
      margin-top: 0;
      margin-bottom: 8px;
      font-size: 18px;
      font-weight: 700;
      color: #e6edf3;
      word-break: break-word;
    }}
    .flagship-tagline {{
      font-size: 13.5px;
      color: #8b949e;
      margin-top: 0;
      margin-bottom: 14px;
      line-height: 1.5;
    }}
    .flagship-highlights ul {{
      margin: 0;
      padding-left: 20px;
      font-size: 13px;
      line-height: 1.6;
      color: #c9d1d9;
    }}
    .flagship-highlights li {{
      margin-bottom: 8px;
      word-break: break-word;
      overflow-wrap: break-word;
    }}
    .flagship-footer {{
      font-size: 12.5px;
      color: #c9d1d9;
    }}

    /* Verified Metric Highlights Table */
    .metrics-table-wrapper {{
      width: 100%;
      overflow-x: auto;
      box-sizing: border-box;
      margin: 12px 0 16px;
      min-width: 0;
      border: 1px solid #30363d;
      border-radius: 6px;
      background: #0d1117;
    }}
    .flight-metrics-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 0;
      background: #0d1117;
      border: none;
      display: table !important;
      min-width: 520px;
    }}
    .flight-metrics-table th {{
      background: #161b22;
      color: #58a6ff;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 11.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 10px 14px;
      border: 1px solid #21262d;
    }}
    .flight-metrics-table td {{
      padding: 10px 14px;
      border: 1px solid #21262d;
      font-size: 12.5px;
      color: #c9d1d9;
      line-height: 1.5;
    }}
    .flight-metrics-table tr:hover td {{
      background: rgba(88, 166, 255, 0.04);
    }}

    /* About Me Terminal Profile Showcase */
    .aboutme-sub-bar {{
      background: #0d1117;
      border-bottom: 1px solid #21262d;
      padding: 8px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 11px;
      color: #7d8590;
      box-sizing: border-box;
    }}
    .aboutme-sub-item {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .sub-dot {{
      color: #39d353;
      font-size: 10px;
    }}
    .aboutme-sub-item code {{
      color: #22d3ee;
      background: transparent;
      padding: 0;
      font-size: 11.5px;
    }}
    .aboutme-content {{
      padding: 20px;
      box-sizing: border-box;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 16px;
      min-width: 0;
      max-width: 100%;
    }}
    .aboutme-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
      width: 100%;
      box-sizing: border-box;
      min-width: 0;
    }}
    .aboutme-field-card {{
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 12px 14px;
      box-sizing: border-box;
      min-width: 0;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }}
    .aboutme-field-card:hover {{
      border-color: #58a6ff;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }}
    .field-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }}
    .field-label {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 10px;
      font-weight: 700;
      color: #7d8590;
      letter-spacing: 0.5px;
    }}
    .field-tag {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 9.5px;
      font-weight: 700;
      padding: 1px 6px;
      border-radius: 3px;
      letter-spacing: 0.3px;
    }}
    .field-value {{
      font-size: 13.5px;
      font-weight: 600;
      color: #e6edf3;
      word-break: break-word;
      overflow-wrap: anywhere;
    }}
    .field-link {{
      color: #58a6ff;
      text-decoration: none;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }}
    .field-link:hover {{
      text-decoration: underline;
    }}
    .aboutme-bio-card {{
      background: #0d1117;
      border: 1px solid #30363d;
      border-left: 3px solid #22d3ee;
      border-radius: 8px;
      padding: 14px 16px;
      box-sizing: border-box;
      width: 100%;
      min-width: 0;
      max-width: 100%;
      overflow-wrap: anywhere;
      word-break: normal;
    }}
    .bio-card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 8px;
      flex-wrap: wrap;
    }}
    .bio-header-left {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .bio-icon {{
      color: #e3b341;
      font-size: 13px;
    }}
    .bio-heading {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 11px;
      color: #22d3ee;
      font-weight: 600;
    }}
    .bio-status-badge {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 10px;
      color: #39d353;
      background: rgba(57, 211, 83, 0.15);
      border: 1px solid rgba(57, 211, 83, 0.3);
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 600;
    }}
    .bio-quote-body {{
      padding: 2px 0;
      min-width: 0;
      max-width: 100%;
      box-sizing: border-box;
      white-space: normal;
      overflow-wrap: anywhere;
      word-break: normal;
    }}
    .bio-paragraph {{
      margin: 0;
      font-size: 12.5px;
      line-height: 1.6;
      color: #c9d1d9;
      font-style: italic;
      white-space: normal;
      overflow-wrap: anywhere;
      word-break: normal;
      min-width: 0;
      max-width: 100%;
      box-sizing: border-box;
    }}
    .aboutme-footer-bar {{
      background: #0d1117;
      border-top: 1px solid #21262d;
      padding: 8px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 11px;
      color: #7d8590;
      box-sizing: border-box;
      min-width: 0;
      max-width: 100%;
      overflow-wrap: anywhere;
    }}
    .aboutme-footer-bar span {{
      min-width: 0;
      max-width: 100%;
      overflow-wrap: anywhere;
      white-space: normal;
    }}

    /* Technical Skills Showcase */
    .skills-panels-container {{
      padding: 20px;
      box-sizing: border-box;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .skill-panel {{
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 14px 16px;
      box-sizing: border-box;
      min-width: 0;
      width: 100%;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }}
    .skill-panel:hover {{
      border-color: #58a6ff;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5);
    }}
    .panel-cyan {{ border-left: 3px solid #22d3ee; }}
    .panel-blue {{ border-left: 3px solid #58a6ff; }}
    .panel-purple {{ border-left: 3px solid #bc8cff; }}
    .panel-orange {{ border-left: 3px solid #ffa657; }}
    .panel-green {{ border-left: 3px solid #39d353; }}

    .skill-panel-inner {{
      display: grid;
      grid-template-columns: 280px minmax(0, 1fr);
      gap: 16px;
      align-items: center;
      width: 100%;
      box-sizing: border-box;
    }}
    .skill-meta-col {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      border-right: 1px solid #21262d;
      padding-right: 14px;
      min-width: 0;
      box-sizing: border-box;
    }}
    .skill-meta-top {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .skill-meta-bottom {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .skill-badge {{
      font-size: 10px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .skill-category-label {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.5px;
    }}
    .skill-tree-node {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 11px;
      color: #6e7681;
    }}
    .skill-count-badge {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 10px;
      color: #8b949e;
      background: #0d1117;
      border: 1px solid #21262d;
      padding: 2px 7px;
      border-radius: 4px;
      font-weight: 600;
      white-space: nowrap;
    }}
    .skill-tags-col {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
      width: 100%;
      box-sizing: border-box;
      min-width: 0;
    }}
    .skill-pill {{
      display: inline-flex;
      align-items: center;
      border-radius: 6px;
      padding: 5px 10px;
      transition: all 0.15s ease;
      box-sizing: border-box;
      max-width: 100%;
    }}
    .skill-pill:hover {{
      transform: translateY(-1px);
    }}
    .skill-pill code {{
      background: transparent;
      padding: 0;
      font-size: 12px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      white-space: normal;
      word-break: break-word;
    }}
    .pill-tag-cyan {{
      background: rgba(34, 211, 238, 0.08);
      border: 1px solid rgba(34, 211, 238, 0.3);
      color: #22d3ee;
    }}
    .pill-tag-cyan:hover {{
      background: rgba(34, 211, 238, 0.16);
      border-color: #22d3ee;
    }}
    .pill-tag-blue {{
      background: rgba(88, 166, 255, 0.08);
      border: 1px solid rgba(88, 166, 255, 0.3);
      color: #58a6ff;
    }}
    .pill-tag-blue:hover {{
      background: rgba(88, 166, 255, 0.16);
      border-color: #58a6ff;
    }}
    .pill-tag-purple {{
      background: rgba(188, 140, 255, 0.08);
      border: 1px solid rgba(188, 140, 255, 0.3);
      color: #bc8cff;
    }}
    .pill-tag-purple:hover {{
      background: rgba(188, 140, 255, 0.16);
      border-color: #bc8cff;
    }}
    .pill-tag-orange {{
      background: rgba(255, 166, 87, 0.08);
      border: 1px solid rgba(255, 166, 87, 0.3);
      color: #ffa657;
    }}
    .pill-tag-orange:hover {{
      background: rgba(255, 166, 87, 0.16);
      border-color: #ffa657;
    }}
    .pill-tag-green {{
      background: rgba(57, 211, 83, 0.08);
      border: 1px solid rgba(57, 211, 83, 0.3);
      color: #39d353;
    }}
    .pill-tag-green:hover {{
      background: rgba(57, 211, 83, 0.16);
      border-color: #39d353;
    }}
    .skills-footer-bar {{
      background: #0d1117;
      border-top: 1px solid #21262d;
      padding: 8px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 11px;
      color: #7d8590;
      box-sizing: border-box;
    }}

    .markdown-body.wide-view .timeline-grid {{
      grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
      gap: 12px !important;
    }}
    .markdown-body.wide-view .interests-grid {{
      grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
      gap: 12px !important;
    }}

    @media (max-width: 768px) {{
      .project-grid {{
        grid-template-columns: 1fr !important;
        padding: 14px;
        gap: 14px;
      }}
      .timeline-grid {{
        grid-template-columns: 1fr !important;
        gap: 12px !important;
      }}
      .interests-grid {{
        grid-template-columns: 1fr !important;
        padding: 12px !important;
        gap: 12px !important;
      }}
      .connect-dashboard {{
        grid-template-columns: 1fr !important;
        padding: 12px !important;
        gap: 12px !important;
      }}
      .aboutme-grid {{
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }}
      .aboutme-content, .skills-panels-container {{
        padding: 12px !important;
      }}
      .skill-panel {{
        padding: 12px !important;
      }}
      .skill-panel-inner {{
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }}
      .skill-meta-col {{
        border-right: none !important;
        border-bottom: 1px solid #21262d !important;
        padding-right: 0 !important;
        padding-bottom: 8px !important;
      }}
      .skill-pill code {{
        font-size: 11px !important;
      }}
      .kaggle-badges-grid {{
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 8px !important;
      }}
      .workflow-sequence-banner {{
        flex-direction: column;
        gap: 6px;
      }}
      .connector-arrow {{
        transform: rotate(90deg);
      }}
    }}
    .markdown-body.mobile-view {{
      max-width: 412px !important;
    }}
    .markdown-body.mobile375-view {{
      max-width: 375px !important;
      border: 1px solid #30363d;
      padding: 14px 10px;
      border-radius: 12px;
      background: #0d1117;
      box-shadow: 0 12px 32px rgba(0,0,0,0.6);
      transition: max-width 0.3s ease;
    }}
    .markdown-body.mobile-view .project-grid,
    .markdown-body.mobile375-view .project-grid {{
      grid-template-columns: 1fr !important;
      padding: 12px !important;
      gap: 12px !important;
    }}
    .markdown-body.mobile-view .timeline-grid,
    .markdown-body.mobile375-view .timeline-grid {{
      grid-template-columns: 1fr !important;
      gap: 12px !important;
    }}
    .markdown-body.mobile-view .interests-grid,
    .markdown-body.mobile375-view .interests-grid {{
      grid-template-columns: 1fr !important;
      padding: 12px !important;
      gap: 12px !important;
    }}
    .markdown-body.mobile-view .aboutme-grid,
    .markdown-body.mobile375-view .aboutme-grid {{
      grid-template-columns: 1fr !important;
      gap: 10px !important;
    }}
    .markdown-body.mobile-view .aboutme-content,
    .markdown-body.mobile375-view .aboutme-content,
    .markdown-body.mobile-view .skills-panels-container,
    .markdown-body.mobile375-view .skills-panels-container {{
      padding: 12px !important;
    }}
    .markdown-body.mobile-view .skill-panel,
    .markdown-body.mobile375-view .skill-panel {{
      padding: 12px !important;
    }}
    .markdown-body.mobile-view .skill-panel-inner,
    .markdown-body.mobile375-view .skill-panel-inner {{
      grid-template-columns: 1fr !important;
      gap: 10px !important;
    }}
    .markdown-body.mobile-view .skill-meta-col,
    .markdown-body.mobile375-view .skill-meta-col {{
      border-right: none !important;
      border-bottom: 1px solid #21262d !important;
      padding-right: 0 !important;
      padding-bottom: 8px !important;
    }}
    .markdown-body.mobile-view .skill-pill code,
    .markdown-body.mobile375-view .skill-pill code {{
      font-size: 11px !important;
    }}
    .markdown-body.mobile-view .connect-dashboard,
    .markdown-body.mobile375-view .connect-dashboard {{
      grid-template-columns: 1fr !important;
      padding: 12px !important;
      gap: 12px !important;
    }}
    .markdown-body.mobile-view .kaggle-badges-grid,
    .markdown-body.mobile375-view .kaggle-badges-grid {{
      grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
      gap: 8px !important;
    }}
    .markdown-body.mobile-view .kaggle-dashboard-section,
    .markdown-body.mobile375-view .kaggle-dashboard-section {{
      padding: 12px !important;
    }}
    .markdown-body.mobile-view .workflow-sequence-banner,
    .markdown-body.mobile375-view .workflow-sequence-banner {{
      flex-direction: column !important;
      gap: 6px !important;
    }}
    .markdown-body.mobile-view .connector-arrow,
    .markdown-body.mobile375-view .connector-arrow {{
      transform: rotate(90deg) !important;
    }}
    .markdown-body.mobile-view .flagship-inner,
    .markdown-body.mobile375-view .flagship-inner {{
      padding: 14px 12px !important;
    }}
  </style>
</head>
<body>
  <div class="preview-banner">
    <div><span>Profile Preview: </span><strong>Ritik Raj (Ritik-62)</strong></div>
    <div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;">
      <span>Viewport:</span>
      <button onclick="setViewport('wide')" id="btn-wide" class="vp-btn">🖥️ Desktop 1440px</button>
      <button onclick="setViewport('desktop')" id="btn-desktop" class="vp-btn active">💻 Desktop 900px</button>
      <button onclick="setViewport('mobile412')" id="btn-mobile412" class="vp-btn">📱 Mobile 412px</button>
      <button onclick="setViewport('mobile375')" id="btn-mobile375" class="vp-btn">📱 Mobile 375px</button>
    </div>
  </div>
  <div class="markdown-body">
    {html_body}
  </div>
  <script>
    function setViewport(mode) {{
      const mb = document.querySelector('.markdown-body');
      const btnW = document.getElementById('btn-wide');
      const btnD = document.getElementById('btn-desktop');
      const btnM412 = document.getElementById('btn-mobile412');
      const btnM375 = document.getElementById('btn-mobile375');
      
      mb.classList.remove('mobile-view', 'mobile375-view', 'wide-view');
      btnW.classList.remove('active');
      btnD.classList.remove('active');
      btnM412.classList.remove('active');
      btnM375.classList.remove('active');

      if (mode === 'mobile375') {{
        mb.classList.add('mobile375-view');
        btnM375.classList.add('active');
      }} else if (mode === 'mobile412') {{
        mb.classList.add('mobile-view');
        btnM412.classList.add('active');
      }} else if (mode === 'wide') {{
        mb.classList.add('wide-view');
        btnW.classList.add('active');
      }} else {{
        btnD.classList.add('active');
      }}
    }}
  </script>
</body>
</html>
"""
    with open(PREVIEW_PATH, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"Generated preview: {PREVIEW_PATH}")

if __name__ == "__main__":
    build_preview()
