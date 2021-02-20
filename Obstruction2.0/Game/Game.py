from Board.Board import Board
import random

class Game:

    def __init__(self):
        self._board = Board()

    @property
    def board(self):
        return self._board

    def movePlayer(self,square):
        self._board.move(square,"O")

    def moveComputer(self):
        options = self._board.getEmptySquares()
        for square in options:
            c = self._board.bcopy()
            c.move(square,"X")
            if len(c.getEmptySquares())==0:
                self._board.move(square,"X")
                return

        move = random.choice(options)

        self._board.move(move,"X")





