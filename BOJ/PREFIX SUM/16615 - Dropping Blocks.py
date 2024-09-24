'''
BOJ 16615 - Dropping Blocks (https://www.acmicpc.net/problem/16615)

The game starts with N empty piles of blocks in a line.
You do the following operation: Choose a pile K and put a block in every pile either to the left or right of pile K.
Given a game state, determine whether the state is valid.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

# Get the minimum number of time each index is chosen

left = [0 for idx in range(length)]
right = [0 for idx in range(length)]

for idx in range(1, length):
    
    if arr[idx-1] > arr[idx]:
        left[idx-1] = arr[idx-1] - arr[idx]

    if arr[idx-1] < arr[idx]:
        right[idx] = arr[idx] - arr[idx-1]

# Get the minimum number of blocks for each index

for idx in range(length-2, -1, -1):
    left[idx] += left[idx+1]
for idx in range(1, length):
    right[idx] += right[idx-1]

ans = "YES"
for idx in range(length):
    if left[idx] + right[idx] > arr[idx]:
        ans = "NO"
        break
print(ans)