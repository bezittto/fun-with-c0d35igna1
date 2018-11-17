
'''
Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": None,
            "right": None
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": None,
            "right": None
        },
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}
the output should be isTreeSymmetric(t) = true.

Here's what the tree in this example looks like:

    1
   / \
  2   2
 / \ / \
3  4 4  3
As you can see, it is symmetric.

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}
the output should be isTreeSymmetric(t) = false.

Here's what the tree in this example looks like:

    1
   / \
  2   2
   \   \
   3    3
As you can see, it is not symmetric.

'''

#
# Definition for binary tree:
class Tree(object):
   def __init__(self, x):
     self.value = x
     self.left = None
     self.right = None

def rebuild_tree( t ):
    if t is not None:
        T = Tree( t['value'] )
        T.left = rebuild_tree( t['left'] )
        T.right = rebuild_tree( t['right'] )
        return T
    return None

def traverse_tree( t, level, values ):
    if t is not None:
        level+=1
        if level not in values:
            values[level]=[]

        if t.left is not None:
            values[level].append(t.left.value)
        else:
            values[level].append(None)
        if t.right is not None:
            values[level].append(t.right.value)
        else:
            values[level].append(None)

        traverse_tree( t.left, level, values )
        traverse_tree( t.right, level, values )

    return values

def isTreeSymmetric(t):
    t = rebuild_tree(t) # this is here because on PC tree must be rebuilt to Tree object, but it was not submitted with this line
    check_dir =  traverse_tree(t, 0, {})
    for k,v in check_dir.items():
        for i in range( int( len(v)/2) ):
            if v[i]!=v[-i-1]:                
                return False
    return True

# tests

t1 = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": None,
            "right": None
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": None,
            "right": None
        },
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}

t2 = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}

t3= {
    "value": 100,
    "left": None,
    "right": {
        "value": 100,
        "left": None,
        "right": None
    }
}

t4 = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}

print ( isTreeSymmetric(t4) )