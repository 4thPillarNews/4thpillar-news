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
