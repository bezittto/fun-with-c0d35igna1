'''
You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. 
You want to know how many distinct sums you can make from non-empty groupings of these coins.

Example

For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should be
possibleSums(coins, quantity) = 9.

Here are all the possible sums:

50 = 50;
10 + 50 = 60;
50 + 100 = 150;
10 + 50 + 100 = 160;
50 + 50 = 100;
10 + 50 + 50 = 110;
50 + 50 + 100 = 200;
10 + 50 + 50 + 100 = 210;
10 = 10;
100 = 100;
10 + 100 = 110.
As you can see, there are 9 distinct sums that can be created from non-empty groupings of your coins.
'''

from itertools import product

def possibleSums(coins, quantity):   
    
    sumslib = []
    results = {}

    for i, q in enumerate(quantity):
        sumslib.append([])
        for j in range( 0, q+1 ):
            sumslib[i].append( coins[i]*j )

    for t in product(*sumslib):
        if sum(t) not in results:
            results[sum(t)] = 1

    return(len(results)-1)
   
  
# tests
coins = [1, 1, 1, 1, 1]
quantity = [9, 19, 18, 12, 19]

#coins = [1, 2]
#quantity = [50000, 2]

coins = [3, 1, 1]
quantity = [111, 84, 104]

coins = [10, 50, 100] 
quantity = [1, 2, 1]

print ( possibleSums(coins, quantity) )
