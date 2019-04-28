# urllib library request test
# program made by Eren Sulutas

import urllib.request


link = urllib.request.urlopen('https://en.wikipedia.org/wiki/Main_Page')

'''print(link.geturl())
print(link.info())'''

# prints the html of the said web page
print(link.read())


# further testing however with an object of type Request this time
obj = urllib.request.Request(url='https://en.wikipedia.org/wiki/Main_Page',
                             data=b'This is the main page of Wikipedia')

link2 = urllib.request.urlopen(obj)

# prints the html of the web page as done in line 13, however formats it as well this time
print(link2.read().decode('utf-8'))


link3 = urllib.request.urlopen('https://en.wikipedia.org/wiki/Special:Random')

# prints the link of a random Wikipedia page (note the difference between the request and parse for this)
print(link3.geturl())
