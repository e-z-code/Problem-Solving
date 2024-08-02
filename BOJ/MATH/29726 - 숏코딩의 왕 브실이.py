'''
BOJ 29726 - Brosil the King of Short Coding (https://www.acmicpc.net/problem/29726)

There is a sequence A of length L. 
The happiness of the sequence is A[L] - A[1].
Given that you can erase at most M elements, print the maximum value of happiness.
'''

import sys


# 1. TO GET THE INPUT

arr_length, erase_count = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


# 2. SOLVE THE PROBLEM

# This part is the optimization of the following code.

'''
min_length = arr_length - erase_count

ans = -float('inf')
for start_idx in range(arr_length - min_length + 1):
    for last_idx in range(start_idx + min_length - 1, arr_length):
        ans = max(ans, arr[last_idx] - arr[start_idx])
print(ans)
'''

# The maximum value of arr[idx:].

max_until_end = [0 for idx in range(arr_length)]
max_until_end[arr_length-1] = arr[arr_length-1]

for idx in range(arr_length-2, -1, -1):
    max_until_end[idx] = max(arr[idx], max_until_end[idx+1])

# Get the maximum value.

min_length = arr_length - erase_count

ans = -float('inf')
for start_idx in range(arr_length - min_length + 1):
    last_idx = start_idx + min_length - 1
    ans = max(ans, max_until_end[last_idx] - arr[start_idx])
print(ans)