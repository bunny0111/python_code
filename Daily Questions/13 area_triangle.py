'''
Write a program to find the area of right angled triangle rounded of to two decimal places

formule = 1/2 * base * height
'''
def area_triangele(b, h):
    area = 0.5 * b * h
    rounded_area = round(area, 2)
    return rounded_area

base = 20
height = 50
print(area_triangele(base, height))