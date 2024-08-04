'''
ABC365B - Second Best (https://atcoder.jp/contests/abc365/tasks/abc365_b)

Given an array, print the index of the second largest element.
'''

import sys


# 1. TO GET THE INPUT

arr_length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

arr_copy = arr[:]
arr_copy.sort()
second_largest = arr_copy[-2]

for idx in range(arr_length):
    if arr[idx] == second_largest:
        print(idx + 1)
        break