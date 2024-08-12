'''
BOJ 3019 - Tetris (https://www.acmicpc.net/problem/3019)

You play Tetris of C columns. 
You do not want to leave a space between blocks.
Given the next block and a state, determine the number of ways you can locate the block.
'''

import sys


# 1. TO GET THE INPUT

col_count, block_num = map(int, sys.stdin.readline().split())
board = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

ans = 0

if block_num == 1:
    ans += col_count
    for idx in range(col_count - 3):
        if board[idx] == board[idx+1] == board[idx+2] == board[idx+3]:
            ans += 1
elif block_num == 2:
    for idx in range(col_count - 1):
        if board[idx] == board[idx+1]:
            ans += 1
elif block_num == 3:
    for idx in range(col_count - 1):
        if board[idx] == board[idx+1] + 1:
            ans += 1
    for idx in range(col_count - 2):
        if board[idx] + 1 == board[idx+1] + 1 == board[idx+2]:
            ans += 1
elif block_num == 4:
    for idx in range(col_count - 1):
        if board[idx] + 1 == board[idx+1]:
            ans += 1
    for idx in range(col_count - 2):
        if board[idx] == board[idx+1] + 1 == board[idx+2] + 1:
            ans += 1
elif block_num == 5:
    for idx in range(col_count - 2):
        if board[idx] == board[idx+1] == board[idx+2]:
            ans += 1
        elif board[idx] == board[idx+1] + 1 == board[idx+2]:
            ans += 1
    for idx in range(col_count - 1):
        if abs(board[idx] - board[idx+1]) == 1:
            ans += 1
elif block_num == 6:
    for idx in range(col_count - 2):
        if board[idx] == board[idx+1] == board[idx+2]:
            ans += 1
        elif board[idx] + 1 == board[idx+1] == board[idx+2]:
            ans += 1
    for idx in range(col_count - 1):
        if board[idx] == board[idx+1]:
            ans += 1
        elif board[idx] == board[idx+1] + 2:
            ans += 1
elif block_num == 7:
    for idx in range(col_count - 2):
        if board[idx] == board[idx+1] == board[idx+2]:
            ans += 1
        elif board[idx] == board[idx+1] == board[idx+2] + 1:
            ans += 1
    for idx in range(col_count - 1):
        if board[idx] == board[idx+1]:
            ans += 1
        elif board[idx] + 2 == board[idx+1]:
            ans += 1

print(ans)