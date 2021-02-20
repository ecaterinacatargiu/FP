class Reservation:

    def __init__(self, ID, roomNr, familyName, nrGuests, arrival, departure):
        self._ID = ID
        self._roomNr = roomNr
        self._familyName = familyName
        self._nrGuests = nrGuests
        self._arrival = arrival
        self._departure = departure

    def __str__(self):
        return "Room ID:" + str(self._ID) + ", Room Number: " + str(self._roomNr) + ", Family Name: " + str(self._familyName) + ", Arrival Date: " + str(self._arrival) + ", Departure date: " +str(self._departure)

    def getID(self):
        return self._ID

    def getRoomNr(self):
        return  self._roomNr

    def setRoomNr(self, newRoomNr):
        self._roomNr = newRoomNr

    def getFamilyName(self):
        return self._familyName

    def setFamilyName(self, newFamilyName):
        self._familyName=newFamilyName

    def getNrGuests(self):
        return self._nrGuests

    def setNrGuests(self, newNrGuests):
        self._nrGuests = newNrGuests

    def getArrival(self):
        return self._arrival

    def setArrival(self, newArrival):
        self._arrival = newArrival

    def getDeparture(self):
        return self._departure

    def setDeparture(self, newDeparture):
        self._departure = newDeparture

