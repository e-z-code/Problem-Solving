'''
BOJ 6840 - Who is in the middle? (https://www.acmicpc.net/problem/6840)

Given three integers, print the second largest one.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

numA = int(sys.stdin.readline())
numB = int(sys.stdin.readline())
numC = int(sys.stdin.readline())

arr = [numA, numB, numC]
print(sum(arr) - max(arr) - min(arr))