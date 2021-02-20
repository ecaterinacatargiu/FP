from domain.Book import Book
from repository.RepositoryException import *
from DataStructure.IterableStructure import *

class BookRepository:
    """Repository for storing domain objects"""

    def __init__(self):
        self._books = DataStructure()

    def __len__(self):
        return len(self._books)

    def addBook(self, book):
        if book in self._books:
            raise RepositoryError("The element already exists")
        self._books.append(book)
        #print(self._books)

    def removeBook(self, bookID):
        n=0
        for book in self._books:
            if book.getBookID == bookID:
                n+=1
        if(n==0):
            raise RepositoryError("The element does not exist!")
        i=0
        for book in self._books:
            if book.getBookID == bookID:
                rbook = self._books[i]
                del self._books[i]
            i+=1
        return rbook

    def updateBook(self, book):
        n = 0
        for book1 in self._books:
            id1 = book1.getBookID
            id2 = book.getBookID
            if id1 == id2:
                n += 1
        if (n == 0):
            raise RepositoryError("The element does not exist!")

        for book1 in self._books:
            id1 = book1.getBookID
            id2 = book.getBookID
            if id1 == id2:
                self.removeBook(id2)
                self.addBook(book)

    def listBooks(self):
        for i in range(len(self._books)):
            return i

    def searchBook(self, bookID):
        n = 0
        for book in self._books:
            if book.getBookID == bookID:
                n += 1
        if (n == 0):
            raise RepositoryError("The element does not exist!")

        for book in self._books:
            if book.getBookID == bookID:
                return book

    def getBookByID(self, bookID):
        n = 0
        for book in self._books:
            if book.getBookID == bookID:
                n += 1
        if (n == 0):
            raise RepositoryError("The element does not exist!")

        for book in self._books:
            if book.getBookID == bookID:
                return book

    def getAll(self):
        return self._books

    def store(self, book):
        self._books.append(book)

            



