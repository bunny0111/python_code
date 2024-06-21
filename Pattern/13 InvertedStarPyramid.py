'''Inverted Star Pyramid
*********
 *******
  *****
   ***
    *
'''

def invertedStarPyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(0, rows - i):
            print(' ', end='')
        for j in range(0, 2*i-1):
            print('*', end='')
        print()
invertedStarPyramid(5)