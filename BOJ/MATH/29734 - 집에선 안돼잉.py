'''
BOJ 29734 - Not in Home (https://www.acmicpc.net/problem/29734)

You have an assignment to do.
Whenever you do an assignment for 8 hours, you must sleep at home.
Determine where you should study: home or outside.
'''

import sys


# 2. A FUNCTION FOR CEILED DIVISION

def divide_ceil(x, y):
    
    if x % y == 0:
        return x // y
    else:
        return x // y + 1


# 1. TO GET THE INPUT

home_study, outside_study = map(int, sys.stdin.readline().split())
move, sleep = map(int, sys.stdin.readline().split())


# 3. TO SOLVE THE PROBLEM

home_total = (divide_ceil(home_study, 8) - 1) * sleep + home_study
outside_total = (divide_ceil(outside_study, 8) - 1) * (move * 2 + sleep) + move + outside_study

if home_total < outside_total:
    print("Zip")
    print(home_total)
else:
    print("Dok")
    print(outside_total)