'''
BOJ 28732 - DnD Dice (https://www.acmicpc.net/problem/28732)

There are five dice: tetrahedron, cube, octahedron, dodecahedron, and icosahedron.
Given the number of each dice, sort all possible sums of dice rolls in non-increasing probability.
'''

import sys


# 1. TO GET THE INPUT

dice_count = list(map(int, sys.stdin.readline().split()))
dice_info = [4, 6, 8, 12, 20]

total_dice = sum(dice_count)


# 2. DP
# dp[i][j] = The number of cases when you used i dices and sum is j

now_idx = 0

dp = [[0 for j in range(501)] for i in range(total_dice)]

for i in range(total_dice):
    
    while dice_count[now_idx] == 0:
        now_idx += 1
    
    if i == 0:
        for j in range(1, dice_info[now_idx] + 1):
            dp[i][j] = 1
    else:
        for j in range(1, 501):
            for k in range(max(1, j - dice_info[now_idx]), j):
                dp[i][j] += dp[i-1][k]

    dice_count[now_idx] -= 1


# 3. TO SOLVE THE PROBLEM

case_count = []
for num in range(1, 501):
    if dp[-1][num] != 0:
        case_count.append((dp[-1][num], num))
case_count.sort(reverse=True)

for count, num in case_count:
    print(num, end = ' ')