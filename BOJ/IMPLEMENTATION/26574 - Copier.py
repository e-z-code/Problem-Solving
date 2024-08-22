'''
BOJ 26574 - Copier (https://www.acmicpc.net/problem/26574)

Copy a given number.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())
for test in range(test_count):
    num = int(sys.stdin.readline())
    print(num, num)