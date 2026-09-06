import feedparser
import base64

LOGO = "4thpillar24x7.jpg"
# logo embed - 404 fix
try:
    with open(LOGO, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        LOGO_SRC = f"data:image/jpeg;base64,{b64}"
except:
    LOGO_SRC = LOGO

# Hindi News RSS
url = "https://news.google.com/rss?hl=hi&gl=IN&ceid=IN:hi"
feed = feedparser.parse(url)

print(f"Found {len(feed.entries)} news")

html = f"""<!DOCTYPE html>
<html lang="hi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>4TH PILLAR NEWS</title>
<style>
body{{margin:0;font-family:Noto Sans, Arial;background:#f1f1f1}}
.top{{background:#cc0000;color:#fff;text-align:center;padding:5px;font-size:12px}}
header{{background:#0d1b2a;color:#fff;display:flex;align-items:center;padding:10px 12px;gap:10px}}
.logo{{width:46px;height:46px;background:#fff;border-radius:8px;object-fit:contain}}
.card{{background:#fff;margin:10px;padding:14px;border-radius:10px;box-shadow:0 1px 3px rgba(0,0,0,.1)}}
.card a{{text-decoration:none;color:#111;font-weight:700;font-size:16px;display:block}}
.card span{{font-size:11px;color:#666;margin-top:4px;display:block}}
</style></head><body>
<div class="top">रविवार, 6 सितंबर 2026 | Ghaziabad, UP | Reporter: Gaurav Sharma</div>
<header><img class="logo" src="{LOGO_SRC}"><div><b>4TH PILLAR NEWS</b><div style="font-size:11px;color:#aaa">24x7 हिंदी खबर</div></div></header>
"""

for e in feed.entries[:30]:
    html += f'<div class="card"><a href="{e.link}" target="_blank">{e.title}</a><span>सोर्स: Google News | खोलने के लिए क्लिक करें</span></div>\n'

html += "</body></html>"

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
