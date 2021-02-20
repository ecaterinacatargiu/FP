from Entities.Board import *
from Entities.GameException import *
from Entities.Game import *
from Entities.Square import *
import unittest
from copy import deepcopy


class Tests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        self.lines = 5
        self.columns = 5
        self.testBoard = Board(7,7)
        self.board = Board(self.lines, self.columns)

        self.game = Game(self.board)

        self.square1 = Square(2,2)
        self.square2 = Square(3,4)
        self.square3 = Square(6,6)


    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def boaardTest(self):

        self.assertEquals(len(self.testBoard.emptySquares(3,3)), 7*7)
        self.assertEquals(len(self.board.emptySquares(self.lines, self.columns)), self.lines*self.columns)

        self.assertEquals(self.board.getSquare(2,2), " ")

        self.assertEquals(self.board.gameWon(self.lines, self.columns), False)

        self.board.Move(Square(self.lines, self.columns), "X", self.lines, self.columns)

        self.assertEquals(self.board.getSquare(2,3), 5)
        self.assertEquals(self.board.getSquare(1,2), "*")

        try:
            self.board.Move(Square(2,2), "X", 3,4)
            assert False
        except GameException as gex:
            self.assertEquals(str(gex), "Position taken!")

        self.board.Move(Square(2,2), "O", 3,4)
        self.assertEquals(self.board.getSquare(2,2), " ")

        self.assertEquals(len(self.board.emptySquares(2,2)), 3*4)
        self.assertEquals(self.board.getSquare(2,2), " ")

    def testObstruction(self):

        self.assertEquals(len(self.game.emptySquaresMinimax(self.board, self.lines, self.columns)), self.lines*self.columns)

        self.board.Move(Square(self.lines, self.columns), "X", self.lines, self.columns)
        self.assertEquals(len(self.game.emptySquaresMinimax(self.board, self.lines, self.columns)))

        try:
            self.board.Move(Square(self.lines, self.columns), "X", self.lines, self.columns)
            assert False
        except GameException as gex:
            self.assertEquals(str(gex), "Your move is outside the boardgame..")

        self.board.Move(Square(3,4),"X", 4,5)
        self.assertEquals(len(self.game.emptySquaresMinimax(self.board,3,4)), 9)

        self.board.Move(Square(4,4), "X", 4,4)

























