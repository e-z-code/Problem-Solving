'''
BOJ 19250 - Flat Earth (https://www.acmicpc.net/problem/19250)

Given a sphere and a plane, calculate the area of a projection of the sphere onto the plane.
'''

import sys
from math import pi


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

# Earth : A sphere of which radius is r and center is (x, y, z)
# Sky : ax + by + cz + d = 0
# The area of the shadow is always the area of the largest circle from the Earth.  

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    x, y, z, r, a, b, c, d = map(int, sys.stdin.readline().split())
    print(pi * pow(r, 2))