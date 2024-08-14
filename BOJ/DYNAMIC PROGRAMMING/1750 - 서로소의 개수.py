'''
BOJ 1750 - Number of Co-prime Pairs (https://www.acmicpc.net/problem/1750)

Given an array, determine a number of subsequences that are a co-prime pair.
'''

import sys
from math import gcd


# 1. TO GET THE INPUT

arr_length = int(sys.stdin.readline())
arr = []
for idx in range(arr_length):
    num = int(sys.stdin.readline())
    arr.append(num)


# 2. DYNAMIC PROGRAMMING
# dp[i][j] = The number of pairs of which gcd is j when considered until index i

dp = [[0 for common_divisor in range(100001)] for idx in range(arr_length)]

for idx in range(arr_length):
    
    num = arr[idx]
    dp[idx][num] = 1
    
    if idx != 0:
        for common_divisor in range(100001):
            # When a number is not included in a subsequence
            dp[idx][common_divisor] += dp[idx-1][common_divisor]
            dp[idx][common_divisor] %= 10000003
            # When a number is included in a subsequence
            next_common_divisor = gcd(common_divisor, num)
            dp[idx][next_common_divisor] += dp[idx-1][common_divisor]
            dp[idx][next_common_divisor] %= 10000003

print(dp[-1][1])