'''
CF973B - Battle for Survive (https://codeforces.com/contest/2013/problem/B)

There is an array A of length N.
You can repeat the following steps N - 1 times.

(1) Choose valid indices i and j.
(2) A[j] = A[j] - A[i]
(3) i becomes an invalid index.

Determine the maximum possible value of the last remaining index.  
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    fighter_count = int(sys.stdin.readline())
    fighters = list(map(int, sys.stdin.readline().split()))
    
    ans = fighters[-1] - (fighters[-2] - sum(fighters[:-2]))
    print(ans)