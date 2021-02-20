'''
Created on Jan 20, 2019

@author: Korina
'''
from Battleships.Board import BoardError, Board
from random import randint, choice


class Game:
    def __init__(self):
        self.__user_board = Board()
        self.__computer_board = Board()
        
        
    def enough_ships(self):
        return self.__user_board.count_ships()

    def show_user_board(self):
        return self.__user_board.cheat()
    def show_computer_board(self):
        return str(self.__computer_board)
    
    def show_cheat(self):
        return self.__computer_board.cheat()
        
    def place_user_ship(self, coord):
        self.__user_board.place_ship(coord)
        
    def place_comp_ships(self):
        
        
        
        decode = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f"}
        
        h = [["a","b","c"],["b","c","d"],["c","d","e"],["d","e","f"]]
        v = [[0,1,2],[1,2,3],[2,3,4],[3,4,5]]
        ch = choice([1,2])
        if ch == 1:
            col = choice(h)
            line = str(choice(range(6)))
            coord = str(col[0])+line+str(col[1])+line+str(col[2])+line
            
        elif ch == 2:
            line = choice(v)
            col = str(decode[choice(range(6))])
            coord = col+str(line[0])+col+str(line[1])+col+str(line[2])
        
        while not(self.__computer_board.validate_placement(coord)):
        
            ch = choice([1,2])
            if ch == 1:
                col = choice(h)
                line = str(choice(range(6)))
                coord = str(col[0])+line+str(col[1])+line+str(col[2])+line
            elif ch == 2:
                line = choice(v)
                col = str(decode[choice(range(6))])
                coord = col+str(line[0])+col+str(line[1])+col+str(line[2])
                
        self.__computer_board.place_ship(coord)
        
    def game_won(self, player):
        if player == "computer":
            if self.__user_board.is_win():
                return True
        elif self.__computer_board.is_win():
            return True
        return False
        
    def user_attack(self, cl):
        return self.__computer_board.attack(cl)
        
    def computer_attack(self):
        
        cl = choice(["a","b","c","d","e","f"])+str(choice(range(6)))
        return self.__user_board.attack(cl)
            
        
        