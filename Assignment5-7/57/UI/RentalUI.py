from domain.Rental import Rental
from controller.RentalController import *
from repository.RentalRepository import *
from datetime import datetime


class RentalConsole():

    def __init__(self, _controller):
        self._controller = _controller

    def addRentalUI(self):
        rentalID = int(input("RentalID: "))
        bookID = int(input("BookID: "))
        clientID = int(input("ClientID: "))
        rd = input("Rented date: ")
        rd = datetime.strptime(rd, '%Y-%m-%d')
        dd = input("Due date: ")
        dd = datetime.strptime(dd, '%Y-%m-%d')
        retd = None
        r = Rental(rentalID, bookID, clientID, rd, dd, retd)
        self._controller.createRental(rentalID,bookID,clientID,rd,dd,retd)

    def ReturnBookUI(self):
        rentalID = int(input("RentalID: "))
        retd = input("Returned date: ")
        retd = datetime.strptime(retd, '%Y-%m-%d')
        self._controller.returnBook(rentalID, retd)



    def removeRentalUI(self):
        rentalID = int(input("RentalID: "))
        self._controller.removeRental(rentalID)

    def listRentalUI(self):
        for i in self._controller.getAllCtrl():
            print(i)

    def MostRentedBooksUI(self):
        self._controller.MostRentedBooks()

    def MostActiveClientsUI(self):
        self._controller.MostActiveClients()

    def MostRentedAuthorUI(self):
        self._controller.MostRentedAuthor()

    def LateRentalsUI(self):
        self._controller.LateRentals()
