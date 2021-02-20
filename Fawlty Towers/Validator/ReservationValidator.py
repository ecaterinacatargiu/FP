from Domain.Reservation import Reservation
from datetime import *


class ReservationValidator:

    def validate(self, reservation):

        errors = []
        if isinstance(reservation, Reservation) == False:
            raise TypeError("Inexisting reservation!")
        if len(reservation.getFamilyName()) == 0:
            errors.append("Invalid family name!")

        if len(str(reservation.getID()))!=4:
            raise ValueError("Invalid ID!")
            #errors.append("Invalid ID!")

        if int(reservation.getNrGuests()) <1 or int(reservation.getNrGuests()) >4:
            errors.append("Invalid number of guests!")

        #if isinstance(reservation.getArrival(), datetime.date) == False:
            #errors.append(("Invalid arrival time!"))

        #if isinstance(reservation.getDeparture(), datetime.date) == False:
            #errors.append(("Invalid departure time!"))

        if len(errors)!=0:
            raise ValueError(errors)

