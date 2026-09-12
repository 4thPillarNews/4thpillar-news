import feedparser, json, requests, re, os
from datetime import datetime
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

# 1. Saare agency ke naam jo hatane hain
BAD_WORDS = [
    "BBC", "बीबीसी", "BCC", "द लेंस", "The Lens", "TheLens", "लेंस",
    "Aaj Tak", "आज तक", "ABP", "NDTV", "Zee", "Republic", 
    "Amar Ujala", "अमर उजाला", "Jagran", "दैनिक जागरण", "Hindustan", "भास्कर", "Times", "PTI", "ANI"
]

# 2. Ye poori line hi delete ho jayegi agar ye shabd aaye
BAD_SENTENCES = [
    "बाहरी साइटों", "सामग्री के लिए जिम्मेदार", "लिंक देने की", "हमारी नीति",
    "एपिसोड", "वोटर ऑफ जनलिज्म", "पीपल्स राइट टू इनफॉर्मेशन", "© 2026"
]

os.makedirs("images", exist_ok=True)

def full_news(url, idx):
    try:
        r = requests.get(url, timeout=20, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.text, 'lxml')

        # IMAGE FIX - Kutte wali image hatao, sirf badi news wali image lo
        img_path = f"images/news_{idx}.jpg"
        final_img_url = img_path
        try:
            best_img = None
            max_size = 0
            for im in soup.find_all("img"):
                src = im.get("src","")
                if src.startswith("http") and len(src)>40 and "logo" not in src.lower():
                    # Sabse badi image lo, choti icon nahi
                    w = int(im.get("width",0) or 0)
                    if w > max_size:
                        max_size = w
                        best_img = src
            if not best_img:
                og = soup.find("meta", property="og:image")
                if og: best_img = og.get("content","")

            if best_img:
                img_data = requests.get(best_img, timeout=20).content
                im = Image.open(BytesIO(img_data))
                w, h = im.size
                if w < 300 or h < 200: # Choti image hai to use mat karo
                    raise Exception("small image")
                # Neeche ka 20% kaat do jahan logo hota hai
                cropped = im.crop((0, 0, w, int(h*0.82)))
                cropped.save(img_path, quality=90)
            else:
                final_img_url = f"https://picsum.photos/seed/news{idx}/800/450"
        except:
            final_img_url = f"https://picsum.photos/seed/news{idx}/800/450"

        # TEXT FIX - The Lens ka naam aur footer delete
        paras = []
        for p in soup.find_all("p"):
            t = p.get_text().strip()
            if len(t) < 70: continue
            
            # Agar ye line The Lens ke footer wali hai to skip
            if any(bad in t for bad in BAD_SENTENCES):
                continue

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
        return f"https://picsum.photos/seed/news{idx}/800/450", "", ""

today = datetime.now().strftime("%d %b %Y")
feed = feedparser.parse("https://feeds.bbci.co.uk/hindi/rss.xml")
all_news = []

for i, entry in enumerate(feed.entries[:8]):
    img, p1, p2 = full_news(entry.link, i)
    if len(p1) < 100: continue
    # Title se bhi The Lens hatao
    title = entry.title
    for bad in BAD_WORDS:
        title = re.sub(re.escape(bad), "", title, flags=re.IGNORECASE)
    title = re.sub(r'\s{2,}', ' ', title).strip()
    title = title.replace("- -", "-").strip()

    all_news.append({
        "id": i, "title": title,
        "para1": p1, "para2": p2, "para3": "", "para4": "",
        "image": img, "link": f"article.html?id={i}",
        "category": "Latest", "date": today,
        "reporter": "Gaurav Sharma", "source": "4th Pillar News"
    })

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=2)
