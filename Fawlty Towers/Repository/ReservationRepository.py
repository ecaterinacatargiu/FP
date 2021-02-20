from Domain.Reservation import Reservation

class ReservationRepository:

    def __init__(self):
        self.__reservations = []
        self.loadFromFile()


    def addReservation(self, reservation):
        self.__reservations.append(reservation)


    def deleteReservation(self, ID):
        n=0
        for r in self.__reservations:
            if r.getID() == ID:
                n+=1
        if (n==0):
            raise ValueError("The reservation doesn't exist.")

        for r in self.__reservations:
            if r.getID == ID:
                self.__reservations.remove(r)
        return self.__reservations


    def listReservations(self):
        for r in range(0, len(self.__reservations)):
            print(r)

    def getAll(self):
        return self.__reservations


    def loadFromFile(self, fileName="Reservations.txt"):
        f = open(fileName, "r")
        content = f.read()
        content = content.split('\n')
        print(content)
        for line in f:
            line = line.split(",")
            if len(line)==2:
                s = Reservation(line[0], line[1])
            else:
                s = Reservation(line[0], line[1], line[2], line[3], line[4], line[5])
            self.__reservations.append(s)

        f.close()
