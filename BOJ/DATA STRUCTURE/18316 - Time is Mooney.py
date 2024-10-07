'''
BOJ 18316 - Time is Mooney (https://www.acmicpc.net/problem/18316)

There is a directed graph of N nodes and M edges.
Bessie wants to visit nodes to make as much money as she can and ends at node 1.
It costs her C X pow(T, 2) to travel for T days.
Given the money she gets when visiting each node, determine the maximum profit possible.
'''

import sys, heapq


# 1. TO GET THE INPUT

node_count, edge_count, cost = map(int, sys.stdin.readline().split())
revenue = list(map(int, sys.stdin.readline().split()))

graph = {}
for node in range(node_count):
    graph[node] = []
for edge in range(edge_count):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append(nodeB)


# 2. TO SOLVE THE PROBLEM

profit = [-1 for node in range(node_count)]

heap = [(0, 0, 0)]
profit[0] = 0

while heap:
    
    now_day, now_loc, now_revenue = heapq.heappop(heap)
    now_profit = now_revenue - cost * pow(now_day, 2)
    if now_profit <= profit[now_loc]:
        for next_loc in graph[now_loc]:
            next_profit = now_revenue + revenue[next_loc] - cost * pow(now_day + 1, 2)
            if next_profit > profit[next_loc]:
                profit[next_loc] = next_profit
                heapq.heappush(heap, (now_day + 1, next_loc, now_revenue + revenue[next_loc]))

print(profit[0])