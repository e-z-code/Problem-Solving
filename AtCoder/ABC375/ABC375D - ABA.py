'''
ABC375D - ABA (https://atcoder.jp/contests/abc375/tasks/abc375_d)

Given a string S, calculate the number of (i, j, k) such that S[i] + S[j] + S[k] is a palindrome.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

string = sys.stdin.readline().strip()

ans = 0

for ascii in range(65, 91):
    
    alphabet = chr(ascii)
    loc = []

    for idx in range(len(string)):
        if string[idx] == alphabet:
            loc.append(idx)
    
    for idx in range(1, len(loc)):
        ans += (loc[idx] - loc[idx-1] - 1) * idx * (len(loc) - idx)
        ans += idx * (len(loc) - idx - 1)

print(ans)