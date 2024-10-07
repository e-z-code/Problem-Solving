'''
BOJ 26075 - Do not cross the line (https://www.acmicpc.net/problem/26075)

There are two binary strings of the same length: S and T.
You can swap adjacent two characters for a string.
Suppose you performed the swap operation X times on S and Y times on T to make S = T.
Determine the minimum value of X ^ 2 + Y ^ 2.
'''


import sys


# 1. TO GET THE INPUT

zero_count, one_count = map(int, sys.stdin.readline().split())

stringA = sys.stdin.readline().strip()
stringB = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM

zeroA = []
zeroB = []
for idx in range(zero_count + one_count):
    if stringA[idx] == "0":
        zeroA.append(idx)
    if stringB[idx] == "0":
        zeroB.append(idx)

swap_count = 0
for idx in range(zero_count):
    swap_count += abs(zeroA[idx] - zeroB[idx])

if swap_count % 2 == 0:
    print(pow(swap_count // 2, 2) * 2)
else:
    print(pow(swap_count // 2, 2) + pow(swap_count // 2 + 1, 2))