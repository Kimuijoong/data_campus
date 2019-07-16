from selenium import webdriver
from bs4 import BeautifulSoup
# from time import sleep

driver = webdriver.Chrome('C:\driver\chromedriver')  # driver path
driver.get('https://www.naver.com')
driver.find_element_by_xpath('//*[@id="news_cast"]/div[1]/ul/li[1]/a').click()
# driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').click()

html=driver.page_source
soup=BeautifulSoup(html,'lxml')
title_list1=soup.find_all('ul',{'class':'hdline_article_list'})
for title1 in title_list1:
    print(title1.text)

title_list2=soup.find_all('ul',{'class':'mlist2 no_bg'})
for title2 in title_list2:
    print(title2.text)

driver.quit()
a=title1.text
b=title2.text
article_title=[a+b]
print(article_title)
with open('article.txt', 'a', encoding="utf8") as f:
    for item in article_title:
        f.write(item)


from konlpy.tag import Hannanum
from collections import Counter
import pytagcloud
f = open("../crawler/article.txt", "r", encoding="UTF-8")
description = f.read()
h = Hannanum()
nouns = h.nouns(description)
count = Counter(nouns)
print(count)

tag = count.most_common(250)
tag_list = pytagcloud.make_tags(tag, maxsize=100)
pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(900, 600), fontname='Korean',rectangular=False)
import webbrowser
webbrowser.open('word_cloud.jpg')
# for title in title_list:
#     print(title.text)


