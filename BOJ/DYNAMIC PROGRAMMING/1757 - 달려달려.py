'''
BOJ 1717 - Run Run (https://www.acmicpc.net/problem/1717)

You can run D[I] meters at time I.
Your fatigue increases by one if you run for a minute and decreases if you rest for a minute.
You cannot run when your fatigue is above M. 
Once you rest, you cannot run until fatigue becomes 0.
Your fatigue must be 0 when you finish the run.
Determine the maximum distance you can run. 
'''

import sys


# 1. TO GET THE INPUT

time_count, max_fatigue = map(int, sys.stdin.readline().split())

distance = []
for time in range(time_count):
    dist = int(sys.stdin.readline())
    distance.append(dist)


# 2. DYNAMIC PROGRAMMING
# dp[i][j][X] = Maximum distance at time i with fatigue of j (X = 0 : Rest, X = 1 : Run)

now_dp = [[0, 0] for fatigue in range(max_fatigue + 1)]
now_dp[0][0] = 0
now_dp[0][1] = distance[0]

for time in range(1, time_count):
    
    next_dp = [[0, 0] for fatigue in range(max_fatigue + 1)]
    
    for fatigue in range(max_fatigue + 1):
        
        # Rest Start
        if fatigue != 0:
            next_dp[fatigue][0] = max(next_dp[fatigue][0], now_dp[fatigue-1][1])
        # Rest Continue
        if fatigue != max_fatigue:
            next_dp[fatigue][0] = max(next_dp[fatigue][0], now_dp[fatigue][0], now_dp[fatigue+1][0])
        # Run Start
        if fatigue == 0:
            next_dp[fatigue][1] = max(next_dp[fatigue][1], now_dp[fatigue+1][0] + distance[time])
        # Run Continue
        if fatigue != max_fatigue:
            next_dp[fatigue][1] = max(next_dp[fatigue][1], now_dp[fatigue-1][1] + distance[time])
    
    now_dp = next_dp

print(max(now_dp[0][0], now_dp[1][0]))