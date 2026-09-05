import json
from datetime import datetime

news_data = [
  {
    "id": 1,
    "title": "पीएम मोदी ने एआई मिशन का किया ऐलान",
    "desc": "प्रधानमंत्री ने आज दिल्ली में नेशनल एआई मिशन का ऐलान किया। इस योजना से गांव-गांव तक एआई पहुंचेगा। 5000 करोड़ का बजट तय किया गया है।",
    "date": "05 Sep 2026",
    "image": "https://images.pexels.com/photos/8386440/pexels-photo-8386440.jpeg"
  }
]

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(news_data, f, ensure_ascii=False, indent=2)
