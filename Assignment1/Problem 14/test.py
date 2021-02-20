def vfprim(nr):
    """A function that decides if a number is prime or not.
       Input: nr an integer
       Output: boolean value"""
    for i in range(2, int(nr/2)+1):
        if nr%i==0:
            return False
    return True

def div(n):
    """A function that finds the divisor, verifies wheather they are prime or not and prints them.
       Input: n - an integer.
       Ourput: """
    for i in range(2,int(n/2)+1):
        if n%i==0:
            if vfprim(i)==True:
                #for j in range(0,i):
                print(i, " ")

    
n=int(input("Write your number:"))
for i in range(1,n):
    if vfprim(n)==True:
        print(n, " ")
    else:
        div(n)




