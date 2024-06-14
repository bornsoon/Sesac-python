import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/index"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

# print(soup)
# items = soup.select('li.today_item')

# # print(items)
# item_list = []
# for item in items:
#     item_list.append(item.select('a'))

# for item in item_list:
#     print(item['href'])
#     print(item['title'])

news_list = soup.select(".today_list > li")
# print(len(news_list))

for news in news_list:
    a_tag = news.select_one('a')
    print(a_tag['title'])
    print(a_tag['href'])