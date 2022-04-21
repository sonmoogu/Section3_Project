from tqdm import tqdm_notebook
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from selenium import webdriver
# explicityly wait 사용하기 위해
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://ediya.com/contents/find_store.html#c")

# xpath를 사용해서 지역검색 클릭
xpath = '//*[@id="contentWrap"]/div[3]/div/div[1]/ul/li[2]/a'
area= WebDriverWait(driver, 10).\
              until(EC.presence_of_element_located((By.XPATH, xpath))).click()
area

time.sleep(3)

driver.maximize_window()

# 강서구와 중구에서 오류가 발생한다
gu = ["서울 강남구","서울 강동구","서울 강북구","서울 강서구","서울 관악구","서울 광진구","서울 구로구","서울 금천구","서울 노원구","서울 도봉구","서울 동대문구","서울 동작구",
    "서울 서대문구","서울 마포구","서울 서초구","서울 성동구","서울 성북구","서울 송파구","서울 양천구","서울 영등포구","서울 용산구","서울 은평구","서울 종로구","서울 중구","서울 중랑구"]

Ediya_list = []
for keyword in tqdm_notebook(gu):
    search_tag = driver.find_element_by_id("keyword")
    search_tag.clear()
    search_tag.send_keys(keyword)
    #button_xpath = '//*[@id="keyword_div"]/form/button'
    button_tag = driver.find_element_by_xpath('//*[@id="keyword_div"]/form/button').click()
    time.sleep(3)
    
    soup = BeautifulSoup(driver.page_source,'html.parser')
    time.sleep(3)
    
    Ediya_soup_list = soup.select('li.item')
    time.sleep(3)
    
    for item in Ediya_soup_list:
        txt = item.select_one("dl").text
        name = txt.split(" ",1)[0]
        address = txt.split(" ",1)[1]
        Ediya_list.append([name, address])

print(Ediya_list[1:5])

columns = ['매장명','주소']
seoul_Ediya_df = pd.DataFrame(Ediya_list, columns = columns)
seoul_Ediya_df["구"] = [eachAddress.split()[1] for eachAddress in seoul_Ediya_df["주소"]]

print(seoul_Ediya_df["구"].unique(), len(seoul_Ediya_df["구"].unique()))

seoul_Ediya_df["위도"] = np.nan
seoul_Ediya_df["경도"] = np.nan


# 암사3동점을 구글맵에서 인식하지 못해
# ediya_address = "이디야커피" + item[1] 불가

import googlemaps
gmaps_key = "AIzaSyALa3WC7ilIbtTRPk5jMXc4YY_sin-8NpI"
gmaps = googlemaps.Client(key = gmaps_key)

n = 0

for item in Ediya_list:
    ediya_address = item[1]
    tmp = gmaps.geocode(ediya_address, language = "ko")

    lat = tmp[0].get("geometry")["location"]["lat"]
    lng = tmp[0].get("geometry")["location"]["lng"]
    
    seoul_Ediya_df["위도"][n] = lat
    seoul_Ediya_df["경도"][n] = lng
    
    n +=1
    
print(n)

seoul_Ediya_df.to_excel('seoul_Ediya_list.xlsx', index=False)

seoul_Ediya_df.to_csv("seoul_Ediya_df.csv",sep=",", encoding = "utf-8-sig")


