'''
BOJ 21479 - Number (https://www.acmicpc.net/problem/21479)

Given N non-negative integers, calculate the largest number possible by concatenating N numbers.
'''

import sys
from functools import cmp_to_key


# 1. COMPARE FUNCTION

def compare(x, y):
    if x + y >= y + x:
        return -1
    else:
        return 1


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

arr = []
count = 100

while count:
    num = sys.stdin.readline().strip()
    arr.append(num)
    count -= 1

ans = sorted(arr, key = cmp_to_key(compare))
print("".join(ans))