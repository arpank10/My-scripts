from urllib.parse import urlencode
from bs4 import BeautifulSoup
from Libgen.Book import Book
import requests


def main():
    baseUrl = "http://libgen.io/search.php?"
    # val = input("Enter Book Name")
    val = "Rich Dad "
    params = {'req': val, 'open': 0, 'res': 25, 'view': 'simple', 'phrase': 1, 'column': 'def'}
    query = urlencode(params)
    requestUrl = baseUrl + query
    page = requests.get(requestUrl)
    soup = BeautifulSoup(page.text, "html.parser")
    # print(soup.prettify())
    tables = soup.find_all("table", class_="c")
    rows = tables[0].contents[1:][::2]
    listOfBooks = ""
    for row in rows:
        rowContent = row.contents[::2]
        book = Book(rowContent[0].text, rowContent[1].text, rowContent[2].text, rowContent[3].text, rowContent[6].text, rowContent[7].text, rowContent[8].text)
        bookUrl = "libgen.io/" + rowContent[2].contents[0]['href']
        book.setBookUrl(bookUrl)
        print("##################################################################")
        print("Id:" + book.getId())
        print("Author:" + book.getAuthor())
        print("Title:" + book.getTitle())
        print("Publisher:" + book.getPublisher())
        print("Language:" + book.getLanguage())
        print("Size:" + book.getSize())
        print("Extension:" + book.getExtension())
        # print(book.getId())
        # print(book.getAuthor())
        # print(book.getTitle())
        # print(book.getPublisher())
        # print(book.getLanguage())
        # print(book.getSize())
        # print(book.getExtension())
        print("##################################################################")
    # print(table.contents)
    # for table in tables :
    #     table.find_all
    # print(table)


if __name__ == '__main__':
    main()
