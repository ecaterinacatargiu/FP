from texttable import Texttable


class Board():

    def __init__(self):
        """Representation of the board"""
        self.__data = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]


    def __str__(self):
        t= Texttable()
        t.add_row([0,1,2,3,4,5])
        for i in range(0,6):
            list = []
            for j in range(0,6):
                list.append(self.__data[i][j])
            t.add_row(list)
        return t.draw()

    def getData(self):
        return self.__data

#b= Board()
#print(b)

