class GameException(Exception):

    def __init__(self, message):
        self.__message = message

    @property
    def getMessage(self):
        return self.__message


class Player:
    def _init_(self, player, typeOfPlayer, runMethod):
        self.__player = player
        self.__type = typeOfPlayer
        self.__runMethod = runMethod
        self.__won = False

    def setRunMethod(self, runMethod):
        self.__runMethod = runMethod

    def setWon(self):
        self._won = not self._won

    def run(self):
        return self.__runMethod()

    def getPlayer(self):
        return self.__player

    def getType(self):
        return self.__type

    def _eq_(self, other):
        if type(other) == str:
            return self.__player == other
        return self.__player == other.getPlayer()

    def _str_(self):
        return "Player " + str(self.__player)