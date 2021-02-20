from repository.BookRepository import *
from domain.Book import Book
from controller.UndoController import *



class BookController:

    def __init__(self, validator, repository, RentalController, UndoController):
        self.__validator = validator
        self.__repository = repository
        self.__UndoController = UndoController
        self.__RentalController = RentalController

    def create(self, bookID, title, description, author):
        newbook = Book(bookID, title, description, author)
        bookList = self.__repository.getAll()

        for book in bookList:
            if book.getBookID == bookID:
                raise ValueError("The ID must be unique!")
        redo = FunctionCall(self.create, bookID, title, description, author)
        undo = FunctionCall(self.remove, bookID)
        oper = Operation(undo, redo)
        self.__UndoController.add(oper)
        self.__repository.addBook(newbook)
        return newbook

    def add(self, bookID):
        return self.__repository.addBook(bookID)

    def remove(self, bookID):
        book = self.__repository.removeBook(bookID)
        bookID = None
        rentals = self.__RentalController.filterRentalsBook(book.getBookID)
        print(str(rentals))
        for rent in rentals:
            self.__RentalController.removeRental(rent.getRentalID)

        undo = FunctionCall(self.create, book.getBookID, book.getTitle, book.getDescription, book.getAuthor)
        redo = FunctionCall(self.remove, book.getBookID)
        oper = Operation(undo, redo)
        self.__UndoController.add(oper)

        co = CascadeOperation()
        co.add(oper)

        for r in rentals:
            undo = FunctionCall(self.__RentalController.createRental, r.getRentalID, r.getBookID, r.getClientID,r.getrd,r.getdd, r.getretd)
            redo = FunctionCall(self.__RentalController.removeRental, r.getRentalID)
            oper = Operation(undo, redo)
            co.add(oper)
        self.__UndoController.add(co)


    def update(self, book):
        oldbook = self.__repository.getBookByID(book.getBookID)
        undo = FunctionCall(self.update, oldbook)
        redo = FunctionCall(self.update, book)
        oper = Operation(undo, redo)
        self.__UndoController.add(oper)

        return self.__repository.updateBook(book)

    def list(self):
        return self.__repository.listBooks()

    def search(self, bookID):
        return self.__repository.searchBook(bookID)

    def getAllCtrl(self):
        return self.__repository.getAll()

