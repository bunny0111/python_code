'''
Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10]
'''

def count_pos_num(numbers):
    positive_number_counts = 0
    for num in numbers:
        if(num>0):
            positive_number_counts += 1
    return positive_number_counts

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10]
print("Final count of positive number=", count_pos_num(numbers))