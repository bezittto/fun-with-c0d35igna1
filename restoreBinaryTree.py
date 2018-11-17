'''
Note: Your solution should have O(inorder.length) time complexity, since this is what you will be asked to accomplish in an interview.

Let's define inorder and preorder traversals of a binary tree as follows:

Inorder traversal first visits the left subtree, then the root, then its right subtree;
Preorder traversal first visits the root, then its left subtree, then its right subtree.
For example, if tree looks like this:

    1
   / \
  2   3
 /   / \
4   5   6
then the traversals will be as follows:

Inorder traversal: [4, 2, 1, 5, 3, 6]
Preorder traversal: [1, 2, 4, 3, 5, 6]
Given the inorder and preorder traversals of a binary tree t, but not t itself, restore t and return it.

Example

For inorder = [4, 2, 1, 5, 3, 6] and preorder = [1, 2, 4, 3, 5, 6], the output should be
restoreBinaryTree(inorder, preorder) = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 4,
            "left": null,
            "right": null
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": {
            "value": 6,
            "left": null,
            "right": null
        }
    }
}
For inorder = [2, 5] and preorder = [5, 2], the output should be
restoreBinaryTree(inorder, preorder) = {
    "value": 5,
    "left": {
        "value": 2,
        "left": null,
        "right": null
    },
    "right": null
}

'''

#
# Definition for binary tree:
class Tree(object):
   def __init__(self, x):
     self.value = x
     self.left = None
     self.right = None

def reconstruct( left_branch, remainder ): 
    if len(remainder)>0:
        peak = remainder[0]
        t = Tree( peak )
        
        left_branch_ = left_branch[: left_branch.index(peak) ]        
        left_remainder_ = remainder[1:1+len(left_branch_)]

        if len ( left_branch_ )>0:
            t.left = reconstruct ( left_branch_ , left_remainder_ )

        right_branch_ = left_branch[ left_branch.index(peak) +1 : ] 
        right_remainder_ = remainder[1+len(left_branch_):]

        if len ( right_branch_ )>0:
            t.right = reconstruct ( right_branch_ , right_remainder_ )

        return t
    else:
        return None

def restoreBinaryTree(inorder, preorder):    
    return reconstruct ( inorder , preorder )    

# tests

inorder = [4, 2, 1, 5, 3, 6] 
preorder = [1, 2, 4, 3, 5, 6]

t = restoreBinaryTree(inorder, preorder)

print ( t.left.left.value )