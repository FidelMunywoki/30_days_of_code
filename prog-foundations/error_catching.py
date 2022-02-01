"""Tyring to Download a webpage that doesn't exist"""

import urllib.request

try:
    webpage = urllib.request.urlopen('http://www.g00gle.com')

except:
    print("Wepage doesn't exist")

else:

    for line in webpage:
        print(line)