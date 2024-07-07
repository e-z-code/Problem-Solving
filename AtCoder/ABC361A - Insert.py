'''
ABC361A - Insert (https://atcoder.jp/contests/abc361/tasks/abc361_a)

Given a number and an array, insert the number at the given index.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

length, idx, num = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr = arr[:idx] + [num] + arr[idx:]
for num in arr:
    print(num, end = ' ')