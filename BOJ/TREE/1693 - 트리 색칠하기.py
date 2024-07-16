'''
BOJ 1693 - Tree Coloring (https://www.acmicpc.net/problem/1693)

There is a tree with N nodes. You must color each node.
If you color a node with color N, it costs N.
You cannot color two adjacent nodes with the same color.
Determine the minimum cost to color all nodes.
'''

import sys

sys.setrecursionlimit(100000)


# 2. A FUNCTION FOR TREE DP
# Maximum number of color used is bound to log N. 

def tree_dp(now_node):

    for connected_node in graph[now_node]:
        if not visited[connected_node]:
            visited[connected_node] = True
            tree_dp(connected_node)
            for color in range(1, 18):
                dp[now_node][color] += min(dp[connected_node][1:color] + dp[connected_node][color+1:])


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())

graph = {}
for node in range(1, node_count+1):
    graph[node] = []

for edge in range(node_count-1):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)


# 3. TREE DP

dp = [[color for color in range(18)] for node in range(node_count+1)]
visited = [0 for node in range(node_count+1)]

visited[1] = 1
tree_dp(1)

print(min(dp[1][1:]))