'''
BOJ 2261 - The Closest Pair (https://www.acmicpc.net/problem/2261)

Given N points on a 2D plane, calculate the distance between the closest pair.
'''

import sys
sys.setrecursionlimit(10 ** 5)


# 1. A FUNCTION TO GET THE DISTANCE BETWEEN TWO POINTS

def dist_squared(p1, p2):
    
    x1, y1 = p1
    x2, y2 = p2
    
    return pow(x1 - x2, 2) + pow(y1 - y2, 2)


# 2. DIVIDE AND CONQUER

def solve(left, right):
    
    if right - left == 1:
    
        p1 = points[left]
        p2 = points[right]
        return dist_squared(p1, p2)
    
    elif right - left == 2:
    
        p1 = points[left]
        p2 = points[left+1]
        p3 = points[right]
        return min(dist_squared(p1, p2), dist_squared(p2, p3), dist_squared(p1, p3))
    
    else:
        
        mid = (left + right) // 2
        
        left_best = solve(left, mid)
        right_best = solve(mid+1, right)
        
        # You do not need to consider points that has no hope of being the closest pair.
        
        band_width = min(left_best, right_best) ** 0.5
        possible_points = []
        for idx in range(left, right+1):
            if points[mid][0] - band_width < points[idx][0] < points[mid][0] + band_width:
                possible_points.append(points[idx])
        possible_points.sort(key = lambda x : x[1])

        # To consider next 11 points is enough. The proof can be done by the pigeonhole principle.
        # Reference: Yonsei University Algorithm Design Course
        
        overlap_best = float('inf')
        for i in range(len(possible_points)):
            now_point = possible_points[i]
            for j in range(i + 1, min(i + 12, len(possible_points))):
                compare_point = possible_points[j]
                overlap_best = min(overlap_best, dist_squared(now_point, compare_point))
        
        return min(left_best, right_best, overlap_best)


# 3. TO GET THE INPUT AND SOLVE THE PROBLEM

point_count = int(sys.stdin.readline())

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

if len(set(points)) != len(points):
    print(0)
else:
    points = list(set(points))
    points.sort()
    print(solve(0, len(points) - 1))