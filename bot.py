import json, random, datetime
from urllib.request import urlopen

# Sample images (copyright free)
images = [
 "https://images.pexels.com/photos/518543/pexels-photo-518543.jpeg",
 "https://images.pexels.com/photos/209174/pexels-photo-209174.jpeg",
 "https://images.pexels.com/photos/356362/pexels-photo-356362.jpeg"
]

# Yaha se roz nayi news ayegi (abhi ke liye demo news)
news_pool = [
 {
  "title": "PM Modi ne AI Mission ka kiya elaan",
  "inshort": "Pradhan Mantri ne aaj Delhi me National AI Mission ka elaan kiya. Is mission ke tehet gaon-gaon tak Artificial Intelligence ki suvidha pahunchayi jayegi. Sarkar ne 5000 crore ka budget rakha hai. Kaha ki kisan se lekar chhatra tak sabko AI se joda jayega. Desh ke 100 colleges me AI labs banayi jayengi."
 },
 {
  "title": "Ghaziabad me Metro ka naya route shuru",
  "inshort": "Ghaziabad me metro ke naye route ki shuruaat ho gayi hai. Isse Noida aur Delhi ka safar 20 minute kam ho jayega. Roz 2 lakh yatriyon ko fayda milega. CM ne kaha ki agle saal tak pure UP me metro connectivity badhayi jayegi."
 }
]

selected = random.sample(news_pool, 2)
for n in selected:
    n["image"] = random.choice(images)
    n["date"] = datetime.datetime.now().strftime("%d %b %Y")
    n["source"] = "Verified"

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(selected, f, ensure_ascii=False, indent=2)

print("news.json updated!")
