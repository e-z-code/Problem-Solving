'''
BOJ 2146 - Bridge Construction (https://www.acmicpc.net/problem/2146)

There is an N X N map.
Determine the minimum length of the bridge to connect two different connected components.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())

grid = []
for row_input in range(size):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)


# 2. DISTINGUISH EACH ISLAND

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

island_num = 1

visited = [[0 for col_num in range(size)] for row_num in range(size)]

for row_num in range(size):
    for col_num in range(size):
        
        if visited[row_num][col_num] == 0 and grid[row_num][col_num] != 0:
            
            queue = deque([(row_num, col_num)])
            visited[row_num][col_num] = island_num
            while queue:
                now_row, now_col = queue.popleft()
                for idx in range(4):
                    next_row = now_row + dy[idx]
                    next_col = now_col + dx[idx]
                    if 0 <= next_row < size and 0 <= next_col < size:
                        if visited[next_row][next_col] == 0 and grid[now_row][now_col] == grid[next_row][next_col]:
                            queue.append((next_row, next_col))
                            visited[next_row][next_col] = island_num

            island_num += 1


# 3. TO SOLVE THE PROBLEM

grid = visited
    
ans = float('inf')

for row_num in range(size):
    for col_num in range(size):
        
        if grid[row_num][col_num] != 0:
            
            start_island = grid[row_num][col_num]
            
            visited = [[-1 for col_num in range(size)] for row_num in range(size)]
            visited[row_num][col_num] = 0

            queue = deque([(row_num, col_num)])
            while queue:
                now_row, now_col = queue.popleft()
                for idx in range(4):
                    next_row = now_row + dy[idx]
                    next_col = now_col + dx[idx]
                    if 0 <= next_row < size and 0 <= next_col < size:
                        if visited[next_row][next_col] == -1 and grid[next_row][next_col] != start_island:
                            if grid[next_row][next_col] == 0:
                                queue.append((next_row, next_col))
                                visited[next_row][next_col] = visited[now_row][now_col] + 1
                            else:
                                ans = min(ans, visited[now_row][now_col])
        
print(ans)