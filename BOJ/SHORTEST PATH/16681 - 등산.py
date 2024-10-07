'''
BOJ 16681 - Hiking (https://www.acmicpc.net/problem/16681)

There is a graph of N nodes.
To hike node X, you ascend from node 1 to node X and descend from node X to node N.
It costs you D for every distance unit.
Given a profit you can earn by hiking each node, determine the maximum possible value of profit - cost.
'''

import sys, heapq
inf = float('inf')


# 2. DIJKSTRA FUNCTION

def dijkstra(start):
    
    dist = [inf for node in range(node_count)]
    dist[start] = 0
    
    heap = [(0, start)]
    while heap:
        now_dist, now_loc = heapq.heappop(heap)
        if now_dist <= dist[now_loc]:
            for next_loc, next_dist in graph[now_loc]:
                if height[next_loc] > height[now_loc] and now_dist + next_dist < dist[next_loc]:
                    dist[next_loc] = now_dist + next_dist
                    heapq.heappush(heap, (now_dist + next_dist, next_loc))

    return dist


# 1. TO GET THE INPUT

node_count, edge_count, cost, benefit = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

graph = {}
for node in range(node_count):
    graph[node] = []

for edge in range(edge_count):
    nodeA, nodeB, length = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append((nodeB, length))
    graph[nodeB].append((nodeA, length))


# 3. TO SOLVE THE PROBLEM

ascending_dist = dijkstra(0)
descending_dist = dijkstra(node_count - 1)

ans = -inf
for idx in range(node_count):
    if ascending_dist[idx] == inf or descending_dist[idx] == inf:
        continue
    ans = max(ans, height[idx] * benefit - (ascending_dist[idx] + descending_dist[idx]) * cost)

if ans == -inf:
    print("Impossible")
else:
    print(ans)