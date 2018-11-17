def sumInRange(nums, queries):
    
    total = 0    
    sum_storage = {}

    temp = 0
    for i in range(len(nums)):
        key_ = str([0,i])
        temp += nums[i]
        sum_storage[key_] = temp
           
    for q in queries:
        key_ = str(q)
        if q[0]==0:
            adder_ = sum_storage[key_]
        else:
            if key_ not in sum_storage:
                key_A_ = str([0,q[0]-1])
                key_B_ = str([0,q[1]])
                sum_storage[key_] = sum_storage[key_B_] - sum_storage[key_A_]
            
            adder_ = sum_storage[key_]
        
        total+= adder_
            
    return  total % (10**9+7)

# tests

nums = [3, 0, -2, 6, -3, 2]
queries = [[0,2],  [2,5],  [0,5]]

#nums = [34, 19, 21, 5, 1, 10, 26, 46, 33, 10]
#queries = [[3,7],  [3,4],  [3,7],  [4,5],  [0,5]]

print ( sumInRange (nums, queries))