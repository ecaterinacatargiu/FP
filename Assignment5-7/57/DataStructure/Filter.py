import unittest

def acceptanceFunction(value, cmp=None):
    if cmp == None:
        cmp = default_cmp
    if value > cmp:
        return True
    return False

def filterFunction(listToBeFiltered, acceptanceFunction):
    intermediateList = listToBeFiltered[:]
    index = 0
    while index < len(intermediateList):
        if not acceptanceFunction(intermediateList[index]):
            del intermediateList[index]
        else:
            index = index + 1
    return intermediateList

#lst = [0,2,-5,2,9,8,-1,10,-2]
#default_cmp = 5
#lst = filterFunction(lst, acceptanceFunction)
#print(lst)


class Test(unittest.TestCase):
    def setUp(self):
        self.lst = [1,2,3,4,5,6,7,8,9,10,11,12]

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def fct(self, param):
        return param < 9

    def test(self):
        self.assertEqual(filterFunction(self.lst,self.fct),[1,2,3,4,5,6,7,8])

