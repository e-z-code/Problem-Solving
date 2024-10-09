'''
BOJ 28381 - Mischievous Math (https://www.acmicpc.net/problem/28381)

Given D, determine three numbers (A, B, C) that satisfy the following conditions.

(1) A, B, C, and D are distinct.
(2) It is impossible to find an arithmetic expression using A, B, and C at most once such that the result equals D.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

goal = int(sys.stdin.readline())

if goal >= 10:
    print(1, 2, 3)
else:
    print(11, 23, 59)