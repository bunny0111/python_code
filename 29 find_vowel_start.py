'''
Write a function to find all words in a sentence that start with a vowel
'''
import re

def words_starting_with_vowel(sentence):
    # Use regex to find words starting with a vowel
    pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
    words = re.findall(pattern, sentence)
    return words

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
vowel_words = words_starting_with_vowel(sentence)
print(vowel_words)


'''
In this function, the regular expression pattern r'\b[aeiouAEIOU][a-zA-Z]*\b' is used to match words that start with a vowel. Here's a breakdown of the pattern:

\b: Matches a word boundary to ensure that we are matching whole words.
[aeiouAEIOU]: Matches any vowel (lowercase or uppercase) at the beginning of a word.
[a-zA-Z]*: Matches zero or more characters (letters) after the vowel.
\b: Matches another word boundary to ensure that the word ends.
The re.findall() function is then used to find all matching words in the sentence.
'''