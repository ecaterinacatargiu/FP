from repository.RentalRepository import *
from repository.RepositoryException import *
from domain.Rental import *
from datetime import datetime

class RentalTextFileRepo(RentalRepository):

    def __init__(self, fileName="rentals.txt"):
        RentalRepository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, obj):
        RentalRepository.addRental(self, obj)
        self._saveFile()

    def remove(self, objID):
        RentalRepository.removeRental(self, objID)
        self._saveFile()


    def _saveFile(self):
        try:
            f = open(self._fileName, "w")
            for s in RentalRepository.getAll(self):
                f.write(str(s.getRentalID) + "," + str(s.getBoookID) + "," + str(s.getClientID) + "," + str(s.getrd) + "," + str(s.dd) + "," + str(s.retd))
        except Exception as e:
            raise RepositoryError("The file cannot be open")
        finally:
            f.close()

    def _loadFile(self):
        try:
            #self._fileName = "D:\\INFO2018-2019\\~INFO\\FP\\Assignments\\AICIASS5-7\\57\\repository\\" + self._fileName
            f = open(self._fileName, "r")
            s = f.readline()
            while len(s) > 1:
                tok = s.split(",")
                if len(tok) == 6:
                    rental = Rental(int(tok[0]), int(tok[1]), int(tok[2]), datetime.strptime(tok[3], '%Y-%m-%d'), datetime.strptime(tok[4], '%Y-%m-%d'), datetime.strptime(tok[5], '%Y-%m-%d'))
                    RentalRepository.addRental(self, rental)

                """if len(tok) == 5:
                    rental = Rental(int(tok[0]), int(tok[1]), int(tok[2]), datetime.strptime(tok[3], '%Y-%m-%d'), datetime.strptime(tok[4], '%Y-%m-%d'),None)
                    RentalRepository.addRental(self, rental)"""
                s = f.readline().strip()
        except Exception as e:
            raise RepositoryError("The file cannot be open")
        finally:
            f.close()

