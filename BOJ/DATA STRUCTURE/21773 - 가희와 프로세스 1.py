'''
BOJ 21773 - Gahui and Process 1 (https://www.acmicpc.net/problem/21773)

Implement a priority scheduler.
If there are processes with the same priority, choose a process with the lowest ID.
If a process is chosen, the priorities of the others increase by 1.
'''

import sys, heapq


# 1. TO GET THE INPUT

time_count, process_count = map(int, sys.stdin.readline().split())

priority_queue = []
for process in range(process_count):
    process_id, time_left, priority = map(int, sys.stdin.readline().split())
    heapq.heappush(priority_queue, (-priority, process_id, time_left))


# 2. TO SIMULATE THE SCHEDULER

for time in range(time_count):
    
    priority, process_id, time_left = heapq.heappop(priority_queue)
    print(process_id)
    
    priority += 1
    time_left -= 1
    if time_left != 0:
        heapq.heappush(priority_queue, (priority, process_id, time_left))