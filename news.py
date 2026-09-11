import json, feedparser, datetime

FEEDS = {
"National": "https://www.amarujala.com/rss/national.xml",
"International": "https://www.amarujala.com/rss/world.xml",
"NCR": "https://www.amarujala.com/rss/delhi-ncr.xml",
"Politics": "https://www.amarujala.com/rss/politics.xml",
"Business": "https://www.amarujala.com/rss/business.xml",
"Sports": "https://www.amarujala.com/rss/sports.xml"
}

all_news = []
nid = 0
for cat, url in FEEDS.items():
    feed = feedparser.parse(url)
    for e in feed.entries[:8]:
        desc = e.get('summary','')[:500] or e.title
        all_news.append({
            "id": nid,
            "category": cat,
            "source": "4th Pillar News",
            "title": e.title,
            "date": datetime.datetime.now().strftime("%d %B %Y"),
            "reporter": "Gaurav Sharma",
            "location": "New Delhi",
            "image": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=800",
            "link": e.link,
            "para1": desc,
            "para2": "4th Pillar News par is khabar ki poori update jari hai.",
            "para3": "Is khabar se judi har chhoti badi jankari aapko yahan milegi.",
            "para4": "Bane rahiye 4th Pillar News ke saath.",
            "para5": "",
            "para6": "",
            "para7": "",
            "para8": ""
        })
        nid+=1

with open('news.json','w',encoding='utf-8') as f:
    json.dump(all_news,f,ensure_ascii=False,indent=2)

print(f"Created {len(all_news)} news")
