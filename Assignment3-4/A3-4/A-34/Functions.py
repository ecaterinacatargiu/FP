from Validations import *
#from Tests import *
from UI1 import *


def TestInit(accountList):
    """Creates the list."""
    accountList.append([1, 300, 'out', 'shoes'])
    accountList.append([2, 100, 'out', 'fancy diner'])
    accountList.append([9, 2000, 'in', 'salary'])
    accountList.append([12, 500, 'in', 'salary'])
    accountList.append([12, 150, 'out', 'clothes'])
    accountList.append([12, 30, 'out', 'burger'])
    accountList.append([12, 250, 'in', 'project'])
    accountList.append([13, 100, 'in', 'rent'])
    accountList.append([15, 300, 'out', 'haircut'])
    accountList.append([15, 150, 'out', 'barber'])
    accountList.append([15, 50, 'in', 'games'])
    accountList.append([17, 75, 'out', 'groceries'])
    accountList.append([22, 3000, 'in', 'personal project'])
    accountList.append([24, 200, 'out', 'night out'])
    accountList.append([26, 25, 'out', 'food'])
    accountList.append([30, 900, 'out', 'clothes'])


import datetime

"""We import datetime for the add operations, in order to get the current day."""


"""Functions for the adding and inserting operations"""

# for the current day we will use:
import datetime


def Add(accountList, params):
    """A function that adds a new transaction  to the current day.
    Input: accountList - list of all transactions, params - list of parameters
    Output: accountList, modified."""
    AddValidation(accountList, params)
    value = params[0]
    typel = params[1]
    description = params[2]
    newList1 = []
    for i in range(0, len(accountList)):
        newList1.append(accountList[i][0])
    accountList.append([int("%s" % datetime.datetime.now().day), value, typel, description])
    BankAccount(accountList)


def AddUI(accountList, params):
    print(params)
    AddValidation(accountList, params)
    Add(accountList, params)


def Insert(accountList, params):
    """A function that inserts a new transaction on a certain day.
    Input: accountList - a list of all transactions, params - list of parametres
    Output: accountList, but modified"""
    InsertValidation(accountList, params)
    day = params[0]
    value = params[1]
    typel = params[2]
    description = params[3]
    newList2 = []
    for i in range(0, len(accountList)):
        newList2.append(accountList[i][0])
    accountList.append([day, value, typel, description])
    BankAccount(accountList)


def InsertUI(accountList, params):
    InsertValidation(accountList, params)
    Insert(accountList, params)


"""Functions for the remove operations"""


def RemoveD(accountList, params):
    """A function that removes all transactions from a certain day.
    Input: accountList - a list of all transactions, params - list of parametres
    Output: accountList, modified"""
    RemoveDValidation(accountList, params)
    indexday = []
    day = int(params[0])
    for i in range(0, len(accountList)):
        # print(accountList[i][0])
        if accountList[i][0] >= day:
            indexday.append(i)
    for i in range(0, len(indexday)):
        accountList.pop(indexday[i])
        accountList.insert(indexday[i], [0, 0, 0, 0])


def RemoveDUI(accountList, params):
    RemoveDValidation(accountList, params)
    RemoveD(accountList, params)


def RemoveBetween(accountList, params):
    """A function that removes all transactions between 2 certain days.
    Input: accountList - a list of all transactions, params - list of parametres
    Output: accountList, modified"""
    RemoveBetweenValidation(accountList, params)
    indexday2 = []
    startday = params[0]
    endday = params[2]
    for i in range(0, len(accountList)):
        if accountList[i][0] >= int(startday) and accountList[i][0] <= int(endday):
            indexday2.append(i)
    for i in range(0, len(indexday2)):
        accountList.pop(indexday2[i])
        accountList.insert(i, [0, 0, 0, 0])


def RemoveBetweenUI(accountList, params):
    RemoveBetweenValidation(accountList, params)
    RemoveBetween(accountList, params)


def RemoveT(accountList, params):
    """A function that removes all transactions with a certain type.
    Input: accountList - a list of all transactions, params - list of parametres
    Output: accountList, modified"""
    RemoveTValidation(accountList, params)
    indexday3 = []
    type1 = params[0]
    for i in range(0, len(accountList)):
        # print(accountList[i][2])
        if accountList[i][2] == type1:
            indexday3.append(i)
    for i in indexday3:
        accountList.pop(i)
        accountList.insert(i, [0, 0, 0, 0])
    # for i in accountList:
    # print(i)


def RemoveTValidation(accountList, params):
    if len(params) != 1:
        raise ValueError("The number of parameters is incorrect!Try again. ")


def RemoveTUI(accountList, params):
    RemoveTValidation(accountList, params)
    RemoveT(accountList, params)


def Replace(accountList, params):
    """A function that replaces the amount for a certain type transaction with a certain description with another one.
    Input: accountList - a list of all transactions, params - list of parametres
    Output: accountList, modified"""
    ReplaceValidation(accountList, params)
    type1 = params[1]
    description = params[2]
    value = int(params[4])
    day = int(params[0])
    for i in range(0, len(accountList)):
        if accountList[i][0] == day and accountList[i][2] == type1 and accountList[i][3] == description:
            accountList.pop(i)
            accountList.insert(i, [day, value, type1, description])
    BankAccount(accountList)


def ReplaceUI(accountList, params):
    ReplaceValidation(accountList, params)
    Replace(accountList, params)

"""Functions for writing operations"""


def writeList(accountList):
    """A function that writes the entire list of transactions.
    Input: accountList - a list of all transactions.
    Output: accountList"""
    # for i in accountList:
    # print (i)
    BankAccount(accountList)


def writeListType(accountList, params):
    """A function that writes the entire list of transactions with a certain type.
    Input: accountList - a list of all transactions, params - the list of all the parametres.
    Output: accountList"""
    writeListTypeValidation(accountList, params)
    typea = params[0]
    newList3 = []
    for i in range(0, len(accountList)):
        if accountList[i][2] == typea:
            newList3.append(accountList[i])
    # for i in newList3:
    # print (i)
    BankAccount(newList3)



def writeList1(accountList, params):
    """A function that writes all the transactions with a certain amount of money.
    Input: accountList - a list of all transactions, params - the list of parametres.
    Output: accountList"""
    writeList1Validation(accountList, params)
    value = int(params[1])
    newList4 = []
    sign = params[0]
    if sign == ">":
        for i in range(0, len(accountList)):
            if accountList[i][1] > value:
                newList4.append(accountList[i])
    elif sign == "<":
        for i in range(0, len(accountList)):
            if accountList[i][1] < value:
                newList4.append(accountList[i])
    elif sign == "=":
        for i in range(0, len(accountList)):
            if accountList[i][1] == value:
                newList4.append(accountList[i])
    # for i in newList4:
    # print(i)
    BankAccount(newList4)


def Balance(accountList, params):
    """A function that computes the account's balance on a certin day.
    Input: accountList - a list of all transactions, params - the list of parameters.
    Output: the balance on the requested day"""
    BalanceValidation(accountList, params)
    day = int(params[1])
    suma = 0
    suma2 = 0
    for i in range(0, len(accountList)):
        if accountList[i][2] == 'in':
            suma = suma + accountList[i][1]
        elif accountList[i][2] == 'out' and accountList[i][0] <= day:
            suma2 = suma2 + accountList[i][1]
    return (suma - suma2)



"""Functions for sum and max operations."""


def SumType(accountList, params):
    """A function that writes the sum from all the in/out transactions.
    Input: accountList - the list of all transactions, params - the list of parametres.
    Output: the total amount from the in/out transactions"""
    SumTypeValidation(accountList, params)
    typel = params[0]
    suma = 0
    for i in range(0, len(accountList)):
        if accountList[i][2] == typel:
            suma = suma + int(accountList[i][1])
    return (suma)


def SumTypeValidation(accountList, params):
    if len(params) != 1:
        raise ValueError("The number of parametres in incorrect.")


def MaxType(accountList, params):
    """A function that writes the maximum in/out transaction on a certain day.
    Input: accountList - the list of all transactions, params - the list of parametres.
    Output: the maximum in/out transaction on a certain day."""
    MaxTypeValidation(accountList, params)
    typel = params[0]
    day = params[1]
    maxim = 0
    for i in range(0, len(accountList)):
        if accountList[i][2] == typel and accountList[i][0] == int(day) and accountList[i][1] > maxim:
            maxim = accountList[i][1]
            return(maxim)
            return(accountList[i])




"""Functions for filtering operations."""


def Filter1(accountList, params):
    """A function that keeps only in/out transactions.
    Input: accountList - the list of all transactions, params - the list of parametres.
    Output: the list with only the in/out transactions"""
    Filter1Validation(accountList, params)
    typel = params[0]
    newList = []
    for i in range(0, len(accountList)):
        if accountList[i][2] == typel:
            newList.append(accountList[i])
    BankAccount(newList)



def Filter2(accountList, params):
    """A function that keeps only the in/out transactions having an amount of money smaller than a certain value.
    Input: accountList - the list of all transactions, params - the list of parametres.
    Output: the list with only the in/out transactions having an amount of money smaller than a certain value."""
    Filter2Validation(accountList, params)
    typel = params[0]
    value = params[1]
    newList9 = []
    for i in range(0, len(accountList)):
        # print(accountList[i])
        if accountList[i][2] == typel and accountList[i][1] < int(value):
            # print('Hello')
            newList9.append(accountList[i])
    BankAccount(newList9)



"""Function for the undo operation."""

def BackUp(accountList, back):
    back.append(accountList[:])


def Undo(accountList, back):
    """A function that makes the last operation that has modified the program data to be reversed.
    Input: accountList - the list of all transactions, params - the list of parametres.
    Output: the program data before the last operation"""
    if len(back) == 0:
        raise ValueError("Nothing to undo!")
    accountList[:]=back.pop()
    BankAccount(accountList)

