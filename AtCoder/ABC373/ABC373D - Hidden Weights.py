'''
ABC373D - Hidden Weights (https://atcoder.jp/contests/abc373/tasks/abc373_d)

You are given a directed graph with N nodes and M edges.
Each edge consists of (U, V, W), which means an edge from U to V weights W.
Assign an integer to each node so that V - U = W for every edge. 
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

graph = {}
for node in range(node_count):
    graph[node] = []

for edge in range(edge_count):
    start, end, weight = map(int, sys.stdin.readline().split())
    start -= 1
    end -= 1
    graph[start].append((end, weight))
    graph[end].append((start, -weight))


# 2. TO SOLVE THE PROBLEM - BFS

visited = [None for node in range(node_count)]

for node in range(node_count):
    if visited[node] == None:
        
        queue = deque([node])
        visited[node] = 0
        
        while queue:
            now_node = queue.popleft()
            for next_node, weight in graph[now_node]:
                if visited[next_node] == None:
                    visited[next_node] = visited[now_node] + weight
                    queue.append(next_node)

print(" ".join(list(map(str, visited))))