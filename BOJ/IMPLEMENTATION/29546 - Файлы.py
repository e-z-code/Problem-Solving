'''
BOJ 29546 - Files (https://www.acmicpc.net/problem/29546)

There are N photos numbered from 1 to N.
For each interval [L, R], print photo names from number L to R in ascending order.
'''

import sys


# 1. TO GET THE INPUT

photo_count = int(sys.stdin.readline())
photos = {}

for photo_num in range(1, photo_count + 1):
    photo_name = sys.stdin.readline().strip()
    photos[photo_num] = photo_name


# 2. TO SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())
for query in range(query_count):
    left, right = map(int, sys.stdin.readline().split())
    for num in range(left, right+1):
        print(photos[num])