from Game.Game import Game


class UI:

    def __init__(self, game):
        self._game = game

    def printBoard(self):
        print(str(self._game.board()))

    def Start(self):
        self.printBoard()
        while True:
            try:
                row = int(input("Enter row: "))
                col = int(input("Enter col: "))
                player = input("Type of player: ")
                self._game.moveHuman(row, col, player)
                if self._game.winChecker("X") == True:
                    self.printBoard()
                    print("CHAOS WON!!!")
                    break
                self._game.moveComputer()
                if self._game.winChecker("0") == True:
                    self.printBoard()
                    print("ORDER WON!!!!")
                    break
                self.printBoard()
            except Exception as error:
                print(error)

#x=chaos, 0-order