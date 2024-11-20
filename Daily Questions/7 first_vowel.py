'''
Write a program that gives the index of the first vowel obtained in a string.
'''

def findvow(str1):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O' , 'u', 'U']
    for i in range (len(str1)):
        if str1[i] in vowels:
            return i
    return None
print(findvow('apple'))
print(findvow('Apple'))
print(findvow('Pineapple'))
print(findvow('fly'))