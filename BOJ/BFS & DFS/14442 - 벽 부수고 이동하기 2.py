'''
BOJ 14442 - Crush the Wall 2 (https://www.acmicpc.net/problem/14442)

Given a graph, determine the minimum length to reach the end of the maze.
You can destroy at most K walls.
'''

import sys
from collections import deque
inf = float('inf')


# 1. TO GET THE INPUT

row_count, col_count, destroy_count = map(int, sys.stdin.readline().split())

grid = []
for row_num in range(row_count):
    row = list(sys.stdin.readline().strip())
    grid.append(row)


# 2. TO SOLVE THE PROBLEM

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[[inf for destroy in range(destroy_count + 1)] for col in range(col_count)] for row in range(row_count)]

queue = deque([(0, 0, 0)])
visited[0][0][0] = 1

while queue:
    
    now_row, now_col, now_destroy = queue.popleft()
    for direction in range(4):
        next_row = now_row + dy[direction]
        next_col = now_col + dx[direction]
        if 0 <= next_row < row_count and 0 <= next_col < col_count:
            if grid[next_row][next_col] == "0":
                if visited[next_row][next_col][now_destroy] == inf:
                    visited[next_row][next_col][now_destroy] = visited[now_row][now_col][now_destroy] + 1
                    queue.append((next_row, next_col, now_destroy))
            else:
                if now_destroy + 1 <= destroy_count and visited[next_row][next_col][now_destroy + 1] == inf:
                    visited[next_row][next_col][now_destroy + 1] = visited[now_row][now_col][now_destroy] + 1
                    queue.append((next_row, next_col, now_destroy + 1))

ans = min(visited[-1][-1])
if ans == inf:
    ans = -1
print(ans)