'''
Write a python function to replace all occurrence of ':)' in a string with a smiley face emoji?
'''

def replace_smileys(text):
    return text.replace(':)', '😊')

# Test the function
text = "Hello :) How are you? :)"
new_text = replace_smileys(text)
print(new_text)
