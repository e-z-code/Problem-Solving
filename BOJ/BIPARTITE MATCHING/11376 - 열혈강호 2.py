'''
BOJ 11376 - The Ruler of the Company 2 (https://www.acmicpc.net/problem/11376)

There are N workers and M assignments.
Each worker can do only one job. Each assignment should be assigned to a worker.
Determine the maximum number of assignments workers can do.
'''

import sys


# 2. BIPARTITE MATCHING

def bimatch(worker):
    
    if visited[worker]:
        return False
    visited[worker] = True
    
    result = False
    for work in graph[worker]:
        if assigned_worker[work] == -1 or bimatch(assigned_worker[work]):
            assigned_worker[work] = worker
            result = True
            break
    return result


# 1. TO GET THE INPUT

worker_count, work_count = map(int, sys.stdin.readline().split())

graph = {}
for worker in range(worker_count):
    capable_work = list(map(int, sys.stdin.readline().split()))[1:]
    graph[worker*2] = capable_work
    graph[worker*2 + 1] = capable_work

assigned_worker = [-1 for work in range(work_count + 1)]


# 3. TO SOLVE THE PROBLEM

for worker in range(2 * worker_count):
    visited = [False for worker in range(2 * worker_count)]
    bimatch(worker)

ans = 0
for work in range(1, work_count + 1):
    if assigned_worker[work] != -1:
        ans += 1
print(ans)