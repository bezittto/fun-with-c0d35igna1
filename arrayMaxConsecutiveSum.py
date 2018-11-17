'''
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.

'''

def arrayMaxConsecutiveSum(inputArray, k):
    subSum = globalMax = 0
    for i in range( len(inputArray) ):
        subSum += inputArray[i]
        if i-k>=0:
            subSum -= inputArray[i-k]
        globalMax = max( subSum, globalMax  )

    return globalMax


# test
inputArray = [2, 4, 10, 1]
k = 2

inputArray = [2, 3, 5, 1, 6]
k = 2

print ( arrayMaxConsecutiveSum( inputArray, k ) )
