'''
BOJ 25212 - Slice Cake (https://www.acmicpc.net/problem/25212)

There are N slice cakes. 
If the sum of the size of some slices is between 0.99 and 1.01, you can make a cake.
Calculate the number of distinct cases that can make a cake. 
'''

import sys
from fractions import Fraction
from itertools import combinations


# 1. TO GET THE INPUT

piece_count = int(sys.stdin.readline())
piece_size = list(map(int, sys.stdin.readline().split()))
for idx in range(piece_count):
    piece_size[idx] = Fraction(1, piece_size[idx])


# 2. TO SOLVE THE PROBLEM

ans = 0

for choice_count in range(piece_count + 1):
    for now_case in combinations(piece_size, choice_count):
        if Fraction(99, 100) <= sum(now_case) <= Fraction(101, 100):
            ans += 1

print(ans)