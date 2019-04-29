# python link grabber
# made with Beautifulsoup 4.7.1 and urllib libraries
# program by Eren Sulutas
# python -m pip install beautifulsoup4

from bs4 import BeautifulSoup
import urllib.request
import re

html_page = urllib.request.urlopen('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(html_page)

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print(link.get('href'))
