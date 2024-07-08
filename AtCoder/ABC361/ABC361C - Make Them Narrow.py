'''
ABC361C - Make Them Narrow (https://atcoder.jp/contests/abc361/tasks/abc361_c)

You can create a new array B by removing K elements from an array A of length N.
Determine the minimum value of max(B) - min(B).
'''

import sys


# 1. TO GET THE INPUT

arr_length, remove_count = map(int, sys.stdin.readline().split())
new_length = arr_length - remove_count

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()


# 2. TO SOLVE THE PROBLEM

if new_length <= 1:
    
    print(0)
    
else:
    
    ans = float('inf')
    for idx in range(new_length-1, arr_length):
        ans = min(ans, arr[idx] - arr[idx - new_length + 1])
    print(ans)