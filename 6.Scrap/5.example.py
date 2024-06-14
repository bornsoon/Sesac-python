import requests
from bs4 import BeautifulSoup

url = "https://www.pythonscraping.com/pages/page3.html"

data =requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

# item = soup.select('tr.gift')
# print(item)
# item_name = []
# for i in item:
#     item_name.append(item.select_one('tr td'))

# print(item_name)

# table_tag = soup.find('table', id="giftList")
# table_tag = soup.select('#giftList')[0]
table_tag = soup.select_one('table#giftList')
# print(table_tag)

# product_trs = table_tag.find_all('tr')
product_trs = table_tag.select('tr')
# print(product_trs)

# product_names = []

# for item in product_trs:
#     product_names.append(item.select_one('td').get_text())

# print(product_names)

item_list = []

for product_tr in product_trs[1:]:
    product_tds = product_tr.select('td')
    # print(product_tds[0], product_tds[2])
    item_list.append({product_tds[0].text.strip(), product_tds[2].text.strip()})
    # print(f"상품명: {product_tds[0].text.strip()} 가격: {product_tds[2].text.strip()}")

print(item_list)