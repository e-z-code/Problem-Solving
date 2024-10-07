'''
BOJ 29669 - Triangle (https://www.acmicpc.net/problem/29669)

Given a triangle, select three points on the sides such that the triangle they formed has an area of S.
'''


import sys


# 1. TO GET THE INPUT

x1, y1, x2, y2, x3, y3 = map(int, sys.stdin.readline().split())
goal_area = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM
# It is enough to calculate the point that internally divides P1-P2 to goal_area : (area - goal_area).

area = abs(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3) / 2

if goal_area > area:
    print("No solution")
else:
    x = (x1 * (area - goal_area) + x2 * goal_area) / area
    y = (y1 * (area - goal_area) + y2 * goal_area) / area
    print(x1, y1)
    print(x3, y3)
    print(x, y)