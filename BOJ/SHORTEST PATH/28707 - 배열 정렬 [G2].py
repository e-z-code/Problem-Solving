'''
BOJ 28707 - Array Sort (https://www.acmicpc.net/problem/28707)

There is an array A of length N.
You are given M operations (L, R, C): Swap A[L] and A[R] using the cost of C.
Determine the minimum cost to sort the array.
'''

import sys, heapq
from itertools import permutations


# 1. TO GET THE INPUT

arr_length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

op_count = int(sys.stdin.readline())
op = []
for op_input in range(op_count):
    left, right, cost = map(int, sys.stdin.readline().split())
    op.append((left-1, right-1, cost))


# 2. NUMBER EACH POSSIBLE CASE
# There are at most 40320 cases. (N <= 8)

case_to_num = {}

case = list(set(permutations(arr)))
for idx in range(len(case)):
    case_to_num[case[idx]] = idx
    

# 3. DIJKSTRA

dist = [float('inf') for idx in range(len(case))]

heap = [(0, tuple(arr))]
dist[case_to_num[tuple(arr)]] = 0
while heap:
    now_dist, now_case = heapq.heappop(heap)
    if now_dist <= dist[case_to_num[now_case]]:
        for left, right, cost in op:
            
            next_dist = now_dist + cost
            next_case = list(now_case)
            next_case[left], next_case[right] = next_case[right], next_case[left]
            next_case = tuple(next_case)
            
            if next_dist < dist[case_to_num[next_case]]:
                dist[case_to_num[next_case]] = next_dist
                heapq.heappush(heap, (next_dist, next_case))


# 4. TO SOLVE THE PROBLEM

goal = tuple(sorted(arr))
if dist[case_to_num[goal]] == float('inf'):
    print(-1)
else:
    print(dist[case_to_num[goal]])