from domain.BookRentalException import BookRentalException
from validator.RentalValidator import *
from domain.Book import *
from domain.Client import *
from repository.RentalRepository import *
from domain.Rental import *
from datetime import datetime
from datetime import date
from repository.BookRepository import *
from DataStructure.CombSort import *
from controller.UndoController import *



class RentalController:

    def __init__(self, repositoryRental, repositoryBooks, repositoryClient, UndoController):
        self.__repositoryRental = repositoryRental
        self.__repositoryBooks = repositoryBooks
        self.__repositoryClient = repositoryClient
        self.__filterValue = None
        self.__UndoController = UndoController


    def createRental(self, rentalID, bookID, clientID, rd, dd, retd):
        rental = Rental(rentalID, bookID, clientID, rd, dd, retd)
        self.__repositoryRental.addRental(rental)
        rentals = self.__repositoryRental.getAll()

        """for rent in rentals:
            if rent.getRentalID == rentalID:
                raise ValueError("The ID must be unique!")"""

        redo = FunctionCall(self.createRental, rentalID, bookID, clientID, rd, dd, retd)
        undo = FunctionCall(self.removeRental, rentalID)
        oper = Operation(undo, redo)
        self.__UndoController.add(oper)
        self.__repositoryRental.addRental(rental)

        return rental


    def returnBook(self, rentalID, retd):
        rent = self.isBookRented(rentalID)
        if rent.getretd == None:
            rent.setretd(retd)


    def removeRental(self, rentalID):

        rentList =  self.__repositoryRental.getAll()

        for rent in rentList:
            self.__repositoryRental.removeRental(rentalID)

        undo = FunctionCall(self.createRental, rent.getRentalID, rent.getBookID, rent.getClientID, rent.getrd, rent.getdd, rent.getretd)
        redo = FunctionCall(self.removeRental, rent.getBookID)
        oper = Operation(undo, redo)
        self.__UndoController.add(oper)

    def isBookAvailable(self, bookID, rd, dd):
        """Check the availability of the given book to be rented in the provided time period
            bookID - The availability of this car is verified
            rd, dd - The time span. The book is available if it is not rented in this time span
            Return True if the book is available, False otherwise"""
        self.__filterValue = bookID
        rentals = self.filterFunction(self.__repositoryRental.getAll(),self.acceptanceFunctionRentals)
        for rent in rentals:
            if str(rd) < str(rent.getdd) and str(dd) > str(rent.getrd):
                return False
        return True


    def isBookRented(self, rentalID):
        rentals = self.__repositoryRental.getAll()
        for rent in rentals:
            #print(rent.getRentalID)
            #print(rentalID)
            if rent.getRentalID == rentalID:
                print(rent)
                return rent


    def filterRentals(self, clientID):
        """Return a list of rentals performed by the provided client for the provided book
        clientID - The client performing the rental. None means all clients
        bookID - The rented car. None means all books"""
        results = []
        for rentals in self.__repositoryRental.getAll():
            if rentals.getClientID == clientID:
                results.append(rentals)
        return results

    def filterRentalsBook(self, bookID):
        """Return a list of rentals performed by the provided client for the provided book
        clientID - The client performing the rental. None means all clients
        bookID - The rented car. None means all books"""
        results = []
        for rentals in self.__repositoryRental.getAll():
            if rentals.getBookID == bookID:
                results.append(rentals)
        return results


    def acceptanceFunctionRentals(self, rental, cmp=None):
        if cmp == None:
            cmp = self.__filterValue
        if rental.getBookID == cmp:
            return True
        return False

    def filterFunction(listToBeFiltered, acceptanceFunction):
        intermediateList = listToBeFiltered[:]
        index = 0
        while index < len(intermediateList):
            if not acceptanceFunction(intermediateList[index]):
                del intermediateList[index]
            else:
                index = index + 1
        return intermediateList



    def getAllCtrl(self):
        return self.__repositoryRental.getAll()



    def combSort(self,input,function):
        gap = len(input)
        swaps = True
        while gap > 1 or swaps:
            gap = max(1, int(gap / 1.25))  # minimum gap is 1
            swaps = False
            for i in range(len(input) - gap):
                j = i + gap
                if function(input[i],input[j]):
                    input[i], input[j] = input[j], input[i]
                    swaps = True
        return input

    def sortDescending(self,firstValue,secondValue):
        if firstValue[1]<secondValue[1]:
            return True
        return False

    def MostRentedBooks(self):
        """This will provide the list of books, sorted in descending order of the
number of times they were rented or the number of days they were rented"""
        mostRentedBooks = [] #a list with the most rented books
        nr=0
        for book in self.__repositoryBooks.getAll():
            for rent in self.__repositoryRental.getAll():
                if book.getBookID == rent.getBookID:
                    nr += 1
            if nr != 0:
                mostRentedBooks.append([book, nr])
            nr=0
        self.combSort(mostRentedBooks,self.sortDescending)
        #mostRentedBooks.sort(key=lambda x: x[1], reverse=True)

        for i in range(0, len(mostRentedBooks)):
            print(mostRentedBooks[i])
            print()
        #print(mostRentedBooks)

    def sortActive(self,fvalue,svalue):
        return fvalue[2]<svalue[2]

    def MostActiveClients(self):
        """This will provide the list of clients, sorted in descending order of the
number of book rental days they have (e.g. having 2 rented books for 3 days each counts
as 2 x 3 = 6 days)."""
        mostActiveClients = []
        nr=0
        for client in self.__repositoryClient.getAll():
            for rent in self.__repositoryRental.getAll():
                if client.getClientID == rent.getClientID:
                    nr += 1
            if nr!=0:
                mostActiveClients.append([client, "Number of rentals: ", nr])
            nr=0

        mostActiveClients = self.combSort(mostActiveClients,self.sortActive)
        #mostActiveClients.sort(key=lambda x: x[1], reverse=True)
        for i in range(0, len(mostActiveClients)):
            print(mostActiveClients[i])
            print()
        #print(mostActiveClients)


    def MostRentedAuthor(self):
        """This provides the list of book authored, sorted in descending order
of the total number of rentals their books have"""
        mostRentedAuthor = []
        nr = 0
        for book in self.__repositoryBooks.getAll():
            for rent in self.__repositoryRental.getAll():
                if book.getBookID == rent.getBookID:
                    nr += 1
            if nr!=0:
                mostRentedAuthor.append([book.getAuthor, "Number of rentals:", nr])
            nr=0

        self.combSort(mostRentedAuthor,self.sortActive)
        #mostRentedAuthor.sort(key=lambda x: x[1], reverse=True)
        for i in range(0, len(mostRentedAuthor)):
            print(mostRentedAuthor[i])
            print()
        #print(mostRentedAuthor)

    def SortLate(self,fv, sv):
        return fv[3]<sv[3]

    def LateRentals(self):
        """All the books that are currently rented, for which the due date for return
        has passed, sorted in descending order of the number of days of delay"""
        today = date.today()
        LateRentals = []
        for rent in self.__repositoryRental.getAll():
            if str(rent.getdd) > str(today):
                dif = rent.getdd-today
                dif = dif.days
                LateRentals.append(["BookID: ",rent.getBookID, "Delay days:", dif])

        self.combSort(LateRentals,self.SortLate)
        #LateRentals.sort(key=lambda x: x[1], reverse=True)
        for i in range(0, len(LateRentals)):
            print(LateRentals[i])
            print()
        #print(LateRentals)










