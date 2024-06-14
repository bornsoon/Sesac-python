# pip install bs4      # DOM을 파싱 (beautifulSoup4)

from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>간단한 HTML 예제</title>
</head>
<body>
    <div class="container">
        <h1>안녕하세요</h1>
        <p>이것은 간단한 HTML 예제입니다.</p>
    </div>
    <a href="https://www.naver.com">네이버 링크</a>
    <img src="example.jpg" alt="예제 이미지">
    <img src="example2.jpg" alt="예제 이미지2" width="500" height="600">
    <div class="content">
        <ul>
            <li>항목 1</li>
            <li>항목 2</li>
            <li>항목 3</li>
        </ul>
    </div>
    <div id="footer">
        <p>Copyright C 2024. 이 페이지는 내꺼</p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, lxml

list_items = soup.ul.find_all('li')
# print(list_items)
# for li in list_items:
#     print(li.text)
# print(list_items[1].text)

# 클래스가 container인 항목 가져오기
container_div = soup.find('div', class_='container')
# print(container_div.p.text)

container_footer = soup.find('div', id='footer')
# print(container_footer.p.text)

content_ul = soup.find('div', class_='content').ul
# print(content_ul)

# for li in content_ul.find_all('li'):
#     print(li.text)

link_tag = soup.body.a # 가장 먼저 DOM에서 접하는 A 태그
print(link_tag.text)
print(link_tag.href) # 속성은 읽을 수 없음
naver_link = link_tag['href']
print(link_tag['href']) # 속성은 문자열로 가지고 와야함

# import requests
# response = requests.get(naver_link)
# print(response.text)

img_tag = soup.img
print(img_tag["src"])
print(img_tag["alt"])

img_tags = soup.find_all('img')
img_tag1 = img_tags[0]
img_tag2 = img_tags[1]
print(f'이미지태그1: ', img_tag1)
print(f'이미지태그2: ', img_tag2)

# 속성이 없을 경우에는 오류 -> get() 함수 사용
print(f"소소: {img_tag.get('src')}, ALT글자: {img_tag.get('alt')}, width: {img_tag.get('width')}")
print(f"소소: {img_tag2['src']}, ALT글자: {img_tag2['alt']}, width: {img_tag2['width']}")