from Repository.ReservationRepository import ReservationRepository
from Domain.Reservation import Reservation
from Validator.ReservationValidator import ReservationValidator

class ReservationController():

    def __init__(self, validator,repository):
        self.__repository  = repository
        self.__validator = validator

    def createReservation(self, ID, roomNr, familyName, nrGuests, arrival, departure):
        newReservation = Reservation(ID, roomNr, familyName, nrGuests, arrival, departure)
        self.__validator.validate(newReservation)
        reservationList = self.__repository.getAll()

        for r in reservationList:
            if r.getID() == ID:
                raise ValueError("The ID must be unique!")

        self.__repository.addReservation(newReservation)
        return newReservation

    def add(self, ID):
        return self.__repository.addReservation(ID)

    def deleteR(self, ID):
        return self.__repository.deleteReservation(ID)


    def list(self):
        return self.__repository.listReservations()

    def getAllCtrl(self):
        return self.__repository.getAll()

