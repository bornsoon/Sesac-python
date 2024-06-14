import requests
from bs4 import BeautifulSoup

url = "http://www.cine21.com/rank/boxoffice/domestic"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

rank = soup.select('li')

print(rank)