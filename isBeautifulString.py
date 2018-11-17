'''
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be
isBeautifulString(inputString) = true;
For inputString = "aabbb", the output should be
isBeautifulString(inputString) = false;
For inputString = "bbc", the output should be
isBeautifulString(inputString) = false.

'''

import string

def isBeautifulString(inputString):
    counter = { c: 0 for c in string.ascii_lowercase }

    for c in inputString:    
        counter[ c ]+=1

    prev_ = None
    for k in counter.keys():
        if prev_ is not None:
            if prev_ < counter[ k ]:
                return False
        prev_ = counter[ k ]

    return True

# test

inputString = "aabbb"

inputString = "bbc"

inputString=  "bbbaacdafe"

print ( isBeautifulString(inputString) )