# import os
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

tag = soup.find_all(name="tr", class_="athing")

my_list = []

for info in tag:
    article_id = info.get("id")
    score_id = "score_" + str(article_id)
    print(article_id)

    article_text=info.find(name="span", class_="titleline").text
    article_link=info.find(name="span", class_="titleline").find("a").get('href')
    my_id = 0
    try:
        my_id=int((soup.find(name="span", class_="score", id=score_id).text).split(" ")[0])


    except:

        print("error")

    print(my_id)
    my_list.append([my_id, article_text, article_link])
my_list.sort(key=lambda x: x[0], reverse=True)
print(my_list)
# for info in tag:
#     print(info.find(name="a").text)
#     print(info.find("a").get('href'))
#     print("---------------------------------------------------")





# # import xml
# file_path = "website.html"
#
# if os.path.exists(file_path) and os.path.isfile(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#
# soup = BeautifulSoup(content, 'html.parser')
# all_anchor_tags = soup.find_all(name='a')
#
# company_url=soup.select_one(selector="#name")
#
# headings=soup.select(".heading")
# print(headings)
#
# print(company_url)