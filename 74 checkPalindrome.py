'''
Write a function called is_palindrome that takes a string as an argument and returns True if it's a palindrome, and False otherwise. A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backward as forwards, such as madam or racecar.
'''

def is_palindrome(s: str) -> bool:
    # Remove any spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))
