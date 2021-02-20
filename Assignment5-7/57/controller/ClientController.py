from repository.ClientRepository import *
from validator.ClientValidator import *
from controller.UndoController import *


class ClientController:

    def __init__(self, repository, validator, RentalController, UndoController):
        self.__repository = repository
        self._RentalController = RentalController
        self._UndoController = UndoController
        self.__Validator = ClientValidator

    def create(self, clientID, name):
        newclient = Client(clientID, name)
        #self.__validator.validate(newclient)

        clientList = self.__repository.getAll()
        for client in clientList:
            if client.getClientID == clientID:
                raise ValueError("The ID must be unique")

        self.__repository.addClient(newclient)

        redo = FunctionCall(self.create, clientID, name)
        undo = FunctionCall(self.remove, clientID)
        oper = Operation(undo, redo)
        self._UndoController.add(oper)

        return newclient


    def remove(self, clientID):

        client = self.__repository.removeClient(clientID)
        bookID = None
        rentals = self._RentalController.filterRentals(client.getClientID)
        print(str(rentals))
        for rent in rentals:
            self._RentalController.removeRental(rent.getRentalID)

        undo = FunctionCall(self.create, client.getClientID, client.getName)
        redo = FunctionCall(self.remove, client.getClientID)
        oper = Operation(undo, redo)
        self._UndoController.add(oper)

        co = CascadeOperation()
        co.add(oper)

        for r in rentals:
            undo = FunctionCall(self._RentalController.createRental, r.getRentalID, r.getBookID, r.getClientID, r.getrd, r.getdd, r.getretd)
            redo = FunctionCall(self._RentalController.removeRental, r.getRentalID)
            oper = Operation(undo, redo)
            co.add(oper)
        self._UndoController.add(co)


    def update(self, client):
        oldclient = self.__repository.getClientByID(client.getClientID)
        undo = FunctionCall(self.update, oldclient)
        redo = FunctionCall(self.update, client)
        oper = Operation(undo, redo)
        self._UndoController.add(oper)

        return self.__repository.updateClient(client)

    def list(self):
        return self.__repository.listClients()

    def search(self, clientID):
        return self.__repository.searchClient(clientID)

    def getAllCtrl(self):
        return self.__repository.getAll()

