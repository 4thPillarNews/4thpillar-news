import json, feedparser, requests, datetime
from bs4 import BeautifulSoup

RSS_FEEDS = {
"National": "https://www.amarujala.com/rss/national.xml",
"International": "https://www.amarujala.com/rss/world.xml",
"NCR": "https://www.amarujala.com/rss/delhi-ncr.xml",
"Politics": "https://www.amarujala.com/rss/politics.xml",
"Business": "https://www.amarujala.com/rss/business.xml",
"Sports": "https://www.amarujala.com/rss/sports.xml"
}

def get_data(url):
    try:
        r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=20)
        soup=BeautifulSoup(r.text,'html.parser')
        og=soup.find('meta',property='og:image')
        img=og['content'] if og and og.get('content') else "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=800"
        paras=[p.get_text().strip() for p in soup.find_all('p') if len(p.get_text().strip())>70]
        if len(paras)<2: return None,None
        data={}
        for i in range(8):
            data[f'para{i+1}']=paras[i] if i < len(paras) else "4th Pillar News par is khabar se juda update jari hai."
        return data,img
    except:
        return None,None

all_news=[]
nid=0
for cat, rss in RSS_FEEDS.items():
    feed=feedparser.parse(rss)
    for e in feed.entries[:8]:
        try:
            d,im=get_data(e.link)
            if not d: continue
            all_news.append({"id":nid,"category":cat,"source":"4th Pillar News","title":e.title,"date":datetime.datetime.now().strftime("%d %B %Y"),"reporter":"Gaurav Sharma","location":"New Delhi","image":im,"link":e.link,**d})
            nid+=1
        except: continue

with open('news.json','w',encoding='utf-8') as f:
    json.dump(all_news,f,ensure_ascii=False,indent=2)

print(f"Total {len(all_news)} news created")
