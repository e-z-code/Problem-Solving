'''
BOJ 5977 - Moving the Lawn (https://www.acmicpc.net/problem/5977)

There is an array A of length N.
You cannot choose more than K consecutive elements.
Determine the maximum value of the sum of chosen elements.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

arr_length, max_count = map(int, sys.stdin.readline().split())

prefix_sum = [0]
for idx in range(arr_length):
    num = int(sys.stdin.readline())
    prefix_sum.append(prefix_sum[-1] + num)


# 2. DYNAMIC PROGRAMMING

# Let dp[N] = (The maximum value of the sum of chosen elements when indices up to N are considered.)
# dp[N] = prefix_sum[N] + max(dp[N-i-1] - prefix_sum[N-i]) (0 <= i <= K)

# Deque is used to reduce time complexity when calculating local maximum.

dp = [0 for idx in range(arr_length + 1)]
subarray = deque([])

for idx in range(1, arr_length + 1):
    
    # Deque Trick
    
    val = dp[idx-1] - prefix_sum[idx]
    
    while len(subarray) != 0 and subarray[0][1] < idx - max_count:
        subarray.popleft()
    while len(subarray) != 0 and subarray[-1][0] <= val:
        subarray.pop()
    subarray.append((val, idx))
    
    if idx <= max_count:
        dp[idx] = prefix_sum[idx]
    else:
        dp[idx] = prefix_sum[idx] + subarray[0][0]

print(dp[-1])