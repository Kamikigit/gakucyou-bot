from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen( "https://www.teu.ac.jp/gakucyou/index.html")
soup = BeautifulSoup(html.read(), "html.parser")
for link in soup.find("ul", {"class":"detail"}).find_all("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])


