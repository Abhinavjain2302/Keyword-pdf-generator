import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.bing.com/search?q=wwe")
print(page)
soup = BeautifulSoup(page.content,"html.parser")
import re
links = soup.findAll("a")
for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    print(re.split(":(?=http)",link["href"].replace("/url?q=","")))