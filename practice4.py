from selenium import webdriver
from bs4 import BeautifulSoup

driver_path = '../resources/chromedriver'  # driver path
url = 'http://100.daum.net/'
descriptions = []
browser = webdriver.Chrome(executable_path=driver_path)  # Chrome driver
browser.get(url)
soup = BeautifulSoup(browser.page_source, "html.parser")

for link in soup.find_all('strong', {'class': 'tit_hotissues'}):
    ranking_url = link.a['href']
    browser.get('http://100.daum.net/'+ranking_url)
    dict = BeautifulSoup(browser.page_source, "html.parser")
    descriptions.append(dict.find('p',{'class':'desc_section fst'}))
browser.quit()
print(descriptions)

print(len(descriptions))

with open('dictionary.txt', 'a', encoding="utf8") as f:
    for item in descriptions:
        f.write(str(item))

from konlpy.tag import Hannanum
from collections import Counter
import pytagcloud
f = open("../crawler/dictionary.txt", "r", encoding="UTF-8")
description = f.read()
h = Hannanum()
nouns = h.nouns(description)
count = Counter(nouns)
print(count)

tag = count.most_common(50)
tag_list = pytagcloud.make_tags(tag, maxsize=100)
pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(900, 600), fontname='Korean',rectangular=False)
import webbrowser
webbrowser.open('word_cloud.jpg')