'''
BOJ 16227 - Medical Device Transportation (https://www.acmicpc.net/problem/16227)

Given a graph, you need to transport a medical device from node 0 to node N+1.
The device is so sensitive that you cannot drive more than 100 without cleaning it, which takes 5 minutes.
Determine the minimum time required for the transportation.
'''

import sys, heapq
inf = float('inf')


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())
node_count += 2

graph = {}
for node in range(node_count):
    graph[node] = []

for edge in range(edge_count):
    nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
    if dist <= 100:
        graph[nodeA].append((nodeB, dist))
        graph[nodeB].append((nodeA, dist))


# 2. TO SOLVE THE PROBLEM - DIJKSTRA
# dist[i][j] = Minimum time required to arrive node i with sand of j.

dist = [[inf for sand in range(101)] for node in range(node_count)]

heap = [(0, 0, 0)]
dist[0][0] = 0
while heap:
    now_dist, now_node, now_sand = heapq.heappop(heap)
    if dist[now_node][now_sand] >= now_dist:
        for next_node, next_dist in graph[now_node]:
            total_dist = now_dist + next_dist
            total_sand = now_sand + next_dist
            if total_sand <= 100:
                if dist[next_node][total_sand] > total_dist:
                    dist[next_node][total_sand] = total_dist
                    heapq.heappush(heap, (total_dist, next_node, total_sand))
            if dist[next_node][0] > total_dist + 5:
                dist[next_node][0] = total_dist + 5
                heapq.heappush(heap, (total_dist + 5, next_node, next_dist))

print(min(dist[-1]))