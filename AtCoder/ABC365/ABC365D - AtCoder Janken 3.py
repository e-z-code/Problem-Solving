'''
ABC365D - AtCoder Janken 3 (https://atcoder.jp/contests/abc365/tasks/abc365_d)

You and Aoki played rock-paper-scissors N times.
You never lost to Aoki and made the same move consecutively.
Given Aoki's move, determine the maximum number of games you won.
'''

import sys


# 1. TO GET THE INPUT

match_count = int(sys.stdin.readline())
aoki_move = sys.stdin.readline().strip()


# 2. DYNAMIC PROGRAMMING
# Index : 0 - Rock, 1 - Scissors, 2 - Paper

dp = [[0, 0, 0] for idx in range(match_count)]

for idx in range(match_count):
    
    if idx == 0:
        if aoki_move[idx] == "S":
            dp[idx][0] = 1
        elif aoki_move[idx] == "P":
            dp[idx][1] = 1
        else:
            dp[idx][2] = 1
    else:
        if aoki_move[idx] == "S":
            dp[idx][0] = max(dp[idx-1][1], dp[idx-1][2]) + 1
            dp[idx][1] = max(dp[idx-1][0], dp[idx-1][2])
        elif aoki_move[idx] == "P":
            dp[idx][1] = max(dp[idx-1][0], dp[idx-1][2]) + 1
            dp[idx][2] = max(dp[idx-1][0], dp[idx-1][1])
        else:
            dp[idx][0] = max(dp[idx-1][1], dp[idx-1][2])
            dp[idx][2] = max(dp[idx-1][0], dp[idx-1][1]) + 1

print(max(dp[-1]))