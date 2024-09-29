'''
ABC373B - 1D Keyboard (https://atcoder.jp/contests/abc373/tasks/abc373_b)

Given a keyboard, calculate the minimum distance to type 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

key = sys.stdin.readline().strip()

ans = 0
for ascii in range(66, 91):
    ans += abs(key.index(chr(ascii)) - key.index(chr(ascii - 1)))
print(ans)