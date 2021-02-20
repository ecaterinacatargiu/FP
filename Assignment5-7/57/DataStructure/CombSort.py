import unittest
def sortAscendint(a,b):
    return a>b


def combSort(input, function):
    gap = len(input)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(input) - gap):
            j = i + gap
            if function(input[i], input[j]):
                input[i], input[j] = input[j], input[i]
                swaps = True
    return input

y = [88, 18, 31, 44, 4, 0, 8, 81, 14, 78, 20, 76, 84, 33, 73, 75, 82, 5, 62, 70]
#combsort(y)
#print(y)
#assert y == sorted(y)

class Test(unittest.TestCase):
    def setUp(self):
        self.list  = [10,-4,5 ,6,800]

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test(self):
        self.assertEqual(combSort(self.list,sortAscendint),[-4,5,6,10,800])



