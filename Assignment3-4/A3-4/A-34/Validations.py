from Functions import *

from UI1 import *


def AddValidation(accountList, params):
    """A function that verifies if the parametres given for the "Add" function command are valid.
    Input: accountList, params.
    Output: calls the Add function after verifing and finding its parametres"""
    if len(params) != 3:
        raise ValueError("The number of parameters is incorrect!Try again.")
    elif int(params[0]) < 0:
        raise ValueError("The amount of money cannot be a negative number. ")


def InsertValidation(accountList, params):
    """A function that verifies if the paramtres given for the "Insert" function are valid.
    Input: accountList - the list of all transactions, params - the list of parametres
    Output: call the Insert function after verifing and finding its parametres."""
    if len(params) != 4:
        raise ValueError("The number of parameters is incorrect!Try again. ")
    elif int(params[0]) < 0 or int(params[0]) > 30:
        raise ValueError("The day doesn't exist!")


def RemoveDValidation(accountList, params):
    if len(params) != 1:
        raise ValueError("The number of parameters is incorrect!Try again. ")
    elif int(params[0]) < 0 or int(params[0]) > 30:
        raise ValueError("The day doesn't exist!")


def RemoveBetweenValidation(accountList, params):
    if len(params) != 3:
        raise ValueError("The number of parameters is incorrect!Try again. ")
    elif (int(params[0]) < 0 or int(params[0]) > 30) or (int(params[2]) < 0 or int(params[2]) > 30):
        raise ValueError("The day doesn't exist!")


def RemoveTValidation(accountList, params):
    if len(params) != 1:
        raise ValueError("The number of parameters is incorrect!Try again. ")


def ReplaceValidation(accountList, params):
    if len(params) != 5:
        raise ValueError("The number of parameters is incorrect!Try again. ")
    elif int(params[0]) < 0 or int(params[0]) > 30:
        raise ValueError("The day doesn't exist!")
    elif int(params[4]) < 0:
        raise ValueError("You can't have a negative amount of money.")

def writeListTypeValidation(accountList, params):
    if len(params) != 1:
        raise ValueError("The number of parametres is incorrect.")


def writeList1Validation(accountList, params):
    if len(params) != 2:
        raise ValueError("The number of parametres is incorrect.")
    elif int(params[1]) < 0:
        raise ValueError("You cannot have a negative amount of money.")


def BalanceValidation(accountList, params):
    if len(params) != 2:
        raise ValueError("The number of parametres is incorrect.")
    elif int(params[1]) < 0 or int(params[1]) > 30:
        raise ValueError("The day doesn't exist!")


def SumTypeValidation(accountList, params):
    if len(params) != 1:
        raise ValueError("The number of parametres in incorrect.")


def MaxTypeValidation(accountList, params):
    if len(params) != 2:
        raise ValueError("The number of parametres is incorrect.")
    elif int(params[1]) < 0 or int(params[1]) > 30:
        raise ValueError("The day doesn't exist!")


def Filter1Validation(accountList, params):
    if len(params) != 1:
        raise ValueError("The number of parametres is incorrect.")


def Filter2Validation(accountList, params):
    if len(params) != 2:
        raise ValueError("The number of parametres is incorrect.")
    elif int(params[1]) < 0:
        raise ValueError("You cannot have a negative amount of money!")

