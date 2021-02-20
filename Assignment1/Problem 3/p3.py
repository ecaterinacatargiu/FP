def smallestnr(number):
    """A function that generates the smallest number by rearranging the digits of a given number.
       Input: lst - an integer
       Output: the smallest number formed by rearranging the digits of the given number"""
    for i,n in enumerate(number): 
        if n!='0':
            nr=number.pop(i)
            break
    return str(nr)+''.join(number)

if __name__=='__main__':
    number=list(str(4558802))
    number.sort()
    print (smallestnr(number))

"""i=index; n=number of the list; nr=removes and stores the digit 
Functions used: enumerate()-loops over something and automatically counts it;
pop()-removes and returns the i-th element of the list
join()-returns a string in which the string elements of sequence have been joined by str separator
sort()-sorts the elements from the smallest to the largest
break-terminates the current loop and resumes takes the execution to the next step"""
