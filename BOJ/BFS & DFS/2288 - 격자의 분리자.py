'''
BOJ 2288 - Grid Separator (https://www.acmicpc.net/problem/2288)

You are given an N X M grid divided into black and white by a separator.
You can simplify the separator by the following steps.

(1) Choose some black nodes adjacent to the separator and include them in the separator.
(2) Choose some separator nodes and convert them into white nodes. A new separator must still be a separator.

Determine the minimum number of separator nodes after simplification.
'''

import sys
from collections import deque
inf = float('inf')


# 3. BFS FUNCTION

def bfs(start_row, start_col):
    
    dy = [1, 0, 0]
    dx = [0, 1, -1]
    
    visited = [[inf for col in range(col_count)] for row in range(row_count)]
    visited[start_row][start_col] = 1
    
    queue = deque([(start_row, start_col)])
    while queue:
        now_row, now_col = queue.popleft()
        for idx in range(3):
            next_row = now_row + dy[idx]
            next_col = now_col + dx[idx]
            if 0 <= next_row < row_count and 0 <= next_col < col_count:
                if grid[next_row][next_col] == "S" and visited[next_row][next_col] == inf:
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    queue.append((next_row, next_col))
    
    return min(visited[-1])


# 1. TO GET THE INPUT

while True:

    row_count, col_count = map(int, sys.stdin.readline().split())
    if row_count == 0 and col_count == 0:
        break

    grid = []
    for row_input in range(row_count):
        row = list(sys.stdin.readline().strip())
        grid.append(row)


    # 2. ADD NEW SEPARATOR NODES

    for row in range(row_count):
        for col in range(col_count-1, 0, -1):
            if grid[row][col-1] == "S":
                grid[row][col] = "S"


    # 4. TO SOLVE THE PROBLEM

    ans = inf
    for col in range(col_count):
        if grid[0][col] == "S":
            min_distance = bfs(0, col)
            ans = min(ans, min_distance)
    print(ans)