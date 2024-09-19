'''
BOJ 8346 - Logarithmic Paprika (https://www.acmicpc.net/problem/8346)

Given powers of 2, determine the minimum number you cannot make.
'''


import sys


# 1. TO GET THE INPUT

max_exp = int(sys.stdin.readline())
count = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

num = 1

while True:

    goal = num
    
    for exp in range(max_exp, -1, -1):
        if (1 << exp) <= goal:
            goal -= (1 << exp) * min(count[exp], goal // (1 << exp))
    
    if goal != 0:
        break
    num += 1

print(num)