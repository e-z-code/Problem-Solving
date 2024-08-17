'''
ABC367B - Cut .0 (https://atcoder.jp/contests/abc367/tasks/abc367_b)

Given a decimal, delete unnecessary trailing zeros.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

num = list(sys.stdin.readline().strip())

while num.count(".") == 1 and (num[-1] == "0" or num[-1] == "."):
    num.pop()
print("".join(num))