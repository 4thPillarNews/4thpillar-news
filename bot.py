import feedparser, json, requests
from bs4 import BeautifulSoup
from datetime import datetime

RSS_URLS = [
 "https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi",
 "https://www.bhaskar.com/rss-v1--category-1.xml"
]

def get_full_text(link):
    try:
        r = requests.get(link, timeout=10, headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(r.text, 'html.parser')
        paras = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paras])[:2000]
        if len(text) < 200: return ""
        # 5-6 paragraph me todo
        sentences = text.split('।')
        out = ""
        para = ""
        count = 0
        for s in sentences:
            if len(s.strip())<10: continue
            para += s.strip() + "। "
            count+=1
            if count==2:
                out += para.strip() + "\n\n"
                para=""; count=0
        if para: out+=para
        return out[:1500]
    except:
        return ""

feeds=[]
for url in RSS_URLS:
    d=feedparser.parse(url)
    for e in d.entries[:5]:
        full = get_full_text(e.link)
        if not full: full = e.get('summary','')*3
        feeds.append({
            "title": e.title,
            "desc": full[:280],
            "content": full,
            "image": f"https://picsum.photos/seed/{abs(hash(e.title))%1000}/600/400",
            "date": datetime.now().strftime("%d %b, %Y • %I:%M %p"),
            "author": "Gaurav Sharma",
            "link": e.link
        })

with open('news.json','w',encoding='utf-8') as f:
    json.dump(feeds[:12], f, ensure_ascii=False, indent=2)
print("Done")
