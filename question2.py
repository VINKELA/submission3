''' This  function  finds the Max of three numbers'''

def maximum_of(first, second, third):
    # check if first,  second, and third are all valid int
    if type(first) is not int:
        raise ValueError("{} is not an int".format(first))
    if type(second) is not int:
        raise ValueError("{} is not an int".format(second))
    if type(second) is not int:
        raise ValueError("{} is not an int".format(second))
    # typecast first, second, and third
    first = int(first)
    second = int(second)
    third = int(third)

    # if first number is greater than second
    if first > second:
        # first number is also greater than third
        if first > third:
            print("The maximum of {f}, {s}, and {t} is {m}".format(f=first, s=second, t=third, m=first))
        else:
            print("The maximum of {f}, {s}, and {t} is {m}".format(f=first, s=second, t=third, m=third))
    # if second number is greater than first number
    else:
        # if second number is greater than third number
        if second > third:
            print("The maximum of {f}, {s}, and {t} is {m}".format(f=first, s=second, t=third, m=second))
        else:
            print("The maximum of {f}, {s}, and {t} is {m}".format(f=first, s=second, t=third, m=third))

