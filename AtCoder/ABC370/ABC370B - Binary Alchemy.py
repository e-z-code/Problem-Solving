'''
ABC370B - Binary Alchemy (https://atcoder.jp/contests/abc370/tasks/abc370_b)

If x >= y, f(x, y) = A[x][y]. Else, f(x, y) = A[y][x].
Calculate f(f(f(1, 1), 2), ..., N). 
'''

import sys


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())

grid = []
for row_num in range(size):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)


# 2. TO SOLVE THE PROBLEM

now = 1
for num in range(1, size + 1):
    if now >= num:
        now = grid[now-1][num-1]
    else:
        now = grid[num-1][now-1]
print(now)