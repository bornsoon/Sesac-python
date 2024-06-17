import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver"

def naver_search(query):
    params = {"query": query}

    response = requests.get(base_url, params=params)
    return response.text

query = "파이썬 프로그래밍"
text = naver_search(query)
soup = BeautifulSoup(text, 'html.parser')

# print(soup)

# headline = soup.select('h2')
# link = soup.select('h2')

# print(headline)

power_link_list = soup.select('ul.lst_type li')
# print(len(power_link_list))
# print(power_link_list)


for lst in power_link_list:
    try:
        print(f"사이트명: {lst.select('a.site')[0].get_text()}, 링크: {lst.select('a.lnk_url')[0].get_text()}")
    except:
        pass


title_list = soup.select('span.cSc2HQxxcP_aSG0g6fzy')
print([title_list])