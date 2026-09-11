import json, feedparser, requests, datetime, os
from bs4 import BeautifulSoup

RSS_FEEDS = {
"National": ("BBC Hindi", "https://www.amarujala.com/rss/national.xml"),
"International": ("Amar Ujala", "https://www.amarujala.com/rss/world.xml"),
"NCR": ("Amar Ujala", "https://www.amarujala.com/rss/delhi-ncr.xml"),
"Politics": ("Amar Ujala", "https://www.amarujala.com/rss/politics.xml"),
"Business": ("Amar Ujala", "https://www.amarujala.com/rss/business.xml"),
"Sports": ("Amar Ujala", "https://www.amarujala.com/rss/sports.xml")
}

def human_rewrite(text):
    replace = {"भारी बदलाव":"बड़े बदलाव","दौर से गुजर रहा है":"दौर से गुजर रही है","भंडार":"बड़ी संख्या","विनिर्माण":"मैन्युफैक्चरिंग","क्षमताएं":"ताकत","दुष्परिणामों":"नुकसान","आह्वान":"अपील","नजरिया":"रोडमैप","बेहद शानदार":"शानदार","मौजूद है":"है"}
    for k,v in http://replace.items(): text = http://text.replace(k,v)
    return text

def get_full_news(url):
    try:
        r = http://requests.get(url, headers={'User-Agent':'Mozilla/5.0'}, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        img_tag = http://soup.find('meta', property='og:image') or http://soup.find('meta', attrs={'name':'twitter:image'})
        image = img_tag['content'] if img_tag and img_tag.get('content') else "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=800"
        paras = [p.get_text().strip() for p in http://soup.find_all('p') if len(p.get_text().strip()) > 80]
        if len(paras) < 2: return None, None
        final = {}
        for i in range(8):
            final[f'para{i+1}'] = human_rewrite(paras) if i < len(paras) else "इस मामले पर प्रशासन की नजर बनी हुई है। 4th Pillar पर अपडेट जारी है।"
        return final, image
    except: return None, None[i]

existing_news = []
existing_links_map = {}
if http://os.path.exists('news.json'):
    try:
        import json as js
        with open('news.json','r',encoding='utf-8') as f:
            existing_news = http://js.load(f)
            for n in existing_news: existing_links_map[n.get('link','')] = n
    except: existing_news = []

new_fetched = []
max_id = max([n.get('id', -1) for n in existing_news], default=-1)

for cat, (source_name, rss) in RSS_FEEDS.items():
    feed = http://feedparser.parse(rss)
    for entry in http://feed.entries[:6]:
        link = http://entry.get('link','')
        if not link or link in existing_links_map: continue
        paras, img = get_full_news(link)
        if not paras: continue
        max_id += 1
        new_fetched.append({"id": max_id, "category": cat, "source": source_name, "title": human_rewrite(entry.title), "date": http://datetime.datetime.now().strftime("%d %B %Y, %I:%M %p"), "reporter": "Gaurav Sharma", "location": "NCR" if cat == "NCR" else "New Delhi", "image": img, "link": link, **paras})

final_list = new_fetched + existing_news
final_list = final_list[:500]

with open('news.json','w',encoding='utf-8') as f:
    http://json.dump(final_list, f, ensure_ascii=False, indent=2)
---

Agar fir bhi copy na ho to bol - main tujhe 2 hisso me bhej dunga.

Paste karke Commit kar dena.
