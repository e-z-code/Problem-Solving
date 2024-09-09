'''
ABC370C - Word Ladder (https://atcoder.jp/contests/abc370/tasks/abc370_c)

You are given two strings of equal length: S and T.
Let X be an empty array and repeat the following operation until S equals T: Change a character in S, and append S to the end of X.
Find X with the minimum number of elements. If there are multiple such arrays, find the lexicographically smallest one.
'''

import sys


# 1. TO GET THE INPUT

string = list(sys.stdin.readline().strip())
goal = list(sys.stdin.readline().strip())


# 2. TO SOLVE THE PROBLEM

better = []
worse = []

for idx in range(len(string)):
    if ord(string[idx]) > ord(goal[idx]):
        better.append(idx)
    elif ord(string[idx]) < ord(goal[idx]):
        worse.append(idx)
worse = reversed(worse)

ans = []

for idx in better:
    string[idx] = goal[idx]
    ans.append("".join(string))
for idx in worse:
    string[idx] = goal[idx]
    ans.append("".join(string))

print(len(ans))
for step in ans:
    print(step)