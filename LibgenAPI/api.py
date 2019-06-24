import json
import jsonpickle
import flask
from flask import request, jsonify
from urllib.parse import urlencode, urlparse, parse_qs
from bs4 import BeautifulSoup
import requests


class Book:
    def __init__(self, bookId, author, title, publisher, language, size, extension):
        self.bookId = bookId
        self.author = author
        self.title = title
        self.publisher = publisher
        self.language = language
        self.size = size
        self.extension = extension
        self.md5 = ""

    def getId(self):
        return self.bookId

    def getAuthor(self):
        return self.author

    def getTitle(self):
        return self.title

    def getPublisher(self):
        return self.publisher

    def getLanguage(self):
        return self.language

    def getSize(self):
        return self.size

    def getExtension(self):
        return self.extension

    def getMd5(self):
        return self.md5

    def setMd5(self, md5):
        self.md5 = md5


app = flask.Flask(__name__)
app.config["DEBUG"] = False


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
    return downloadUrl
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
        book.setMd5(md5[0])
        book = json.dumps(book, default=lambda o: o.__dict__)
        # book = jsonpickle.encode(book)
        listOfBooks.append(book)
    return listOfBooks


@app.route('/', methods=['GET'])
def home():
    return "<h1>Quick Access Libgen API</h1><p>This site is a prototype API for fetching download urls from libgen</p>"


@app.route('/books', methods=['GET'])
def api_id():
    if 'name' in request.args:
        bookName = (request.args['name'])
        print(bookName)
    else:
        return "Error: Please Enter a book name"

    # Create an empty list for our results
    results = fetchSearchResults(bookName)
    return jsonify(results)


@app.route('/books/url', methods=['GET'])
def api_url():
    if 'md5' in request.args:
        md5 = (request.args['md5'])
        print(md5)
    else:
        return "Error: Please enter valid "

    # Create an empty list for our results
    results = fetchBookUrl(md5)
    return jsonify(results)


if __name__ == '__main__':
    fetchSearchResults("Rich Dad")
    app.run(host="127.0.0.1", port=80)


# app.run()
