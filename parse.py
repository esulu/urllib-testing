# urllib library parse test
# program made by Eren Sulutas

from urllib.parse import urlparse


def print_link(link):
    print("\nscheme: {} \nnetloc: {} \npath: {} \nparams: {} \nquery: {} \nfragment: {}"
          .format(link.scheme, link.netloc, link.path, link.params, link.query, link.fragment))


# link to the Wikipedia main page
print_link(urlparse('https://en.wikipedia.org/wiki/Main_Page'))
