'''
BOJ 30797 - Trip with Ga-hee (https://www.acmicpc.net/problem/30797)

There is a graph with N nodes and Q edges.
You aim to connect all N nodes with the minimum cost as fast as possible.
Determine if it is possible. If possible, print the minimum cost and the fastest time.
'''

import sys
from collections import deque
sys.setrecursionlimit(300000)


# 2. UNION FIND

def find(node):
    
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(nodeA, nodeB):
    
    parentA = find(nodeA)
    parentB = find(nodeB)
    
    if parentA < parentB:
        parent[parentA] = parentB
    else:
        parent[parentB] = parentA


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

edges = []
for edge in range(edge_count):
    
    start, end, cost, time = map(int, sys.stdin.readline().split())
    start -= 1
    end -= 1
    edges.append((cost, time, start, end))

edges.sort()


# 3. KRUSKAL

parent = [node for node in range(node_count)]

ans_time = 0
ans_cost = 0
used_edge = 0

for cost, time, start, end in edges:
    
    if find(start) != find(end):
        union(start, end)
        ans_time = max(ans_time, time)
        ans_cost += cost
        used_edge += 1

if used_edge != node_count - 1:
    print(-1)
else:
    print(ans_time, ans_cost)