'''
BOJ 32032 - Pace Counter Agent Service (https://www.acmicpc.net/problem/32032)

There are N points on an x-axis.
For every point, you should walk D meters after first arriving at a point and return to the point.
You must come back to 0 after visiting all points.
Determine the minimum distance to walk. 
'''

import sys


# 1. TO GET THE INPUT

point_count, dist = map(int, sys.stdin.readline().split())
points = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM
# After arriving at the leftmost (or rightmost) point, we should consider whether it is beneficial to move to the other end. 

points.sort()

if 0 < points[0]:
    print(points[-1] * 2 + dist)
elif points[-1] < 0:
    print(abs(points[0]) * 2 + dist)
else:
    total_length = points[-1] - points[0]
    print(2 * total_length + min(2 * dist, 2 * points[-1] + dist, 2 * abs(points[0]) + dist, max(2 * total_length, dist)))