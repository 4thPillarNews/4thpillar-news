import feedparser, json, random, re
from bs4 import BeautifulSoup

RSS = [
 "https://www.bhaskar.com/rss-v1--category-1742.xml",
 "https://navbharattimes.indiatimes.com/rssfeeds/9097204.cms"
]

def clean(s):
    return BeautifulSoup(s,'html.parser').get_text().strip()

news=[]
for i, url in enumerate(RSS):
    feed = feedparser.parse(url)
    for j, e in enumerate(feed.entries[:10]):
        t = e.get('title','').strip()
        if not t: continue
        d = clean(e.get('summary','') or e.get('description','') or t)
        sents = d.split('. ')
        p1 = '. '.join(sents[0:2]) + '.'
        p2 = '. '.join(sents[2:4]) + '.' if len(sents)>3 else 'Prashasan ne is par janch shuru kar di hai.'
        p3 = '. '.join(sents[4:6]) + '.' if len(sents)>5 else 'Janpratinidhiyon ne is par pratikriya di hai.'
        p4 = '4th Pillar News is par lagatar nazar banaye hue hai.'

        news.append({
            "id": len(news),
            "title": t,
            "para1": p1, "para2": p2, "para3": p3, "para4": p4, "para5":"", "para6":"",
            "image": f"https://picsum.photos/seed/{len(news)}{random.randint(1,9999)}/800/450",
            "link": e.get('link',''),
            "category": "Latest", "date": "13 Sep 2026",
            "reporter": "4th Pillar News", "source": "4th Pillar News"
        })
        if len(news)>=20: break

with open('news.json','w',encoding='utf-8') as f:
    json.dump(news,f,ensure_ascii=False,indent=2)
