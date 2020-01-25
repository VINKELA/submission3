'''This Python function  accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''

def upper_lower_count(word):
    # number of uppercase letters
    upperCount = 0
    # number of lowercase letters
    lowerCount = 0
    for alphabet in word:
        if alphabet.isupper():
            upperCount = upperCount + 1
        elif alphabet.islower():
            lowerCount = lowerCount + 1
    print("No. of Upper case characters : {up}\nNo. of Lower case Characters : {lo}".format(up = upperCount, lo = lowerCount))
