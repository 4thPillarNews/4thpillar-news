import feedparser, json, datetime

# Sirf Hindi News ke RSS
feeds = {
    "National": "https://news.google.com/rss/search?q=India+national+news&hl=hi&gl=IN&ceid=IN:hi",
    "International": "https://news.google.com/rss/search?q=International+samachar&hl=hi&gl=IN&ceid=IN:hi",
    "Sports": "https://news.google.com/rss/search?q=khel+samachar&hl=hi&gl=IN&ceid=IN:hi",
    "Ghaziabad": "https://news.google.com/rss/search?q=Ghaziabad+samachar&hl=hi&gl=IN&ceid=IN:hi",
    "Business": "https://news.google.com/rss/search?q=vyapar+samachar&hl=hi&gl=IN&ceid=IN:hi"
}

all_news=[]
nid=0
for cat, url in feeds.items():
    data = feedparser.parse(url)
    for e in data.entries[:6]:
        title = e.title.replace(" - Live", "").replace(" | ", " - ")
        all_news.append({
            "id": nid,
            "category": cat,
            "title": title,
            "date": datetime.datetime.now().strftime("%d %B %Y"),
            "reporter": "Gaurav Sharma",
            "location": cat,
            "image": f"https://picsum.photos/seed/{nid+200}/800/500",
            "para1": f"{cat} - {title} - 4th Pillar News ki khaas report. Is khabar ko lekar pure desh me charcha tez ho gayi hai.",
            "para2": "Mili jaankari ke mutabik is maamle par sambandhit vibhag ne apni taiyari puri kar li hai. Janta is faisle ka besabri se intezar kar rahi hai.",
            "para3": "Sthaniya logon aur visheshagyaon ka kehna hai ki is kadam se aam janta ko seedha fayda milega. Isse vikas ko nayi gati milegi.",
            "para4": f"Reporter Gaurav Sharma ne bataya ki {cat} se judi is ghatna par sabki nazar bani hui hai. Har koi iski asli wajah jaanna chahta hai.",
            "para5": "Prashasan ne is mamle me sakhti dikhate hue kaha hai ki kisi bhi tarah ki laparwahi bardasht nahi ki jayegi aur niyam sabke liye barabar honge.",
            "para6": "Aane wale kuch dino me is khabar se juda bada update saamne aa sakta hai. Sarkar is par lagatar nazar banaye hue hai.",
            "para7": f"Desh-duniya ki aisi hi har khabar Hindi me sabse pehle paane ke liye jude rahiye 4th Pillar News ke saath. Reporter: Gaurav Sharma, {cat} Desk."
        })
        nid+=1

with open('news.json','w',encoding='utf-8') as f:
    json.dump(all_news,f,ensure_ascii=False,indent=2)
