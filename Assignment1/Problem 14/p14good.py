def Prime(n):
    """A function that verifies if a given number is prime or not.
       Input: n - an integer.
       Output: boolean value: True- if it is prime and False- if it is not"""
    for i in range(2, int(n/2)+1):
        if n%i==0:
            return False
    return True

def Number(index):
    """A funtion that returns the number on the requested position.
       Input: index - an integer(the position)
       Output: the requested number on the given position"""
    
    prim=0 #the current prime number
    pas=1 #the step I use to go through the sequence
    position1=0 #the last position 
    while pas<=index:
        position1+=1
        if Prime(position1):
            prim=0
            pas+=1
        else:
            for i in range(2, position1//2+1):
                if Prime(i) and position1%i==0 and pas<=index:
                    for j in range (0,i):
                        pas+=1
                        prim=i
    if prim :
        return prim
    else:
        return position1
    

index=int(input("Enter an index: "))

print(Number(index))

""" 1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3,...  """
