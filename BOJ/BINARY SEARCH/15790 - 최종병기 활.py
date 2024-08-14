'''
BOJ 15790 - War of the Arrows (https://www.acmicpc.net/problem/15790)

There is a rubber band of length N with M grooves.
You can only cut the band at the grooves.
You want to make K straight rubber strings, and the shortest one will determine the length of your arrow.
Determine the length of the longest arrow you can make.
'''

import sys


# 1. TO GET THE INPUT

circle_length, groove_count, required_rubber = map(int, sys.stdin.readline().split())

grooves = []
for idx in range(groove_count):
    groove = int(sys.stdin.readline())
    grooves.append(groove)


# 2. TO SOLVE THE PROBLEM

left = 1
right = circle_length // required_rubber + 1

while left + 1 < right:
    
    mid = (left + right) // 2
    possible = False
    
    for idx in range(groove_count):
        
        start = True
        now_idx = idx
        rubber_count = 0
        now_length = 0
        
        while now_idx != idx or start:
            
            start = False
            
            next_idx = (now_idx + 1) % groove_count
            new_length = grooves[next_idx] - grooves[now_idx]
            if new_length < 0:
                new_length += circle_length
            
            now_length += new_length
            if now_length >= mid:
                rubber_count += 1
                now_length = 0
            
            now_idx = next_idx

        if rubber_count >= required_rubber:
            possible = True
            break
    
    if possible:
        left = mid
    else:
        right = mid

print(left)