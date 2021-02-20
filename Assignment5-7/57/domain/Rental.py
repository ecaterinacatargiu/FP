class Rental:

    def __init__(self, rentalID, bookID, clientID, rd, dd, retd):
        """rd = rented date, dd = due date, retd = returned date"""
        self._rentalID = rentalID
        self._bookID = bookID
        self._clientID = clientID
        self._rd = rd
        self._dd = dd
        self._retd = retd

    def __eq__(self, other):
        return self._rentalID == other.getRentalID and self._bookID == other.getBookID and\
               self._clientID == other.getClientID and self._rd == other.getrd and\
               self._dd == other.getdd and self._retd == other.getretd

    def __str__(self):
        if self._retd != None:
            return "RentalID: " + str(self._rentalID) + ", BookID: " + str(self._bookID) + ", ClientID: " + str(self._clientID) + ", Rented date: " + self._rd.strftime('%Y-%m-%d') + ", Due date: " + self._dd.strftime('%Y-%m-%d') + ", Returned date: " + self._retd.strftime('%Y-%m-%d')
        return "RentalID: " + str(self._rentalID) + ", BookID: " + str(self._bookID) + ", ClientID: " + str(self._clientID) + ", Rented date: " + self._rd.strftime('%Y-%m-%d') + ", Due date: " + self._dd.strftime('%Y-%m-%d')

    @property
    def getRentalID(self):
        return self._rentalID

    @property
    def getBookID(self):
        return self._bookID

    #bookID setter
    def setBookID(self, newBookID):
        self._bookID = newBookID

    @property
    def getClientID(self):
        return self._clientID

    #clientID setter
    def setClientID(self, newClientID):
        self._clientID = newClientID

    @property
    def getrd(self):
        return self._rd

    def setrd(self, newrd):
        self._rd = newrd

    @property
    def getdd(self):
        return self._dd

    def setdd(self, newdd):
        self._dd = newdd

    @property
    def getretd(self):
        return self._retd

    def setretd(self, newretd):
        self._retd = newretd




