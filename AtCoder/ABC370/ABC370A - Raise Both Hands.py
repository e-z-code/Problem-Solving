'''
ABC370A - Raise Both Hands (https://atcoder.jp/contests/abc370/tasks/abc370_a)

If Snuke only raises his left hand, it means "Yes".
If Snuke only raises his right hand, it means "No".
Otherwise, the signal is invalid.
Determine what signal Snuke sent.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

left, right = map(int, sys.stdin.readline().split())

if left + right == 1:
    if left == 1:
        print("Yes")
    else:
        print("No")
else:
    print("Invalid")