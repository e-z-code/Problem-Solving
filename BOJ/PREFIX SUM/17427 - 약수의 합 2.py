'''
BOJ 17427 - Sum of Divisors 2 (https://www.acmicpc.net/problem/17427)

Given N, f(N) is the sum of all divisors of N.
When g(N) = f(1) + f(2) + ... + f(N), calculate g(N).
'''

import sys


# 1. TO CALCULATE f(N) for all possible N.

N = int(sys.stdin.readline())

divisor_sum = [0 for num in range(N + 1)]

for num in range(1, N + 1):
    for multiple in range(num, N + 1, num):
        divisor_sum[multiple] += num


# 2. TO CALCULATE g(N) AND SOLVE THE PROBLEM

prefix_sum = [0 for num in range(N + 1)]

for num in range(1, N + 1):
    prefix_sum[num] = prefix_sum[num-1] + divisor_sum[num]

print(prefix_sum[N])