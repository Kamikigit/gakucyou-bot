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
    years = [year for year in range(2020, datetime.now().year+1)]
    for year in years:
        url = "/gakucyou/" + str(year) + "/index.html"
        getLinks(url)
serchLinks()

#print(pages)



