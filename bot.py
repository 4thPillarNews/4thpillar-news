import feedparser
import json
import datetime
import re

RSS_URL = "https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi"
feed = feedparser.parse(RSS_URL)

def is_hindi(text):
    # Agar text me Hindi ke akshar hain to hi rakho
    return bool(re.search(r'[\u0900-\u097F]', text))

news_list = []
for entry in feed.entries:
    if not is_hindi(entry.title):
        continue  # English news ko skip
    if len(news_list) >= 20:
        break
    news_list.append({
        "title": entry.title,
        "link": entry.link,
        "description": entry.title,
        "pubDate": datetime.datetime.now().strftime("%d %b, %Y - %I:%M %p"),
        "source": entry.source.title if hasattr(entry, 'source') else "Google News",
        "image": f"https://picsum.photos/seed/{abs(hash(entry.title))}/800/450"
    })

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news_list, f, ensure_ascii=False, indent=2)

print(f"Saved {len(news_list)} Hindi news only")
