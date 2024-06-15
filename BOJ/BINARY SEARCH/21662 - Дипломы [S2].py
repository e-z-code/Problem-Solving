'''
BOJ 21662 - Diplomas (https://www.acmicpc.net/problem/21662)

There are N diplomas of size W X H.
Print the minimum value of A so that all diplomas can fit in A X A square.
'''

import sys


# 1. TO GET THE INPUT

width, height, count = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

left = 0
right = 10 ** 14

while left + 1 < right:
    
    length = (left + right) // 2
    max_count = (length // width) * (length // height)

    if max_count >= count:
        right = length
    else:
        left = length

print(right)