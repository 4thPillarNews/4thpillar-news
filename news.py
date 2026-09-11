import feedparser, json
from bs4 import BeautifulSoup

RSS = [
 "https://www.bhaskar.com/rss-v1--category-1742.xml",
 "https://navbharattimes.indiatimes.com/rssfeeds/9097204.cms"
]

def clean(s):
    return BeautifulSoup(s,'html.parser').get_text().strip()

def get_image(title, nid):
    t=title.lower()
    if 'nepal' in t: q="nepal,flood"
    elif any(x in t for x in ['visa','america','अमेरिका']): q="usa,visa"
    elif any(x in t for x in ['putin','रूस','विमान']): q="russia,jet"
    elif any(x in t for x in ['हत्या','गोली','murder','police','gurugram']): q="police,crime"
    elif 'brazil' in t or 'ब्राजील' in t: q="brazil,court"
    elif 'तापमान' in t or 'गर्मी' in t: q="climate"
    else: q="india,news"
    return f"https://loremflickr.com/800/450/{q}?lock={nid}"

news=[]
for url in RSS:
    for e in feedparser.parse(url).entries[:10]:
        title=e.get('title','').strip()
        if len(title)<10: continue
        desc=clean(e.get('summary','') or e.get('description','') or title)
        # Sirf asli news, koi filler nahi
        parts = desc.split('. ')
        p1 = '. '.join(parts[:2]) + '.' if len(parts)>=2 else desc
        p2 = '. '.join(parts[2:4]) + '.' if len(parts)>=4 else ''

        news.append({
            "id": len(news),
            "title": title,
            "para1": p1,
            "para2": p2,
            "para3": "",
            "para4": "",
            "image": get_image(title, len(news)),
            "link": f"article.html?id={len(news)}",
            "category": "Latest",
            "date": "11 Sep 2026",
            "reporter": "Gaurav Sharma",
            "source": "4th Pillar News"
        })

with open('news.json','w',encoding='utf-8') as f:
    json.dump(news,f,ensure_ascii=False,indent=2)
