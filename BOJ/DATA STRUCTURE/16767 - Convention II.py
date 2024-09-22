'''
BOJ 16767 - Convention II (https://www.acmicpc.net/problem/16767)

You are given information on N cows, which will arrive on X and take Y before leaving the queue.
If multiple cows wait, the cow with the highest seniority becomes the next one to leave.
Determine the longest time a cow will wait.
'''

import sys, heapq
from collections import deque


# 1. TO GET THE INPUT

cow_count = int(sys.stdin.readline())

cows = []
for cow in range(cow_count):
    arrival_time, eat_time = map(int, sys.stdin.readline().split())
    cows.append((arrival_time, eat_time, cow))
cows.sort()


# 2. TO SOLVE THE PROBLEM

cows = deque(cows)

ans = 0
time = 0
waiting = []

while cows:
    
    # Choose a cow when there is no waiting cow
    arrival_time, eat_time, priority = cows.popleft()
    time = arrival_time + eat_time
    
    while True:
        # Simulate which cow is in a waiting list
        while len(cows) > 0 and cows[0][0] <= time:
            next_arrival_time, next_eat_time, next_priority = cows.popleft()
            heapq.heappush(waiting, (next_priority, next_arrival_time, next_eat_time))
        # If no cow waits, choose a new one
        if len(waiting) == 0:
            break
        # Choose next cow among waiting list 
        chosen_priority, chosen_arrival_time, chosen_eat_time = heapq.heappop(waiting)
        ans = max(ans, time - chosen_arrival_time)
        time += chosen_eat_time
    
print(ans)