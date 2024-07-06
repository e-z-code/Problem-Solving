'''
BOJ 7453 - Four integers that the sum is 0 (https://www.acmicpc.net/problem/21662)

Given integer arrays A, B, C, and D, print the number of pairs (a, b, c, d) so that A[a] + B[b] + C[c] + D[d] = 0.
'''

import sys


# 1. TO GET THE INPUT

A = []
B = []
C = []
D = []

length = int(sys.stdin.readline())
for idx in range(length):
    numA, numB, numC, numD = map(int, sys.stdin.readline().split())
    A.append(numA)
    B.append(numB)
    C.append(numC)
    D.append(numD)


# 2. MEET IN THE MIDDLE

AB = {}

for i in range(length):
    for j in range(length):
        num = A[i] + B[j]
        AB[num] = AB.get(num, 0) + 1

ans = 0
for i in range(length):
    for j in range(length):
        num = C[i] + D[j]
        ans += AB.get(-num, 0)
print(ans)