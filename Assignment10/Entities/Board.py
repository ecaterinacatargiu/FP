from texttable import Texttable
from random import choice
from copy import deepcopy
from Entities.GameException import *
from Entities.Square import *



class Board():

    """Board representation - repository"""

    def __init__(self, lines, columns):

        self.__data = []
        for i in range(0, lines):
            self.__data.append([])
            for j in range(0, columns):
                self.__data[i].append(" ")

    def getData(self):
        return self.__data


    def __str__(self):
        printS = " "
        for i in range(0, len(self.__data)):
            table = self.__data[i]
            if i>0:
                for j in range(0, len(table)):
                    printS += '----'
            printS += '\n'
            for k in range(0, len(table)):
                printS += " "
                printS += self.__data[i][k]
                if k < len(table)-1:
                    printS += ' |'
            printS += '\n'

        return printS


    def Move(self, square, sign, lines, columns):
        """Function that checks the validity of the move and if the move  is posible, it makes it.
        Input: square(the move itself), sign(meaning X or O), lines and columns.7
        Output: - (raise Error, eventually)"""

        if sign not in ['X','O']:
            raise GameException("Invalid sign! You have to use X or O!")

        """ here put X or O on board """

        if 1 <= square.getLine() <= lines and 1 <= square.getCol() <= columns: #here we check the move to be inside the board
            if self.__data[square.getLine()-1][square.getCol()-1] == " ": #here we check if the position is not occupied yet
                self.__data[square.getLine()-1][square.getCol()-1] = sign

                """here we fill all the heighbours with * """

                if 1<= square.getLine() -1 <=lines and 1<=square.getCol()-1 <=columns:
                    self.__data[square.getLine()-2][square.getCol()-2] = "*"

                if 1<= square.getLine() -1 <=lines and 1<=square.getCol() <=columns:
                    self.__data[square.getLine()-2][square.getCol()-1] = "*"

                if 1<= square.getLine() -1 <=lines and 1<=square.getCol()+1 <=columns:
                    self.__data[square.getLine()-2][square.getCol()] = "*"

                if 1<= square.getLine()<=lines and 1<=square.getCol()-1 <=columns:
                    self.__data[square.getLine()-1][square.getCol()-2] = "*"

                if 1<= square.getLine()<=lines and 1<=square.getCol()+1 <=columns:
                    self.__data[square.getLine()-1][square.getCol()] = "*"

                if 1<= square.getLine() +1 <=lines and 1<=square.getCol()-1 <=columns:
                    self.__data[square.getLine()][square.getCol()-2] = "*"

                if 1<= square.getLine() +1 <=lines and 1<=square.getCol()<=columns:
                    self.__data[square.getLine()][square.getCol()-1] = "*"

                if 1<= square.getLine() +1 <=lines and 1<=square.getCol()+1 <=columns:
                    self.__data[square.getLine()][square.getCol()] = "*"

            else:
                raise ValueError("Invalid position!")
        else:
            raise ValueError("your move is out of the board!")


    def moveToWin(self, lines, columns):
        """A function that checks if the computer can make a move or nto.
        We make a copy of the board here, in rder to test is it is a winning move or not
        Input: lines and columns.
        Output: the move or false otherwise"""

        moveToWin = Square(-1,-1)
        emptySquaresL = Board.emptySquares(self, lines, columns)
        try1 = deepcopy(self.__data)
        for move in emptySquaresL:
            Board.Move(self, move, 'O', lines, columns)
            if Board.gameWon(self, lines, columns):
                moveToWin = move
                break
            self.__data = deepcopy(try1)

        self.__data = deepcopy(try1)
        if moveToWin.getLine() !=-1 and moveToWin.getCol() != -1:
            return moveToWin
        else:
            return False


    def gameWon(self, lines, columns):
        """Function that checks if the game was won or not.
        Input: lines, columns
        Output: True or False"""

        for i in range(0, lines):
            for j in range(0, columns):
                if self.__data[i][j] == " ":
                    return False
        return True

    def getSquare(self, line, column):
            return self.__data[line][column]



    def emptySquares(self, lines, columns):
        """Random function that returns a list of empty squares"""

        """for i in range(0, lines):
            for j in range(0, columns):
                if self.__data[i][j]== " ":
                    return Square(i+1, j+1)"""

        return [Square(i+1, j+1) for i in range(0, lines) for j in range(0, columns) if self.__data[i][j] == " "]




#b = Board(8,8)
#print(b)