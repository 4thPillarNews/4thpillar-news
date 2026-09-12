import feedparser, json, requests, re, os
from datetime import datetime
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

BAD_WORDS = ["BBC","बीबीसी","BCC","Aaj Tak","आज तक","ABP","NDTV","Zee","Republic","Amar Ujala","अमर उजाला","Jagran","दैनिक जागरण","Navbharat","Hindustan","भास्कर","Times","Hindu","PTI","ANI","CNN"]

os.makedirs("images", exist_ok=True)

def full_news(url, idx):
    try:
        r = requests.get(url, timeout=20, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.text, 'lxml')

        # Photo download + CROP LOGO
        img_path = f"images/news_{idx}.jpg"
        final_img_url = f"images/news_{idx}.jpg"  # local path
        try:
            img_tag = None
            for im in soup.find_all("img"):
                src = im.get("src","")
                if src.startswith("http") and len(src)>40 and "logo" not in src.lower():
                    img_tag = src
                    break
            if not img_tag:
                og = soup.find("meta", property="og:image")
                if og: img_tag = og.get("content","")

            if img_tag:
                img_data = requests.get(img_tag, timeout=20).content
                im = Image.open(BytesIO(img_data))
                w, h = im.size
                # Neeche ka 20% aur upar ka 8% kaat do jahan The Lens / BBC ka logo hota hai
                cropped = im.crop((0, int(h*0.08), w, int(h*0.80)))
                cropped.save(img_path, quality=90)
            else:
                final_img_url = f"https://picsum.photos/seed/final{idx}/800/450"
        except:
            final_img_url = f"https://picsum.photos/seed/final{idx}/800/450"

        paras = []
        for p in soup.find_all("p"):
            t = p.get_text().strip()
            if len(t) < 80: continue
            if "AI" in t and "अनुवाद" in t: continue
            for bad in BAD_WORDS:
                t = re.sub(re.escape(bad), "", t, flags=re.IGNORECASE)
            t = re.sub(r'\s{2,}', ' ', t).strip()
            if len(t) > 50:
                paras.append(t)

        text = " ".join(paras)
        words = text.split()
        mid = len(words)//2
        p1 = " ".join(words[:mid])
        p2 = " ".join(words[mid:])

        return final_img_url, p1, p2
    except:
        return f"https://picsum.photos/seed/final{idx}/800/450", "", ""

today = datetime.now().strftime("%d %b %Y")
feed = feedparser.parse("https://feeds.bbci.co.uk/hindi/rss.xml")
all_news = []

for i, entry in enumerate(feed.entries[:8]):
    img, p1, p2 = full_news(entry.link, i)
    if len(p1) < 100: continue
    all_news.append({
        "id": i, "title": entry.title,
        "para1": p1, "para2": p2, "para3": "", "para4": "",
        "image": img, "link": f"article.html?id={i}",
        "category": "Latest", "date": today,
        "reporter": "Gaurav Sharma", "source": "4th Pillar News"
    })

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=2)
