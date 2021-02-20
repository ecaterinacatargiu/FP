from repository.RentalRepository import *
from domain.Book import *
import pickle

class RentalPickleFileRepo(RentalRepository):

    def __init__(self,fileName="rentals.pickle"):
        self._fileName=fileName
        RentalRepository.__init__(self)
        self.readBinaryFile(self._fileName)


    def addRental(self,other):
        RentalRepository.addRental(self,other)
        self._saveFile()

    def removeRental(self,clientID):
        RentalRepository.removeRental(self,clientID)
        self._saveFile()

    def _saveFile(self):
        """f = open(self._fileName, "wb")
        list=RentalRepository.getAll(self)
        for c in list:
            pickle.dump(c,f)
        f.close()"""

        f = open(self._fileName, "wb")
        print("here")
        pickle.dump(self._rentals, f)
        f.close()


    def readBinaryFile(self,fileName):
        result = []
        with open(fileName, 'rb') as f:
            try:
                self._rentals = pickle.load(f)
            except EOFError:
                self._rentals = []
