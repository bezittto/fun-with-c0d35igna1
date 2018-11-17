'''
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
removeKFromList(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7]
'''

# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def removeKFromList(l, k):
    # reconstruct l in proper way
    ls = [ 0 for i in range( len(l) ) ] 
    for i, j in enumerate(l):
        ls[i] = ListNode(j)
        if i>0:
            ls[i-1].next =ls[i]

    l = ls[0]

    # 
    ls = [] 
    while l is not None:
        if l.value != k:
            ls.append( l.value )
        l = l.next

    ls2 = [ 0 for i in range( len(ls) ) ] 
    for i, j in enumerate(ls):
        ls2[i] = ListNode(j)
        if i>0:
            ls2[i-1].next =ls2[i]

    if len(ls2)>0: 
        return ls2[0]
    return None


# test

l = [3, 1, 2, 3, 4, 5]
k = 3

l = [1000, 1000]
k = 1000

removeKFromList(l,k)