import json
import datetime
import random

# Ye teri khud ki original news headlines hai - roz isi tarah update hongi
headlines = [
    "Ghaziabad me aaj subah se tez baarish, sadkon par jalbharav",
    "UP me naye sarkari yojana ka elaan, kisanon ko milega fayda",
    "Ghaziabad Nagar Nigam ne safai abhiyan tez kiya",
    "Yuvaon ke liye rozgar mela Ghaziabad me kal se shuru",
    "Delhi-Meerut Expressway par traffic me badlav, naya rule lagu"
]

news = []
for i, title in enumerate(headlines):
    news.append({
        "id": i,
        "title": title,
        "slug": title.lower().replace(" ", "-"),
        "description": f"{title}. Is khabar ki puri report 4th Pillar News ki team ne Ghaziabad se cover ki hai. Vistaar se janne ke liye puri khabar padhein.",
        "content": f"{title}. 4th Pillar News, Ghaziabad. Reporter Gaurav Sharma ki khaas report. Is vishay par adhik jaankari aur ground report jaldi hi prakashit ki jayegi.",
        "date": datetime.datetime.now().strftime("%d %b %Y"),
        "reporter": "Gaurav Sharma",
        "location": "Ghaziabad",
        "image": f"https://picsum.photos/seed/{i+100}/800/450"
    })

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(news, f, ensure_ascii=False, indent=2)

print(f"{len(news)} original news saved!")
