from texttable import Texttable
from Square.Sqaure import Square
import copy
from copy import deepcopy
from Game.GameException import GameException

class Board():

    def __init__(self):
        """representation of the board"""
        self.__data = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]

    def getData(self):
        return self.__data

    def getEmptySquares(self):
        """Creates a list with all the empty squares on the list"""
        res = []
        for i in self.__data:
            for j in i:
                if j == " ":
                    res.append(Square(self.__data.index(i), i.index(j)))
        return res


    def move(self, square, symbol):
        """Validates one move, puts it into the board and mers the heighbours of the square
        input: square and symbol x or o, ouput: --"""

        if square.row not in range(6) or square.col not in range(6):
            raise GameException("Move outside the board!")

        #if symbol not in ["X", "O"]:
            #raise GameException("Use X or 0")

        d = self.__data

        if d[square.row][square.col] != " ":
            raise GameException("Square already taken!")

        x=square.row
        y=square.col
        n=[(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

        for position in n:
            if position[0] in range(len(d)) and position[1] in range(len(d[0])):
                if d[position[0]][position[1]] == " " and position[0] in range(6) and position[1] in range(6):
                    d[position[0]][position[1]] = "~"


    def bcopy(self):
        """Creates a copy of the board"""
        b = Board
        b.__data = copy.deepcopy(self.__data)

        return b

    def content(self,square):
        """shows the content of a sqaure and that is X or 0"""
        return self.__data[square.row][square.col]


    def __str__(self):
        t = Texttable()
        t.add_row([" ",0,1,2,3,4,5])
        for i in range(0,6):
            list = []
            list.append(i)
            for obj in self.__data[i]:
                list.append(obj)
            t.add_row(list)
        return t.draw()


#b = Board()
#print(b)
