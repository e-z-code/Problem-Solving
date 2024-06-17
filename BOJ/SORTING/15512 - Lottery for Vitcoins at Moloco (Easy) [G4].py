'''
BOJ 15512 - Lottery for Vitcoins at Moloco [Easy] (https://www.acmicpc.net/problem/15512)

For each lottery, the prize value and winning probability are given.
At each step, you can choose a lottery and claim the prize immediately.
If you win the lottery, you can pick another one. 
Print the order that maximizes the prize value you win.
'''

import sys
from functools import cmp_to_key


# 2. COMPARISON FUNCTION

def compare(lotteryA, lotteryB):
    
    valA, probA, numA = lotteryA
    valB, probB, numB = lotteryB

    key = valB * (10000 - probB) - valA * (10000 - probA) + (valA + valB) * (probB - probA)
    if key > 0:
        return 1
    elif key < 0:
        return -1
    else:
        return 0


# 1. TO GET THE INPUT

lottery_count = int(sys.stdin.readline())

lottery = []
for lottery_num in range(1, lottery_count+1):
    val, prob = map(int, sys.stdin.readline().split())
    lottery.append((val, prob, lottery_num))


# 3. TO SOLVE THE PROBLEM

ans = sorted(lottery, key = cmp_to_key(compare))
for val, prob, num in ans:
    print(num, end = ' ')