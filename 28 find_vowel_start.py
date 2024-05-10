'''
Write a function to find all words in a sentence that start with a vowel
'''

def find_vowel(sentence):
    words = sentence.split()
    vowel_words = []

    for word in words:
        if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowel_words.append(word)
    return vowel_words

sentence1 = "I am doing fine"
sentence2 = "The quick brown fox jumps over the lazy dog"
sentence3 = "The weather is nice today"
sentence4 = "No words start with a vowel"
sentence5 = "Hello, How are you"
print(find_vowel(sentence1))
print(find_vowel(sentence2))
print(find_vowel(sentence3))
print(find_vowel(sentence4))
print(find_vowel(sentence5))