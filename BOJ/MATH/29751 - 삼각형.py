'''
BOJ 29751 - Triangle (https://www.acmicpc.net/problem/29751)

Calculate the area of a given triangle.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

width, height = map(int, sys.stdin.readline().split())
print(format(width * height / 2, ".1f"))