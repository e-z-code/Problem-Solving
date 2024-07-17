'''
CF958D - The Omnipotent Monster Killer (https://codeforces.com/contest/1988/problem/D)

There is a tree. There is a monster on each node.

In each round, the following happens.
(1) All living monsters attack you. Your damage equals to the sum of attack points of all living monsters.
(2) You select monsters and kill them. However, you cannot kill two monsters that are directly connected by an edge.

Determine the minimum damage you will get until the end.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    node_count = int(sys.stdin.readline())
    attack_point = [0] + list(map(int, sys.stdin.readline().split()))
    
    graph = {}
    for node in range(1, node_count+1):
        graph[node] = []

    for edge in range(node_count - 1):
        nodeA, nodeB = map(int, sys.stdin.readline().split())
        graph[nodeA].append(nodeB)
        graph[nodeB].append(nodeA)

    
    # 2. NON-RECURSIVE TREE DP
    # dp[X][Y] = Minimum damage when the monster in node X is killed at round Y.
        
    parent = [-1 for node in range(node_count+1)]
    dp = [[attack_point[node] * death_round for death_round in range(20)] for node in range(node_count + 1)]
    
    stack = [(1, 0)]
    while stack:
        now_node, now_visited = stack.pop()
        if now_visited == 0:
            stack.append((now_node, 1))
            for connected_node in graph[now_node]:
                if connected_node != parent[now_node]:
                    parent[connected_node] = now_node
                    stack.append((connected_node, 0))
        else:
            for death_round in range(1, 20):
                dp[now_node][death_round] = attack_point[now_node] * death_round
            for connected_node in graph[now_node]:
                if connected_node != parent[now_node]:
                    for death_round in range(1, 20):
                        dp[now_node][death_round] += min(dp[connected_node][1:death_round] + dp[connected_node][death_round+1:])
    
    print(min(dp[1][1:]))