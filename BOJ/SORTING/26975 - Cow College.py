'''
BOJ 26975 - Cow College (https://www.acmicpc.net/problem/26975)

There are N students.
Given the maximum tuition each student will pay, determine tuition to maximize revenue.
'''

import sys


# 1. TO GET THE INPUT

cow_count = int(sys.stdin.readline())
cows_demand = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

cows_demand.sort(reverse=True)

max_revenue = 0
ans_tuition = 0

for idx in range(cow_count):
    tuition = cows_demand[idx]
    if tuition * (idx + 1) >= max_revenue:
        max_revenue = tuition * (idx + 1)
        ans_tuition = tuition

print(max_revenue, ans_tuition)