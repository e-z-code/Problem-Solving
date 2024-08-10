'''
BOJ 8673 - Taps (https://www.acmicpc.net/problem/8673)

There are N water taps. Water flows from a tap if the temperature of the tap is above zero.
The temperature of the tank is the average temperature of all the taps from which water flows.
Determine the minimum number of taps to close to make the temperature equal to or greater than W.
'''

import sys


# 1. TO GET THE INPUT

tap_count, goal_temp = map(int, sys.stdin.readline().split())
tap_temp = list(map(int, sys.stdin.readline().split()))

tap_temp.sort(reverse=True)


# 2. TO SOLVE THE PROBLEM

if tap_temp[0] < goal_temp:
    print("NIE")
else:
    
    ans = 0
    
    temp_sum = 0
    for idx in range(tap_count):
        if tap_temp[idx] > 0:
            temp_sum += tap_temp[idx]
            if temp_sum < goal_temp * (idx + 1):
                ans += 1
    
    print(ans)
