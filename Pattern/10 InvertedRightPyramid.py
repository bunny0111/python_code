'''Inverted Right Pyramid'''
def InvertedRightPyramid(row):
    for i in range(row, 0, -1):
        for j in range(i, 0, -1):
            print('*', end=' ')
        print()
InvertedRightPyramid(6)