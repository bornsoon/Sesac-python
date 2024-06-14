import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/section/105"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

# print(soup)
headline = soup.select('li.sa_item._SECTION_HEADLINE a.sa_text_title')
# print(len(headline))

for title in headline:
    print(f"헤드라인 [제목]: {title.select('strong')[0].get_text()}, [링크]: {title['href']}")

print('-------------parse-------------')

article = soup.select('div.section_article._TEMPLATE div.sa_text')
# print(article)

for title in article:
    print(f"기사 [제목]: {title.select_one('strong').text}, [링크]: {title.select_one('a')['href']}")