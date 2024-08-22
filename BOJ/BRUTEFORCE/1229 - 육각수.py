'''
BOJ 1229 - Hexagonal Number (https://www.acmicpc.net/problem/1229)

Given N, calculate the minimum number X such that X hexagonal numbers exist, the sum of which equals N.
'''

import sys
from itertools import product


# 1. TO GET HEXAGONAL NUMBERS

goal_num = int(sys.stdin.readline())

hexagonal_nums = [1]
add_num = 5
while hexagonal_nums[-1] + add_num <= goal_num:
    hexagonal_nums.append(hexagonal_nums[-1] + add_num)
    add_num += 4


# 2. TO SOLVE THE PROBLEM

ans = 0
done = False
for num_count in range(1, 7):
    for perm in product(hexagonal_nums, repeat=num_count):
        if sum(perm) == goal_num:
            ans = num_count
            done = True
            break
    if done:
        break

print(ans)