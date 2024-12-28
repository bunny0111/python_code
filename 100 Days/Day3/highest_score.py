'''Find the highest score'''

numbers = [567, 943, 235, 789, 432, 112, 876, 543, 998, 321, 645, 289, 190, 874, 567, 394, 837, 921, 405, 720, 638, 249, 788, 102, 985, 460, 753, 298, 569, 670]

# Find sum of total number
sum = 0
for score in numbers:
    # sum += score
    sum = sum + score
print ("Sum=",sum)

# Inbuilt function
largest = max(numbers)
print("Largest=",largest)

max_score = 0

for score in numbers:
    if score > max_score:
        max_score = score
print("Highest score=",max_score)