'''
ABC367C - Enumerate Sequences (https://atcoder.jp/contests/abc367/tasks/abc367_c)

There is an array R of length N.
Print all integer arrays X that satisfy the following conditions in ascending order.

(1) 1 <= X[i] <= R[i]
(2) sum(X) % K = 0
'''

import sys
from itertools import product


# 1. TO GET THE INPUT

arr_length, divisor = map(int, sys.stdin.readline().split())
max_num = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM - BRUTEFORCE

ans = []

arrays = product([1, 2, 3, 4, 5], repeat=arr_length)

for array in arrays:
    
    valid = True
    
    for idx in range(arr_length):
        if array[idx] > max_num[idx]:
            valid = False
            break
    
    if sum(array) % divisor != 0:
        valid = False
    
    if valid:
        ans.append(list(array))

ans.sort()
for array in ans:
    print(" ".join(map(str, array)))