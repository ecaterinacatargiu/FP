class DataStructure:
    def __init__(self):
        self.__index = 0
        self.__data = list()

    def append(self, value):
        self.__data.append(value)

    def __setitem__(self, index, value):
        self.__data[index] = value

    def __getitem__(self, index):
        return self.__data[index]

    def __delitem__(self, index):
        del self.__data[index]

    def __len__(self):
        return len(self.__data)

    def __next__(self):
        if self._index >= len(self.__data):
            self.__index = 0
            raise StopIteration
        index = self.__index
        self._index = self._index + 1
        return self.__data[index]

    def __iter__(self):
        return iter(self.__data)

    def __str__(self):
        return str(self.__data)

    def __eq__(self, other):
        return self.__data == other