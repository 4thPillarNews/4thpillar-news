import feedparser, base64
try:
  with open("4thpillar24x7.jpg","rb") as f:
    b64=base64.b64encode(f.read()).decode()
    logo=f"data:image/jpeg;base64,{b64}"
except:
  logo="4thpillar24x7.jpg"

feed=feedparser.parse("https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi")

html=f"""<!DOCTYPE html><html lang="hi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>4TH PILLAR NEWS</title><style>body{{margin:0;font-family:Arial;background:#eee}}header{{background:#111;color:#fff;display:flex;align-items:center;padding:10px;gap:10px}}.logo{{width:44px;height:44px;background:#fff;border-radius:8px;object-fit:contain}}.card{{background:#fff;margin:10px;padding:14px;border-radius:8px}}.card a{{text-decoration:none;color:#111;font-weight:bold;font-size:16px;display:block}}</style></head><body><header><img class="logo" src="{logo}"><b>4TH PILLAR NEWS - हिंदी</b></header>"""

for e in feed.entries[:30]:
  html+=f'<div class="card"><a href="{e.link}" target="_blank">{e.title}</a></div>'

html+="</body></html>"
open("index.html","w",encoding="utf-8").write(html)
