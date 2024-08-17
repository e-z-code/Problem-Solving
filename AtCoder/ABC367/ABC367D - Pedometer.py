'''
ABC367D - Pedometer (https://atcoder.jp/contests/abc367/tasks/abc367_d)

There are N points around a circle numbered from 1 to N.
The distances between adjacent points are given.
Find the number of pairs (s, t) such that the clockwise distance from s to t is a multiple of M.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

point_count, divisor = map(int, sys.stdin.readline().split())
dist = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

ans = 0
count = [0 for mod in range(divisor)]

arr = deque([0])
count[0] = 1

for idx in range(point_count):
    add_val = (arr[-1] + dist[idx]) % divisor
    arr.append(add_val)
    count[add_val] += 1
    if len(arr) >= point_count:
        delete_val = arr.popleft()
        count[delete_val] -= 1
        ans += count[delete_val]

for idx in range(point_count - 2):
    add_val = (arr[-1] + dist[idx]) % divisor
    arr.append(add_val)
    count[add_val] += 1
    if len(arr) >= point_count:
        delete_val = arr.popleft()
        count[delete_val] -= 1
        ans += count[delete_val]

print(ans)