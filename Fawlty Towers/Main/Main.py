from Repository.ReservationRepository import *
from Controller.ReservationController import *
from UI.ReservationUI import *
from Validator.ReservationValidator import *
from datetime import *


def PrintMenu():
    print("You have the following options: ")
    print("1.Add a reservation")
    print("2.List all reservations")
    print("3.Delete a reservation")
    print("4.Show available rooms")
    print("5.Monthly report")
    print("6.Day of week report")

valid = ReservationValidator()

repoReservation = ReservationRepository()
reservationCtrl = ReservationController(valid,repoReservation)
uiReservation = ReservationUI(reservationCtrl)

uiReservation.listReservations()


def Start():
    PrintMenu()
    while True:
        option = int(input("Enter your option: "))
        if option ==1:
            uiReservation.addReservationUI()
        elif option ==2:
            uiReservation.listReservations()
        elif option ==3:
            uiReservation.removeReservationUI()
        else:
            print("Invalid command")

Start()
