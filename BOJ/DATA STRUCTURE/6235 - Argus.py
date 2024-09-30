'''
BOJ 6235 - Argus (https://www.acmicpc.net/problem/6235)

A query P Q prints every Q minute.
Output first K results.
'''

import sys, heapq


# 1. TO GET THE INPUT

instructions = []

while True:
    instruction = list(sys.stdin.readline().strip().split())
    if instruction[0] == "#":
        break
    else:
        register, query_id, period = instruction
        query_id = int(query_id)
        period = int(period)
        heapq.heappush(instructions, (period, query_id, period))


# 2. TO SOLVE THE PROBLEM

return_count = int(sys.stdin.readline())

while return_count > 0:
    
    period, query_id, interval = heapq.heappop(instructions)
    print(query_id)
    heapq.heappush(instructions, (period + interval, query_id, interval))
    
    return_count -= 1