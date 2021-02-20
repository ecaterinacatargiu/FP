class Client:

    def __init__(self, clientID, name):
        self._clientID  = clientID
        self._name = name

    def __str__(self):
        return "ClientId: " + str(self._clientID) + ", Name: " + str(self._name)

    def __repr__(self):
        return str(self)

    @property
    #ClientID getter
    def getClientID(self):
        return self._clientID

    @property
    #Name getter
    def getName(self):
        return self._name

    #@name.setter
    #Name setter
    def setName(self, newName):
        self._name = newName

