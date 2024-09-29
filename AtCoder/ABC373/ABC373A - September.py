'''
ABC373A - September (https://atcoder.jp/contests/abc373/tasks/abc373_a)

There are 12 strings: S[1], S[2], ..., S[12].
Determine the number of integers X such that len(S[X]) = X.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

ans = 0

for length in range(1, 13):
    word = sys.stdin.readline().strip()
    if len(word) == length:
        ans += 1

print(ans)