'''
BOJ 13531 - Secret Santa (https://www.acmicpc.net/problem/13531)

There is an array A. You shuffle the array and get a new array B.
Determine the probability that A[i] = B[i] for some i.
'''

import sys


# 1. TO GET FACTORIAL AND DERANGEMENT PERMUTATION
# D[n] = (n - 1) * (D[n-1] + D[n-2])

factorial = [1, 1, 2]
for num in range(3, 11):
    factorial.append(factorial[-1] * num)

derangement = [0, 0, 1]
for num in range(3, 11):
    derangement.append((num - 1) * (derangement[-1] + derangement[-2]))


# 2. TO SOLVE THE PROBLEM

num = int(sys.stdin.readline())

if num >= 10:
    num = 10
print(1 - derangement[num] / factorial[num])