# 크롬 드라이버가 버전이 나중에 안맞는게 문제임
# 크롬 드라이버를 관리해주는 드라이버 라이브러리가 있음..

# pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

# 크롬 실행시에 필요한 옵션들 추가하기
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저를 숨겨서 실행
chrome_options.add_argument("--window-size=1920,1000")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 웹 페이지 열기
driver.get('https://www.google.com')

# 검색창에서 내가 원하는 글자 입력하기
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Python Programming')

# 엔터를 치던지 검색 버튼을 가져와서 그걸 클릭을 하던지
# search_box.submit()
search_box.send_keys(Keys.RETURN)

# time.sleep(5)

# 결과 페이지를 스크린샷 뜨고 싶으면?
driver.save_screenshot('search_result_003.png')

# 브라우저 닫기
driver.quit()