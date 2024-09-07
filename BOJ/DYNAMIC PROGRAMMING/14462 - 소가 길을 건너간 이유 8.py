'''
BOJ 14462 - Why Did the Cow Cross the Road II (Gold) (https://www.acmicpc.net/problem/14462)

There are N cows on each side of the road.
Farmer John wants to connect a cow on one side to a cow on the other side.
Each field can be accessible via at most one crosswalk, and the difference between two cows must not exceed 4.
Determine the maximum number of crosswalks.
'''

import sys


# 1. TO GET THE INPUT

cow_count = int(sys.stdin.readline())

left = []
right = []

for left_cow in range(cow_count):
    cow = int(sys.stdin.readline())
    left.append(cow)
for right_cow in range(cow_count):
    cow = int(sys.stdin.readline())
    right.append(cow)


# 2. DYNAMIC PROGRAMMING - LCS 

dp = [[0 for j in range(cow_count + 1)] for i in range(cow_count + 1)]

for i in range(1, cow_count + 1):
    for j in range(1, cow_count + 1):
        
        if abs(left[i-1] - right[j-1]) <= 4:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])