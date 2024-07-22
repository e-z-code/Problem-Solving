'''
BOJ 2375 - Basketball Hoop Installation (https://www.acmicpc.net/problem/2375)

Given N points, choose a point X such that the sum of manhattan distances from X to N points is minimum.
'''

import sys


# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())

points = []

x_coordinates = []
y_coordinates = []

for point in range(point_count):
    
    x, y, repeat_count = map(int, sys.stdin.readline().split())
    points.append((x, y))
    
    for repeat in range(repeat_count):
        x_coordinates.append(x)
        y_coordinates.append(y)

x_coordinates.sort()
y_coordinates.sort()


# 2. TO SOLVE THE PROBLEM

length = len(x_coordinates)
print(x_coordinates[(length-1) // 2], y_coordinates[(length-1) // 2])