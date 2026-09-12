import feedparser
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_full_news(url):
    try:
        r = requests.get(url, timeout=10, headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(r.text, 'html.parser')
        paras = [p.get_text().strip() for p in soup.find_all('p') if len(p.get_text().strip()) > 80]
        # 4 bade paras bana de
        return paras[:4] if len(paras) >= 4 else (paras + [""]*4)[:4]
    except:
        return ["News content load nahi ho paya.", "", "", ""]

all_news = []
today = datetime.now().strftime("%d %b %Y")

feeds = ["https://feeds.bbci.co.uk/hindi/rss.xml", "https://navbharattimes.indiatimes.com/rssfeeds/898109650.cms"]

news_id = 0
for rss in feeds:
    try:
        feed = feedparser.parse(rss)
        for entry in feed.entries[:4]:
            full = get_full_news(entry.link)
            # Agar full news nahi mili to summary use kar le
            if not full[0]:
                full = [entry.summary if hasattr(entry,'summary') else entry.title, "", "", ""]

            all_news.append({
                "id": news_id,
                "title": entry.title,
                "para1": full[0],
                "para2": full[1] if len(full)>1 else "",
                "para3": full[2] if len(full)>2 else "",
                "para4": full[3] if len(full)>3 else "",
                "image": f"https://picsum.photos/seed/{news_id}news/800/450",
                "link": f"article.html?id={news_id}",
                "category": "Latest",
                "date": today,
                "reporter": "Gaurav Sharma",
                "source": "4th Pillar News"
            })
            news_id += 1
    except:
        continue

# Backup agar phir bhi khali hai
if len(all_news) == 0:
    for i in range(4):
        all_news.append({
            "id": i,
            "title": f"Breaking Update {i+1}",
            "para1": "Ye full news ka backup hai. Agli baar pura content load ho jayega.",
            "para2": "4th Pillar News aapko roz taza khabrein deta hai.",
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

print(f"Saved {len(all_news)} FULL news with date {today}")
