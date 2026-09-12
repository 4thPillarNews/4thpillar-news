import feedparser
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def get_real_news(url):
    try:
        r = requests.get(url, timeout=20, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.text, 'lxml')

        # Real photo
        img = ""
        og = soup.find("meta", property="og:image")
        if og:
            img = og.get("content","")

        # Puri real news - sirf article ke <p>
        article = soup.find("article") or soup
        raw_paras = [p.get_text().strip() for p in article.find_all("p") if len(p.get_text().strip()) > 80]

        # Saaf karo - BBC ke bekar lines hatao
        filtered = []
        for t in raw_paras:
            if "BBC" in t and len(t) < 150: continue
            if "क्लिक करें" in t: continue
            filtered.append(t)

        full_text = " ".join(filtered) # Ye puri real khabar hai

        # Ab isko 10-12 line ke 2 hisse me tod do - No AI, sirf split
        # 1 line ~ 12 words, 10 line ~ 120 words
        words = full_text.split()
        mid = len(words) // 2
        para1 = " ".join(words[:mid])
        para2 = " ".join(words[mid:])

        return img, para1, para2
    except:
        return "", "", ""

all_news = []
today = datetime.now().strftime("%d %b %Y")
feed = feedparser.parse("https://feeds.bbci.co.uk/hindi/rss.xml")

for i, entry in enumerate(feed.entries[:8]):
    img, p1, p2 = get_real_news(entry.link)

    if not img:
        if hasattr(entry, 'media_thumbnail'):
            img = entry.media_thumbnail[0]['url']
        else:
            img = f"https://picsum.photos/seed/{i}/800/450"

    # Agar scraping fail ho to summary lo, par usko bhi 2 part me tod do
    if len(p1) < 100:
        full = entry.summary if hasattr(entry, 'summary') else entry.title
        w = full.split()
        m = len(w)//2
        p1 = " ".join(w[:m])
        p2 = " ".join(w[m:])

    all_news.append({
        "id": i,
        "title": entry.title, # Title ko thoda change kar lena AdSense ke liye - jaise apne words me
        "para1": p1,
        "para2": p2,
        "para3": "", # Sirf 2 para rakhe hain jaise bola
        "para4": "",
        "image": img,
        "link": f"article.html?id={i}",
        "category": "Latest",
        "date": today,
        "reporter": "Gaurav Sharma",
        "source": "4th Pillar News"
    })

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=2)
