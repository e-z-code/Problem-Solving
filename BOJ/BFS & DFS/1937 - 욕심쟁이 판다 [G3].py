'''
BOJ 1937 - Greedy Panda (https://www.acmicpc.net/problem/1937)

There is an N X N grid.
A panda can start from any cell.
However, it can only move to an adjacent cell with a higher value.
Determine the length of the longest route the panda can take. 
'''

import sys
sys.setrecursionlimit(10 ** 6)


# 2. A FUNCTION FOR DFS
# dfs(i, j) stores the length of the longest route that ends at grid[i][j].

def dfs(i, j):
    
    length = 1
    
    for idx in range(4):
        
        new_i = i + dy[idx]
        new_j = j + dx[idx]
        
        if 0 <= new_i < size and 0 <= new_j < size and grid[i][j] < grid[new_i][new_j]:
            if visited[new_i][new_j] == 0:
                length = max(length, dfs(new_i, new_j) + 1)
            else:
                length = max(length, visited[new_i][new_j] + 1)
    
    visited[i][j] = length

    return length


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())

grid = []
for row_input in range(size):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)


# 3. TO SOLVE THE PROBLEM

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[0 for j in range(size)] for i in range(size)]

for i in range(size):
    for j in range(size):
        if visited[i][j] == 0:
            dfs(i, j)

ans = 0
for row in visited:
    ans = max(ans, max(row))
print(ans)