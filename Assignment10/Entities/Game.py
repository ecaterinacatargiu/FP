from random import random
from Entities.Square import Square
from Entities.Board import *
from Entities.GameException import *
from Entities.GameException import *
from copy import deepcopy

class Game:
    """controller"""

    def __init__(self, board):
        self.__board = board


    def moveHuman(self, square, lines, columns):
        self.__board.Move(square, 'X', lines, columns)


    """def moveComputer(self, square, lines, columns, c):
        A function that makes a move for the computer, if the lines and columns are odd.
        Input: square,lines,columns, c(c means a contor)
        Output: -
        if c == 1:
            self.__board.Move(Square(lines //2 + 1, columns //2 +1), "O", lines, columns)
        else:
            self.__board.Move(Square(lines - square.getLine()+1, columns - square.getCol()+1), "O", lines, columns)


    def moveRandom(self, lines, columns):
        A function that makes the computers to move in the smartest way possible in order to win and if not, random.
        Input: lines, columns
        Output: -
        randomL = self.__board.emptySquares(lines, columns)
        if not self.__board.moveToWin(lines, columns):
            self.__board.Move(choice(randomL), "O", lines, columns)
        else:
            print(self.__board.moveToWin(lines, columns))
            self.__board.Move(self.__board.moveToWin(lines, columns), "O", lines, columns)"""


    def emptySquaresMinimax(self, board, line, column):
        emptySquares = []
        for i in range(0, line):
            for j in range(0, column):
                if board[i][j] == " ":
                    emptySquares.append([j, i])
        return emptySquares



    def minimaxAi(self, newBoard, player, depth, alpha, beta, lines, columns):
        emptySquares = self.emptySquaresMinimax(newBoard, lines, columns)
        if len(emptySquares) == 0:
            if player == 'ai':
                return [-1, -1, -10]#-1,-1 positie pe board are s anujexiste
            else:
                return [-1, -1, 10]

        if player == 'ai':
            bestScore = [-1, -1, -100]
            opponent = 'human'
            sign = "O"
            #opponent = playerList[indexOpponent]

        else:
            bestScore = [-1, -1, 100]
            opponent = 'ai'
            sign = "X"
            #opponent = playerList[indexOpponent]

        for position in emptySquares:
            x, y = position[0], position[1]
            newBoard[y][x] = sign
            directionX = [-1, 0, 1, 1, 1, 0, -1, -1]
            directionY = [-1, -1, -1, 0, 1, 1, 1, 0]
            obstruction = []
            for indexDirection in range(8):
                if x + directionX[indexDirection] in range(0, columns) \
                        and y + directionY[indexDirection] in range(0, lines):
                    if newBoard[y + directionY[indexDirection]][x + directionX[indexDirection]] == ' ':
                        newBoard[y + directionY[indexDirection]][x + directionX[indexDirection]] = '*'
                        obstruction.append([x + directionX[indexDirection], y + directionY[indexDirection]])

            score = self.minimaxAi(newBoard, opponent, depth + 1, alpha, beta, lines, columns)
            score[0], score[1] = x, y
            newBoard[y][x] = ' '
            directionX = [-1, 0, 1, 1, 1, 0, -1, -1]
            directionY = [-1, -1, -1, 0, 1, 1, 1, 0]
            for index in obstruction:
                newBoard[index[1]][index[0]] = ' '

            if player == 'ai':
                if score[2] > bestScore[2]:

                    bestScore = score
                    alpha = max([alpha, score[2]])
                    if alpha >= beta:
                        break
            elif score[2] < bestScore[2]:
                bestScore = score
                beta = min([beta, score[2]])
                if alpha >= beta:
                    break

        return bestScore


    def runAIPlayer(self, lines, columns):
        board = deepcopy(self.__board.getData())
        bestMove = self.minimaxAi(board, 'ai', 0, -100, 100, lines, columns)
        self.__board.Move(Square(bestMove[1]+1, bestMove[0]+1), 'O', lines, columns)
