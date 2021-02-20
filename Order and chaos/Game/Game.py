from Board.Board import Board
import random

class Game:

    def __init__(self):
        self._board = Board()

    def board(self):
        return self._board

    def moveHuman(self, row, col,player):
        data = self._board.getData()
        if data[row][col] == " ":
            data[row][col] = player
        else:
            raise ValueError("Invalid move")


    def moveComputer(self):
        data = self._board.getData()
        ok = False
        while ok == False:
            row = random.randint(0,5)
            col = random.randint(0,5)
            player = random.choice(["X","0"])
            if data[row][col] == " ":
                data[row][col] = player
                ok = True
                if ok == True:
                    break


    def winChecker(self,player):
        data = self._board.getData()
        #orizontal
        for i in range(0,6):
            if data[i][0] == player and data[i][1] == player and data[i][2] == player and data[i][3] == player and data[i][4] == player:
                return True
            if data[i][1] == player and data[i][2] == player and data[i][3] == player and data[i][4] == player and data[i][5] == player:
                return True

        #vertical
        for j in range(0,6):
            if data[0][j] == player and data[1][j] == player and data[2][j] == player and data[3][j] == player and data[4][j] == player:
                return True
            if data[1][j] == player and data[2][j] == player and data[3][j] == player and data[4][j] == player and data[5][j] == player:
                return True


        #diagonal
        for i in range(0,5):
            for j in range(0,5):
                if data[i][j] == player and data[i+1][j+1] == player and data[i+2][j+2] == player and data[i+3][j+3] == player and data[i+4][j+4] == player:
                    return True

        for i in range(1,5):
            for j in range(0,4):
                if data[i][j] == player and data[i-1][j-1] == player and data[i-2][j-2] == player and data[i-3][j-3] == player and data[i-4][j-4] == player:
                    return True
        return False



