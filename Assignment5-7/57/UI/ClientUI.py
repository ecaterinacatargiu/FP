from controller.ClientController import *
from repository.ClientRepository import *
from repository.ClientRepository import *
from domain.Client import *
from controller.ClientController import *


class ClientConsole():

    def __init__(self, _controller):
        self._controller = _controller

    def addClientUI(self):
        clientID = int(input("ClientID: "))
        name = input("Name: ")
        #c = Client(clientID, name)
        self._controller.create(clientID, name)

    def removeClientUI(self):
        clientID = int(input("ClientID: "))
        self._controller.remove(clientID)

    def updateClientUI(self):
        clientID = int(input("ClientID: "))
        name = input("Name: ")
        client = Client(clientID, name)
        self._controller.update(client)

       def listClientUI(self):
        clients = self._controller.getAllCtrl()
        for i in clients:
            print(i)

    def searchClientUI(self):
        clientID = int(input("ClientID: "))
        self._controller.search(clientID)


