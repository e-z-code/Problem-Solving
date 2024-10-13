'''
BOJ 23325 - Magic Thousand Characters (https://www.acmicpc.net/problem/23325)

Given an ambiguous arithmetic expression of '+' and '-', determine the maximum possible value.
'''

import sys
inf = float('inf')


# 1. TO GET THE INPUT

arr = list(sys.stdin.readline().strip())


# 2. DYNAMIC PROGRAMMING
# dp[i] = The maximum result when i-th index is interpreted as a part of number

dp = [-inf for idx in range(len(arr))]

for idx in range(len(arr)):
    
    if idx == 0:
        if arr[idx] == "+":
            dp[idx] = 10
        else:
            dp[idx] = 1
    
    elif idx == 1:
        if arr[idx-1] == "+" and arr[idx] == "-":
            dp[idx] = 11
    
    elif idx == 2:
        
        if arr[idx] == "+":
            if arr[idx-1] == "-":
                dp[idx] = dp[idx-2] - 10
            else:
                dp[idx] = dp[idx-2] + 10
        else:
            if arr[idx-1] == "-":
                dp[idx] = dp[idx-2] - 1
            else:
                dp[idx] = dp[idx-2] + 1
    
    else:
        
        if arr[idx] == "+":
            if arr[idx-1] == "-":
                dp[idx] = dp[idx-2] - 10
            else:
                dp[idx] = dp[idx-2] + 10
        else:
            if arr[idx-1] == "-":
                dp[idx] = dp[idx-2] - 1
            else:
                dp[idx] = dp[idx-2] + 1
                if arr[idx-2] == "+":
                    dp[idx] = max(dp[idx], dp[idx-3] + 11)
                else:
                    dp[idx] = max(dp[idx], dp[idx-3] - 11)

print(dp[-1])