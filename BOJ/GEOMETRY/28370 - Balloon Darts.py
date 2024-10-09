'''
BOJ 28370 - Balloon Darts (https://www.acmicpc.net/problem/28370)

Given N points, determine if it is possible to cover all points with three straight lines.
'''

import sys
from random import sample


# 2. CCW

def same_line(p1, p2, p3):
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    if x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3 == 0:
        return True
    else:
        return False


# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))


# 3. RANDOMIZATION

ans = "impossible"
count = 100

while count:
    
    if len(points) < 2:
        ans = "possible"
        break
    
    leftA = []
    i, j = sample(range(point_count), 2)
    for idx in range(point_count):
        if not same_line(points[i], points[j], points[idx]):
            leftA.append(points[idx])
    
    if len(leftA) < 2:
        ans = "possible"
        break
    
    leftB = []
    i, j = sample(range(len(leftA)), 2)
    for idx in range(len(leftA)):
        if not same_line(leftA[i], leftA[j], leftA[idx]):
            leftB.append(leftA[idx])
    
    if len(leftB) < 2:
        ans = "possible"
        break
    
    result = True
    for idx in range(2, len(leftB)):
        if not same_line(leftB[0], leftB[1], leftB[idx]):
            result = False
            break
    
    if result:
        ans = "possible"
        break
    
    count -= 1

print(ans)