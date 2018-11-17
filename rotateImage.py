'''
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]

'''

def rotateImage(a):
    b= [ [0 for i in range(len(a))] for j in range(len(a)) ]

    for i in range(0,len(a)):
        for j in range(0,len(a)):
            z = [ x for x in range(len(a))]
            n = z[ -(z.index(i)+1) ]
            b[j][n] = a[i][j]
    return b


# test

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print ( rotateImage(a) )