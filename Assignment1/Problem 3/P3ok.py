def getSmallest(number):
    """A function that returns the smallest number formed by rearranging the digits of a given number.
       Input: an integer
       Output: the smallest numbe formed by rearranging the digits of the given number."""

    if number[0] != '0':
        return "".join(number)
    else:
        count = 0
        for n in number:
            if n == '0':
                count += 1
            else:
                break
        return "".join(number[count:count+1] + number[:count] + number[count+1:])

number =sorted(list(input("Enter the initial number: ")))
print()
print("The smallest number is: ", getSmallest(number))

"""join()-function that returns a string in which the string elements of sequence have been joined by str separator""" 
