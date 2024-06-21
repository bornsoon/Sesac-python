from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cine_database as my_db
# pip install openpyxl  # 엑셀파일을 다루기 위한 라이브러리

import time

# 크롬 실행시에 필요한 옵션들 추가하기
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 브라우저를 숨겨서 실행
# chrome_options.add_argument("--window-size=1920,1000")

# 페이지 대기를 위한 데이터 생성 - 내가 시킨 일에 대해서 최대 10초까지 기다려라...
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

wait = WebDriverWait(driver, 10)

conn, cur = my_db.init_db()

def boxoffice(n):
    data = []
    # 웹 페이지 열기
    base_url = 'http://www.cine21.com'
    ranking_url = base_url + '/rank/boxoffice/domestic'
    driver.get(ranking_url)
    n -= 1

    if n > 9:
        page_next = driver.find_element(By.CSS_SELECTOR, "a.btn_next")
        # page_next = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.page a')))
        page_next.click()
        time.sleep(1)
        n -= 10
    
    # n 번째 페이지 가져오기
    page_tags = driver.find_elements(By.CSS_SELECTOR, "div.page a")
    
    # page_tags = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.page a')))

    page_tags[n].click()
    time.sleep(1)

    # 페이지 소스 가져오기...
    # page_source = driver.page_source
    # soup = BeautifulSoup(page_source, 'html.parser')
    # boxoffice_list_content = soup.find('div', id='boxoffice_list_content')

    boxoffice_list_content = driver.find_element(By.ID, 'boxoffice_list_content')

    boxoffice_li_list = boxoffice_list_content.find_elements(By.CSS_SELECTOR,'li.boxoffice_li')
    for boxoffice_li in boxoffice_li_list:
        mov_name_div = boxoffice_li.find_element(By.CSS_SELECTOR, 'div.mov_name')
        people_num_div = boxoffice_li.find_element(By.CSS_SELECTOR, 'div.people_num')
        rank_num_div = boxoffice_li.find_element(By.CSS_SELECTOR, 'span.grade')
        
        a_link = boxoffice_li.find_element(By.TAG_NAME, 'a')
        mov_link = base_url + a_link.get_attribute('href')

        rank = rank_num_div.text.strip()
        mov_name = mov_name_div.text.strip()
        people_num = people_num_div.text.strip().replace('관객수|','')

        # print(f"순위: {rank}, 영화 제목: {mov_name}, 관객수: {people_num}, 웹사이트정보: {mov_link}")
        data.append((rank, mov_name, people_num, mov_link))

    return data

# for row in boxoffice(1):
#     print('-' * 30)
#     print(row)

for row in boxoffice(1):
    my_db.save_to_db(conn, cur, row)

my_db.query_movie(cur)

my_db.close_db(conn)

# 브라우저 닫기
driver.quit()