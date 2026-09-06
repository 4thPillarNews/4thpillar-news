import json, os, datetime
try:
    import feedparser
except:
    feedparser = None

old_news = []
if os.path.exists('news.json'):
    try:
        with open('news.json','r',encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list): old_news = data
    except: old_news = []

new_list = []
if feedparser:
    sources = [
        ("National","https://feeds.bbci.co.uk/hindi/rss.xml"),
        ("Sports","https://navbharattimes.indiatimes.com/rssfeeds/1081479908.cms"),
        ("Ghaziabad","https://news.google.com/rss/search?q=Ghaziabad&hl=hi&gl=IN&ceid=IN:hi"),
    ]
    for cat, url in sources:
        try:
            d = feedparser.parse(url)
            for e in d.entries[:5]:
                title = getattr(e,'title','खबर')[:130]
                if any(title==o.get('title') for o in old_news): continue
                if any(title==o.get('title') for o in new_list): continue
                new_list.append({
                    "id":0,"category":cat,"title":title,
                    "date":datetime.datetime.now().strftime("%d %B %Y"),
                    "reporter":"Gaurav Sharma","location":"Ghaziabad",
                    "image":f"https://picsum.photos/seed/{len(old_news)+len(new_list)+50}/800/500",
                    "para1":f"{title}। इस घटना को लेकर पूरे क्षेत्र में चर्चा तेज हो गई है। 4th पिलर न्यूज़ को मिली जानकारी के अनुसार यह मामला बेहद महत्वपूर्ण माना जा रहा है।",
                    "para2":"विश्वसनीय सूत्रों से मिली जानकारी के मुताबिक संबंधित विभाग ने इस विषय पर अपनी पूरी तैयारी कर ली है। लोगों में इसको लेकर काफी उत्सुकता देखी जा रही है।",
                    "para3":"स्थानीय नागरिकों का कहना है कि यदि इस पर समय रहते उचित कदम उठाए गए तो आम जनता को इसका सीधा लाभ मिलेगा। इससे विकास कार्यों को नई दिशा मिलेगी।",
                    "para4":f"रिपोर्टर गौरव शर्मा ने बताया कि {cat} से जुड़ी इस खबर पर प्रशासन की पैनी नजर बनी हुई है।",
                    "para5":"प्रशासन ने स्पष्ट रूप से कहा है कि इस मामले में किसी भी प्रकार की लापरवाही को बर्दाश्त नहीं किया जाएगा।",
                    "para6":"आने वाले कुछ दिनों में इस खबर से जुड़ा बड़ा खुलासा सामने आने की संभावना है।",
                    "para7":"इस घटना के बाद राजनीतिक और सामाजिक क्षेत्रों में भी हलचल तेज हो गई है।",
                    "para8":"ताजा और सच्ची खबरें सबसे पहले हिंदी में पाने के लिए जुड़े रहिए 4th पिलर न्यूज़ के साथ। रिपोर्टर - गौरव शर्मा, गाजियाबाद।"
                })
        except: pass

# Agar feed se kuch nahi aaya toh purani khabrein hi rakho, fail mat karo
if not new_list and not old_news:
    new_list.append({
        "id":0,"category":"National","title":"गाजियाबाद में विकास कार्यों को मिली नई गति",
        "date":datetime.datetime.now().strftime("%d %B %Y"),
        "reporter":"Gaurav Sharma","location":"Ghaziabad",
        "image":"https://picsum.photos/seed/1/800/500",
        "para1":"गाजियाबाद में विकास कार्यों को लेकर चर्चा तेज हो गई है। 4th पिलर न्यूज़ को मिली जानकारी के अनुसार यह मामला बेहद महत्वपूर्ण माना जा रहा है।",
        "para2":"विश्वसनीय सूत्रों से मिली जानकारी के मुताबिक संबंधित विभाग ने इस विषय पर अपनी पूरी तैयारी कर ली है।",
        "para3":"स्थानीय नागरिकों का कहना है कि इससे आम जनता को सीधा लाभ मिलेगा।",
        "para4":"रिपोर्टर गौरव शर्मा ने बताया कि इस खबर पर प्रशासन की पैनी नजर बनी हुई है।",
        "para5":"प्रशासन ने स्पष्ट रूप से कहा है कि किसी भी प्रकार की लापरवाही को बर्दाश्त नहीं किया जाएगा।",
        "para6":"आने वाले कुछ दिनों में बड़ा खुलासा सामने आने की संभावना है।",
        "para7":"इस घटना के बाद राजनीतिक और सामाजिक क्षेत्रों में भी हलचल तेज हो गई है।",
        "para8":"ताजा खबरों के लिए जुड़े रहिए 4th पिलर न्यूज़ के साथ। रिपोर्टर - गौरव शर्मा।"
    })

final = new_list + old_news
final = final[:100]
for i,n in enumerate(final): n['id']=i

with open('news.json','w',encoding='utf-8') as f:
    json.dump(final,f,ensure_ascii=False,indent=2)

print(f"SUCCESS: Total {len(final)} news")
