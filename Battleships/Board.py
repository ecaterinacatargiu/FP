from texttable import Texttable


class BoardError(Exception):
    
    pass


class Board:
    def __init__(self):
        self.__data = []
        for i in range(6):
            self.__data.append([0]*6)
        
    def __str__(self):
        decode = {0:" ",1:" ",2:" ",-1:"o",3:"X"}
        d = self.__data
        t = Texttable()
        t.header([" "]+["A","B","C","D","E","F"])
        for i in range(6):
            t.add_row([i]+[decode[d[i][j]] for j in range(6)])
            
        return t.draw()
    
    def cheat(self):
        decode = {0:" ",1:"+",2:"+",-1:"o",3:"X"}
        d = self.__data
        t = Texttable()
        t.header([" "]+["A","B","C","D","E","F"])
        for i in range(6):
            t.add_row([i]+[decode[d[i][j]] for j in range(6)])
            
        return t.draw()
    
    def validate_placement(self, coord):
        decode = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5}
        c= [decode[coord[0]],decode[coord[2]],decode[coord[4]]]
        l = [int(coord[1]),int(coord[3]),int(coord[5])]
        
        for i in range(3):
            if self.__data[l[i]][c[i]] !=0:
                return False
            
        return True
            
    
    def __switch_nr_ships(self):
        """
        Switces the number of the ships on the board and deletes the first one 
        input: none
        output: the modified board
        """
        for i in range(6):
            for j in range(6):
                if self.__data[i][j] == 1:
                    self.__data[i][j] = 0
                if self.__data[i][j] == 2:
                    self.__data[i][j] = 1
                
    
    def count_ships(self):
        for i in range(6):
            if 2 in self.__data[i]:
                return True
        return False
    
    def place_ship(self, coord):
        """
        Places one battleship on the board
        input: coord - list of coordinates for the ship
        output: the modified board with the ship placed on the given coordinates
        
        """
        
        
        
        decode = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5}
        c= [decode[coord[0]],decode[coord[2]],decode[coord[4]]]
        l = [int(coord[1]),int(coord[3]),int(coord[5])]
        
        for col in c:
            if col<0 or col>5:
                raise BoardError("Ship placed outside the board!")
        for line in l:
            if line<0 or line>5:
                raise BoardError("Ship placed outside the board!")
            
        if not(c[0] == c[1] == c[2] or l[0] == l[1] == l[2]):
            raise BoardError("The ship should be on the same line or on the same column!")
            
        
            
        board_number = 1
        for i in range(6):
            if 1 in self.__data[i]:
                board_number = 2
            if 2 in self.__data[i]:
                self.__switch_nr_ships()
                board_number = 2
                break
            
        for i in range(3):
            if self.__data[l[i]][c[i]] !=0:
                raise BoardError("There is already a board on these coordinates!")
            
        
        for i in range(3):
            
            line = l[i]
            col = c[i]
#             print(line, col, board_number)
            self.__data[line][col] = board_number
            
    def attack(self,cl):
        decode = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5}
        line = int(cl[1])
        col =int(decode[cl[0]])
        
        if self.__data[line][col] == 1 or  self.__data[line][col] == 2:
            self.__data[line][col] = 3
            return " hits!"
        
        self.__data[line][col] = -1
        return " misses!"
            
    def is_win(self):
        for i in range(6):
#             for j in range(6):
            if 1 in self.__data[i] or 2 in self.__data[i]:
                return False
        return True
        
        
            
               
        
            
        
        
        
        
        
        
        
        
# b = Board()
# print(b)
# print(b.cheat())
# 
# b.place_ship("a0a1a2")
# print(b)
# print(b.cheat())
# b.place_ship("c3d3e3")
# print(b)
# print(b.cheat())
# b.place_ship("a1b1c1")
# print(b)
# print(b.cheat())
        