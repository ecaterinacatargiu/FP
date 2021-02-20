from repository.ClientRepository import *
from domain.Client import *
import pickle

class ClientPickleFileRepo(ClientRepository):

    def __init__(self,fileName="clients.pickle"):
        self._fileName=fileName
        ClientRepository.__init__(self)
        #self._loadBinaryFile(self._fileName)
        self.readBinaryFile(self._fileName)


    def addClient(self,other):
        ClientRepository.addClient(self,other)
        self._saveFile()

    def removeClient(self,clientID):
        client = ClientRepository.removeClient(self,clientID)
        self._saveFile()
        return client

    def updateClient(self,client):
        ClientRepository.updateClient(self, client)
        self._saveFile()

    def _saveFile(self):
        """f = open(self._fileName, "wb")
        list=ClientRepository.getAll(self)
        for c in list:
            pickle.dump(c,f)
        f.close()"""

        f = open(self._fileName, "wb")
        pickle.dump(self._clients, f)
        f.close()

    """def _loadBinaryFile(self,fileName):
        for c in self.readBinaryFile(fileName):
            self.add(c)"""

    def readBinaryFile(self,fileName):
        f = open(fileName, 'rb')

        try:
            self._clients = pickle.load(f)

        except EOFError:
            print("here")
            self._clients = []
        f.close()