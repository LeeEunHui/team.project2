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

dust_table=driver.find_element_by_class_name("tb_scroll").text
print(dust_table)

with urlopen('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%A0%84%EA%B5%AD%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80') as response:
    soup = BeautifulSoup(response,'html.parser')

    dust=soup.find('div',{'class':'tb_scroll'})

    dust_n = dust.select('th')
    dust_na=[]
    for i in dust_n :
        dust_na.append(i.text)
    dust_name=[]
    for i in range(len(dust_na)):
        if i>3:
            dust_name.append(dust_na[i])
    # print(dust_name)

    dust_t=dust.select("td")
    dust_td=[]
    dust_cc = []
    for i in dust_t:
        dust_td.append(i.text)
    for i in range(len(dust_td)):
        if i%3==0:
            k=int(dust_td[i])
            dust_cc.append(k)
    # print(dust_cc)

#추정훈 크롤러 코딩

    dust_am=[]
    for i in range(len(dust_td)):
        if i%3==1:
            dust_am.append(dust_td[i])
    # print(dust_am)


    dust_pm = []
    for i in range(len(dust_td)):
        if i % 3 == 2:
            dust_pm.append(dust_td[i])
    # print(dust_pm)
 # 이은희 크롤러 코딩

    x = []
    for i in range(1, 18):
        x.append(i)
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.bar(x, dust_cc)
    plt.xticks(x, dust_name)
    plt.xlabel('지역명')
    plt.ylabel('농도')
    plt.title("각 지역에 따른 미세먼지 농도")
    plt.show()
    # 추정훈 그래프 코딩

    name=input("지역을 검색하시오 : ")

    index=dust_name.index(name)
    # print(index)
    print("오전예보 :",dust_am[index])
    print("오후예보 :",dust_pm[index])
#이은희 그래프 코딩