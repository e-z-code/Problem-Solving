'''
BOJ 14811 - Parenting Partnering (Small) (https://www.acmicpc.net/problem/14811)

Cameron and Jamie want to be in charge of the baby for exactly 12 hours per day.
Given their daily routine, determine the minimum number of exchanges possible.
The number of activities in the daily routine will not exceed 2.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(1, test_count+1):
    
    father_work_count, mother_work_count = map(int, sys.stdin.readline().split())
    
    father_sched = []
    for father_work in range(father_work_count):
        start, end = map(int, sys.stdin.readline().split())
        father_sched.append((start, end))
    father_sched.sort()
    
    mother_sched = []
    for mother_work in range(mother_work_count):
        start, end = map(int, sys.stdin.readline().split())
        mother_sched.append((start, end))
    mother_sched.sort()
    
    
    # 2. TO SOLVE THE PROBLEM
    
    ans = 0
    
    if father_work_count == 0:
        if mother_work_count == 1:
            ans = 2
        else:
            if mother_sched[1][1] - mother_sched[0][0] <= 720 or mother_sched[0][1] + 1440 - mother_sched[1][0] <= 720:
                ans = 2
            else:
                ans = 4
    elif father_work_count == 1:
        if mother_work_count == 0:
            ans = 2
        else:
            ans = 2
    else:
        if father_sched[1][1] - father_sched[0][0] <= 720 or father_sched[0][1] + 1440 - father_sched[1][0] <= 720:
            ans = 2
        else:
            ans = 4
    
    print("Case #{}: {}".format(test, ans))