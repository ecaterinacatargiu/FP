def f(l):
    print("A")
    if l == []:
        raise ValueError()
    print("B")

def start():
    l = []
    try:
        print("A")
        f(l)
        print("D")
    except ValueError:
        print("C")

start()




class A:
    def f(self, l,nr):
        l.append(nr)

class B:
    def g(self, l, nr):
        nr=nr-1
        l = l+[-2]

a = A()
b = B()
l = [1,2]
c = -1

a.f(l,6)
b.g(l,c)
print(l,c)

a = lambda x: [x+1]
b = a(1)
c = lambda x: x + b
d = c([1])

a = 1
b = 3
print (a, b, c(4), d[1])



def function(n):
    d = 2
    while (d < n - 1) and n % d > 0:
        d += 1
    return d >= n - 1

print(function(5))
print(function(6))
print(function(7))


assert function(5) == True
assert function(6) == False
assert function(7) == True
assert function(8) == False



def complexity_1(x):
    m = len(x)
    found = False
    while m >= 1:
        c = m - m / 3 * 3
        if c == 1:
            found = True
        m = m / 3


print(complexity_1('abc'))


def complexity_3(n, i):
    if n > 1:
        i *= 2
        m = n // 2
        complexity_3(m, i - 2)
        complexity_3(m, i - 1)
        complexity_3(m, i + 2)
        complexity_3(m, i + 1)
    else:
        print(i)

print(complexity_3(3,3))


l = [["paine", "aliment", 2], ["apa", "lichid", 6], ["mere", "fructe",5]]

l.sort(key=lambda l:l[1])
print(l)
l.sort(key=lambda l:l[2], reverse=True)
print(l)


"""GREEDY"""

def _computeSum(b, SUM):
    '''
    Compute the paid amount with the current candidate
    '''
    amount = 0
    for coin in b:
        nrCoins = (SUM - amount) // coin
        # If this is a candidate solution,
        # we need to use at least 1 coin
        if nrCoins == 0:
            nrCoins = 1
        amount += nrCoins * coin
    return amount


def selectMostPromising(c):
    '''
    Select the largest coin from the remaining
    input:
        c - candidate coins
    Return the largest coin
    '''
    return max(c)


def acceptable(b, SUM):
    '''
    Verify if a candidate solution is valid (we are not over amount)
    '''
    amount = _computeSum(b, SUM)
    return amount <= SUM


def solution(b, SUM):
    '''
    Verify if a candidate solution is an actual solution
    (we are at the required amount)
    '''
    amount = _computeSum(b, SUM)
    return amount == SUM


def buildSolutionString(b, SUM):
    '''
    Pretty print the solution
    '''
    solStr = ''
    amount = 0
    for coin in b:
        nrCoins = (SUM - amount) // coin
        solStr += str(nrCoins) + '*' + str(coin)
        amount += nrCoins * coin
        if SUM - amount > 0:
            solStr += " + "
    return solStr


def greedy(c, SUM):
    '''
    Main function
    '''
    # The empty set is the candidate solution
    b = []
    while not solution(b, SUM) and c != []:
        # Select best candidate (local optimum)
        candidate = selectMostPromising(c)
        c.remove(candidate)
        # If the candidate is acceptable, add it
        if acceptable(b + [candidate], SUM):
            b.append(candidate)
    if solution(b, SUM):
        return buildSolutionString(b, SUM)


'''
    Let's see how it works
'''
for amount in range(1, 55):
    print('Amount ' + str(amount) + "=" + greedy([1, 5, 10], amount))


