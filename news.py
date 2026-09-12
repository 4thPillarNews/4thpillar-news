import feedparser
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def get_real_data(url):
    try:
        r = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.text, 'lxml')
        # Asli photo
        real_img = ""
        og = soup.find("meta", property="og:image")
        if og and og.get("content"):
            real_img = og["content"]

        # Puri khabar ke paras
        paras = []
        for p in soup.find_all('p'):
            txt = p.get_text().strip()
            if len(txt) > 60 and "BBC" not in txt and "Navbharat" not in txt:
                paras.append(txt)
            if len(paras) == 4:
                break
        while len(paras) < 4:
            paras.append("")
        return real_img, paras
    except:
        return "", ["", "", "", ""]

all_news = []
today = datetime.now().strftime("%d %b %Y")

feed = feedparser.parse("https://feeds.bbci.co.uk/hindi/rss.xml")

for i, entry in enumerate(feed.entries[:10]):
    real_img, full_paras = get_real_data(entry.link)

    if not real_img:
        if hasattr(entry, 'media_thumbnail'):
            real_img = entry.media_thumbnail[0]['url']
        else:
            real_img = f"https://picsum.photos/seed/{i}news/800/450"

    if not full_paras[0]:
        full_paras[0] = entry.summary if hasattr(entry, 'summary') else entry.title

    all_news.append({
        "id": i,
        "title": entry.title,
        "para1": full_paras[0],
        "para2": full_paras[1],
        "para3": full_paras[2],
        "para4": full_paras[3],
        "image": real_img,
        "link": f"article.html?id={i}",
        "category": "Latest",
        "date": today,
        "reporter": "Gaurav Sharma",
        "source": "4th Pillar News"
    })

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=2)

print(f"Done {len(all_news)} news with real photo")
