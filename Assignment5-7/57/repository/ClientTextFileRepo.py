from repository.ClientRepository import *
from repository.RepositoryException import *
from domain.Client import *


class ClientTextFileRepo(ClientRepository):

    def __init__(self, fileName="clients.txt"):
        ClientRepository.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, obj):
        ClientRepository.addClient(self, obj)
        self._saveFile()

    def remove(self, objID):
        ClientRepository.removeClient(self, objID)
        self._saveFile()

    def update(self, obj):
        ClientRepository.updateClient(self, obj)
        self._saveFile()


    def _saveFile(self):
        try:
            f = open(self._fileName, "w")
            for s in ClientRepository.getAll(self):
                f.write(str(s.getClientID) + "," + str(s.getName))
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
                client = Client(int(tok[0]), tok[1])
                ClientRepository.addClient(self, client)
                s = f.readline()
        except Exception as e:
            raise RepositoryError("The file cannot be open")
        finally:
            f.close()





