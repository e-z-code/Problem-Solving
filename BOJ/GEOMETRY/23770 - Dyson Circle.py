'''
BOJ 23770 - Dyson Circle (https://www.acmicpc.net/problem/23770)

Given N points, determine the minimum possible length to enclose all points.
'''


import sys


# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))


# 2. TO SOLVE THE PROBLEM
# If you remove all dents, the sum of distances between two farthest suns on two diagonal axis determines the answer.

positive = set()
negative = set()

for x, y in points:
    positive.add(x + y)
    negative.add(x - y)

ans = 4
ans += max(positive) - min(positive) + max(negative) - min(negative)
# Corner case : If all starts are on the same diagonal, you should add 1 to connect inner grids.
if point_count != 1 and (len(positive) == 1 or len(negative) == 1):
    ans += 1
print(ans)