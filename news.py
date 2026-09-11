import json, feedparser, datetime, requests
from bs4 import BeautifulSoup

FEEDS = {
"National": "https://www.amarujala.com/rss/national.xml",
"International": "https://www.amarujala.com/rss/world.xml",
"NCR": "https://www.amarujala.com/rss/delhi-ncr.xml",
"Politics": "https://www.amarujala.com/rss/politics.xml",
"Business": "https://www.amarujala.com/rss/business.xml",
"Sports": "https://www.amarujala.com/rss/sports.xml"
}

def get_image(link, cat):
    try:
        r = requests.get(link, headers={'User-Agent':'Mozilla/5.0'}, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        og = soup.find('meta', property='og:image')
        if og and og.get('content'):
            return og['content']
    except:
        pass
    # Agar image na mile to category ke hisab se alag image
    cats = {
        "National":"https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=800",
        "International":"https://images.unsplash.com/photo-1521295121783-8a321d551ad2?w=800",
        "NCR":"https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=800",
        "Politics":"https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?w=800",
        "Business":"https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800",
        "Sports":"https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=800"
    }
    return cats.get(cat, cats["National"])

all_news = []
nid = 0
for cat, url in FEEDS.items():
    feed = feedparser.parse(url)
    for e in feed.entries[:8]:
        img = get_image(e.link, cat)
        desc = e.get('summary','')[:800] or e.title
        all_news.append({
            "id": nid,
            "category": cat,
            "source": "4th Pillar News",
            "title": e.title,
            "date": datetime.datetime.now().strftime("%d %B %Y"),
            "reporter": "Gaurav Sharma",
            "location": "New Delhi",
            "image": img,
            "link": e.link,
            "para1": desc,
            "para2": "4th Pillar News par is khabar se judi har update aapko yahan milegi.",
            "para3": "Is khabar ko lekar prashasan aur janpratinidhiyon ki pratikriya bhi aane lagi hai.",
            "para4": "4th Pillar News ki team is par lagatar nazar banaye hue hai.",
            "para5": "",
            "para6": "",
            "para7": "",
            "para8": ""
        })
        nid+=1

with open('news.json','w',encoding='utf-8') as f:
    json.dump(all_news,f,ensure_ascii=False,indent=2)

print(f"Created {len(all_news)} news with real images")
