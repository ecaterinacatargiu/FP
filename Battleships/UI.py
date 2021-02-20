'''
Created on Jan 20, 2019

@author: Korina
'''
from Battleships.Board import BoardError


class UI:
    def __init__(self,game):
        self.__game = game
        

    def __print_menu(self):
        print("Your options are:")
        print("\t place ship: ship <C1L1C2L2C3L3>")
        print("\t start the game: start")
        
        print("\t stop the game: stop")
    
    def __start_GAME(self):
        commands = {"stop":2,"attack":3, "cheat":0}
        self.__game.place_comp_ships()
        self.__game.place_comp_ships()
        
        print("-> In order to attack the computer write : attack <CL> \n If you want to stop write: stop ")
        print("If you want to cheat write: cheat")
        while True:
            try:
                print("USER BOARD")
                print(self.__game.show_user_board())
                print("COMPUTER BOARD")
                print(self.__game.show_computer_board())
                inpt = input("command expected >> ").lower().split()
                if inpt[0] not in commands.keys():
                    raise ValueError("Invalid command!")
                if inpt[0] == "attack":
                    print("User"+ self.__game.user_attack(inpt[1]))
                    print("Computer"+ self.__game.computer_attack())
                    if self.__game.game_won("computer"):
                        print("COMPUTER WINS!")
                        return
                    elif self.__game.game_won("user"):
                        print("USER WINS!")
                        return
                elif inpt[0] == "cheat":
                    print(self.__game.show_cheat())
#                     self.__game.attack_computer(inpt[1])
                elif inpt[0] == "stop":
                    return
#                 else:
#                     raise Exception("Something went wrong!")
                
            except Exception as e:
                print(str(e))
    
    def start(self):
        commands = {"start":1,"ship":2,"stop":3}#"attack":3}
        print("Welcome to the Battleship game!")
        while True:
            try:
                self.__print_menu()
                inpt = input("command expected >> ").lower().split()
                if inpt[0] not in commands.keys():
                    raise ValueError("Invalid command!")
                if inpt[0] == "ship":
                    self.__game.place_user_ship(inpt[1])
                    print("User board")
                    print(self.__game.show_user_board())
                elif inpt[0] == "start":
                    if self.__game.enough_ships():
                        self.__start_GAME()
                        return
                    else:
                        raise BoardError("Not enough ships have been placed!")
                elif inpt[0] == "stop":
                    return
#                 else:
#                     raise Exception("Something went wrong!")
                
            except Exception as e:
                print(str(e))
                
                
                