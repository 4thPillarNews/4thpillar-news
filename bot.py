import json, datetime
titles = [
    "Ghaziabad me jalbharav: Nagar Nigam ne tez kiya kaam",
    "Ghaziabad ke bazaaron me tyohar ki raunak, bheed umdi",
    "UP me kisanon ke liye nayi yojana ka elaan hua",
    "Delhi-Meerut Expressway par traffic ke naye niyam lagu",
    "Ghaziabad me yuvaon ke liye rozgar mele ka aayojan"
]
news=[]
for i,t in enumerate(titles):
  news.append({
    "id": i,
    "title": t,
    "date": datetime.datetime.now().strftime("%d %B %Y"),
    "reporter": "Gaurav Sharma",
    "location": "Ghaziabad",
    "image": f"https://picsum.photos/seed/{i+50}/800/500",
    "para1": f"{t}. 4th Pillar News ki team ne mauke par jaakar jayja liya. Sthaniya logon se baat ki gayi aur sthiti ko samjha gaya.",
    "para2": "Sthaniya prashasan ke anusar is samasya ke samadhan ke liye pehle se hi yojna banayi ja rahi thi. Adhikariyon ne bataya ki jald hi iska sthayi samadhan nikal liya jayega.",
    "para3": "Ghaziabad ke nagrikon ka kehna hai ki pichle kuch dino se is tarah ki pareshani badh gayi hai. Logon ne prashasan se jaldi kadam uthane ki maang ki hai.",
    "para4": "4th Pillar News ke Reporter Gaurav Sharma ne jab ground report ki toh pata chala ki kaam zameen par ho raha hai lekin abhi aur tezi ki zarurat hai.",
    "para5": "Visheshagyaon ka manna hai ki agar sahi samay par kadam uthaye jayen toh is tarah ki samasyaon se bacha ja sakta hai. Janta ko bhi jagruk hone ki zarurat hai.",
    "para6": "Is poore mamle par Nagar Nigam aur Jila Prashasan lagatar nazar banaye hue hai. Kaha ja raha hai ki agle 24 ghante me sthiti samanya ho jayegi.",
    "para7": "Aise hi Ghaziabad ki har khabar sabse pehle paane ke liye jude rahiye 4th Pillar News ke saath. Reporter Gaurav Sharma ki ye vishesh report."
  })
with open('news.json','w',encoding='utf-8') as f:
  json.dump(news,f,ensure_ascii=False,indent=2)
