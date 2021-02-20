class GameException(Exception):

    def __init__(self, mes):
        self.__mes = mes

    @property
    def getMessage(self):
        return self.__mes