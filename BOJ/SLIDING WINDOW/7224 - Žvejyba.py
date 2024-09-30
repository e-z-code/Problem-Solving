'''
BOJ 7224 - Fishing (https://www.acmicpc.net/problem/7224)

Given an array X and an integer N, determine the index I where X[I:I+N] has the most 'L'.
If there are multiple indices, print the smallest one. 
'''

import sys


# 1. TO GET THE INPUT

day_count, length = map(int, sys.stdin.readline().split())
days = list(sys.stdin.readline().strip())


# 2. TO SOLVE THE PROBLEM

ans = -1
rainy_max = -1

rainy = 0

for start in range(day_count):
    
    if start == 0:
        for day in range(start, start + length):
            if days[day] == "L":
                rainy += 1
    else:
        if days[start-1] == "L":
            rainy -= 1
        if days[start+length-1] == "L":
            rainy += 1
    
    if rainy_max < rainy:
        rainy_max = rainy
        ans = start + 1

print(ans)