'''
BOJ 9881 - Ski Course Design (https://www.acmicpc.net/problem/9881)

There are N hills in Farmer John's ski training camp. 
John wants to reduce the difference between the highest and the lowest hill equal to or smaller than 17.
It costs pow(x, 2) money to change the height of a hill by x units.
Calculate the minimum amount of money Farmer John will need to pay.
'''

import sys


# 1. TO GET THE INPUT

hill_count = int(sys.stdin.readline())

heights = []
for hill in range(hill_count):
    height = int(sys.stdin.readline())
    heights.append(height)


# 2. TO SOLVE THE PROBLEM

ans = float('inf')
for min_height in range(101):
    cost = 0
    for height in heights:
        if height < min_height:
            cost += pow(min_height - height, 2)
        elif height > min_height + 17:
            cost += pow(height - min_height - 17, 2)
    if cost < ans:
        ans = cost
print(ans)