'''
CF958C - Increasing Sequence with Fixed OR (https://codeforces.com/contest/1988/problem/C)

Given a positive integer N, find the longest sequence of positive integers A that satisfies the following conditions.

(1) All elements are equal to or less than N.
(2) A is strictly increasing. 
(3) A[i] | A[i-1] = N for 1 <= i < len(A).
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    num = int(sys.stdin.readline())


    # 2. TO SOLVE THE PROBLEM  
    # One way to construct A is to make a set of numbers that are only a bit off from N.
    
    ans = [num]
    
    now = 1
    while now <= num:
        if num & now:
            if num ^ now != 0:
                ans.append(num ^ now)
        now *= 2
    
    ans.sort()
    
    print(len(ans))
    for num in ans:
        print(num, end = ' ')
    print()