'''
BOJ 26020 - Jesting Jabberwocky (https://www.acmicpc.net/problem/26020)

Given cards, you can repeatedly pick a card and insert it somewhere else.
Determine the minimum number of moves to sort cards by suit.
'''

import sys
from itertools import permutations
inf = float('inf')


# 1. TO GET THE INPUT

cards = list(sys.stdin.readline().strip())
kinds = list(set(cards))


# 2. TO SOLVE THE PROBLEM
# dp[i][j] = The minimum number of cards to remove such that the first i cards are sorted and the last card is of suit j.

ans = inf

for permutation in permutations(kinds, len(kinds)):
    
    dp = [[inf for suit in range(len(kinds) + 1)] for idx in range(len(cards) + 1)]
    for suit in range(len(kinds) + 1):
        dp[0][suit] = 0

    for i in range(1, len(cards) + 1):
        for j in range(1, len(kinds) + 1):
            
            if cards[i-1] == permutation[j-1]:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1])

    ans = min(ans, dp[-1][-1])

print(ans)