import feedparser, json, datetime, os

RSS = "https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi"
feed = feedparser.parse(RSS)

news = []
for i, e in enumerate(feed.entries[:20]):
    news.append({
        "id": i,
        "title": e.title,
        "link": e.link,
        "description": e.title,
        "date": datetime.datetime.now().strftime("%d %b %Y"),
        "image": f"https://picsum.photos/seed/{i+10}/800/450"
    })

# news.json save
with open("news.json","w",encoding="utf-8") as f:
    json.dump(news,f,ensure_ascii=False,indent=2)

# index.html auto generate - isme click pe puri khabar khulegi
html = """
<!DOCTYPE html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>4th Pillar News - Hindi</title>
<style>body{font-family:system-ui;max-width:900px;margin:auto;padding:10px;background:#f5f5f5}
.card{background:white;border-radius:12px;overflow:hidden;margin:12px 0;box-shadow:0 2px 8px #0001}
.card img{width:100%;height:200px;object-fit:cover}
.card.c{padding:12px}
.btn{display:inline-block;background:#d32f2f;color:white;padding:10px 16px;border-radius:6px;text-decoration:none;margin-top:8px}
</style></head><body>
<h2>4th Pillar - ताज़ा हिंदी समाचार</h2>
<div id="list"></div>
<script>
fetch('news.json').then(r=>r.json()).then(d=>{
let h='';
d.forEach((n,i)=>{
h+=`<div class="card"><img src="${n.image}"><div class="c"><h3>${n.title}</h3><small>${n.date}</small><p>${n.description}</p><a class="btn" href="${n.link}" target="_blank">पुरी खबर पढ़ें</a> <a class="btn" style="background:#333" href="article.html?id=${i}">यहाँ देखें</a></div></div>`;
});
document.getElementById('list').innerHTML=h;
});
</script></body></html>
"""
with open("index.html","w",encoding="utf-8") as f:
    f.write(html)

# article.html auto generate
article = """
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>News</title>
<style>body{font-family:system-ui;max-width:800px;margin:auto;padding:15px} img{width:100%;border-radius:10px}.btn{background:red;color:white;padding:12px 20px;text-decoration:none;border-radius:6px;display:inline-block;margin-top:10px}</style>
</head><body><div id="n"></div><script>
fetch('news.json').then(r=>r.json()).then(d=>{
const id=new URLSearchParams(location.search).get('id')||0; const x=d[id];
document.getElementById('n').innerHTML=`<a href="./">← वापस</a><img src="${x.image}"><h1>${x.title}</h1><p>${x.date}</p><p style="font-size:18px;line-height:1.7">${x.description}<br><br>यह खबर ${x.title} से संबंधित है। पूरी जानकारी के लिए Original Source पर जाएं।</p><a class="btn" href="${x.link}" target="_blank">पुरी खबर Original Site पर पढ़ें</a>`;
});
</script></body></html>
"""
with open("article.html","w",encoding="utf-8") as f:
    f.write(article)

print(f"DONE {len(news)} news, index + article generated")
