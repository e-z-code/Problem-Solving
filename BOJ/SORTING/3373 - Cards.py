'''
BOJ 3373 - Cards (https://www.acmicpc.net/problem/3373)

You are given N double-sided cards.
Fill in the following equation and minimize the result.

□ - □ + □ - □ + ... + □ - □
'''

import sys


# 1. TO GET THE INPUT

card_count = int(sys.stdin.readline())

cards = []
for card in range(card_count):
    front, back = map(int, sys.stdin.readline().split())
    cards.append((front + back, min(front, back), max(front, back)))
    

# 2. TO SOLVE THE PROBLEM
# You should put larger number for - and smaller number for +.
# The cost for changing a card (X, Y) from - to + equals X + Y.

cards.sort()

ans = 0
for idx in range(card_count // 2):
    ans += cards[idx][1]
    ans -= cards[-idx-1][2]
print(ans)