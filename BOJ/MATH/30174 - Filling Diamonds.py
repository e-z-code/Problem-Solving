'''
BOJ 30174 - Filling Diamonds (https://www.acmicpc.net/problem/30174)

Calculate how many ways are there to fully cover a belt-like area of 4N - 2 triangles with diamond shapes of 2 triangles.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM
# If you put one diamond straight, the others are determined.

test_count = int(sys.stdin.readline())

for test in range(test_count):

    length = int(sys.stdin.readline())
    print(length)