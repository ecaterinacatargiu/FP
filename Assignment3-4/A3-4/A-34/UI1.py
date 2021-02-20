from Functions import *
from Validations import *


def BankAccount(accountList):
    """Lists all the transactions in a prettier way."""
    i = 0
    while i < len(accountList):
        if i != 0 and accountList[i][0] != accountList[i - 1][0] or i == 0:
            print("Date: ", accountList[i][0])
        print("\t", "-", accountList[i][1], "RON", accountList[i][2], accountList[i][3])
        i += 1

def PrintCommands():
    """PrintS all the possible commands."""
    print()
    print("Your possible options are: ")
    print()
    print('\t', 'add <value> <type> <description>')
    print()
    print('\t', 'insert <day> <value> <type> <description>')
    print()
    print('\t', 'remove <day>')
    print()
    print('\t', 'remove <start day> to <end day>')
    print()
    print('\t', 'remove <type>')
    print()
    print('\t', 'replace <day> <type> <description> with <value>')
    print()
    print('\t', 'list')
    print()
    print('\t', 'list <type>')
    print()
    print('\t', 'list [ < | = | > ] <value>')
    print()
    print('\t', 'list balance <day>')
    print()
    print('\t', 'sum <type>')
    print()
    print('\t', 'max <type> <day>')
    print()
    print('\t', 'filter <type>')
    print()
    print('\t', 'filter <type> <value>')
    print()
    print('\t', 'undo')
    print()


def readCommand():
    """A function that reads and analize user commands.
    Input: -
    Output: a list [command, params], where command - user command and params - parameters"""
    userInput = input()
    if userInput.find(' ') == -1:
        return [userInput.lower(), []]
    while userInput.find(' ') == 0:
        userInput[1:]
    command = userInput[0:userInput.find(' ')].lower()
    params = userInput[userInput.find(' '):].split(' ')
    for i in range(0, len(params)):
        params[i] = params[i].strip().lower()
    params = params[1:]
    return [command.lower(), params]


def RemoveFunctionUI(accountList, params):
    if len(params) == 1:
        if params[0] == 'in' or params[0] == 'out':
            RemoveTUI(accountList, params)
            BankAccount(accountList)
        else:
            RemoveDUI(accountList, params)
            BankAccount(accountList)
    elif len(params) == 3:
        RemoveBetweenUI(accountList, params)
        BankAccount(accountList)


def WriteFunctionUI(accountList, params):
    if len(params) == 0:
        writeList(accountList)
    elif len(params) == 1:
        writeListType(accountList, params)
    elif len(params) == 2:
        if params[0] == 'balance':
            Balance(accountList, params)
        else:
            writeList1(accountList, params)


def Filter1FunctionUI(accountList, params):
    if len(params) == 1:
        Filter1(accountList, params)
    elif len(params) == 2:
        Filter2(accountList, params)

def Start():
    #TestAll()
    back = []
    accountList = []
    TestInit(accountList)
    BankAccount(accountList)
    PrintCommands()
    while True:
        command = readCommand()
        cmd = command[0]
        params = command[1]
        if cmd == 'add':
            BackUp(accountList, back)
            AddUI(accountList, params)
        elif cmd == 'insert':
            BackUp(accountList, back)
            InsertUI(accountList, params)
        elif cmd == 'remove':
            BackUp(accountList, back)
            if len(params) == 1:
                if params[0] == 'in' or params[0] == 'out':
                    RemoveTUI(accountList, params)
                    BankAccount(accountList)
                else:
                    RemoveDUI(accountList, params)
                    BankAccount(accountList)
            elif len(params) == 3:
                RemoveBetweenUI(accountList, params)
                BankAccount(accountList)
            #RemoveFunctionUI(accountList, params)
        elif cmd == 'replace':
            BackUp(accountList, back)
            ReplaceUI(accountList, params)
        elif cmd == 'list':
            BackUp(accountList, back)
            if len(params) == 0:
                writeList(accountList)
            elif len(params) == 1:
                writeListType(accountList, params)
            elif len(params) == 2:
                if params[0] == 'balance':
                    Balance(accountList, params)
                else:
                    writeList1(accountList, params)
            #WriteFunctionUI(accountList, params)
        elif cmd == 'sum':
            if len(params) == 1:
                BackUp(accountList, back)
                SumType(accountList, params)
        elif cmd == 'max':
            if len(params) == 2:
                BackUp(accountList, back)
                MaxType(accountList, params)
        elif cmd == 'filter':
            BackUp(accountList, back)
            if len(params) == 1:
                Filter1(accountList, params)
            elif len(params) == 2:
                Filter2(accountList, params)
            #FilterFunctionUI(accountList, params)
        elif cmd == 'undo':
            Undo(accountList, back)
        elif cmd == 'Exit':
            break


