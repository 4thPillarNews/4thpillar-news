
import json, feedparser, requests, datetime, os
from bs4 import BeautifulSoup

RSS_FEEDS = {
    "National": "https://feeds.bbci.co.uk/hindi/rss.xml",
    "Ghaziabad": "https://www.amarujala.com/rss/ghaziabad.xml",
    "Noida": "https://www.amarujala.com/rss/noida.xml",
    "Politics": "https://www.amarujala.com/rss/politics.xml",
    "Business": "https://www.amarujala.com/rss/business.xml"
}

def human_rewrite(text):
    replace = {
        "भारी बदलाव": "बड़े बदलाव", "दौर से गुजर रहा है": "दौर से गुजर रही है",
        "भंडार": "बड़ी संख्या", "विनिर्माण": "मैन्युफैक्चरिंग",
        "क्षमताएं": "ताकत", "दुष्परिणामों": "नुकसान", "आह्वान": "अपील",
        "नजरिया": "रोडमैप", "बेहद शानदार": "शानदार", "मौजूद है": "है"
    }
    for k,v in replace.items():
        text = text.replace(k,v)
    return text

def get_full_news(url):
    try:
        r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'}, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        img_tag = soup.find('meta', property='og:image')
        image = img_tag['content'] if img_tag and img_tag.get('content') else "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=800"
        paras = [p.get_text().strip() for p in soup.find_all('p') if len(p.get_text().strip()) > 80]
        if len(paras) < 2: return None, None
        final = {}
        for i in range(8):
            if i < len(paras):
                final[f'para{i+1}'] = human_rewrite(paras[i])
            else:
                final[f'para{i+1}'] = "इस मामले पर प्रशासन की नजर बनी हुई है। 4th Pillar पर अपडेट जारी है।"
        return final, image
    except:
        return None, None

existing_news = []
existing_links = set()
if os.path.exists('news.json'):
    try:
        with open('news.json','r',encoding='utf-8') as f:
            existing_news = json.load(f)
            existing_links = {n.get('link','') for n in existing_news}
    except:
        existing_news = []

new_fetched = []
for cat, rss in RSS_FEEDS.items():
    feed = feedparser.parse(rss)
    for entry in feed.entries[:5]:
        link = entry.get('link','')
        if not link or link in existing_links: continue
        paras, img = get_full_news(link)
        if not paras: continue
        new_fetched.append({
            "category": cat,
            "title": human_rewrite(entry.title),
            "date": datetime.datetime.now().strftime("%d %B %Y, %I:%M %p"),
            "reporter": "Gaurav Sharma",
            "location": "Ghaziabad" if cat in ["Ghaziabad","Noida"] else "New Delhi",
            "image": img,
            "link": link,
            **paras
        })
        existing_links.add(link)

final_list = new_fetched + existing_news
final_list = final_list[:500]
for idx, item in enumerate(final_list):
    item['id'] = idx

with open('news.json','w',encoding='utf-8') as f:
    json.dump(final_list, f, ensure_ascii=False, indent=2)
print(f"Total {len(final_list)} news saved")
