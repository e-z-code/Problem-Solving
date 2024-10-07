'''
BOJ 5865 - Milk Routing (https://www.acmicpc.net/problem/5865)

There is a graph of N nodes and M edges.
Each path connecting node 1 to node N has latency and consistency.
The latency of the path is the sum of the latencies along the path.
The capacity of the path is the minimum of the capacities along the path.
It takes L + X / C time to send X units of milk through a pipe with latency L and capacity C.
Determine the minimum amount of time to send X units of milk.
'''


import sys, heapq
inf = float('inf')


# 2. DIJKSTRA FUNCTION

def dijkstra(bottleneck):
    
    visited = [inf for node in range(node_count)]

    heap = [(0, 0)]
    visited[0] = 0

    while heap:
        
        now_latency, now_loc = heapq.heappop(heap)
        if now_latency <= visited[now_loc]:
            for next_loc, next_latency, next_capacity in graph[now_loc]:
                new_latency = now_latency + next_latency
                if new_latency < visited[next_loc] and next_capacity >= bottleneck:
                    visited[next_loc] = new_latency
                    heapq.heappush(heap, (new_latency, next_loc))

    return visited[node_count-1]


# 1. TO GET THE INPUT

node_count, edge_count, milk_amount = map(int, sys.stdin.readline().split())

graph = {}
for node in range(node_count):
    graph[node] = []
for edge in range(edge_count):
    nodeA, nodeB, latency, capacity = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append((nodeB, latency, capacity))
    graph[nodeB].append((nodeA, latency, capacity))


# 3. TO SOLVE THE PROBLEM

ans = inf

edge_capacity = set()
for nodeA in range(node_count):
    for nodeB, latency, capacity in graph[nodeA]:
        edge_capacity.add(capacity)

for capacity in list(edge_capacity):
    latency = dijkstra(capacity)
    ans = min(ans, latency + milk_amount / capacity)

print(int(ans))