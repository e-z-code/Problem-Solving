'''
BOJ 10375 - Digits (https://www.acmicpc.net/problem/10375)

Given N, calculate the minimum possible total sum of N positive number with equal sum of digits.
'''

import sys


# 1. PRE-PROCESSING

sum_of_num = [0 for sum_of_digit in range(64)]
count = [0 for sum_of_digit in range(64)]

ans = [float('inf') for length in range(5001)]

now = 1
while now != 1000001:
    
    sum_of_digit = sum(list(map(int, list(str(now)))))
    sum_of_num[sum_of_digit] += now
    count[sum_of_digit] += 1
    if count[sum_of_digit] <= 5000:
        ans[count[sum_of_digit]] = min(ans[count[sum_of_digit]], sum_of_num[sum_of_digit])
    
    now += 1


# 2. TO SOLVE THE PROBLEM

sum_of_digit = int(sys.stdin.readline())
print(ans[sum_of_digit])