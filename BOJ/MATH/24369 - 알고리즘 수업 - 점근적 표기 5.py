'''
BOJ 24369 - Algorithm 101 : Asymptotic Notation 5 (https://www.acmicpc.net/problem/24369)

You are given f(n), C, and N.
Determine if f(n) >= C X n^2 for all n >= N.
'''

import sys


# 2. A FUNCTION F

def f(x):
    return a * pow(x, 2) + b * x + c


# 1. TO GET THE INPUT
# Let's assume f(x) = ax^2 + bx + c

a, b, c = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
N = int(sys.stdin.readline())


# 3. TO SOLVE THE PROBLEM

a -= C

if a < 0:
    print(0)
elif a > 0:
    axis = - b / (2 * a)
    if axis <= N:
        if f(N) >= 0:
            print(1)
        else:
            print(0)
    else:
        if f(axis) >= 0:
            print(1)
        else:
            print(0)
else:
    if b != 0:
        if b > 0:
            if b * N + c >= 0:
                print(1)
            else:
                print(0)
        else:
            print(0)
    else:
        if c >= 0:
            print(1)
        else:
            print(0)