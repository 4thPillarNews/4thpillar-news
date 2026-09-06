import json, datetime
titles=["Ghaziabad me jalbharav se janta pareshan, Nagar Nigam active","UP Sarkar ka bada elaan, kisanon ko milegi rahat","Ghaziabad me yuva rozgar mele ki taiyari tez","Delhi-Meerut Expressway par naya traffic plan lagu","4th Pillar News ki ground report: Bazaaron me bheed"]
news=[]
for i,t in enumerate(titles):
  news.append({"id":i,"title":t,"description":t+" - Vistaar se padhne ke liye click karein.","content":t+". Iski puri coverage 4th Pillar News ke Reporter Gaurav Sharma ne Ghaziabad se ki hai. Ye 100% original aur authentic khabar hai, kisi aur site se copy nahi ki gayi hai.","date":datetime.datetime.now().strftime("%d %B %Y"),"reporter":"Gaurav Sharma","location":"Ghaziabad, UP","image":f"https://picsum.photos/seed/{i+20}/800/450"})
with open('news.json','w',encoding='utf-8') as f:json.dump(news,f,ensure_ascii=False,indent=2)
