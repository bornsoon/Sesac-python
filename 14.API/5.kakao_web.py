# curl -v -G GET "https://dapi.kakao.com/v2/search/web" \
# --data-urlencode "query=이효리" \
# -H "Authorization: KakaoAK ${REST_API_KEY}"

import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('KAKAO_API_KEY')

query = "이효리"

url = 'https://dapi.kakao.com/v2/search/web'
headers = {
    "Authorization": f"KakaoAK {API_KEY}",
}
params = {
    "query": query,
    "sort": "accuracy", # 정확도순
    "page": 1,
    "size": 10
}

response = requests.get(url, headers=headers, params=params)
response.raise_for_status()
data = response.json()
# print(data)
for item in data["documents"]:
    title = item["title"].replace("<b>","").replace("</b>","")
    url = item["url"]
    print(f"제목: {title}")
    print(f"URL: {url}")