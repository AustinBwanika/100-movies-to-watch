import requests
from bs4 import BeautifulSoup
import html

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
title_check = soup.find_all(name="h3", class_="title")
# <h3 class="title">
#           52) Once Upon A Time In The West
#          </h3>


list_titles = []

for i in title_check:
    title = i.get_text()
    list_titles.append(html.unescape(str(title)))

list_titles.reverse()

with open("100_films.txt", "w") as file:
    for movie in list_titles:
        file.write(f"{movie}\n")

# print(soup.prettify())




