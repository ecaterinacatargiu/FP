class Square:

    """domain """

    def __init__(self, line, col):
        self.__line = line
        self.__col = col

    def getLine(self):
        return self.__line

    def getCol(self):
        return self.__col

    def __str__(self):
        return str(self.__line) + " " + str(self.__col)
