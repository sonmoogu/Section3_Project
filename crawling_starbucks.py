from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from selenium import webdriver
# explicityly wait 사용하기 위해
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 지역검색을 누른 상태의 url가져오기
url = "https://www.istarbucks.co.kr/store/store_map.do?disp=locale"
driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(5)
driver.get(url)

# css를 활용해서 서울 클릭
css = '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'
seoul_button= WebDriverWait(driver, 10).\
              until(EC.presence_of_element_located((By.CSS_SELECTOR, css))).click()
seoul_button

css_2 = '#mCSB_2_container > ul > li:nth-child(1) > a'
all_button= WebDriverWait(driver, 10).\
              until(EC.presence_of_element_located((By.CSS_SELECTOR, css_2))).click()
all_button

time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

time.sleep(2)

print(soup.prettify()) # 서울시 전체 스타벅스 받아오기

time.sleep(2)

print()

starbucks_soup_list = soup.select('li.quickResultLstCon')
print("서울시내 스타벅스 점포 수: ", len(starbucks_soup_list))

# starbucks_soup_list[0] 확인
startbucks_store = starbucks_soup_list[0]
name = startbucks_store['data-name']
lat = startbucks_store['data-lat']
lng = startbucks_store['data-long']
address = str(startbucks_store.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
print(name)         # 매장명
print(lat)          # 위도
print(lng)          # 경도
print(address)      # 주소

starbucks_list = []
for item in starbucks_soup_list:
    name = item['data-name']
    lat = item['data-lat'].strip()
    lng = item['data-long'].strip()
    address = str(item.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
    
    starbucks_list.append( [ name, lat, lng, address])

columns = ['매장명','위도','경도','주소']
seoul_starbucks_df = pd.DataFrame(starbucks_list, columns = columns)
seoul_starbucks_df.head()

seoul_starbucks_df["구"] = [eachAddress.split()[1] for eachAddress in seoul_starbucks_df["주소"]]

# 25개여야 함
print()
print(seoul_starbucks_df["구"].unique(), len(seoul_starbucks_df["구"].unique()))

seoul_starbucks_df.to_excel('seoul_starbucks_list.xlsx', index=False)
seoul_starbucks_df.to_csv("seoul_starbucks_df.csv",sep=",", encoding = "utf-8-sig")

driver.quit()


