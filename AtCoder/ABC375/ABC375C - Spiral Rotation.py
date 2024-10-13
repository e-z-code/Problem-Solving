'''
ABC375C - Spiral Rotation (https://atcoder.jp/contests/abc375/tasks/abc375_c)

Given a grid of size N, you perform the following operation for 1 <= i <= N // 2.

- Swap (x, y) with (y, N + 1 - x) for every (x, y) such that i <= x <= N + 1 - i and i <= y <= N + 1 - i

Print the result.
'''

import sys


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())

grid = []
for row_input in range(size):
    row = list(sys.stdin.readline().strip())
    grid.append(row)


# 2. TO SOLVE THE PROBLEM

ans = [["" for col in range(size)] for grid in range(size)]

for i in range(size):
    for j in range(size):
        
        key_i = i
        key_j = j
        if key_i >= size // 2:
            key_i = size - key_i - 1
        if key_j >= size // 2:
            key_j = size - key_j - 1
        shell_num = (min(key_i, key_j) + 1) % 4
        
        goal_i = i
        goal_j = j
        while shell_num:
            goal_i, goal_j = goal_j, size - 1 - goal_i
            shell_num -= 1
        ans[goal_i][goal_j] = grid[i][j]

for row in ans:
    print("".join(row))