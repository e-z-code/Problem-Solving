'''
BOJ 13713 - String and Query (https://www.acmicpc.net/problem/13713)

Given a string, answer the query: Determine the length of the longest common prefix of S and S[i:].
'''

import sys


# 1. TO GET THE INPUT

string = sys.stdin.readline().strip()
string = string[::-1]


# 2. Z ALGORITHM
# z[i] = The length of the longest common prefix of S and S[i:]

max_prefix_left = 0
max_prefix_right = 0

z = [0 for idx in range(len(string))]
z[0] = len(string)

for idx in range(1, len(string)):
    
    if idx > max_prefix_right:
        z[idx] = 0
    else:
        z[idx] = min(z[idx - max_prefix_left], max_prefix_right - idx + 1)
    
    while idx + z[idx] < len(string) and string[z[idx]] == string[idx + z[idx]]:
        z[idx] += 1
    
    if idx > max_prefix_right or idx + z[idx] - 1 > max_prefix_right:
        max_prefix_left = idx
        max_prefix_right = idx + z[idx] - 1


# 3. TO SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())
for query in range(query_count):
    idx = int(sys.stdin.readline())
    print(z[len(string) - idx])