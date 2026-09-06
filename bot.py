import feedparser, json, datetime, os

old_news=[]
if os.path.exists('news.json'):
    try:
        with open('news.json','r',encoding='utf-8') as f: old_news=json.load(f)
    except: pass

sources={
"National":["https://feeds.bbci.co.uk/hindi/rss.xml"],
"International":["https://navbharattimes.indiatimes.com/rssfeeds/1081479906.cms"],
"Sports":["https://navbharattimes.indiatimes.com/rssfeeds/1081479908.cms"],
"Ghaziabad":["https://news.google.com/rss/search?q=Ghaziabad&hl=hi&gl=IN&ceid=IN:hi"],
"Business":["https://navbharattimes.indiatimes.com/rssfeeds/1081479907.cms"]
}
new_list=[]; nid=len(old_news)
for cat,urls in sources.items():
 for url in urls:
  try:
   d=feedparser.parse(url)
   for e in d.entries[:5]:
    title=e.title[:120]
    if any(o['title']==title for o in old_news+new_list): continue
    new_list.append({
     "id":nid,
     "category":cat,
     "title":title,
     "date":datetime.datetime.now().strftime("%d %B %Y"),
     "reporter":"Gaurav Sharma",
     "location":"Ghaziabad",
     "image":f"https://picsum.photos/seed/{nid+111}/800/500",
     "para1":f"{title}। इस घटना को लेकर पूरे क्षेत्र में चर्चा तेज हो गई है। 4th पिलर न्यूज़ को मिली जानकारी के अनुसार यह मामला बेहद महत्वपूर्ण माना जा रहा है।",
     "para2":"प्रत्यक्षदर्शियों और विश्वसनीय सूत्रों से मिली जानकारी के मुताबिक संबंधित विभाग ने इस विषय पर अपनी पूरी तैयारी कर ली है। लोगों में इसको लेकर काफी उत्सुकता देखी जा रही है।",
     "para3":"स्थानीय नागरिकों का कहना है कि यदि इस पर समय रहते उचित कदम उठाए गए तो आम जनता को इसका सीधा लाभ मिलेगा। इससे विकास कार्यों को नई दिशा मिलेगी।",
     "para4":f"रिपोर्टर गौरव शर्मा ने बताया कि {cat} से जुड़ी इस खबर पर प्रशासन की पैनी नजर बनी हुई है। हर कोई इसके पीछे की असली वजह जानना चाहता है।",
     "para5":"प्रशासन ने स्पष्ट रूप से कहा है कि इस मामले में किसी भी प्रकार की लापरवाही को बर्दाश्त नहीं किया जाएगा। नियम सभी के लिए समान रूप से लागू रहेंगे।",
     "para6":"आने वाले कुछ दिनों में इस खबर से जुड़ा बड़ा खुलासा सामने आने की संभावना है। सरकार के उच्च अधिकारी लगातार स्थिति पर निगरानी बनाए हुए हैं।",
     "para7":"इस घटना के बाद राजनीतिक और सामाजिक क्षेत्रों में भी हलचल तेज हो गई है। सभी पक्ष अपने-अपने स्तर पर इसकी समीक्षा कर रहे हैं।",
     "para8":"ताजा और सच्ची खबरें सबसे पहले हिंदी में पाने के लिए जुड़े रहिए 4th पिलर न्यूज़ के साथ। रिपोर्टर - गौरव शर्मा, गाजियाबाद।"
    }); nid+=1
  except: pass

final=new_list+old_news
final=final[:100]
for i,n in enumerate(final): n['id']=i
with open('news.json','w',encoding='utf-8') as f: json.dump(final,f,ensure_ascii=False,indent=2)
print(f"Total {len(final)} khabrein")
