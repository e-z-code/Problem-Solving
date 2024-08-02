'''
BOJ 27727 - Button Sort (https://www.acmicpc.net/problem/27727)

There is a sequence A of length N.
If you push a button, the minimum value of the sequence will increase by 1.
If there are multiple minimum values, the foremost element will increase.
Given K, calculate how many times A is sorted.
'''

import sys


# 1. TO GET THE INPUT

arr_length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
push_count = int(sys.stdin.readline())


# 2. PUSH UNTIL THE FIRST SORT

push_to_sort = 0

target_val = 0
for idx in range(arr_length - 1):
    if arr[idx] > arr[idx+1]:
        target_val = max(target_val, arr[idx])

for idx in range(arr_length):
    if target_val > arr[idx]:
        push_to_sort += target_val - arr[idx]
        arr[idx] = target_val
        


# 3. TO SOLVE THE PROBLEM

if push_to_sort > push_count:
    print(0)
elif push_to_sort == push_count:
    print(1)
else:

    ans = 1
    if push_to_sort == 0:
        ans = 0
    push_count -= push_to_sort

    for idx in range(1, arr_length):
        push_needed = (arr[idx] - arr[idx-1]) * idx
        if push_needed <= push_count:
            ans += arr[idx] - arr[idx-1]
            push_count -= push_needed
        else:
            ans += push_count // idx
            push_count = 0
            break
    
    if push_count != 0:
        ans += push_count // arr_length
        push_count = 0

    print(ans)