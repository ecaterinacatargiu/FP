def Fibbo(n):
    """A function that returns the smallest Fibonacci number that is larger than a given number and its position.
       Input: n - an integer.
       Output: the requested number and its position."""
    a,b=1,1
    nr=2
    while a+b<=n:
        c=a+b
        nr+=1
        a=b
        b=c      
    l=[]
    l.append(a+b)
    l.append(nr+1)
    return l

l=[]
n=int(input('Enter an integer other than 0: '))
while n!=0:
    l=Fibbo(n)
    print('The requested number is: ', l[0], 'on position: ', l[1])
    n=int(input('Enter an integer: '))



