import feedparser, json, os
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
    elif any(x in t for x in ['visa','अमेरिका','america']): q="usa,visa"
    elif any(x in t for x in ['putin','रूस']): q="russia,jet"
    elif any(x in t for x in ['हत्या','गोली','murder','police','gurugram']): q="police,crime"
    elif 'brazil' in t or 'ब्राजील' in t: q="brazil,court"
    elif 'तापमान' in t or 'गर्मी' in t: q="heatwave,india"
    else: q="india,news,breaking"
    return f"https://source.unsplash.com/800x450/?{q}&sig={nid}"

# Purani news load rakho
old_news = []
if os.path.exists('news.json'):
    try:
        with open('news.json','r',encoding='utf-8') as f:
            old_news = json.load(f)
    except: old_news = []

titles_old = set([n['title'] for n in old_news])
new_list = []

for url in RSS:
    for e in feedparser.parse(url).entries[:10]:
        title=e.get('title','').strip()
        if len(title)<10 or title in titles_old: continue
        desc=clean(e.get('summary','') or e.get('description','') or title)
        parts=desc.split('. ')
        p1='. '.join(parts[:2])+'.' if len(parts)>=2 else desc
        p2='. '.join(parts[2:4])+'.' if len(parts)>=4 else ''
        new_list.append({
            "id": 0,
            "title": title,
            "para1": p1, "para2": p2, "para3": "", "para4": "",
            "image": "",
            "link": "", "category": "Latest", "date": "11 Sep 2026",
            "reporter": "Gaurav Sharma", "source": "4th Pillar News"
        })

# Nayi + Purani jod do
full = new_list + old_news
for i, n in enumerate(full):
    n['id'] = i
    n['link'] = f"article.html?id={i}"
    n['image'] = get_image(n['title'], i)
    full[i] = n

with open('news.json','w',encoding='utf-8') as f:
    json.dump(full[:50],f,ensure_ascii=False,indent=2)
