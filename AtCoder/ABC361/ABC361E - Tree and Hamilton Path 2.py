'''
ABC361E - Tree and Hamilton Path 2 (https://atcoder.jp/contests/abc361/tasks/abc361_e)

Given a tree, determine the minimum travel distance to visit all cities at least once.
'''

import sys
from collections import deque


# 2. FUNCTIONS TO GET A DIAMETER OF THE TREE
# Since a path to node A from node B is unique in tree, it is OK to use BFS.

def bfs(start):
    
    visited = [-1 for node in range(node_count + 1)]
    
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        now_node = queue.popleft()
        for next_node, dist in graph[now_node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[now_node] + dist
                queue.append((next_node))
    
    return visited

def tree_diameter():
    
    first_bfs = bfs(1)
    farthest_dist = max(first_bfs)
    
    new_start = None
    for node in range(1, node_count + 1):
        if first_bfs[node] == max_dist:
            new_start = node
            break
    
    return max(bfs(new_start))


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())
total_dist = 0

graph = {}
for node in range(1, node_count + 1):
    graph[node] = []

for edge in range(node_count - 1):
    nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
    total_dist += dist
    graph[nodeA].append((nodeB, dist))
    graph[nodeB].append((nodeA, dist))


# 3. TO SOLVE THE PROBLEM
# Total distance = Length of diameter + 2 * Remainders

first_bfs = bfs(1)
max_dist = max(first_bfs)

new_start = None
for node in range(1, node_count+1):
    if first_bfs[node] == max_dist:
        new_start = node
        break

diameter = tree_diameter()
print(diameter + (total_dist - diameter) * 2)
