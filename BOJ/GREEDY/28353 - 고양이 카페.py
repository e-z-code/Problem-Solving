'''
BOJ 28353 - Cat Cafe (https://www.acmicpc.net/problem/28353)

There are N cats.
Your friends are happy if they carry two cats and the sum of their weights does not exceed K.
Determine the maximum number of friends who can be happy.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

cat_count, max_weight = map(int, sys.stdin.readline().split())
cat_weight = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

cat_weight.sort()
cat_weight = deque(cat_weight)

ans = 0

while len(cat_weight) >= 2:
    if cat_weight[0] + cat_weight[-1] <= max_weight:
        ans += 1
        cat_weight.popleft()
        cat_weight.pop()
    else:
        cat_weight.pop()

print(ans)