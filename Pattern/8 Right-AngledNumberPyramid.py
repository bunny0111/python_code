'''Right-Angled Number Pyramid
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
def RightAngledNumberPyramid(row):
    for i in range(1, row+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
RightAngledNumberPyramid(6)