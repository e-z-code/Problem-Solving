'''
BOJ 1068 - Tree (https://www.acmicpc.net/problem/1068)

Given a tree and a vertex, count the number of leaf nodes after deleting the vertex. 
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())
parent = list(map(int, sys.stdin.readline().split()))
delete_node = int(sys.stdin.readline())

root = None

graph = {}
for node in range(node_count):
    graph[node] = []

for node in range(node_count):
    if parent[node] != -1:
        graph[parent[node]].append(node)
    else:
        root = node


# 2. BFS

ans = 0

queue = deque([root])
if delete_node == root:
    queue.popleft()

while queue:
    
    now_node = queue.popleft()
    leaf_node = True
    for next_node in graph[now_node]:
        if next_node != delete_node:
            leaf_node = False
            queue.append(next_node)
    if leaf_node:
        ans += 1

print(ans)