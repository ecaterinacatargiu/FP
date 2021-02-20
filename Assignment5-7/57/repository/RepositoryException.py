

class RepositoryError(Exception):
    def __init__(self, mes):
        self._message = mes

    @property
    def message(self):
        return self._message

import random


def test():
    r = random.randint(0, 2)
    if r == 0:
        raise ValueError("ve")
    elif r == 1:
        raise TypeError("te")
    else:
        raise RepositoryError("re")


for i in range(10):
    try:
        test()
    except Exception as re:
        print(re)


def test2():
    r = random.randint(0, 2)
    if r == 1:
        raise Exception("?")

    test()