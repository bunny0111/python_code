'''
Input Format: N = 6
Result:   
1
01
101
0101
10101
010101
'''

def generate_pattern(n):
    for i in range(1, n+1):
        start_char = '1' if i % 2 != 0 else '0'
        pattern_line = ''
        for j in range(i):
            pattern_line += start_char
            start_char = '0' if start_char == '1' else '1'
        print(pattern_line)

n = 6
generate_pattern(n)