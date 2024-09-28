'''
CF975B - All Pairs Segments (https://codeforces.com/contest/2019/problem/B)

You are given N points.
For every pair (i, j) with 1 <= i < j <= N, you draw the segment A[i] ~ A[j].
Answer Q queries: Calculate how many integer points are in K segments.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    point_count, query_count = map(int, sys.stdin.readline().split())
    points = list(map(int, sys.stdin.readline().split()))
    queries = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
        
    dict = {}
    
    # Each endpoint
    for idx in range(point_count):
        count = (idx + 1) * (point_count - idx) - 1
        dict[count] = dict.get(count, 0) + 1
    # Points between two endpoints
    for idx in range(1, point_count):
        count = idx * (point_count - idx)
        dict[count] = dict.get(count, 0) + points[idx] - points[idx-1] - 1
    
    for query in queries:
        print(dict.get(query, 0), end = ' ')
    print()