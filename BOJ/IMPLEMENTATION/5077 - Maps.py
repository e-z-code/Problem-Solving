'''
BOJ 5077 - Maps (https://www.acmicpc.net/problem/5077)

Given a pattern and a map, determine how many times the pattern appears on the map. 
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    pattern_row_count, pattern_col_count = map(int, sys.stdin.readline().split())
    
    pattern = []
    for pattern_row_input in range(pattern_row_count):
        pattern_row = list(sys.stdin.readline().strip())
        pattern.append(pattern_row)
    
    grid_row_count, grid_col_count = map(int, sys.stdin.readline().split())
    
    grid = []
    for grid_row_input in range(grid_row_count):
        grid_row = list(sys.stdin.readline().strip())
        grid.append(grid_row)


    # 2. TO SOLVE THE PROBLEM
    
    ans = 0
    
    for y in range(grid_row_count - pattern_row_count + 1):
        for x in range(grid_col_count - pattern_col_count + 1):
            
            same = True
            for i in range(pattern_row_count):
                for j in range(pattern_col_count):
                    if grid[y+i][x+j] != pattern[i][j]:
                        same = False
                        break
            
            if same:
                ans += 1
    
    print(ans)