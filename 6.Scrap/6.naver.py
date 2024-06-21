import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/index"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser') # 기본 파서, lxml 이라고 불리는 더 좋은 (추가 설치해야함)

# print(soup)                              # 1. Ctrl + Shift + C를 눌러서, 원하는 영역을 선택한다.
# items = soup.select('li.today_item')     # 2. 화살표 왼쪽을 눌러서 한 단계씩 위로 올라간다.
                                           # 3. 내가 원하는 리스트 전체를 포함하는 시점까지 올라간다.
# # print(items)                           # 4. 해당 시점이 되었을 때, 일반적으로 ul, ol, table이거나 등등일 가능성이 큼(아니어도 무방)
# item_list = []                           # 5. 그 시점이 되었을 때, DOM요소(element)의 class거나 id를 가져온다. (ID는 해당 페이지에서 unique하기 때문에 그걸 찾으면 BEST)
# for item in items:                       # 6. 주의 사항: 클래스명이 unique하지 않을 수 있음.
#     item_list.append(item.select('a'))
                                                 # select <-- 여러개를 반납 (리스트)
# for item in item_list:                         # select_one <-- 하나만 나옴
#     print(item['href'])                        # => CSS 셀렉터를 사용해서 요소를 선택한다.
#     print(item['title'])
                                                 # find <-- 하나만 나옴
news_list = soup.select(".today_list > li")      # find_all <-- 여러개를 반납 (리스트)
# print(len(news_list))                          # => DOM 요소를 사용해서 요소를 선택한다.

for news in news_list:
    a_tag = news.select_one('a')
    print(a_tag['title'])
    div_tag = news.select_one('title')
    print(div_tag.text.strip())
    print(a_tag['href'])