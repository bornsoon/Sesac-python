#pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 크롬 드라이버 초기화
service = Service(executable_path="./chromedriver.exe")  # 크롬 버전에 맞게 설치해야함
driver = webdriver.Chrome(service=service)

# 웹 페이지 열기
driver.get('https://www.naver.com')

# 브라우저 닫기
driver.quit()