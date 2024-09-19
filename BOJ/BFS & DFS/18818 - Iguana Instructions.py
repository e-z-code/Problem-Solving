'''
BOJ 18818 - Iguana Instructions (https://www.acmicpc.net/problem/18818)

Your friend is trapped in a maze.
You can give the friend instructions, which consist of directions and amounts.
Determine the minimum number of instructions to help the friend reach the end of the maze.
'''


import sys
from collections import deque


# 2. A FUNCTION TO CHECK WHERE THE IGUANA CAN REACH WITH ONE INSTRUCTION

def by_instruction(row, col, direction):
    
    now_row = row
    now_col = col
    
    connected = []
    
    while True:
        
        next_row = now_row + dy[direction]
        next_col = now_col + dx[direction]
        
        if 0 <= next_row < size and 0 <= next_col < size and grid[next_row][next_col] == ".":
            now_row = next_row
            now_col = next_col
            connected.append((now_row, now_col))
        else:
            break
    
    return connected


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())

grid = []
for row in range(size):
    row_input = list(sys.stdin.readline().strip())
    grid.append(row_input)


# 3. TO CONSTRUCT A GRAPH

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

graph = {}
for row in range(size):
    for col in range(size):
        graph[(row, col)] = []
        for direction in range(4):
            graph[(row, col)].extend(by_instruction(row, col, direction))


# 4. TO SOLVE THE PROBLEM

visited = [[-1 for col in range(size)] for row in range(size)]

queue = deque([(0, 0)])
visited[0][0] = 0

while queue:
    now_row, now_col = queue.popleft()
    for next_row, next_col in graph[(now_row, now_col)]:
        if visited[next_row][next_col] == -1:
            visited[next_row][next_col] = visited[now_row][now_col] + 1
            queue.append((next_row, next_col))

print(visited[-1][-1])