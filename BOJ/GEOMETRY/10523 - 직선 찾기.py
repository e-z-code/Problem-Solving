'''
BOJ 10523 - Find the line (https://www.acmicpc.net/problem/10523)

Given N points, determine if there is a line that crosses at least P% of total points.
'''

import sys, random


# 2. A FUNCTION TO CHECK WHETHER THREE POINTS ARE ON THE SAME LINE

def line(x1, y1, x2, y2, x3, y3):
    
    if x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3 == 0:
        return True
    else:
        return False


# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())
percentage = int(sys.stdin.readline())

min_point = point_count * percentage // 100
if (point_count * percentage) % 100 != 0:
    min_point += 1

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))


# 3. TO SOLVE THE PROBLEM - RANDOMIZATION
# Since 20 <= P <= 100, the worst possibility is around 4%.

if point_count == 1:
    
    print("possible")

else:
    
    ans = "impossible"
    loop = 500

    while loop:
        
        pointA, pointB = random.sample(points, 2)
        x1, y1 = pointA
        x2, y2 = pointB
        
        count = 0
        for point in points:
            x3, y3 = point
            if line(x1, y1, x2, y2, x3, y3):
                count += 1
        
        if count >= min_point:
            ans = "possible"
            break

        loop -= 1

    print(ans)