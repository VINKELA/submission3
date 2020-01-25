'''This function  takes a number as a parameter and checks if the number is prime or not.'''

def isprime(number):
    if type(number) is not int:
         raise TypeError("function isprime accepts an int as parameter")
    # if number is less than or equal to 1 return number is prime
    if number < 1 or number == 1:
        return print("{} is not prime".format(number))
    # if any number between 2 and the number(the number not inclusive) can divide it without remainder, return number is prime
    # % gives the remainder when the first number on the right divides the number on the left
    for i in range(2, number):
        if number % i == 0:
            return print("{} is not prime".format(number))
    # The number is prime
    print("{} is prime".format(number))
    
