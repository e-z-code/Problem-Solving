'''
BOJ 22625 - Erratic Sleep Habits (https://www.acmicpc.net/problem/22625)

You sleep at midnight every day and have a sleeping cycle.
You have job interviews this month and do not want to miss any.
If you take caffeine, your sleep cycle will reset and start from day 1.
Given the job interview schedule, determine the minimum amount of caffeine required. 
'''

import sys
inf = float('inf')


# 1. TO GET THE INPUT

cycle_length = int(sys.stdin.readline())
cycle = [0] + list(map(int, sys.stdin.readline().split()))

interview_count = int(sys.stdin.readline())
earliest_interview = [24 for day in range(101)]
for interview in range(interview_count):
    day, time = map(int, sys.stdin.readline().split())
    earliest_interview[day] = min(earliest_interview[day], time)


# 2. TO SOLVE THE PROBLEM

dp = [[inf for day_in_cycle in range(cycle_length + 1)] for day in range(101)]

if cycle[1] <= earliest_interview[1]:
    dp[1][1] = 0

for day in range(2, 101):
    for day_in_cycle in range(1, cycle_length + 1):
        
        if day_in_cycle <= day:
            if cycle[day_in_cycle] <= earliest_interview[day]:
                if day_in_cycle == 1:
                    dp[day][day_in_cycle] = min(min(dp[day-1]) + 1, dp[day-1][cycle_length])
                else:
                    dp[day][day_in_cycle] = dp[day-1][day_in_cycle-1]

print(min(dp[-1]))