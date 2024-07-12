'''
BOJ 20208 - Jinwoo's Mint Chocolate Milk (https://www.acmicpc.net/problem/20208)

There is an N X N grid.
You start from a given point and search for mint chocolate milk.
You can only move to adjacent cells, and each move costs stamina of 1.
You cannot move when your stamina is 0, but you can recover it by H after drinking mint chocolate milk.
Determine the maximum number of mint chocolate milk you can drink.
'''

import sys
from collections import deque


# 3. TO COUNT THE NUMBER OF BITS

def bit(num):
    
    result = 0
    
    while num != 0:
        if num % 2 == 1:
            result += 1
        num //= 2
    
    return result


# 1. TO GET THE INPUT

grid_size, start_stamina, mint_stamina = map(int, sys.stdin.readline().split())

start_row, start_col = None, None
mint_loc = []

grid = []
for row_num in range(grid_size):
    row = list(map(int, sys.stdin.readline().split()))
    for col_num in range(grid_size):
        if row[col_num] == 1:
            start_row, start_col = row_num, col_num
        elif row[col_num] == 2:
            mint_loc.append((row_num, col_num))
    grid.append(row)
    
mint_num = {}
for idx in range(len(mint_loc)):
    mint_num[mint_loc[idx]] = idx 


# 2. BFS

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

queue = deque([(start_row, start_col, start_stamina, 0)])

visited = [[[[0 for mint in range(1024)] for stamina in range(100)] for col_num in range(10)] for row_num in range(10)]
visited[start_row][start_col][start_stamina][0] = 0

while queue:
    
    now_row, now_col, now_stamina, now_mint = queue.popleft()
    
    if now_stamina == 0:
        continue
    
    for idx in range(4):
        
        next_row = now_row + dy[idx]
        next_col = now_col + dx[idx]
        next_stamina = now_stamina - 1
        next_mint = now_mint

        if 0 <= next_row < grid_size and 0 <= next_col < grid_size:
            
            if grid[next_row][next_col] == 2:
                new_mint = 1 << mint_num[(next_row, next_col)]
                if not (now_mint & new_mint):
                    next_stamina = min(grid_size * grid_size - 1, next_stamina + mint_stamina)
                    next_mint |= new_mint
            
            if visited[next_row][next_col][next_stamina][next_mint] == 0:
                visited[next_row][next_col][next_stamina][next_mint] = 1
                queue.append((next_row, next_col, next_stamina, next_mint))


# 4. TO SOLVE THE PROBLEM

ans = 0

for stamina in range(100):
    for mint in range(1024):
        if visited[start_row][start_col][stamina][mint]:
            ans = max(ans, bit(mint))

print(ans)