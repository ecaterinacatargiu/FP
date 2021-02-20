from domain.Rental import Rental
from repository.RepositoryException import *
from DataStructure.IterableStructure import *



class RentalRepository:
    """Repository for storing domain objects"""

    def __init__(self):
        self._rentals = DataStructure()

    def __str__(self):
        return len(self._rentals)

    def addRental(self, rental):
        #if rental in self._rentals:
         #   raise RepositoryError("The element already exists")
        self._rentals.append(rental)

    def removeRental(self, rentalID):
        #if rentalID not in self._rentals.getRentalID:
            #raise RepositoryError("The element does not exist!")
        i=0
        while i < len(self._rentals):
            if self._rentals[i].getRentalID == rentalID:
                del self._rentals[i]
            i += 1

    def returnBook(self, rental):
        for rent in self._rentals:
            if rent.getRentalID() == rental.getRentalID:
                rent = rental

    def listRentals(self):
        for i in range(len(self._rentals)):
            return i

    def getAll(self):
        return self._rentals

    def store(self, rental):
        self._rentals.append(rental)


    def prs(self):
        print("whts")