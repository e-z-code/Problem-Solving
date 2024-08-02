'''
BOJ 16654 - Generalized German Quotation (https://www.acmicpc.net/problem/16654)

In German, <<>> and >><< are both valid quote marks.
Given a string, determine whether the string is correct and restore it if so. 
'''

import sys


# 1. TO GET THE INPUT 

quote = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM

open_mark = None

ans = ""
stack = []

for idx in range(0, len(quote), 2):
    
    mark = quote[idx]
    
    if len(stack) == 0:
        open_mark = mark
        stack.append(mark)
        ans += "["
    else:
        if mark != open_mark:
            stack.pop()
            ans += "]"
        else:
            stack.append(mark)
            ans += "["

if len(stack) != 0:
    print("Keine Loesung")
else:
    print(ans)