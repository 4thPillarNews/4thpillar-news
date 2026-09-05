import json
import feedparser
from datetime import datetime
import os

# Hindi RSS
RSS_URL = "https://feeds.bbci.co.uk/hindi/rss.xml"

def get_news():
    try:
        feed = feedparser.parse(RSS_URL)
        items = []
        for i, entry in enumerate(feed.entries[:6]):
            items.append({
                "id": i+1,
                "title": entry.title,
                "desc": entry.summary[:200] if hasattr(entry, 'summary') else entry.title,
                "description": entry.summary[:200] if hasattr(entry, 'summary') else entry.title,
                "content": entry.summary if hasattr(entry, 'summary') else entry.title,
                "summary": entry.title,
                "date": datetime.now().strftime("%d %b %Y"),
                "image": "https://images.pexels.com/photos/518543/pexels-photo-518543.jpeg",
                "link": entry.link
            })
        if items:
            return items
    except:
        pass
    
    # Fallback agar RSS fail ho
    return [
      {
        "id": 1,
        "title": "पीएम मोदी ने एआई मिशन का किया ऐलान",
        "desc": "प्रधानमंत्री ने नेशनल एआई मिशन का ऐलान किया। 5000 करोड़ का बजट तय हुआ है।",
        "description": "प्रधानमंत्री ने नेशनल एआई मिशन का ऐलान किया। 5000 करोड़ का बजट तय हुआ है।",
        "content": "प्रधानमंत्री ने नेशनल एआई मिशन का ऐलान किया।",
        "summary": "AI Mission launched",
        "date": datetime.now().strftime("%d %b %Y"),
        "image": "https://images.pexels.com/photos/8386440/pexels-photo-8386440.jpeg"
      }
    ]

# Purani news load karo
old_news = []
if os.path.exists('news.json'):
    try:
        with open('news.json','r', encoding='utf-8') as f:
            old_news = json.load(f)
    except:
        old_news = []

new_news = get_news()

# Nayi + Purani (max 20 rakhenge)
combined = new_news + old_news
# Duplicate title hatana
seen = set()
final_news = []
for n in combined:
    if n['title'] not in seen:
        seen.add(n['title'])
        final_news.append(n)
    if len(final_news) >= 20:
        break

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(final_news, f, ensure_ascii=False, indent=2)

print(f"Total {len(final_news)} news saved")
