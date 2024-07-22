'''
BOJ 13967 - Balls and Needles (https://www.acmicpc.net/problem/13967)

You are given N tuple pairs: {(x1, y1, z1), (x2, y2, z2)}.
Determine whether some pairs consist closed chains or floor closed chains.
'''

import sys
sys.setrecursionlimit(10 ** 5)


# 2. DFS

def total_chain_check(now_node, before_node):
    
    global total_chain
    
    for next_node in needle_graph[now_node]:
        if next_node != before_node:
            if needle_visited[next_node]:
                total_chain = True
                break
            needle_visited[next_node] = 1
            total_chain_check(next_node, now_node)

def shadow_chain_check(now_node, before_node):
    
    global shadow_chain
    
    for next_node in shadow_graph[now_node]:
        if next_node != before_node:
            if shadow_visited[next_node]:
                shadow_chain = True
                break
            shadow_visited[next_node] = 1
            shadow_chain_check(next_node, now_node)


# 1. TO GET THE INPUT

edge_count = int(sys.stdin.readline())

needle_graph = {}
needle_visited = {}

shadow_graph = {}
shadow_visited = {}

for edge_num in range(edge_count):
    
    x1, y1, z1, x2, y2, z2 = map(int, sys.stdin.readline().split())
    
    if (x1, y1, z1) in needle_graph:
        needle_graph[(x1, y1, z1)].add((x2, y2, z2))
    else:
        needle_graph[(x1, y1, z1)] = set([(x2, y2, z2)])
    if (x2, y2, z2) in needle_graph:
        needle_graph[(x2, y2, z2)].add((x1, y1, z1))
    else:
        needle_graph[(x2, y2, z2)] = set([(x1, y1, z1)])
    needle_visited[(x1, y1, z1)] = 0
    needle_visited[(x2, y2, z2)] = 0
        
    if (x1, y1) != (x2, y2):
        if (x1, y1) in shadow_graph:
            shadow_graph[(x1, y1)].add((x2, y2))
        else:
            shadow_graph[(x1, y1)] = set([(x2, y2)])
        if (x2, y2) in shadow_graph:
            shadow_graph[(x2, y2)].add((x1, y1))
        else:
            shadow_graph[(x2, y2)] = set([(x1, y1)])
        shadow_visited[(x1, y1)] = 0
        shadow_visited[(x2, y2)] = 0


# 3. TO SOLVE THE PROBLEM

total_chain = False
needles = list(needle_graph.keys())
for needle in needles:
    if needle_visited[needle] == 0:
        needle_visited[needle] = 1
        total_chain_check(needle, -1)

shadow_chain = False
shadows = list(shadow_graph.keys())
for shadow in shadows:
    if shadow_visited[shadow] == 0:
        shadow_visited[shadow] = 1
        shadow_chain_check(shadow, -1)

if total_chain:
    print("True closed chains")
else:
    print("No true closed chains")
    
if shadow_chain:
    print("Floor closed chains")
else:
    print("No floor closed chains")