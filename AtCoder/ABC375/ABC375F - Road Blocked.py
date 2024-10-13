'''
ABC375F - Road Blocked (https://atcoder.jp/contests/abc375/tasks/abc375_f)

There is a graph of N nodes and M edges.
Process the following two types of queries:

(1) Invalidate edge X.
(2) Print the shortest distance from city X to city Y.
'''

import sys
inf = float('inf')


# 3. FLOYD-BASED UPDATE FUNCTION 

def update(nodeA, nodeB):
    
    for i in range(node_count):
        for j in range(node_count):
            if graph[i][j] > graph[i][nodeA] + graph[nodeA][j]:
                graph[i][j] = graph[i][nodeA] + graph[nodeA][j]
    
    for i in range(node_count):
        for j in range(node_count):
            if graph[i][j] > graph[i][nodeB] + graph[nodeB][j]:
                graph[i][j] = graph[i][nodeB] + graph[nodeB][j]


# 1. TO GET THE INPUT

node_count, edge_count, query_count = map(int, sys.stdin.readline().split())
graph = [[inf for j in range(node_count)] for i in range(node_count)]

edges = []

for edge_input in range(edge_count):

    nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1

    edges.append((nodeA, nodeB, dist))
    graph[nodeA][nodeB] = dist
    graph[nodeB][nodeA] = dist

queries = []

for query_input in range(query_count):
    
    query = list(sys.stdin.readline().strip().split())
    
    if query[0] == "1":
        
        query_type, road_num = query
        query_type = int(query_type)
        road_num = int(road_num) - 1
        queries.append((query_type, road_num))
        
        nodeA, nodeB, dist = edges[road_num]
        graph[nodeA][nodeB] = inf
        graph[nodeB][nodeA] = inf
        
    else:
        
        query_type, nodeA, nodeB = query
        query_type = int(query_type)
        nodeA = int(nodeA) - 1
        nodeB = int(nodeB) - 1
        queries.append((query_type, nodeA, nodeB))


# 2. FLOYD

for node in range(node_count):
    graph[node][node] = 0
for k in range(node_count):
    for i in range(node_count):
        for j in range(node_count):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


# 4. TO SOLVE THE PROBLEM

ans = []

while queries:
    
    query = queries.pop()
    
    if query[0] == 1:
        
        query_type, road_num = query
        nodeA, nodeB, dist = edges[road_num]
        graph[nodeA][nodeB] = min(graph[nodeA][nodeB], dist)
        graph[nodeB][nodeA] = min(graph[nodeA][nodeB], dist)
        update(nodeA, nodeB)
    
    else:
        
        query_type, nodeA, nodeB = query
        if graph[nodeA][nodeB] == inf:
            ans.append(-1)
        else:
            ans.append(graph[nodeA][nodeB])

while ans:
    print(ans.pop())