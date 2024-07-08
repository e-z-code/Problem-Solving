'''
ABC361B - Intersection of Cuboids (https://atcoder.jp/contests/abc361/tasks/abc361_b)

Given two cuboids, determine whether they intersect or not.
'''

import sys


# 1. A FUNCTION TO DETERMINE INTERSECTION

def intersect(x1, x2, x3, x4):
    
    if x4 <= x1 or x3 >= x2:
        return False
    else:
        return True


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM
# If segments of all axes intersect, two cuboids intersect. 

x1, y1, z1, x2, y2, z2= map(int, sys.stdin.readline().split())
x3, y3, z3, x4, y4, z4 = map(int, sys.stdin.readline().split())

if intersect(x1, x2, x3, x4) and intersect(y1, y2, y3, y4) and intersect(z1, z2, z3, z4):
    print("Yes")
else:
    print("No")
