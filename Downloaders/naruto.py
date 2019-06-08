import sys
from urllib.request import urlopen, Request, quote
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from selenium import webdriver
import requests


def progress(count, total, status):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def download(file_name, url):
    href = urljoin(url, quote(file_name))
    try:
        # create response object
        r = requests.get(href, stream=True)
        total = r.headers['Content-length']
        total = int(total)
        x = total / (1024 * 1024)
        print("Size = %d MB" % x)
        print(
            "Enter path of folder(in format /x/y/z/) where you want to place the file (Leave empty to download in "
            "current directory)")
        file_path = ""
        file_path = input()
        file_path = file_path + file_name
        # download started
        size = 0
        status = "Downloading file:" + (file_name)
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    size += 1024 * 1024
                    f.write(chunk)
                    progress(size, total, status)

        print("%s downloaded!\n" % (file_name))
    except:
        print('failed to download')


def main():
    url = "https://www.animeland.us/naruto-shippuden-episode-1-english-dubbed"
    driver = webdriver.Firefox()
    driver.get(url)
    for a in  driver.find_elements_by_tag_name('a'):
        print(a.get_attribute('href'))
    # scraper = cfscrape.create_scraper()
    # html = scraper.get(url).content
    # print(html)
    # soup = BeautifulSoup(html, "html.parser")
    # lis = soup.find_all('a')
    # for link in lis:
    #     print(link.string)
    # download(file_name, url)


if __name__ == '__main__':
    main()
