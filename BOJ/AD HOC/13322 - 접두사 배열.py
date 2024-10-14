'''
BOJ 13322 - Prefix Array (https://www.acmicpc.net/problem/13322)

Given a string, sort every prefix in lexicographical order.
Then, print the starting index of each prefix in that order.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

string = sys.stdin.readline().strip()

for idx in range(len(string)):
    print(idx)