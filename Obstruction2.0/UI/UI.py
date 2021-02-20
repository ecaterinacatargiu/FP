from Game.Game import Game
from Square.Sqaure import Square



class UI():

    def __init__(self, game):
        self._game = game

    def printBoard(self):
        print(str(self._game.board()))

    def readMove(self):
        while True:
            try:
                row=int(input("Enter row: "))
                col = int(input("Enter col: "))
                return Square(row, col)
            except Exception as e:
                print(e)


    def Start(self):
        #self.printBoard()
        while True:
            #try:
                b = self._game.board
                print(b)
                move = self.readMove()
                self._game.movePlayer(move)

                if len(self._game.board.getEmptySquares()) == 0:
                    print(b)
                    print("You won!")
                    break
                self._game.moveComputer()
                if len(self._game.board.getEmptySquares()) == 0:
                    print(b)
                    print("Computer won!")
                    break

            #except Exception as e:
                #print(e)

