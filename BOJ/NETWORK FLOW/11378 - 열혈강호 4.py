'''
BOJ 11378 - The Ruler of the Company 4 (https://www.acmicpc.net/problem/11378)

There are N workers and M assignments.
If a worker has a penalty of X, the worker can do at most X+1 jobs.
You can distribute K penalties as you want.
Determine the maximum number of assignments workers can do.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT AND CONSTRUCT A GRAPH
# Worker : Node 0 ~ N-1 / Work : Node N ~ N + M - 1

worker_count, work_count, penalty = map(int, sys.stdin.readline().split())
node_count = worker_count + work_count + 3

source = worker_count + work_count
sink = worker_count + work_count + 2

graph = [[0 for nodeB in range(node_count)] for nodeA in range(node_count)]
capacity = [[0 for nodeB in range(node_count)] for nodeA in range(node_count)]
flow = [[0 for nodeB in range(node_count)] for nodeA in range(node_count)]

graph[source][source+1] = 1
graph[source+1][source] = 1
capacity[source][source+1] = penalty

for worker in range(worker_count):
    
    graph[source][worker] = 1
    graph[worker][source] = 1
    capacity[source][worker] = 1
    
    graph[source+1][worker] = 1
    graph[worker][source+1] = 1
    capacity[source+1][worker] = penalty
    
    capable_work = list(map(int, sys.stdin.readline().split()))[1:]
    for work in capable_work:
        
        work -= 1
        work += worker_count
        
        graph[worker][work] = 1
        graph[work][worker] = 1
        capacity[worker][work] = 1

for work in range(work_count):
    
    work += worker_count
    
    graph[work][sink] = 1
    graph[sink][work] = 1
    capacity[work][sink] = 1


# 2. EDMOND-KARP

ans = 0

while True:
    
    parent = [-1 for node in range(node_count)]
    
    queue = deque([source])
    while queue and parent[sink] == -1:
        now_node = queue.popleft()
        for next_node in range(node_count):
            if graph[now_node][next_node] and parent[next_node] == -1 and capacity[now_node][next_node] > flow[now_node][next_node]:
                queue.append(next_node)
                parent[next_node] = now_node
    
    if parent[sink] == -1:
        break
    
    amount = float('inf')
    node = sink
    while node != source:
        amount = min(amount, capacity[parent[node]][node] - flow[parent[node]][node])
        node = parent[node]
    
    node = sink
    while node != source:
        flow[parent[node]][node] += amount
        flow[node][parent[node]] -= amount
        node = parent[node]
    ans += amount

print(ans)