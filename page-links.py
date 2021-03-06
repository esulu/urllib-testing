# urllib test
# attempt to retrieve every link on a web page
# adds the links to a set and prints them

import urllib.request
import re

link = urllib.request.urlopen('https://en.wikipedia.org/wiki/Main_Page')
source = str(link.read())  # converts the sources from bytes to String

links = set()
regex = re.compile('(?:a href=("/wiki/[^:]*?"))')
path_list = regex.findall(source)

# iterates through every element
for i in path_list:
    links.add('https://en.wikipedia.org' + i.split("\"")[1])  # adds the link, where i.split(...) is the specific article

links.discard(link.geturl())  # removes all links that refer to the start page
# note: .discard() doesn't raise an error if the item dne, unlike .remove()

print(links)
