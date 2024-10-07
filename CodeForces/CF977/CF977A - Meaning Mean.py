'''
CF977A - Meaning Mean (https://codeforces.com/contest/2021/problem/A)

There is an array A of N positive integers.
You repeat the following three-step operations until the array size becomes 1.

(1) Pick two indices i and j.
(2) Append (A[i] + A[j]) // 2 to the end.
(3) Remove A[i] and a[j].

Determine the maximum possible value of the element left.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    num_count = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    
    ans = arr[0]
    for idx in range(1, num_count):
        ans = (ans + arr[idx]) // 2
    print(ans)