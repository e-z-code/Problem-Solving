'''
BOJ 20222 - Jam-packed (https://www.acmicpc.net/problem/20222)

You want to pack N jars of jam. Each box can hold up to K jars.
You want the box with the least number of jars to be as full as possible.
Determine the number of jars that the least filled box contains.
'''

import sys


# 1. TO GET THE INPUT

jar_count, max_capacity = map(int, sys.stdin.readline().split())


# 2. PARAMETRIC SEARCH

# To get the number of boxes needed

box_count = jar_count // max_capacity
if jar_count % max_capacity != 0:
    box_count += 1

# Is the minimum capacity valid?

left = 0
right = max_capacity

while left + 1 < right:
    
    mid = (left + right) // 2
    
    if mid * box_count <= jar_count:
        left = mid
    else:
        right = mid

if max_capacity * box_count == jar_count:
    print(right)
else:
    print(left)