'''Right-Angled Number Pyramid - II
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
def RightAngledNumberPyramid(row):
    for i in range(1, row+1):
        for j in range(1, i+1):
            print(i, end=' ')
        print()
RightAngledNumberPyramid(6)