import sys

from urllib.request import urlopen, urlretrieve, quote
from urllib.parse import urljoin
import requests
import json

URL = 'https://api.lyrics.ovh/v1/'


def fetchLyrics():
    print(artist)
    print(name)
    href = URL + quote(artist) + '/' + quote(name)
    try:
        print(href)
        # create response object
        r = requests.get(href, stream=True)
        total = r.headers['Content-length']
        content = json.loads(r.content.decode('UTF-8'))

        print(content["lyrics"])
    except:
        print('failed to fetch lyrics')


if __name__ == '__main__':
    print("Enter artist name")
    artist = input()

    print("Enter official song name")
    name = input()

    fetchLyrics()
