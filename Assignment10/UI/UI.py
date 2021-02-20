from Entities.Square import *
from Entities.Board import *
from Entities.Game import Game


class UI:
    def __init__(self, board, game, lines, columns, option):
        self.__board = board
        self.__game = game
        self.__lines = lines
        self.__columns = columns
        self.__option = option

    @staticmethod
    def Menu():
        while True:
            try:
                size = input("Please enter the wanted size of the table:")
                lines = int(size[0:size.find(',')])
                columns = int(size[size.find(',') + 1:])
                break
            except ValueError:
                print("Invalid size!")

        if size.find(',') == -1:
            print("Invalid size. Please use coma.")
            size = input("Please enter the wanted size of the table:")


        o = input("Press 1 if you want to start or 2 if you want your computer to start")
        while o != '1' and o != '2':
            print("Please enter 1 or 2")
            o = input("Press 1 if you want to start or 2 if you want the computer to start")
        return [lines, columns, o]


    def Start(self):
        ok = 0
        computer = 1
        if self.__option == "2":
            print("Computer moved first!")
        c = 0  # c is a contor
        square = Square(0, 0)
        while not self.__board.gameWon(self.__lines, self.__columns):  # cat timp inca nu e castigat jocul

            if self.__option == "2":
                if self.__lines % 2 == 1 and self.__columns % 2 == 1:
                    if computer != 0:
                        c = c + 1
                        #self.__game.moveComputer(square, self.__lines, self.__columns, c)
                        self.__game.runAIPlayer(self.__lines, self.__columns)
                else:
                    if computer != 0:
                        c = c + 1
                        #self.__game.moveRandom(self.__lines, self.__columns)
                        self.__game.runAIPlayer(self.__lines, self.__columns)
                print(self.__board)

                if not self.__board.gameWon(self.__lines, self.__columns):

                    while self.__board.gameWon(self.__lines, self.__columns) == False:
                        try:
                            sizeP = input("Please enter the move you want to make on the table")
                            line = int(sizeP[0:sizeP.find(',')])
                            col = int(sizeP[sizeP.find(',') + 1:])
                            break
                        except ValueError:
                            print("Invalid data!")

                    try:
                        square = Square(line, col)
                        self.__game.moveHuman(square, self.__lines, self.__columns)
                        computer = 1
                        ok = 1
                    except ValueError as ve:
                        computer = 0
                        print(ve)
            else:
                print(self.__board)
                while True:
                    try:
                        sizeP = input("Please enter the move you want to make on the table")
                        line = int(sizeP[0:sizeP.find(',')])
                        col = int(sizeP[sizeP.find(',') + 1:])
                        break
                    except ValueError:
                        print("Invalid data!")

                try:
                    square = Square(line, col)
                    self.__game.moveHuman(square, self.__lines, self.__columns)
                    computer = 1
                    ok = 1
                except ValueError as ve:
                    computer = 0
                    print(ve)

                if computer != 0 and self.__board.gameWon(self.__lines, self.__columns) == False:
                    c = c + 1
                    #self.__game.moveRandom(self.__lines, self.__columns)
                    self.__game.runAIPlayer(self.__lines, self.__columns)
                    ok = 0


        print(self.__board)
        if ok == 0:
            print("Computer won!")
        else:
            print("You won!")
