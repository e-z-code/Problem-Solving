'''
BOJ 21737 - SMUPC Calculator (https://www.acmicpc.net/problem/21737)

Implement a calculator that uses 'S', 'M', 'U', 'P', and 'C' instead of '-', '*', '/', '+', and 'return'.
'''

import sys


# 1. TO GET THE INPUT

operator_count = int(sys.stdin.readline())
expression = sys.stdin.readline().strip()


# 2. TO TOKENIZE THE EXPRESSION

token = []

now_num = 0
for char in expression:
    if 48 <= ord(char) <= 57:
        now_num = now_num * 10 + int(char)
    else:
        token.append(now_num)
        now_num = 0
        token.append(char)

# If the result is not printed, there is no need to calculate.
while len(token) > 0 and token[-1] != "C":
    token.pop()


# 3. TO CALCULATE THE RESULT

if len(token) == 0:
    print("NO OUTPUT")
else:
    
    result = token[0]

    for idx in range(len(token)):
        if type(token[idx]) != int:
            op = token[idx]
            if op == "S":
                result -= token[idx+1]
            elif op == "M":
                result *= token[idx+1]
            elif op == "U":
                if result * token[idx+1] < 0:
                    result = (result * (-1) // token[idx+1]) * (-1)
                else:
                    result = result // token[idx+1]
            elif op == "P":
                result += token[idx+1]
            else:
                print(result, end = ' ')