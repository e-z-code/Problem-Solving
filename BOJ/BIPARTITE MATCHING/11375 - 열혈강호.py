'''
BOJ 11375 - The Ruler of the Company (https://www.acmicpc.net/problem/11375)

There are N workers and M assignments.
Each worker can do only one job. Each assignment should be assigned to a worker.
Determine the maximum number of assignments workers can do.
'''

import sys


# 2. BIPARTITE MATCHING 

def bimatch(worker):
    
    # To prevent infinite loop
    if visited[worker]:
        return False
    visited[worker] = 1
    
    result = False
    
    # If the work is assigned or the assigned worker can be re-assigned, then the work can be assigned.
    for work in graph[worker]:
        if assigned[work] == -1 or bimatch(assigned[work]):
            assigned[work] = worker
            result = True
            break
    
    return result


# 1. TO GET THE INPUT

worker_count, work_count = map(int, sys.stdin.readline().split())

graph = {}
for worker in range(worker_count):
    capable_work = list(map(int, sys.stdin.readline().split()))[1:]
    graph[worker] = capable_work

assigned = [-1 for work in range(work_count+1)]


# 3. TO SOLVE THE PROBLEM

for worker in range(worker_count):
    visited = [0 for worker in range(worker_count)]
    bimatch(worker)

ans = 0
for work in range(work_count+1):
    if assigned[work] != -1:
        ans += 1
print(ans)