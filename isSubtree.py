'''
Given two binary trees t1 and t2, determine whether the second tree is a subtree of the first tree. 
A subtree for vertex v in a binary tree t is a tree consisting of v and all its descendants in t. 
Determine whether or not there is a vertex v (possibly none) in tree t1 such that a subtree for vertex v (possibly empty) in t1 equals t2.

Example

For

t1 = {
    "value": 5,
    "left": {
        "value": 10,
        "left": {
            "value": 4,
            "left": {
                "value": 1,
                "left": null,
                "right": null
            },
            "right": {
                "value": 2,
                "left": null,
                "right": null
            }
        },
        "right": {
            "value": 6,
            "left": null,
            "right": {
                "value": -1,
                "left": null,
                "right": null
            }
        }
    },
    "right": {
        "value": 7,
        "left": null,
        "right": null
    }
}
and

t2 = {
    "value": 10,
    "left": {
        "value": 4,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 6,
        "left": null,
        "right": {
            "value": -1,
            "left": null,
            "right": null
        }
    }
}
the output should be isSubtree(t1, t2) = true.

This is what these trees look like:

      t1:             t2:
       5              10
      / \            /  \
    10   7          4    6
   /  \            / \    \
  4    6          1   2   -1
 / \    \
1   2   -1
As you can see, t2 is a subtree of t1 (the vertex in t1 with value 10).

For

t1 = {
    "value": 5,
    "left": {
        "value": 10,
        "left": {
            "value": 4,
            "left": {
                "value": 1,
                "left": null,
                "right": null
            },
            "right": {
                "value": 2,
                "left": null,
                "right": null
            }
        },
        "right": {
            "value": 6,
            "left": {
                "value": -1,
                "left": null,
                "right": null
            },
            "right": null
        }
    },
    "right": {
        "value": 7,
        "left": null,
        "right": null
    }
}
and

t2 = {
    "value": 10,
    "left": {
        "value": 4,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 6,
        "left": null,
        "right": {
            "value": -1,
            "left": null,
            "right": null
        }
    }
}
the output should be isSubtree(t1, t2) = false.

This is what these trees look like:

        t1:            t2:
         5             10
       /   \          /  \
     10     7        4    6
   /    \           / \    \
  4     6          1   2   -1
 / \   / 
1   2 -1
As you can see, there is no vertex v such that the subtree of t1 for vertex v equals t2.

For

t1 = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": null
    },
    "right": {
        "value": 2,
        "left": null,
        "right": null
    }
}
and

t2 = {
    "value": 2,
    "left": {
        "value": 1,
        "left": null,
        "right": null
    },
    "right": null
}
the output should be isSubtree(t1, t2) = false.

'''
#
# Definition for binary tree:
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def rebuildTree(t):
    tree = None
    if t is not None:
        tree = Tree(t['value'])
        tree.left = rebuildTree(t['left'])
        tree.right = rebuildTree(t['right'])
    return tree

def findRoots(t, t2):
    result = []

    if t is not None or result is None:
        if t2 is not None:
            if t.value == t2.value:
                result.append( t )
        
        tmp_ = findRoots(t.left, t2)
        if tmp_ != []:
            result += tmp_ 
        tmp_ = findRoots(t.right, t2)
        if tmp_ != []:
            result += tmp_ 
    else:
        if t is None and t2 is None:
            result.append( t )
    return result

def compareTrees(t1, t2):
    if t1 is not None and t2 is not None:
        if t1.value != t2.value:
            return False
        else:
            if compareTrees(t1.left, t2.left) == False:
                return False
            if compareTrees(t1.right, t2.right) == False:
                return False

            return True
    elif ( t1 is not None and t2 is None ) or (t1 is None and t2 is not None ):
        return False
    else:
        return True

def isSubtree(t1, t2):
    # build tree as objec first
    t1 = rebuildTree(t1)
    t2 = rebuildTree(t2)
    # submit
    t2_roots_in_t1 = findRoots(t1, t2)
    if t1 is None and t2 is None:
        return True

    for t in t2_roots_in_t1:
        if compareTrees(t, t2 ) == True:
            return True

    return False

# tests

t1 = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": None
    },
    "right": {
        "value": 2,
        "left": None,
        "right": None
    }
}

t2 = {
    "value": 2,
    "left": {
        "value": 1,
        "left": None,
        "right": None
    },
    "right": None
}


'''

t1 = {
    "value": 5,
    "left": {
        "value": 10,
        "left": {
            "value": 4,
            "left": {
                "value": 1,
                "left": None,
                "right": None
            },
            "right": {
                "value": 2,
                "left": None,
                "right": None
            }
        },
        "right": {
            "value": 6,
            "left": None,
            "right": {
                "value": -1,
                "left": None,
                "right": None
            }        
        }
    },
    "right": {
        "value": 7,
        "left": None,
        "right": None
    }
}

t2 = {
    "value": 10,
    "left": {
        "value": 4,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 2,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 6,
        "left": None,
        "right": {
            "value": -1,
            "left": None,
            "right": None
        }
    }
}
'''

'''
t1: {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": None
    },
    "right": {
        "value": 2,
        "left": None,
        "right": None
    }
}
t1 = None

t2 = None
'''

print ( isSubtree(t1, t2) )
