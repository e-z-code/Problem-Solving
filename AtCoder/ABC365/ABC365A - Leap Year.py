'''
ABC365A - Leap Year (https://atcoder.jp/contests/abc365/tasks/abc365_a)

The year Y is given.
If the year is a leap year, print 366.
Otherwise, print 365. 
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

year = int(sys.stdin.readline())

if year % 4 != 0:
    print(365)
else:
    if year % 100 != 0:
        print(366)
    else:
        if year % 400 != 0:
            print(365)
        else:
            print(366)