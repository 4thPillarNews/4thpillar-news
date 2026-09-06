import feedparser
import json
import datetime
import os

RSS = "https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi"

print("Fetching news...")
feed = feedparser.parse(RSS)

news = []
for i, e in enumerate(feed.entries[:20]):
    news.append({
        "id": i,
        "title": e.title,
        "link": e.link,
        "description": getattr(e, 'summary', e.title)[:150],
        "date": datetime.datetime.now().strftime("%d %b %Y, %I:%M %p"),
        "image": f"https://picsum.photos/seed/{i+10}/800/450"
    })

# news.json me save karna - ye line tere code me missing thi
with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(news, f, ensure_ascii=False, indent=2)

print(f"Success! {len(news)} news saved to news.json")
