'''
BOJ 4311 - Expanding Rods (https://www.acmicpc.net/problem/4311)

A thin rod of length L expands to (1 + N X C) X L when heated N degrees.
When a thin rod is mounted on two walls and then heated, it takes the shape of a circular segment, with the original rod being the chord.
Determine the distance by which the center of the rod is displaced.
'''

import sys
from math import cos, sin


# 1. TO GET THE INPUT

while True:
    
    rod_length, temperature, coefficient = map(float, sys.stdin.readline().split())
    if rod_length == -1 and temperature == -1 and coefficient == -1:
        break
    
    
    # 2. TO GET THE CENTRAL ANGLE AND RADIUS - BINARY SEARCH
    
    count = 0
    
    left = 0
    right = 3.14159265368979
    
    while count <= 100:
        
        mid = (left + right) / 2
        
        key = mid / sin(mid / 2)
        if key >= (2 + 2 * temperature * coefficient):
            right = mid
        else:
            left = mid
        
        count += 1
    
    central_angle = right
    radius = (rod_length / central_angle) * (1 + temperature * coefficient)
    
    
    # 3. TO SOLVE THE PROBLEM
    
    print(format(radius * (1 - cos(central_angle / 2)), ".3f"))