from Repository.ReservationRepository import *
from Controller.ReservationController import *
from random import random
from datetime import *

class ReservationUI():

    def __init__(self, controller):
        self._controler = controller

    def addReservationUI(self):
        ID = int(input("ID:"))
        roomNr = int(input("Room nr: "))
        familyName = input("Family name: ")
        nrGuests = int(input("Number gusts: "))
        arrival = input("Arrival date: ")
        arrival = datetime.strptime(arrival, '%Y-%m-%d')
        departure = input("Departure date: ")
        departure = datetime.strptime(departure, '%Y-%m-%d')

        reservation = Reservation(ID, roomNr, familyName, nrGuests, arrival, departure)
        self._controler.createReservation(ID, roomNr, familyName, nrGuests, arrival, departure)

    def removeReservationUI(self):
        ID = int(input("ID:"))
        self._controler.deleteR(ID)

    def listReservations(self):
        reservations = self._controler.getAllCtrl()
        for r in reservations:
            print(r)
