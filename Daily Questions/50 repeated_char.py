'''
Find the first non-repeated character
'''

def repeated_char(string):
    for char in string:
        print(char)
        if(string.count(char)) == 1:
            return char
        
s = "teeteracdacdacd"
print("Repeated String= ",repeated_char(s))