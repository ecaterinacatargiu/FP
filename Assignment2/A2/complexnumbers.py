def getReal(c):
    #return cn[0]
    return c["Real"]

def getIm(c):
    #return cn[1]
    return c["Im"]

def setReal(cn, newReal):
    #cn[0]=newReal
    cn["Real"]=newReal

def setIm(cn, newIm):
    #cn[1]=newIm
    cn["Im"]=newIm 


def create(Real, Im):
    #return[Real, Im]
    return {"Real": Real, "Im": Im}



def printMenu():
    print("1.Read a complex number: ")
    print("2.Print the list of numbers: ")
    print("3.Print the longest sequence of numbers that have the same modulus: ")
    print("4.Print the longest sequence of numbers that are real numbers: ")
    print("5.Exit the application. ")

def addNumbers(cn):
    Real=int(input("The real part is: "))
    Im=int(input("The imaginary part is: "))
    cn.append(create(Real, Im))


def printList(cn):
    for i in range (0, len(cn)):
        if getIm(cn[i])<0:
            print(getReal(cn[i]), "-" ,-getIm(cn[i]),"i")
        if getIm(cn[i])>0:
            print(getReal(cn[i]), "+" ,getIm(cn[i]),"i")
        if getIm(cn[i])==0:
            print(getReal(cn[i]))


def getModulus(cn):
    """A function that return the moduus of a complex number.
   Input: a list that denote a complex number
   Output: the modulus of the complex number"""
    mod=int(((getReal(cn)*getReal(cn))+(getIm(cn)*getIm(cn)))**(1/2))
    return mod

def sameModulussequence(cn):
    """A function that returns the longest sequence of complex numbers that have the same modulus.
    Input: a list of lists
    Output: the longest sequence of complex numbers that have the same modulus"""
    sequence=[]
    maxSequence=[]
    i=1
    sequence.append(cn[0])
    while i<len(cn):
        if getModulus(cn[i])==getModulus(cn[i-1]):
            sequence.append(cn[i])
        else:
            if len(sequence)>len(maxSequence):
                maxSequence=[]
                maxSequence=sequence
            sequence=[]
            sequence.append(cn[i])
        i+=1
    if len(sequence)>len(maxSequence):
        maxSequence=[]
        maxSequence=sequence
    return maxSequence

def RealNumbers(cn):
    """A function that reuturns the longest sequence of real numbers(Im=0)
    Input: cn
    Output: the longest sequence of real numbers"""
    sequence=[]
    maxSequence=[]
    i=0
    while i<len(cn):
        if getIm(cn[i])==0:
            sequence.append(cn[i])
        else:
            if len(sequence)>len(maxSequence):
                maxSequence=[]
                maxSequence=sequence
            sequence=[]
            #sequence.append(cn[i])
        i+=1
    if len(sequence)>len(maxSequence):
        maxSequence=[]
        maxSequence=sequence
    return maxSequence


def Values(cn):
    """Adds complex numbers.
    Input: cn - a list
    Output: the list cn with the values"""
    cn.append(create(2,5))
    cn.append(create(4,7))
    cn.append(create(1,2))
    cn.append(create(2,1))
    cn.append(create(1,2))
    cn.append(create(3,0))
    cn.append(create(5,0))
    cn.append(create(11,0))

def Start():
    cn=[]
    Values(cn)
    while True:
        printMenu()
        option=int(input())
        if option==1:
            addNumbers(cn)
        elif option==2:
            printList(cn)
        elif option==3:
            printList(sameModulussequence(cn))
        elif option==4:
            printList(RealNumbers(cn))
        elif option==5:
            return
        else:
            print("Invalid command! ")



Start()


