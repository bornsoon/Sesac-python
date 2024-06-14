import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/section/105"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

# print(soup)
print('-------------parse-------------')
headline = soup.select('.sa_item._SECTION_HEADLINE a')

headline_title = headline['title']
print(headline)
# print(len(news_list))