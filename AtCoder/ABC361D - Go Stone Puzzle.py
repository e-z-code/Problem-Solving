'''
ABC361D - Go Stone Puzzle (https://atcoder.jp/contests/abc361/tasks/abc361_d)

There are N + 2 cells arranged in a row.
Two cells are empty, and N cells contain either a white or a black stone.
You can do the following operation any number of times.

(1) Choose a pair of adjacent cells that both contain stones.
(2) Swap stones with empty cells while preserving the order.

Given an initial state, determine the minimum number of operations needed to reach the goal state.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
initial_state = sys.stdin.readline().strip() + ".."
final_state = sys.stdin.readline().strip() + ".."


# 2. BFS

visited = {initial_state:0}
queue = deque([initial_state])

while queue:
    
    now_state = queue.popleft()
    dot_loc = now_state.find(".")
    
    for idx in range(len(now_state) - 1):

        next_state = list(now_state)
        if not (dot_loc <= idx <= dot_loc + 1 or dot_loc <= idx + 1 <= dot_loc + 1):
            next_state[idx:idx+2] = ".."
            next_state[dot_loc:dot_loc+2] = now_state[idx:idx+2]
        next_state = "".join(next_state)
        
        if next_state not in visited:
            visited[next_state] = visited[now_state] + 1
            queue.append(next_state)


# 3. TO SOLVE THE PROBLEM

if final_state not in visited:
    print(-1)
else:
    print(visited[final_state])