'''
BOJ 1867 - Remove Rocks (https://www.acmicpc.net/problem/1867)

There are K rocks on an N X N grid.
In an operation, you can choose a row or a column and remove all rocks on the row or the column.
Determine the minimum number of operations needed to remove all rocks.
'''

import sys


# 2. BIPARTITE MATCHING

def bimatch(row):
    
    if visited[row]:
        return False
    visited[row] = True
    
    result = False
    for col in graph[row]:
        if row_assigned[col] == -1 or bimatch(row_assigned[col]):
            result = True
            row_assigned[col] = row
            break
    
    return result


# 1. TO GET THE INPUT AND CONSTRUCT A BIPARTITE GRAPH
# Each rock (i, j) is an edge that connects the vertex row[i] and the vertex col[j].
# Then, the problem is equivalent to calculating the size of a minimum vertex cover set. 

grid_size, rock_count = map(int, sys.stdin.readline().split())

graph = {}
for row in range(grid_size):
    graph[row] = []

for rock in range(rock_count):
    row, col = map(int, sys.stdin.readline().split())
    graph[row-1].append(col-1)


# 3. TO SOLVE THE PROBLEM
# According to Kőnig's theorem, the minimum vertex cover set and the maximum matching set have the same size.

row_assigned = [-1 for col in range(grid_size)]

for row in range(grid_size):
    
    visited = [False for row in range(grid_size)]
    bimatch(row)

print(grid_size - row_assigned.count(-1))