'''
CF956B - Corner Twist (https://codeforces.com/contest/1983/problem/B)

There are two N X M grids: A and B. Each cell contains 0, 1, or 2.
You can perform the following operation on A as you want.

(1) Pick any sub-rectangle in the grid with length and width >= 2.
(2) Take any pair of diagonally opposite corners and add 1 to their values modulo 3.
(3) For the pair of corners not picked, add 2 to their values modulo 3.

Determine if it is possible to construct B from A.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    row_count, col_count = map(int, sys.stdin.readline().split())
    
    initial_grid = []
    for row_input in range(row_count):
        row = list(sys.stdin.readline().strip())
        row = list(map(int, row))
        initial_grid.append(row)
    
    final_grid = []
    for row_input in range(row_count):
        row = list(sys.stdin.readline().strip())
        row = list(map(int, row))
        final_grid.append(row)
    
    
    # 2. TO SOLVE THE PROBLEM
    # Always choose the entire grid. [PROOF TBA]
    
    for row_num in range(row_count-1):
        for col_num in range(col_count-1):
            
            now_num = initial_grid[row_num][col_num]
            final_num = final_grid[row_num][col_num]
            
            if (now_num == 0 and final_num == 1) or (now_num == 1 and final_num == 2) or (now_num == 2 and final_num == 0):
                initial_grid[row_num][col_num] = (initial_grid[row_num][col_num] + 1) % 3
                initial_grid[-1][-1] = (initial_grid[-1][-1] + 1) % 3
                initial_grid[row_num][-1] = (initial_grid[row_num][-1] + 2) % 3
                initial_grid[-1][col_num] = (initial_grid[-1][col_num] + 2) % 3
            elif (now_num == 0 and final_num == 2) or (now_num == 1 and final_num == 0) or (now_num == 2 and final_num == 1):
                initial_grid[row_num][col_num] = (initial_grid[row_num][col_num] + 2) % 3
                initial_grid[-1][-1] = (initial_grid[-1][-1] + 2) % 3
                initial_grid[row_num][-1] = (initial_grid[row_num][-1] + 1) % 3
                initial_grid[-1][col_num] = (initial_grid[-1][col_num] + 1) % 3
    
    if initial_grid == final_grid:
        print("Yes")
    else:
        print("No")