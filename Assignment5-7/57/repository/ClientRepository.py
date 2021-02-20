from domain.Client import Client
from repository.RepositoryException import *
from DataStructure.IterableStructure import *


class ClientRepository():
        """Repository for storing domain objects"""
        def __init__(self):
            self._clients = DataStructure()

        def __len__(self):
            return len(self._clients)

        def addClient(self, client):
            if client in self._clients:
                raise RepositoryError("The element already exists")
            self._clients.append(client)

        def removeClient(self, clientID):
            n = 0
            for client in self._clients:
                if client.getClientID == clientID:
                    n += 1
            if (n == 0):
                raise RepositoryError("The element does not exist!")
            i = 0
            rclient = None
            for client in self._clients:
                if client.getClientID == clientID:
                    #print("workk")
                    rclient = client
                    #print(rclient)
                    del self._clients[i]
                i += 1
            #print(rclient)
            return rclient

        def updateClient(self, client):
            n = 0
            for client1 in self._clients:
                id1 = client1.getClientID
                id2 = client.getClientID
                if id1 == id2:
                    n += 1
            if (n == 0):
                raise RepositoryError("The element does not exist!")

            for client1 in self._clients:
                id1 = client1.getClientID
                id2 = client.getClientID
                if id1 == id2:
                    self.removeClient(id2)
                    self.addClient(client)

        def listClients(self):
                for i in range(len(self._clients)):
                    return i
#

        def searchClient(self, clientID):
            n = 0
            for client in self._clients:
                if client.getClientID == clientID:
                    n += 1
            if (n == 0):
                raise RepositoryError("The element does not exist!")
            for client in self._clients:
                if client.getClientID == clientID:
                    print(client)

        def getClientByID(self, clientID):
            n = 0
            for client in self._clients:
                if client.getClientID == clientID:
                    n += 1
            if (n == 0):
                raise RepositoryError("The element does not exist!")
            for client in self._clients:
                if client.getClientID == clientID:
                    return client


        def getAll(self):
            return self._clients

        def store(self, client):
            self._clients.append(client)
