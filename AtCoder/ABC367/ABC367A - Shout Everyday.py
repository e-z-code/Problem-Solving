'''
ABC367A - Shout Everyday (https://atcoder.jp/contests/abc367/tasks/abc367_a)

You are given three times: A, B, and C.
Determine whether A is between B and C.
'''

import sys


# 1. TO GET THE INPUT

shout_time, sleep_time, wake_time = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

if shout_time < sleep_time:
    shout_time += 24
if wake_time < sleep_time:
    wake_time += 24

if sleep_time <= shout_time <= wake_time:
    print("No")
else:
    print("Yes")