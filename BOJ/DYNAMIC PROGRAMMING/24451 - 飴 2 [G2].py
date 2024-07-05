'''
BOJ 24451 - Candy 2 (https://www.acmicpc.net/problem/24451)

There are N candies. 
You can eat at most 2 candies among K consecutive candies.
Determine the maximum sum of the value of candies you eat. 
'''

import sys


# 1. TO GET THE INPUT

candy_count, range_length = map(int, sys.stdin.readline().split())
candy = list(map(int, sys.stdin.readline().split()))


# 2. DYNAMIC PROGRAMMING
# dp[i][j] = The maximum sum of the value of candies when eat i-th candy after 1 ~ j-th candy.

dp = [[0 for last in range(candy_count)] for now in range(candy_count)]

for now in range(candy_count):
    
    for last in range(now):
        
        if now < range_length:
            dp[now][last] = candy[now] + candy[last]
        
        else:
            if now - last >= range_length:
                dp[now][last] = dp[last][last-1] + candy[now]
            else:
                if now - range_length >= 0:
                    dp[now][last] = max(dp[last][now-range_length], candy[last]) + candy[now]
    
    for last in range(1, now):
        
        dp[now][last] = max(dp[now][last], dp[now][last-1])


# 3. TO SOLVE THE PROBLEM

ans = 0

for row in dp:
    ans = max(ans, max(row))

print(ans)