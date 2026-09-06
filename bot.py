import feedparser
import json
from datetime import datetime

# RSS Feed
feed_url = "https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi"
feed = feedparser.parse(feed_url)

news_list = []
for entry in feed.entries[:20]:
    news_list.append({
        "title": entry.title,
        "link": entry.link,
        "date": datetime.now().strftime("%d %b %Y, %I:%M %p")
    })

# news.json save karo
with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news_list, f, ensure_ascii=False, indent=2)

# index.html banao - LOGO FIX YAHI HAI
html_template = f"""
<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Fourth Pillar News</title>
<style>
body{{font-family: Arial; margin:0; background:#f5f5f5;}}
header{{background:#111; color:white; padding:12px 20px; display:flex; align-items:center;}}
header img{{height:48px; width:48px; border-radius:50%; margin-right:12px; border:2px solid white;}}
.card{{background:white; margin:15px; padding:15px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.1);}}
.card a{{text-decoration:none; color:#111; font-weight:bold; font-size:18px;}}
</style>
</head>
<body>
<header>
<img src="the4thpillarnews.jpg" alt="The Fourth Pillar Logo">
<h2 style="margin:0;">The Fourth Pillar News</h2>
</header>

<div id="news">
"""

for news in news_list:
    html_template += f"""
    <div class="card">
        <a href="{news['link']}" target="_blank">{news['title']}</a>
        <p style="color:gray; font-size:13px; margin-top:8px;">{news['date']}</p>
    </div>
    """

html_template += """
</div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Done - Logo ke saath update ho gaya")
