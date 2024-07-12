'''
BOJ 2751 - Last Letter (https://www.acmicpc.net/problem/2751)

There is a string S.
If the last letter is 'G', delete it. Otherwise, add 'G'.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

length = int(sys.stdin.readline())
string = sys.stdin.readline().strip()

if string[-1] == "G":
    print(string[:-1])
else:
    print(string + "G")