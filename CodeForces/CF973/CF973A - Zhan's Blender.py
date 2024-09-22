'''
CF973A - Zhan's Blender (https://codeforces.com/contest/2013/problem/A)

Zhan has N fruits.
The blender can mix up to X fruits per second, and Zhan can put up to Y fruits into the blender.
Determine the minimum amount of time required to blend all fruits.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    fruit_count = int(sys.stdin.readline())
    blender_max, input_max = map(int, sys.stdin.readline().split())
    
    ans = fruit_count // min(blender_max, input_max)
    if fruit_count % min(blender_max, input_max) != 0:
        ans += 1
    print(ans)