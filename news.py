import feedparser, json
from datetime import datetime
RSS_FEEDS = ["https://www.bhaskar.com/rss-v1--category-1.xml","https://navbharattimes.indiatimes.com/rss.cms"]
all_news=[];news_id=0
for rss_url in RSS_FEEDS:
 for entry in feedparser.parse(rss_url).entries[:5]:
  today=datetime.now().strftime("%d %b %Y")
  img=f"https://picsum.photos/seed/{news_id}/800/450"
  all_news.append({"id":news_id,"title":entry.title,"para1":entry.summary if hasattr(entry,'summary') else entry.title,"para2":"","para3":"","para4":"","image":img,"link":f"article.html?id={news_id}","category":"Latest","date":today,"reporter":"Gaurav Sharma","source":"4th Pillar News"})
  news_id+=1
with open('news.json','w',encoding='utf-8') as f: json.dump(all_news,f,ensure_ascii=False,indent=2)
