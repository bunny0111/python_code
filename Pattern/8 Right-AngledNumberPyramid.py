'''Right-Angled Number Pyramid'''

def RightAngledNumberPyramid(row):
    for i in range(1, row+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
RightAngledNumberPyramid(6)