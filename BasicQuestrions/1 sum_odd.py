# Write a code using while loop that adds all odd numbers from 1 to 50

a = 1
total = 0
while a <= 50:
    if a % 2 != 0:
        total += a
    a += 1
print(total)