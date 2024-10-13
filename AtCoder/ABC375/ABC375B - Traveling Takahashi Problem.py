'''
ABC375B - Traveling Takahashi Problem (https://atcoder.jp/contests/abc375/tasks/abc375_b)

Given N points, calculate the minimum distance to visit each node in that order.
'''

import sys


# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())
points = [(0, 0)]
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))
points.append((0, 0))


# 2. TO SOLVE THE PROBLEM

ans = 0
for idx in range(1, len(points)):
    
    x1, y1 = points[idx]
    x2, y2 = points[idx-1]
    
    ans += pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)

print(ans)