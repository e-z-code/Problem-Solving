'''
BOJ 12911 - Favorite Array (https://www.acmicpc.net/problem/12911)

Your favorite array satisfies following characteristics.

(1) The length of the array is N.
(2) Each element X satisfies 1 <= X <= K.
(3) For every i (1 <= i < N), A[i-1] <= A[i] or A[i-1] % A[i] != 0

Given N and K, determine the number of different favorite arrays.
'''

import sys
mod = 10 ** 9 + 7


# 1. TO GET THE INPUT

arr_length, max_num = map(int, sys.stdin.readline().split())


# 2. DYNAMIC PROGRAMMING
# dp[X][Y] = Number of arrays when the length is X and the array ends with Y.

dp = [[0 for end_num in range(max_num+1)] for length in range(arr_length+1)]

for end_num in range(1, max_num+1):

    dp[1][end_num] = 1

for length in range(2, arr_length+1):
    
    total_case = sum(dp[length-1])
    
    # If A[i-1] > A[i] and A[i-1] % A[i] == 0, then the case is invalid.
    for end_num in range(1, max_num+1):
        now_case = total_case
        for multiple in range(end_num*2, max_num+1, end_num):
            now_case = (now_case - dp[length-1][multiple]) % mod
        dp[length][end_num] = now_case

print(sum(dp[arr_length]) % mod)