import re


def get_coord(url):
    regex = r'https://www.google.pl/maps/place/(.*)/@([0-9\.]+),([0-9\.]+),([0-9\.]+)z'
    print(re.search(regex, url).groups())
