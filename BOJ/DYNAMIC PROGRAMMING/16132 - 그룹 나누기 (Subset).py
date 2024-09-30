'''
BOJ 16132 - Group Division (https://www.acmicpc.net/problem/16132)

Determine the number of ways to divide [1, 2, ..., N] into two arrays such that the sum is equal.
'''

import sys


# 1. TO GET THE INPUT 

max_num = int(sys.stdin.readline())
total = max_num * (max_num + 1) // 2


# 2. TO SOLVE THE PROBLEM - DP
# dp[i][j] = The number of cases when the biggest number is i and sum is j.

dp = [[0 for sum in range(1251)] for num in range(max_num+1)]

for now_num in range(max_num + 1):
    
    if now_num == 0:
        dp[0][0] = 1
    else:
        for last_num in range(now_num):
            for last_sum in range(1251):
                if last_sum + now_num <= 1250:
                    dp[now_num][last_sum + now_num] += dp[last_num][last_sum]

ans = 0
if total % 2 == 0:
    for num in range(max_num + 1):
        ans += dp[num][total // 2]
print(ans // 2)