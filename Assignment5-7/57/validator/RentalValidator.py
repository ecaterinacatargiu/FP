from domain.Rental import Rental
from datetime import date
from validator.ValidatorException import ValidatorException


class RentalValidator:

    def rentalvalidate(self, rental):
        if isinstance(rental, Rental) == False:
            raise TypeError("Not a rental!")
        errors = []
        now = date(2000, 1, 1)
        if rental.rd < now:
            errors.append("Rental cannot start in the past!")
        if len(rental) < 1:
            errors.append("Rental must last at least 1 day!")
        if len(errors) !=0:
            raise ValidatorException(errors)

