from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import datetime

pages = [] 

def getLinks(pageUrl):
    global pages 
    html = urlopen("https://www.teu.ac.jp" + pageUrl)
    soup = BeautifulSoup(html.read(), "html.parser")
    for link in soup.find("div", {"class":"mainarea"}).find_all("a", href = re.compile("^(/gakucyou/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href'] 
                #print(newPage)
                pages.append(newPage)
                getLinks(newPage)
               
def serchLinks():
    year = [i for i in range(2011, datetime.now().year)]
    for i in range(9):
        url = "/gakucyou/" + str(year[i]) + "/index.html"
        getLinks(url)
serchLinks()

#print(pages)



