from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import getLink
import os

def scraping(url):
    html = urlopen("https://www.teu.ac.jp" + url)

    soup = BeautifulSoup(html.read(), "html.parser")

    column_tag = soup.find("div", {"class":"infoDetailBox01"}) or soup.find("div", {"class": "mainbox columntxt"})
    column = column_tag.get_text("", strip=True)
    print(column)

    file = open("column.txt", "a")
    file.write(column)
    file.close()

if __name__ == "__main__":
    os.remove("column.txt")
    for page in getLink.pages:
        scraping(page)


