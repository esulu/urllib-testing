# urllib library parse test
# program made by Eren Sulutas

from urllib.parse import urlparse


def print_link(link):
    print("\nscheme: {} \nnetloc: {} \npath: {} \nparams: {} \nquery: {} \nfragment: {}"
          .format(link.scheme, link.netloc, link.path, link.params, link.query, link.fragment))


# link to the Wikipedia main page
print_link(urlparse('https://en.wikipedia.org/wiki/Main_Page'))

# link to a random Wikipedia page
print_link(urlparse('https://en.wikipedia.org/wiki/Special:Random'))

# link to an amazon item page
print_link(urlparse('https://www.amazon.ca/Star-Wars-Black-Skywalker-Lightsaber/dp/B017KIQOSQ/ref=lp_11992409011_1_13?srs=11992409011&ie=UTF8&qid=1556476876&sr=8-13'))

# link to an amazon item through a search
print_link(urlparse('https://www.amazon.ca/Black-OBI-Wan-Kenobi-Force-Lightsaber/dp/B07C7JKWST/ref=sr_1_6?keywords=black+series+lightsaber&qid=1556476935&s=gateway&sr=8-6'))
