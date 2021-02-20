from controller.BookController import BookController
from repository.BookRepository import *


class BookConsole():

    def __init__(self, _controller):
        self._controller = _controller

    def addBookUI(self):
        bookID = int(input("BookID: "))
        title = input("Title: ")
        description = input("Description: ")
        author = input("Author: ")
        b = Book(bookID, title, description, author)
        self._controller.create(bookID, title, description, author)

    def removeBookUI(self):
        bookID = int(input("BookID: "))
        self._controller.remove(bookID)

    def updateBookUI(self):
        bookID = int(input("BookID: "))
        title = str(input("Title: "))
        description = str(input("Description: "))
        author = str(input("Author: "))
        book = Book(bookID, title, description, author)
        self._controller.update(book)

    def listBookUI(self):
        for book in self._controller.getAllCtrl():
            print(book)

    def searchBookUI(self):
        bookID = int(input("BookID: "))
        print(self._controller.search(bookID))


