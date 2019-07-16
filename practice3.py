from selenium import webdriver
from bs4 import BeautifulSoup
# from time import sleep

driver = webdriver.Chrome('C:\driver\chromedriver')  # driver path
driver.get('https://www.naver.com')
driver.find_element_by_xpath('//*[@id="news_cast"]/div[1]/ul/li[1]/a').click()
# driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').click()

# article 1
driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list1=soup.find_all('h3',{'class':'tts_head'})
for title1 in title_list1:
    print(title1.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 2
driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list2=soup.find_all('h3',{'class':'tts_head'})
for title2 in title_list2:
    print(title2.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 3
driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list3=soup.find_all('h3',{'class':'tts_head'})
for title3 in title_list3:
    print(title3.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 4
driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list4=soup.find_all('h3',{'class':'tts_head'})
for title4 in title_list4:
    print(title4.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 5
driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list5=soup.find_all('h3',{'class':'tts_head'})
for title5 in title_list5:
    print(title5.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 6
driver.find_element_by_xpath('//*[@id="section_politics"]/div[2]/div/ul/li[1]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list6=soup.find_all('h3',{'class':'tts_head'})
for title6 in title_list6:
    print(title6.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 7
driver.find_element_by_xpath('//*[@id="section_politics"]/div[2]/div/ul/li[2]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list7=soup.find_all('h3',{'class':'tts_head'})
for title7 in title_list7:
    print(title7.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 8
driver.find_element_by_xpath('//*[@id="section_politics"]/div[2]/div/ul/li[3]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list8=soup.find_all('h3',{'class':'tts_head'})
for title8 in title_list8:
    print(title8.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 9
driver.find_element_by_xpath('//*[@id="section_politics"]/div[2]/div/ul/li[4]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list9=soup.find_all('h3',{'class':'tts_head'})
for title9 in title_list9:
    print(title9.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 10
driver.find_element_by_xpath('//*[@id="section_politics"]/div[2]/div/ul/li[5]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list10=soup.find_all('h3',{'class':'tts_head'})
for title10 in title_list10:
    print(title10.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#article 11
driver.find_element_by_xpath('//*[@id="section_economy"]/div[2]/div/ul/li[1]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list11=soup.find_all('h3',{'class':'tts_head'})
for title11 in title_list11:
    print(title11.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 12
driver.find_element_by_xpath('//*[@id="section_economy"]/div[2]/div/ul/li[2]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list12=soup.find_all('h3',{'class':'tts_head'})
for title12 in title_list12:
    print(title12.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 13
driver.find_element_by_xpath('//*[@id="section_economy"]/div[2]/div/ul/li[3]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list13=soup.find_all('h3',{'class':'tts_head'})
for title13 in title_list13:
    print(title13.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 14
driver.find_element_by_xpath('//*[@id="section_economy"]/div[2]/div/ul/li[4]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list14=soup.find_all('h3',{'class':'tts_head'})
for title14 in title_list14:
    print(title14.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 15
driver.find_element_by_xpath('//*[@id="section_economy"]/div[2]/div/ul/li[5]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list15=soup.find_all('h3',{'class':'tts_head'})
for title15 in title_list15:
    print(title15.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 16
driver.find_element_by_xpath('//*[@id="section_society"]/div[2]/div/ul/li[1]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list16=soup.find_all('h3',{'class':'tts_head'})
for title16 in title_list16:
    print(title16.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 17
driver.find_element_by_xpath('//*[@id="section_society"]/div[2]/div/ul/li[2]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list17=soup.find_all('h3',{'class':'tts_head'})
for title17 in title_list17:
    print(title17.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 18
driver.find_element_by_xpath('//*[@id="section_society"]/div[2]/div/ul/li[3]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list18=soup.find_all('h3',{'class':'tts_head'})
for title18 in title_list18:
    print(title18.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 19
driver.find_element_by_xpath('//*[@id="section_society"]/div[2]/div/ul/li[4]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list19=soup.find_all('h3',{'class':'tts_head'})
for title19 in title_list19:
    print(title19.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 20
driver.find_element_by_xpath('//*[@id="section_society"]/div[2]/div/ul/li[5]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list20=soup.find_all('h3',{'class':'tts_head'})
for title20 in title_list20:
    print(title20.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 21
driver.find_element_by_xpath('//*[@id="section_life"]/div[2]/div/ul/li[1]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list21=soup.find_all('h3',{'class':'tts_head'})
for title21 in title_list21:
    print(title21.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 22
driver.find_element_by_xpath('//*[@id="section_life"]/div[2]/div/ul/li[2]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list22=soup.find_all('h3',{'class':'tts_head'})
for title22 in title_list22:
    print(title22.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 23
driver.find_element_by_xpath('//*[@id="section_life"]/div[2]/div/ul/li[3]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list23=soup.find_all('h3',{'class':'tts_head'})
for title23 in title_list23:
    print(title23.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 24
driver.find_element_by_xpath('//*[@id="section_life"]/div[2]/div/ul/li[4]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list24=soup.find_all('h3',{'class':'tts_head'})
for title24 in title_list24:
    print(title24.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 25
driver.find_element_by_xpath('//*[@id="section_life"]/div[2]/div/ul/li[5]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list25=soup.find_all('h3',{'class':'tts_head'})
for title25 in title_list25:
    print(title25.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 26
driver.find_element_by_xpath('//*[@id="section_world"]/div[2]/div/ul/li[1]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list26=soup.find_all('h3',{'class':'tts_head'})
for title26 in title_list26:
    print(title26.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 27
driver.find_element_by_xpath('//*[@id="section_world"]/div[2]/div/ul/li[2]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list27=soup.find_all('h3',{'class':'tts_head'})
for title27 in title_list27:
    print(title27.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 28
driver.find_element_by_xpath('//*[@id="section_world"]/div[2]/div/ul/li[3]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list28=soup.find_all('h3',{'class':'tts_head'})
for title28 in title_list28:
    print(title28.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 29
driver.find_element_by_xpath('//*[@id="section_world"]/div[2]/div/ul/li[4]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list29=soup.find_all('h3',{'class':'tts_head'})
for title29 in title_list29:
    print(title29.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 30
driver.find_element_by_xpath('//*[@id="section_world"]/div[2]/div/ul/li[5]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list30=soup.find_all('h3',{'class':'tts_head'})
for title30 in title_list30:
    print(title30.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 31
driver.find_element_by_xpath('//*[@id="section_it"]/div[2]/div/ul/li[1]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list31=soup.find_all('h3',{'class':'tts_head'})
for title31 in title_list31:
    print(title31.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 32
driver.find_element_by_xpath('//*[@id="section_it"]/div[2]/div/ul/li[2]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list32=soup.find_all('h3',{'class':'tts_head'})
for title32 in title_list32:
    print(title32.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 33
driver.find_element_by_xpath('//*[@id="section_it"]/div[2]/div/ul/li[3]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list33=soup.find_all('h3',{'class':'tts_head'})
for title33 in title_list33:
    print(title33.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 34
driver.find_element_by_xpath('//*[@id="section_it"]/div[2]/div/ul/li[4]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list34=soup.find_all('h3',{'class':'tts_head'})
for title34 in title_list34:
    print(title34.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 35
driver.find_element_by_xpath('//*[@id="section_it"]/div[2]/div/ul/li[5]/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list35=soup.find_all('h3',{'class':'tts_head'})
for title35 in title_list35:
    print(title35.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 36
driver.find_element_by_xpath('//*[@id="section_politics"]/div[2]/dl/dd/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list36=soup.find_all('h3',{'class':'tts_head'})
for title36 in title_list36:
    print(title36.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 37
driver.find_element_by_xpath('//*[@id="section_economy"]/div[2]/dl/dd/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list37=soup.find_all('h3',{'class':'tts_head'})
for title37 in title_list37:
    print(title37.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 38
driver.find_element_by_xpath('//*[@id="section_society"]/div[2]/dl/dd/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list38=soup.find_all('h3',{'class':'tts_head'})
for title38 in title_list38:
    print(title38.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 39
driver.find_element_by_xpath('//*[@id="section_life"]/div[2]/dl/dd/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list39=soup.find_all('h3',{'class':'tts_head'})
for title39 in title_list39:
    print(title39.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 40
driver.find_element_by_xpath('//*[@id="section_world"]/div[2]/dl/dd/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list40=soup.find_all('h3',{'class':'tts_head'})
for title40 in title_list40:
    print(title40.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

#article 41
driver.find_element_by_xpath('//*[@id="section_it"]/div[2]/dl/dd/a').click()
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list41=soup.find_all('h3',{'class':'tts_head'})
for title41 in title_list41:
    print(title41.text)
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[1]/a/span').click()

# 변수 할당 (완전 직관적, 쉽게 할 수 있는 방법을 찾아야 한다...)
driver.quit()
a1=title1.text
a2=title2.text
a3=title3.text
a4=title4.text
a5=title5.text
a6=title6.text
a7=title7.text
a8=title8.text
a9=title9.text
a10=title10.text
a11=title11.text
a12=title12.text
a13=title13.text
a14=title14.text
a15=title15.text
a16=title16.text
a17=title17.text
a18=title18.text
a19=title19.text
a20=title20.text
a21=title21.text
a22=title22.text
a23=title23.text
a24=title24.text
a25=title25.text
a26=title26.text
a27=title27.text
a28=title28.text
a29=title29.text
a30=title30.text
a31=title31.text
a32=title32.text
a33=title33.text
a34=title34.text
a35=title35.text
a36=title36.text
a37=title37.text
a38=title38.text
a39=title39.text
a40=title40.text
a41=title41.text
article_Head_title=[a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27+a28+a29+a30+a31+a32+a33+a34+a35+a36+a37+a38+a39+a40+a41]
print(article_Head_title)

#워드 클라우드 실행
with open('article_title.txt', 'a', encoding="utf8") as f:
    for item in article_Head_title:
        f.write(item)


from konlpy.tag import Hannanum
from collections import Counter
import pytagcloud
f = open("../crawler/article_title.txt", "r", encoding="UTF-8")
description = f.read()
h = Hannanum()
nouns = h.nouns(description)
count = Counter(nouns)
print(count)

tag = count.most_common(200)
tag_list = pytagcloud.make_tags(tag, maxsize=50)
pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(900, 600), fontname='Korean',rectangular=False)
import webbrowser
webbrowser.open('word_cloud.jpg')
# for title in title_list:
#     print(title.text)


