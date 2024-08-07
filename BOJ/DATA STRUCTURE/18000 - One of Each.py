'''
BOJ 18000 - One of Each (https://www.acmicpc.net/problem/18000)

There is an array X of length N in which 1 to K appears at least once.
Find the lexicographically smallest subsequence that contains 1 to K exactly once.
'''

import sys


# 1. TO GET THE INPUT

arr_length, max_num = map(int, sys.stdin.readline().split())
arr = []

for idx in range(arr_length):
    num = int(sys.stdin.readline())
    arr.append(num)


# 2. TO SOLVE THE PROBLEM

last_idx = [0 for num in range(max_num + 1)]
for idx in range(arr_length):
    last_idx[arr[idx]] = idx

is_included = [0 for num in range(max_num + 1)]
stack = []
for idx in range(arr_length):
    num = arr[idx]
    if is_included[num]:
        continue
    else:
        while len(stack) != 0 and stack[-1] > num and last_idx[stack[-1]] > idx:
            is_included[stack[-1]] = 0
            stack.pop()
        is_included[num] = 1
        stack.append(num)

for num in stack:
    print(num, end = ' ')