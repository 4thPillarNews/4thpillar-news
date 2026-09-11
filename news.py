import feedparser, json, re
from bs4 import BeautifulSoup

RSS = [
 "https://www.bhaskar.com/rss-v1--category-1742.xml",
 "https://navbharattimes.indiatimes.com/rssfeeds/9097204.cms"
]

def clean(s):
    return BeautifulSoup(s,'html.parser').get_text().strip()

def get_resemble_image(title, nid):
    t = title.lower()
    if any(x in t for x in ['nepal', 'बाढ़', 'तबाही', 'बारिश']):
        q = "nepal,flood"
    elif any(x in t for x in ['h-1b', 'visa', 'अमेरिका', 'अमेरिकी']):
        q = "usa,white-house"
    elif any(x in t for x in ['putin', 'पुतिन', 'विमान', 'रूस']):
        q = "fighter-jet,russia"
    elif any(x in t for x in ['हत्या', 'गोली', 'gurugram', 'मर्डर', 'पुलिस', 'अपराध']):
        q = "police,crime-scene"
    elif any(x in t for x in ['ब्राजील', 'brazil', 'court']):
        q = "brazil,court"
    elif any(x in t for x in ['तापमान', 'गर्मी', 'समंदर', 'पश्चिमी']):
        q = "climate,heatwave"
    elif any(x in t for x in ['मोहम्मद बिन सलमान', 'सऊदी', 'ट्रंप', 'trump']):
        q = "donald-trump,saudi"
    elif any(x in t for x in ['एयरपोर्ट', 'airport', 'metro', 'छात्र']):
        q = "delhi-metro,airport"
    else:
        q = "india,news"

    # loremflickr keyword se milti julti image deta hai, random nahi
    return f"https://loremflickr.com/800/450/{q}?lock={nid}"

all_news=[]
for url in RSS:
    feed=feedparser.parse(url)
    for e in feed.entries[:10]:
        title=e.get('title','').strip()
        if not title or len(title)<10: continue
        desc=clean(e.get('summary','') or e.get('description','') or title)
        parts=desc.split('. ')
        mid=len(parts)//2
        p1='. '.join(parts[:mid])+'.' if mid>0 else desc
        p2='. '.join(parts[mid:])+'.' if len(parts)>mid else ''

        all_news.append({
            "id": len(all_news),
            "title": title,
            "para1": p1, "para2": p2, "para3": "", "para4": "",
            "image": get_resemble_image(title, len(all_news)),
            "link": f"article.html?id={len(all_news)}",
            "category": "Latest",
            "date": "11 September 2026",
            "reporter": "Akash Sharma",
            "source": "4th Pillar News"
        })
        if len(all_news)>=18: break

with open('news.json','w',encoding='utf-8') as f:
    json.dump(all_news,f,ensure_ascii=False,indent=2)

print(f"Done {len(all_news)} with resemble images")
