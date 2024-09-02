'''
BOJ 14279 - Multiple (https://www.acmicpc.net/problem/14279)

You are given three positive integers: a, b, and c.
Choose A, B, and C so that |A - a| + |B - b| + |C - c| becomes minimum.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

numA, numB, numC = map(int, sys.stdin.readline().split())

ans = float('inf')
for x in range(1, 10 ** 6 + 1):
    for y in range(1, 10 ** 6 + 1):
        ans = min(ans, abs(numA - x) + abs(numB - y) + abs(numC - x * y))
        if x * y > numC:
            break

print(ans)