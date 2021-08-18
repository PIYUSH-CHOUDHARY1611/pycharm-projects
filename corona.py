import requests
from bs4 import BeautifulSoup

import urllib.request

url1="https://en.wikipedia.org/wiki/Harvard_University"
source=urllib.request.urlopen(url1).read()

soup = BeautifulSoup(source, 'html.parser')
c=soup.table['class']
e=soup.find_all('class')
#d=c.get('class')
print(e)
