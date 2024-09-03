'''
BOJ 32158 - SWAPC

Given a string, swap P and C as much as you can.
'''

import sys


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())
string = list(sys.stdin.readline().strip())


# 2. TO SOLVE THE PROBLEM

p_loc = []
c_loc = []

for idx in range(size):
    char = string[idx]
    if char == "P":
        p_loc.append(idx)
    if char == "C":
        c_loc.append(idx)

for idx in range(min(len(p_loc), len(c_loc))):
    string[p_loc[idx]] = "C"
    string[c_loc[idx]] = "P"

print("".join(string))