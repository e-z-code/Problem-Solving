'''
CF956A - Array Divisibility (https://codeforces.com/contest/1983/problem/A)

Construct an array such that the sum of A[Y] for all Y, a multiple of X, is a multiple of X for all X.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM
# [1, 2, ..., N] satisfies the condition.

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length = int(sys.stdin.readline())
    for num in range(1, length+1):
        print(num, end = ' ')
    print()