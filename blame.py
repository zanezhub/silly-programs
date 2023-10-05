from requests import get
from bs4 import BeautifulSoup
import os

num = 66
while num < 70:
    req = get(f"https://blame-manga.com/manga/blame-chapter-{num}").text

    if num <= 9:
        dir = "0" + str(num)
        os.mkdir(dir)
        os.chdir(dir)

    else:
        dir = str(num)
        os.mkdir(dir)
        os.chdir(dir)


    r = BeautifulSoup(req, features="html.parser")
    for link in r.find_all('meta'):
        page = link.get('content')
        if str(page).startswith("https://blo"):
            with open('urls.txt', 'a') as file:
                file.write(page + "\n")

    os.chdir("..") 
    num = num + 1 