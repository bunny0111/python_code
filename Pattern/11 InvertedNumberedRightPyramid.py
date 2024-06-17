'''Inverted Numbered Right Pyramid'''
def invertedNumberedRightPyramid(row):
    for i in range(row, 0, -1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
invertedNumberedRightPyramid(5)