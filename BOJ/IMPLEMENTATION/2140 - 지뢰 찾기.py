'''
BOJ 2140 - Minesweeper (https://www.acmicpc.net/problem/2140)

You play Minesweeper on an N X N board.
Cells along four sides are already open.
Determine the maximum number of mines.
'''

import sys


# 2. FUNCTION TO COUNT ADJACENT MINES

def mine_count(row_num, col_num):
    
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    
    result = 0
    
    for idx in range(8):
        target_row = row_num + dy[idx]
        target_col = col_num + dx[idx]
        if 0 <= target_row < size and 0 <= target_col < size:
            if board[target_row][target_col] == "X":
                result += 1
    
    return result

# 1. TO GET THE INPUT

size = int(sys.stdin.readline())

board = []
for row_input in range(size):
    row = list(sys.stdin.readline().strip())
    board.append(row)


# 2. TO SOLVE THE PROBLEM

if size <= 2:
    print(0)
elif size == 3:
    if int(board[0][0]) == 1:
        print(1)
    else:
        print(0)
else:
    
    for row_num in range(size - 2):
        
        total_mine = int(board[row_num][0])
        revealed_mine = mine_count(row_num, 0)
        if total_mine - revealed_mine != 0:
            board[row_num+1][1] = "X"
        else:
            board[row_num+1][1] = "."

    for col_num in range(1, size-2):
        
        total_mine = int(board[size-1][col_num])
        revealed_mine = mine_count(size-1, col_num)
        if total_mine - revealed_mine != 0:
            board[size-2][col_num+1] = "X"
        else:
            board[size-2][col_num+1] = "."
            
    for row_num in range(size-2, 1, -1):
    
        total_mine = int(board[row_num][size-1])
        revealed_mine = mine_count(row_num, size-1)
        if total_mine - revealed_mine != 0:
            board[row_num-1][size-2] = "X"
        else:
            board[row_num-1][size-2] = "."
            
    for col_num in range(size-2, 2, -1):
        
        total_mine = int(board[0][col_num])
        revealed_mine = mine_count(0, col_num)
        if total_mine - revealed_mine != 0:
            board[1][col_num-1] = "X"
        else:
            board[1][col_num-1] = "."
        
    ans = 0
    for row in board:
        ans += row.count("X") + row.count("#")
    print(ans)