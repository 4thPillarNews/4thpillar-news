import feedparser, json, os
from datetime import datetime
feed_url = "https://feeds.bbci.co.uk/hindi/rss.xml"
feed = feedparser.parse(feed_url)
news = []
if os.path.exists('news.json'):
    try:
        with open('news.json','r',encoding='utf-8') as f:
            news = json.load(f)
    except: news=[]

for entry in feed.entries[:10]:
    if not any(n['title']==entry.title for n in news):
        summary = entry.get('summary','')
        # 600 words ke liye 4000 characters tak lega
        if len(summary) < 500:
            summary = entry.get('description','') or summary
        summary = summary[:4000]
        news.insert(0,{
          "title": entry.title,
          "desc": summary,
          "description": summary,
          "content": summary,
          "date": datetime.now().strftime("%d %b %Y, %I:%M %p"),
          "author": "Gaurav Sharma - 4thPillar News",
          "image": "https://images.pexels.com/photos/518543/pexels-photo-518543.jpeg"
        })

news = news[:30]
with open('news.json','w',encoding='utf-8') as f:
    json.dump(news,f,ensure_ascii=False,indent=2)
