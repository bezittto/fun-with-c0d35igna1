'''
Given an array of equal-length strings, check if it is possible to rearrange the strings 
in such a way that after the rearrangement the strings at consecutive positions would differ by exactly one character.

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false.

All rearrangements don't satisfy the description condition.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

Strings can be rearranged in the following way: "aa", "ab", "bb".

'''
from itertools import permutations

def stringsRearrangement(inputArray):   
    for p in  list( permutations(inputArray) ):
        tests_ = 0
        for i in range(len(p)-1):
            if sum( [ 1 if x!=y else 0 for x,y in zip( p[i], p[i+1] ) ] ) != 1:
                break
            else:
                tests_+=1
        if tests_==len(p)-1:
            return True
    return False

# tests
inputArray = ["ab",  "ad",   "ef",  "eg"]
inputArray=  ["ab",  "bb",  "aa"]
inputArray = ["f",  "g",  "a",  "h"]
inputArray = ["aba",  "bbb", "bab"]
inputArray = ["ab",  "ad", "ef", "eg"]
inputArray = ["abc",  "abx",  "axx",  "abx", "abc"] 
inputArray = ["abc", "abx",   "axx", "abc"]
inputArray = ["ff",  "gf",  "af", "ar",  "hf"]
inputArray = ["abc",  "abx",  "axx",  "abx"] 
inputArray = ["abc",  "abx",   "abc" ,"axx"]
inputArray = ["ab",  "ad",   "ef",  "eg"]
inputArray = ["abc",  "abx",  "axx",  "abx", "abc"]
inputArray = ["ab",  "bb",  "aa"]
inputArray = ["abc",  "abx",  "axx",  "abc"]
inputArray = ["ab",  "bb",   "aa"]
inputArray =["abc",  "bef", "bcc", "bec","bbc", "bdc"]

print ( stringsRearrangement(inputArray) )
