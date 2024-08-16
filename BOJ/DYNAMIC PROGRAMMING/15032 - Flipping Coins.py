'''
BOJ 15032 - Flipping Coins (https://www.acmicpc.net/problem/15032)

There are N coins lined up in a row, initially heads facing down.
For exactly K times, you can choose a coin and toss it into the air.
Determine the maximum expected number of heads-up coins after K tosses.
'''

import sys
from fractions import Fraction


# 1. TO GET THE INPUT

coin_count, toss_count = map(int, sys.stdin.readline().split())


# 2. DYNAMIC PROGRAMMING
# dp[i][j] = Probability that the number of heads-up coins equals j after i tosses.

dp = [[Fraction(0, 1) for head_coin in range(coin_count + 1)] for toss in range(toss_count + 1)]
dp[0][0] = Fraction(1, 1)

for toss in range(toss_count):
    for head_coin in range(coin_count + 1):
        if head_coin == coin_count:
            dp[toss+1][head_coin] += dp[toss][head_coin] / 2
            dp[toss+1][head_coin-1] += dp[toss][head_coin] / 2
        else:
            dp[toss+1][head_coin] += dp[toss][head_coin] / 2
            dp[toss+1][head_coin+1] += dp[toss][head_coin] / 2


# 3. TO SOLVE THE PROBLEM

ans = 0

for head_coin in range(coin_count + 1):
    ans += head_coin * dp[toss_count][head_coin]

print(float(ans))