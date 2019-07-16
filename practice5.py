from selenium import webdriver
from bs4 import BeautifulSoup
from konlpy.tag import Hannanum
from collections import Counter
import pytagcloud  # Add fonts supporting Korean

driver_path = '../resources/chromedriver'  # driver path
url = 'https://book.naver.com/'

descriptions = []

browser = webdriver.Chrome(executable_path=driver_path)  # Chrome driver
browser.get(url)
soup = BeautifulSoup(browser.page_source, "html.parser")
######
link = soup.find('li',{'class':'depth3'})
ranking_url = link.a['href']
browser.get("https://book.naver.com/"+ranking_url)
soup_ranking = BeautifulSoup(browser.page_source, "html.parser")
#####
# for i in range(0,7):
#     page=soup_ranking.find_all('span',{'class':'blind'})
#     book0 = page.find_all('a',{'onclick':'return selectPage'+'('+str(i)+')'})
#
for j in range(0,25):
    book1=soup_ranking.find_all('dt',{'id':'book_title_'+str(j)})
    for book in book1:
        book_url = book.a['href']
        browser.get(book_url)
        book_desc = BeautifulSoup(browser.page_source, "html.parser")
        descriptions.append(book_desc.find('meta',{'property':'og:description'})['content'])
browser.quit()
print(len(descriptions))
with open('description.txt','a',encoding="utf8") as f:
    for item in descriptions:
        f.write(item)

f = open("description.txt", "r", encoding="UTF-8")
description = f.read()

h = Hannanum()
nouns = h.nouns(description)
count = Counter(nouns)
print(count)

tag = count.most_common(150)
tag_list = pytagcloud.make_tags(tag, maxsize=100)
pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(900, 600), fontname='Korean', rectangular=False)

import webbrowser
webbrowser.open('word_cloud.jpg')