'''
BOJ 2210 - Keypad Jump (https://www.acmicpc.net/problem/2210)

There is a 5 X 5 grid with a single-digit number on each cell.
You make a six-digit number by starting from any cell and moving to an adjacent cell five times.
Determine the number of distinct numbers you can make.
'''

import sys
from itertools import product


# 1. TO GET THE INPUT

grid = []
for row_input in range(5):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)


# 2. TO SOLVE THE PROBLEM

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
moves = list(product(direction, repeat = 5))

possible = [0 for num in range(1000000)]
for start_row in range(5):
    for start_col in range(5):
        for move in moves:
            
            valid = True 
            
            now_row = start_row
            now_col = start_col
            now_num = grid[start_row][start_col]
            
            for idx in range(5):
                dy, dx = move[idx]
                if 0 <= now_row + dy < 5 and 0 <= now_col + dx < 5:
                    now_row = now_row + dy
                    now_col = now_col + dx
                    now_num = now_num * 10 + grid[now_row][now_col]
                else:
                    valid = False
                    break
            
            if valid:
                possible[now_num] = 1

print(possible.count(1))