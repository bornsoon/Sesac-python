import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/section/105"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

# # print(soup)
# headline = soup.select('li.sa_item._SECTION_HEADLINE a.sa_text_title')
# # print(len(headline))

# for title in headline:
#     print(f"헤드라인 [제목]: {title.select('strong')[0].get_text()}, [링크]: {title['href']}")

# print('-------------parse-------------')

# article = soup.select('div.section_article._TEMPLATE div.sa_text')
# # print(article)

# for title in article:
#     print(f"기사 [제목]: {title.select_one('strong').text}, [링크]: {title.select_one('a')['href']}")

#----------------------------------------------------------------------------------------------------------------


def print_articles(headline=True):
    if headline:
        section_articles = soup.select('div.section_article.as_headline._TEMPLATE')
    else:
        section_articles = soup.select('div.section_article._TEMPLATE')

    for section_article in section_articles:
        sa_text_titles = section_article.find_all('a', class_='sa_text_title')
        # print(len(sa_text_titles))
        for sa_text_title in sa_text_titles:
            print(sa_text_title.get_text().strip())

# section_articles = soup.find_all('div', class_='section_article.as_headline _TEMPLATE')

# Ctrl + Shift + C 하고 태그 우클릭 ( Copy > Copy selector )
# section_articles = soup.select_one('#newsct > div.section_component.as_section_headline._PERSIST_CONTENT > div.section_article.as_headline._TEMPLATE')
# print(section_articles)

print_articles(headline=True)
print('-' * 50)
print_articles(headline=False)