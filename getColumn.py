from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def scraping():
    url = "https://www.teu.ac.jp/gakucyou/2019.html?id=144"
   
    html = urlopen(url)

    soup = BeautifulSoup(html.read(), "html.parser")

    column_tag = soup.select_one(".mainbox.columntxt")
    column = column_tag.get_text("", strip=True)

    print(column)

for link in 

if __name__ == "__main__":
    scraping()
