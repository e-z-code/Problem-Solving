'''
BOJ 5934 - Visiting Cows (https://www.acmicpc.net/problem/5934)

Given a tree, print the number of the maximum independent set.
'''


import sys
from collections import deque

sys.setrecursionlimit(100000)


# 2. A FUNCTION TO CONSTRUCT TREE

def tree(now_node, parent_node):
    
    for connected_node in graph[now_node]:
        if connected_node != parent_node:
            children[now_node].append(connected_node)
            parent[connected_node] = now_node
            tree(connected_node, now_node)


# 4. A FUNCTION FOR TREE DP

def solve(now_node):
    
    included = 1
    not_included = 0
    
    for child_node in children[now_node]:
        solve(child_node)
        included += dp[child_node][1]
        not_included += max(dp[child_node])

    dp[now_node] = [included, not_included]
    

# 1. TO GET THE INPUT

cow_count = int(sys.stdin.readline())

graph = {}
for cow in range(1, cow_count + 1):
    graph[cow] = []

for edge in range(cow_count - 1):
    cowA, cowB = map(int, sys.stdin.readline().split())
    graph[cowA].append(cowB)
    graph[cowB].append(cowA)


# 3. TO CONSTRUCT A TREE

parent = [0 for cow in range(cow_count + 1)]
children = [[] for cow in range(cow_count + 1)]

tree(1, -1)


# 5. TO SOLVE THE PROBLEM

dp = [[0, 0] for cow in range(cow_count + 1)]

solve(1)

print(max(dp[1]))