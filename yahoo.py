# import requests
# from bs4 import BeautifulSoup
# query = "python"
# url = "http://in.search.yahoo.com/search?p=wwe"
# r = requests.get(url) 
# print(r.links)
# soup =  BeautifulSoup(r.content, 'html.parser')
# soup.find_all(attrs={"class": "yschttl"})

# for link in soup.find_all(attrs={"class": "yschttl"}):
#     print(link.get('href'))
#     print ("%s (%s)" %(link.text, link.get('href')))

from yahoo import search
for url in search("what does the fox say?"):
        print(url)