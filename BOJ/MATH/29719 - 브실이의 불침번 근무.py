'''
BOJ 29719 - Night Watch (https://www.acmicpc.net/problem/29719)

There are M soldiers, including you. A soldier should be a night watchman every day.
Determine the number of cases in which you become a night watchman at least once.
'''

import sys
mod = 10 ** 9 + 7


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM
# pow() function is already fast in Python.

day_count, soldier_count = map(int, sys.stdin.readline().split())
print((pow(soldier_count, day_count, mod) - pow(soldier_count-1, day_count, mod)) % mod)