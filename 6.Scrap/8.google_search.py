import requests
from bs4 import BeautifulSoup

base_url = "https://www.google.co.kr/search"

def naver_search(query):
    params = {"q": query}

    response = requests.get(base_url, params=params)
    return response.text

query = "파이썬 프로그래밍"
soup = naver_search(query)

print(soup)