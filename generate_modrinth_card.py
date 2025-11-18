import requests
import textwrap

PROJECT_ID = "the-next-mobs"  # ← change to your project id

data = requests.get(f"https://api.modrinth.com/v2/project/{PROJECT_ID}").json()

icon = data.get("icon_url", "")
name = data.get("title", "")
summary = data.get("description", "").replace("\n", " ")
summary_short = textwrap.shorten(summary, width=80, placeholder="…")
slug = data.get("slug", PROJECT_ID)

svg = f"""
<svg width="600" height="180" viewBox="0 0 600 180" xmlns="http://www.w3.org/2000/svg">
  <style>
    .card {{
      fill: #202020;
      stroke: #2a2a2a;
      stroke-width: 2;
      rx: 18;
    }}
    .title {{
      fill: #ffffff;
      font: 700 22px Inter, sans-serif;
    }}
    .summary {{
      fill: #bdbdbd;
      font: 15px Inter, sans-serif;
    }}
    .button-bg {{
      fill: #00ff88;
      rx: 12;
    }}
    .button-text {{
      fill: #000000;
      font: 600 16px Inter, sans-serif;
    }}
  </style>

  <rect class="card" x="0" y="0" width="600" height="180" />

  <image href="{icon}" x="25" y="40" width="64" height="64" rx="12" />

  <text class="title" x="110" y="65">{name}</text>
  <text class="summary" x="110" y="100">{summary_short}</text>

  <a href="https://modrinth.com/project/{slug}">
    <rect class="button-bg" x="420" y="60" width="150" height="50" />
    <text class="button-text" x="445" y="92">Go to Modrinth!</text>
  </a>
</svg>
"""

with open("modrinth-card.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Generated modrinth-card.svg")
