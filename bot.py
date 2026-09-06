import feedparser
import base64
import os

logo_path = "4thpillar24x7.jpg"  # TERA SAHI NAAM
logo_src = logo_path

if os.path.exists(logo_path):
    with open(logo_path, "rb") as img:
        b64 = base64.b64encode(img.read()).decode('utf-8')
        logo_src = f"data:image/jpeg;base64,{b64}"

feed = feedparser.parse("https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi")
all_news = feed.entries[:30]

html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>4th Pillar News</title>
<style>body{{margin:0;font-family:Arial;background:#eee}} header{{background:#000;color:#fff;padding:12px;display:flex;align-items:center}} .logo{{width:45px;height:45px;border-radius:50%;margin-right:10px;border:2px solid white}} .card{{background:#fff;margin:10px;padding:14px;border-radius:8px}} .card a{{text-decoration:none;color:#111;font-weight:bold}}</style>
</head><body>
<header>
<img class="logo" src="{logo_src}">
<div><b>4TH PILLAR NEWS</b><br><small>Live News</small></div>
</header>
"""

for n in all_news:
    html += f'<div class="card"><a href="{n.link}" target="_blank">{n.title}</a></div>\n'

html += "</body></html>"

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)

print("Fixed with 4thpillar24x7.jpg")
