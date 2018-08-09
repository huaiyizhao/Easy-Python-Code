from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])
print(sum)
