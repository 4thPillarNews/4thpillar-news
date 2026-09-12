import feedparser
import json
from datetime import datetime

all_news = []
today = datetime.now().strftime("%d %b %Y")

# Try RSS
try:
    feed = feedparser.parse("https://feeds.bbci.co.uk/hindi/rss.xml")
    for i, entry in enumerate(feed.entries[:6]):
        all_news.append({
            "id": i,
            "title": entry.title,
            "para1": entry.summary if hasattr(entry, 'summary') else entry.title,
            "para2": "",
            "para3": "",
            "para4": "",
            "image": f"https://picsum.photos/seed/{i}news/800/450",
            "link": f"article.html?id={i}",
            "category": "Latest",
            "date": today,
            "reporter": "Gaurav Sharma",
            "source": "4th Pillar News"
        })
except:
    pass

# Agar abhi bhi khali hai to backup news bana de - taaki site kabhi khali na dikhe
if len(all_news) == 0:
    for i in range(6):
        all_news.append({
            "id": i,
            "title": f"Breaking News {i+1} - 4th Pillar News Update",
            "para1": "Ye khabar automatically update hui hai. RSS feed temporary fail hone par backup news dikhai ja rahi hai.",
            "para2": "",
            "para3": "",
            "para4": "",
            "image": f"https://picsum.photos/seed/{i}news/800/450",
            "link": f"article.html?id={i}",
            "category": "Latest",
            "date": today,
            "reporter": "Gaurav Sharma",
            "source": "4th Pillar News"
        })

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=2)

print(f"Saved {len(all_news)} news with date {today}")
