'''
BOJ 2688 - Not Decreasing (https://www.acmicpc.net/problem/2688)

Given N, calculate how many numbers of N digits are non-decreasing.
Leading zero is allowed.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length = int(sys.stdin.readline())
    
    
    # 2. TO SOLVE THE PROBLEM
    # dp[i][j] = Non-decreasing numbers of length i of which end digit is j
    
    dp = [[0 for end_digit in range(10)] for now_length in range(length + 1)]
    
    for now_length in range(1, length+1):
        for end_digit in range(10):
            if now_length == 1:
                dp[now_length][end_digit] = 1
            else:
                for last_end_digit in range(end_digit + 1):
                    dp[now_length][end_digit] += dp[now_length - 1][last_end_digit]
    
    print(sum(dp[-1]))