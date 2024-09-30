'''
BOJ 7107 - Journey of a Knight (https://www.acmicpc.net/problem/7107)

Determine the minimum number of knight moves from (0, 0) to (X, Y).
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

row_count, col_count, goal_row, goal_col = map(int, sys.stdin.readline().split())
goal_row -= 1
goal_col -= 1


# 2. TO SOLVE THE PROBLEM - BFS

dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

visited = [[-1 for col in range(col_count)] for row in range(row_count)]

queue = deque([(0, 0)])
visited[0][0] = 0
while queue:
    now_row, now_col = queue.popleft()
    for idx in range(8):
        next_row = now_row + dy[idx]
        next_col = now_col + dx[idx]
        if 0 <= next_row < row_count and 0 <= next_col < col_count and visited[next_row][next_col] == -1:
            visited[next_row][next_col] = visited[now_row][now_col] + 1
            queue.append((next_row, next_col))

ans = visited[goal_row][goal_col]
if ans == -1:
    ans = "NEVAR"
print(ans)