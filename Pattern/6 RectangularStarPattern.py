'''Rectangular Star Pattern'''

def RectStarPattern(row, col):
    for i in range(row):
        for j in range(col):
            print('*', end=' ')
        print()

RectStarPattern(4, 6)