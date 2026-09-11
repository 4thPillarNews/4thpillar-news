import json, feedparser, requests, datetime, os
from bs4 import BeautifulSoup

RSS_FEEDS = {
"National": "https://www.amarujala.com/rss/national.xml",
"International": "https://www.amarujala.com/rss/world.xml",
"NCR": "https://www.amarujala.com/rss/delhi-ncr.xml",
"Politics": "https://www.amarujala.com/rss/politics.xml",
"Business": "https://www.amarujala.com/rss/business.xml",
"Sports": "https://www.amarujala.com/rss/sports.xml"
}

def human_rewrite(t):
    for k,v in {"भारी बदलाव":"बड़े बदलाव","भंडार":"बड़ी संख्या","विनिर्माण":"मैन्युफैक्चरिंग"}.items():
        t=t.replace(k,v)
    return t

def get_news(url):
    try:
        r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=15)
        s=BeautifulSoup(r.text,'html.parser')
        img=s.find('meta',property='og:image')
        image=img['content'] if img else "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=800"
        paras=[p.get_text().strip() for p in s.find_all('p') if len(p.get_text().strip())>80]
        if len(paras)<2: return None,None
        d={}
        for i in range(8):
            d[f'para{i+1}']=human_rewrite(paras[i]) if i < len(paras) else "4th Pillar News par is khabar ka update jari hai."
        return d,image
    except: return None,None

all_news=[]
nid=0
for cat,rss in RSS_FEEDS.items():
    feed=feedparser.parse(rss)
    for e in feed.entries[:8]:
        paras,img=get_news(e.link)
        if not paras: continue
        all_news.append({"id":nid,"category":cat,"source":"4th Pillar News","title":human_rewrite(e.title),"date":datetime.datetime.now().strftime("%d %B %Y, %I:%M %p"),"reporter":"Gaurav Sharma","location":"New Delhi","image":img,"link":e.link,**paras})
        nid+=1

with open('news.json','w',encoding='utf-8') as f:
    json.dump(all_news[:500],f,ensure_ascii=False,indent=2)
