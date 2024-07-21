'''
BOJ 17370 - Ant in Hexagon Cage (https://www.acmicpc.net/problem/17370)

An ant moves along a hexagon pattern. Each side has a length of 1.
At every point of intersection, the ant chooses one of two paths he did not come from.
The ant stops if he already arrived at the point of intersection.
Determine the number of distinct paths of length N.
'''

import sys
from itertools import product


# 1. PRE-PROCESSING
# Following is the code I used.

'''
dx = [0, 1, 1, 0, -1, -1]
dy = [2, 1, -1, -2, -1, 1]

ans = 0
cases = list(product(["L", "R"], repeat = move_count))

for case in cases:
    
    visited = {}
    visited[(0, 0)] = 1
    visited[(0, 2)] = 1
    
    now_op = 0
    now_x, now_y = 0, 2
    
    for idx in range(move_count):
    
        op = case[idx]
        if op == "R":
            now_op = (now_op + 1) % 6
        else:
            now_op = (now_op - 1) % 6

        now_x += dx[now_op]
        now_y += dy[now_op]
    
        if (now_x, now_y) in visited:
            if idx == move_count-1:
                ans += 1
            break
        else:
            visited[(now_x, now_y)] = 1

print(ans)
'''

ans = [0, 0, 0, 0, 0, 2, 2, 4, 8, 26, 36, 80, 148, 332, 556, 1172, 2112, 4350, 7732, 15568, 28204, 56100, 101640]


# 2. TO SOLVE THE PROBLEM

move_count = int(sys.stdin.readline())
print(ans[move_count])