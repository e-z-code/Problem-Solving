'''
BOJ 2412 - Climbing (https://www.acmicpc.net/problem/2412)

You can move from (x, y) to (a, b) if |a - x| <= 2 and |b - y| <= 2.
Determine the minimum distance from (0, 0) to a point at which the y-coordinate is T.
'''

import sys
from bisect import bisect_left
from collections import deque


# 1. TO GET THE INPUT

node_count, max_height = map(int, sys.stdin.readline().split())

nodes = [[] for height in range(max_height + 1)]
for node in range(node_count):
    x, y = map(int, sys.stdin.readline().split())
    nodes[y].append(x)
for height in range(max_height + 1):
    nodes[height].sort()


# 2. TO SOLVE THE PROBLEM : BFS

visited = {}
visited[(0, 0)] = 0

queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    for next_y in range(max(0, y - 2), min(max_height + 1, y + 3)):
        idx = bisect_left(nodes[next_y], x - 2)
        while idx < len(nodes[next_y]) and x - 2 <= nodes[next_y][idx] <= x + 2:
            next_x = nodes[next_y][idx]
            if (next_x, next_y) not in visited:
                queue.append((next_x, next_y))
                visited[(next_x, next_y)] = visited[(x, y)] + 1
            idx += 1

ans = float('inf')
for x, y in visited:
    if y == max_height:
        ans = min(ans, visited[(x, y)])

if ans == float('inf'):
    print(-1)
else:
    print(ans)