'''
BOJ 14651 Lemon Three - (https://www.acmicpc.net/problem/14651)

Print the number of multiples of 3 of length N consisting of 0, 1, 2. 
'''

import sys

# 1. DYNAMIC PROGRAMMING
# The sum of all digits of a multiple of 3 is also a multiple of 3. 
# dp[i][j] = The number of length i of which the sum of all digits mod 3 equal j. 

mod = 10 ** 9 + 9

dp = [[0 for j in range(3)] for i in range(40000)]
dp[1] = [0, 1, 1]
for i in range(2, 40000):
    dp[i][0] = sum(dp[i-1]) % mod
    dp[i][1] = sum(dp[i-1]) % mod
    dp[i][2] = sum(dp[i-1]) % mod


# 2. TO SOLVE THE PROBLEM

length = int(sys.stdin.readline())
print(dp[length][0])