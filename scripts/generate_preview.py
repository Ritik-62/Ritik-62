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
      overflow: auto;
      font-size: 85%;
      line-height: 1.45;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      color: #e6edf3;
      margin-top: 0;
      margin-bottom: 0;
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
      display: inline-table;
      border: 1px solid #30363d;
      border-radius: 6px;
      overflow: hidden;
      background: #0d1117;
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
  </style>
</head>
<body>
  <div class="preview-banner">
    <div><span>Profile Preview: </span><strong>Ritik Raj (Ritik-62)</strong></div>
    <div>Theme: GitHub Dark · Matches Avi Vashishta Aesthetic</div>
  </div>
  <div class="markdown-body">
    {html_body}
  </div>
</body>
</html>
"""
    with open(PREVIEW_PATH, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"Generated preview: {PREVIEW_PATH}")

if __name__ == "__main__":
    build_preview()
