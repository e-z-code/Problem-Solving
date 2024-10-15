'''
BOJ 16229 - Repeated Pattern (https://www.acmicpc.net/problem/16229)

A string S contains a repeated pattern X if S can be created by concatenating X equal to or more than two times.
You can add at most K characters at the end of S.
Determine the maximum length of possible repeated pattern that creates S.
The maximum length should not exceed the initial length of S.
'''

import sys


# 1. TO GET THE INPUT

length, max_add = map(int, sys.stdin.readline().split())
string = sys.stdin.readline().strip()


# 2. Z ALGORITHM

max_prefix_left = 0
max_prefix_right = 0

z = [0 for idx in range(length)]
z[0] = length

for idx in range(1, length):
    
    if max_prefix_right < idx:
        z[idx] = 0
    else:
        z[idx] = min(z[idx - max_prefix_left], max_prefix_right - idx + 1)
    
    while idx + z[idx] < length and string[z[idx]] == string[idx + z[idx]]:
        z[idx] += 1
    
    if max_prefix_right < idx or max_prefix_right < idx + z[idx] - 1:
        max_prefix_left = idx
        max_prefix_right = idx + z[idx] - 1


# 3. TO SOLVE THE PROBLEM

if length <= max_add:
    print(length)
else:
    
    ans = 0
    for idx in range(1, length):
        
        # If idx + z[idx] < length, then the entire string must be a pattern.
        
        if idx + z[idx] == length:
            
            pattern_count = length // idx
            if length % idx != 0:
                pattern_count += 1
            needed_length = pattern_count * idx
            
            if needed_length - length <= max_add:
                ans = max(ans, idx)

    print(ans)