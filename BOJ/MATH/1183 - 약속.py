'''
BOJ 1183 - Appointment (https://www.acmicpc.net/problem/1183)

There are two arrays: A and B. You can add T to all numbers of A.
Determine the number of T that minimizes the sum(abs(A[i] - B[i])).
'''

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())

diff = []
for idx in range(length):
    scheduled_time, arrival_time = map(int, sys.stdin.readline().split())
    diff.append(scheduled_time - arrival_time)


# 2. TO SOLVE THE PROBLEM
# For sum(abs(diff)) to be the minimum, there must be an equal number of negative numbers and non-negative numbers.

if length % 2 == 1:
    print(1)
else:
    diff.sort()
    print(diff[length // 2] - diff[length // 2 - 1] + 1)