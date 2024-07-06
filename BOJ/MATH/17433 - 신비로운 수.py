'''
BOJ 17433 - Mysterious Number (https://www.acmicpc.net/problem/17433)

Given N numbers, an integer M is mysterious if all N numbers are congruent to mod M.
Determine the highest mysterious number.
'''

import sys
from math import gcd


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    num_count = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    # If M is a mysterious number, then the difference of any pair of N numbers is a multiple of M.
    
    arr = list(set(arr))
    
    if len(arr) == 1:
        print("INFINITY")
    else:
    
        diff = []
        for idx in range(1, len(arr)):
            diff.append(arr[idx] - arr[idx-1])

        ans = diff[0]
        for idx in range(1, len(diff)):
            ans = gcd(ans, diff[idx])
        
        print(ans)