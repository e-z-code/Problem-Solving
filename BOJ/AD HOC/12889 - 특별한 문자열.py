'''
BOJ 12889 - Special String (https://www.acmicpc.net/problem/12889)

A binary string S is special if U is always lexicographically smaller than V when S = UV.
Given a special binary string X, determine the special binary string Y that comes right after X in lexicographical order.
'''

import sys

def valid(string):
    
    result = True
    for idx in range(1, length):
        if string[:idx] >= string[idx:]:
            result = False
            break
    return result


string = sys.stdin.readline().strip()
length = len(string)

if length == 1:
    if string == "0":
        print(1)
    else:
        print(-1)
else:
    if string == "0" + "1" * (length - 1):
        print(-1)
    else:
        
        string = list(string)
        
        last_zero = length - 1
        while string[last_zero] != "0":
            last_zero -= 1
        string[last_zero] = "1"
        
        for idx in range(last_zero + 1, length - 1):
            string[idx] = "0"
            if not valid("".join(string)):
                string[idx] = "1"
        
        print("".join(string))