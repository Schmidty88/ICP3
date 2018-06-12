import urllib.request
from bs4 import BeautifulSoup
import os

link = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#this is how we find the table
source = urllib.request.urlopen(link)
plain_text = source
soup = BeautifulSoup(plain_text, "html.parser")
body = soup.find('table', {'class': 'wikitable sortable plainrowheaders'})
table_row = body.find_all('tr')

#this is finding rows in the
for tr in table_row:
    td = tr.find_all('th')
    th = tr.find_all('th')
    print(td)
    print(th)


#this is printing title of the page
print(soup.title.string)

#this is printing all tags
print(soup.find_all('a'))

#finding the href
for url in soup.find_all('a'):
    print(url.get('href'))