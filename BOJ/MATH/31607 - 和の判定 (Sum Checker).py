'''
BOJ 31607 - Sum Checker (https://www.acmicpc.net/problem/31607)

Given three integers, determine if an integer is the sum of the others.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

nums = []
for idx in range(3):
    num = int(sys.stdin.readline())
    nums.append(num)

if sum(nums) == 2 * max(nums):
    print(1)
else:
    print(0)