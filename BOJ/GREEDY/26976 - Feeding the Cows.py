'''
BOJ 26976 - Feeding the Cows (https://www.acmicpc.net/problem/26976)

There are N cows, either a Guernsey or a Holstein on a horizontal line.
Each cow can move a maximum of K to reach a patch.
Determine the minimum amount of patches needed and the optimal configuration to feed all cows.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    arr_length, cover_length = map(int, sys.stdin.readline().split())
    arr = list(sys.stdin.readline().strip())
    
    
    # 2. TO SOLVE THE PROBLEM
    
    patch_count = 0
    ans = ["." for idx in range(arr_length)]
    
    idx = 0
    while idx < arr_length:
        if arr[idx] == "G":
            idx = min(arr_length - 1, idx + cover_length)
            ans[idx] = "G"
            patch_count += 1
            idx += cover_length + 1
        else:
            idx += 1
    
    idx = 0
    while idx < arr_length:
        if arr[idx] == "H":
            idx = min(arr_length - 1, idx + cover_length)
            while ans[idx] != ".":
                idx -= 1
            ans[idx] = "H"
            patch_count += 1
            idx += cover_length + 1
        else:
            idx += 1

    print(patch_count)
    print("".join(ans))