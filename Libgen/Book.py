class Book:
    def __init__(self, bookId, author, title, publisher, language, size, extension):
        self.bookId = bookId
        self.author = author
        self.title = title
        self.publisher = publisher
        self.language = language
        self.size = size
        self.extension = extension
        self.bookUrl = ""

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

    def getBookUrl(self):
        return self.bookUrl

    def setBookUrl(self, url):
        self.bookUrl = url
