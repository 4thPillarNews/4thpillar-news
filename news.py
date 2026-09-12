import re

# Saari news agencies ke naam - ye sab hat jayenge
BAD_WORDS = [
    "BBC", "बीबीसी", "BCC",
    "Aaj Tak", "आज तक", "AajTak",
    "ABP", "ABP News", "एबीपी",
    "NDTV", "एनडीटीवी",
    "Zee News", "Zee", "ज़ी न्यूज़", "ज़ी",
    "Republic", "रिपब्लिक",
    "Amar Ujala", "अमर उजाला",
    "Dainik Jagran", "दैनिक जागरण", "Jagran",
    "Navbharat Times", "नवभारत",
    "Hindustan", "हिंदुस्तान", "Dainik Bhaskar", "भास्कर",
    "Times of India", "TOI",
    "The Hindu", "Indian Express", "PTI", "ANI", "IANS",
    "CNN", "Reuters", "AFP"
]

def full_news(url):
    try:
        r = requests.get(url, timeout=20, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.text, 'lxml')

        img = ""
        for im in soup.find_all("img"):
            src = im.get("src","")
            if src.startswith("http") and len(src) > 40:
                if "logo" in src.lower(): continue
                img = src
                break
        if not img:
            og = soup.find("meta", property="og:image")
            if og: img = og.get("content","")

        paras = []
        for p in soup.find_all("p"):
            t = p.get_text().strip()
            if len(t) < 80: continue
            if "AI" in t and "अनुवाद" in t: continue
            if "कृत्रिम बुद्धिमत्ता" in t: continue

            # Saare agency ke naam hatao
            for bad in BAD_WORDS:
                # Case-insensitive hatane ke liye
                t = re.sub(re.escape(bad), "", t, flags=re.IGNORECASE)
            
            # Extra space saaf karo
            t = re.sub(r'\s{2,}', ' ', t).strip()
            if len(t) < 50: continue
            paras.append(t)

        text = " ".join(paras)
        words = text.split()
        mid = len(words)//2
        p1 = " ".join(words[:mid])
        p2 = " ".join(words[mid:])

        return img, p1, p2
    except:
        return "", "", ""
