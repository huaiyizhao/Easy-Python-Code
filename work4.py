import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url - ')
counts = input('Enter counts - ')
position = input('Enter position - ')
for i in range(int(counts)):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[int(position) - 1].get('href', None)
    if i == int(counts) - 1:
        print(tags[int(position) - 1].contents[0])
