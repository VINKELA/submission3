'''This function  takes a number as a parameter and check the number is prime or not.'''

def isprime(number):
    if type(number) is not int:
         raise TypeError("function isprime accepts an int as parameter")
    # if number is less than or equal to 1 return false
    if number < 1 or number == 1:
        return print("{} is not prime".format(number))
    # if any number between 2 and the number(the number not inclusive) can divide it without remainder, return False
    for i in range(2, number):
        if number % i == 0:
            return print("{} is not prime".format(number))
    print("{} is prime".format(number))
    
