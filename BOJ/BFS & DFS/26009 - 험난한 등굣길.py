'''
BOJ 26009 - Harsh Way to School (https://www.acmicpc.net/problem/26009)

There is an N X M grid. You want to go to (N, M) from (1, 1).
There are K hazards represented by (R, C, D): Every cell of which distance with (R, C) is less than D is inaccessible.
Determine whether you can arrive (N, M). If possible, print the minimum distance.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT AND MARK THE HAZARD
# Marking the boundary of a hazard is enough. 

row_count, col_count = map(int, sys.stdin.readline().split())
hazard_count = int(sys.stdin.readline())

grid = [[0 for col_num in range(col_count)] for row_num in range(row_count)]
for hazard in range(hazard_count):
    
    row, col, dist = map(int, sys.stdin.readline().split())
    row -= 1
    col -= 1
    for x_diff in range(-dist, dist+1):
        
        new_row = row + dist - abs(x_diff)
        new_col = col + x_diff
        if 0 <= new_row < row_count and 0 <= new_col < col_count:
            grid[new_row][new_col] = 1
        
        new_row = row - dist + abs(x_diff)
        if 0 <= new_row < row_count and 0 <= new_col < col_count:
            grid[new_row][new_col] = 1


# 2. TO SOLVE THE PROBLEM - BFS

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

visited = [[-1 for col_num in range(col_count)] for row_num in range(row_count)]

bfs = deque([(0, 0)])
visited[0][0] = 0

while bfs:
    
    row, col = bfs.popleft()
    for idx in range(4):
        new_row = row + dy[idx]
        new_col = col + dx[idx]
        if 0 <= new_row < row_count and 0 <= new_col < col_count:
            if grid[new_row][new_col] == 0 and visited[new_row][new_col] == -1:
                bfs.append((new_row, new_col))
                visited[new_row][new_col] = visited[row][col] + 1

if visited[-1][-1] == -1:
    print("NO")
else:
    print("YES")
    print(visited[-1][-1])