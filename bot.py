import feedparser, json, datetime, os

old_news=[]
if os.path.exists('news.json'):
    try:
        with open('news.json','r',encoding='utf-8') as f: 
            old_news=json.load(f)
            print(f"Purani khabrein mili: {len(old_news)}")
    except: old_news=[]

sources={
"National":["https://feeds.bbci.co.uk/hindi/rss.xml","https://navbharattimes.indiatimes.com/rssfeeds/1081479906.cms","https://rss.jagran.com/rss/news/national.xml"],
"International":["https://navbharattimes.indiatimes.com/rssfeeds/1081479906.cms","https://feeds.bbci.co.uk/hindi/rss.xml"],
"Sports":["https://navbharattimes.indiatimes.com/rssfeeds/1081479908.cms","https://rss.jagran.com/rss/news/sports.xml"],
"Ghaziabad":["https://news.google.com/rss/search?q=Ghaziabad&hl=hi&gl=IN&ceid=IN:hi","https://news.google.com/rss/search?q=Noida+Ghaziabad+news&hl=hi&gl=IN&ceid=IN:hi"],
"Business":["https://navbharattimes.indiatimes.com/rssfeeds/1081479907.cms"]
}

new_list=[]
for cat,urls in sources.items():
 for url in urls:
  try:
   d=feedparser.parse(url)
   for e in d.entries[:6]: # har feed se 6 khabar
    title=e.title.strip()[:130]
    # agar purani me same title hai toh skip
    if any(title==o['title'] for o in old_news): continue
    if any(title==o['title'] for o in new_list): continue
    
    new_list.append({
     "id":0, "category":cat, "title":title,
     "date":datetime.datetime.now().strftime("%d %B %Y"),
     "reporter":"Gaurav Sharma","location":"Ghaziabad",
     "image":f"https://picsum.photos/seed/{len(old_news)+len(new_list)+100}/800/500",
     "para1":f"{title}। इस घटना को लेकर पूरे क्षेत्र में चर्चा तेज हो गई है। 4th पिलर न्यूज़ को मिली जानकारी के अनुसार यह मामला बेहद महत्वपूर्ण माना जा रहा है।",
     "para2":"विश्वसनीय सूत्रों से मिली जानकारी के मुताबिक संबंधित विभाग ने इस विषय पर अपनी पूरी तैयारी कर ली है। लोगों में इसको लेकर काफी उत्सुकता देखी जा रही है।",
     "para3":"स्थानीय नागरिकों का कहना है कि यदि इस पर समय रहते उचित कदम उठाए गए तो आम जनता को इसका सीधा लाभ मिलेगा। इससे विकास कार्यों को नई दिशा मिलेगी।",
     "para4":f"रिपोर्टर गौरव शर्मा ने बताया कि {cat} से जुड़ी इस खबर पर प्रशासन की पैनी नजर बनी हुई है। हर कोई इसके पीछे की असली वजह जानना चाहता है।",
     "para5":"प्रशासन ने स्पष्ट रूप से कहा है कि इस मामले में किसी भी प्रकार की लापरवाही को बर्दाश्त नहीं किया जाएगा। नियम सभी के लिए समान रूप से लागू रहेंगे।",
     "para6":"आने वाले कुछ दिनों में इस खबर से जुड़ा बड़ा खुलासा सामने आने की संभावना है। उच्च अधिकारी लगातार स्थिति पर निगरानी बनाए हुए हैं।",
     "para7":"इस घटना के बाद राजनीतिक और सामाजिक क्षेत्रों में भी हलचल तेज हो गई है। सभी पक्ष अपने-अपने स्तर पर इसकी समीक्षा कर रहे हैं।",
     "para8":"ताजा और सच्ची खबरें सबसे पहले हिंदी में पाने के लिए जुड़े रहिए 4th पिलर न्यूज़ के साथ। रिपोर्टर - गौरव शर्मा, गाजियाबाद।"
    })
  except as ex: print(ex); pass

final = new_list + old_news
final = final[:100]
for i,n in enumerate(final): n['id']=i

with open('news.json','w',encoding='utf-8') as f: json.dump(final,f,ensure_ascii=False,indent=2)

print(f"Nayi: {len(new_list)}, Purani: {len(old_news)}, Total: {len(final)}")
