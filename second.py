import selenium
from selenium import webdriver
import matplotlib.pyplot as plt
import matplotlib
from bs4 import BeautifulSoup
from urllib.request import urlopen

URL = "https://www.naver.com/"
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)

search_box=driver.find_element_by_name("query")
search_box.send_keys("전국초미세먼지")

search_btn=driver.find_element_by_id("search_btn")
search_btn.click()

# dust_name=driver.find_elements_by_tag_name('tr')
# print(dust_name)
# dust_name1=[]
# for i in dust_name:
#     dust_name1.append(i.text)
# print(dust_name1)
#
#이은희 크롤러 코딩