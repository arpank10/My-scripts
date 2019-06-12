from urllib.parse import urlencode, urlparse, parse_qs
from bs4 import BeautifulSoup
from Libgen.Book import Book
import requests

booksdescr = "http://booksdescr.org/ads.php?md5="
libgenrs = "http://library1.org/ads/"


def fetchBookUrl(md5):
    url = "http://booksdescr.org/ads.php?md5=" + md5
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all('a')
    downloadUrl = links[0]['href']
    print(downloadUrl)
    # print(soup.prettify())


def fetchSearchResults(bookName):
    baseUrl = "http://libgen.io/search.php?"
    params = {'req': bookName, 'open': 0, 'res': 25, 'view': 'simple', 'phrase': 1, 'column': 'def'}
    query = urlencode(params)
    requestUrl = baseUrl + query
    page = requests.get(requestUrl)
    soup = BeautifulSoup(page.text, "html.parser")
    tables = soup.find_all("table", class_="c")
    rows = tables[0].contents[1:][::2]
    listOfBooks = list()
    for row in rows:
        rowContent = row.contents[::2]
        book = Book(rowContent[0].text, rowContent[1].text, rowContent[2].text, rowContent[3].text, rowContent[6].text,
                    rowContent[7].text, rowContent[8].text)
        if rowContent[2].contents[0].has_attr('href'):
            bookUrl = rowContent[2].contents[0]['href']
            if bookUrl.startswith("search"):
                if rowContent[2].contents[1].has_attr('href'):
                    bookUrl = rowContent[2].contents[1]['href']
                else:
                    continue
        parsed = urlparse(bookUrl)
        md5 = parse_qs(parsed.query)['md5']
        book.setMd5(md5)
        listOfBooks.append(book)
        print("##################################################################")
        fetchBookUrl(md5[0])
        print("##################################################################")


if __name__ == '__main__':
    fetchSearchResults("Rich Dad")
