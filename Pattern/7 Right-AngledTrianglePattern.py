'''Right-Angled Triangle Pattern'''

def RightAngledTrianglePattern(row):
    for i in range(row+1):
        for j in range(i):
            print('*', end=' ')
        print()
RightAngledTrianglePattern(5)