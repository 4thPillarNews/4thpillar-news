import feedparser

feeds = [
    "https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi",
    "https://rss.bhaskar.com/rss-v1--category-0.xml"
]

all_news = []
for url in feeds:
    f = feedparser.parse(url)
    for e in f.entries[:10]:
        all_news.append({"title": e.title, "link": e.link})

# HTML Banao
html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>4th Pillar News</title>
<style>body{{margin:0;font-family:Arial;background:#f2f2f2}} header{{background:#000;color:#fff;padding:10px;display:flex;align-items:center;}} .logo{{width:40px;height:40px;border-radius:50%;background:#fff;margin-right:10px;object-fit:cover}} .card{{background:#fff;margin:10px;padding:15px;border-radius:8px}} .card a{{color:#000;text-decoration:none;font-weight:bold}}</style>
</head><body>
<header>
<img class="logo" src="https://raw.githubusercontent.com/4thPillarNews/4thpillar-news/main/the4thpillarnews.jpg">
<div><b>4TH PILLAR NEWS</b><br><small>रविवार, 6 सितंबर 2026 | Ghaziabad, UP</small></div>
<div style="margin-left:auto;font-size:12px">Reporter: Gaurav Sharma</div>
</header>
"""

for n in all_news[:30]:
    html += f'<div class="card"><a href="{n["link"]}" target="_blank">{n["title"]}</a></div>\n'

html += "</body></html>"

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)

print(f"{len(all_news)} news updated")
