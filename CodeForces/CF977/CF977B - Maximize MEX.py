'''
CF977B - Maximize MEX (https://codeforces.com/contest/2021/problem/B)

Given an array A of length N and integer X, you can do the following two-step operation any number of times.

(1) Choose an index i.
(2) Increase A[i] by X.

Find the maximum possible value of the MEX of A.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length, added_num = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    
    count = [0 for num in range(length + 1)]
    for num in arr:
        if num <= length:
            count[num] += 1
    
    for num in range(length + 1):
        if count[num] == 0:
            print(num)
            break
        else:
            if num + added_num <= length:
                count[num + added_num] += count[num] - 1
                count[num] = 1