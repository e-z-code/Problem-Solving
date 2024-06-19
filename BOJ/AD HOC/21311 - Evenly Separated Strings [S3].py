'''
BOJ 21311 - Evenly Separated Strings (https://www.acmicpc.net/problem/21311)

A string is evenly separated iff there is an even number of characters between every pair of the same characters.
Determine whether a given string is evenly separated or not.
'''


import sys

# 1. TO GET THE INPUT

string = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM

ans = "YES"
lower_char = "abcdefghijklmnopqrstuvwxyz"

for char in lower_char:
    
    char_count = string.count(char)
    
    # A character can appear at most twice.
    if char_count > 2:
        ans = "NO"
        break
    
    elif char_count == 2:
        index_first, index_second = -1, -1
        for index in range(len(string)):
            if string[index] == char:
                if index_first == -1:
                    index_first = index
                else:
                    index_second = index
        if (index_second - index_first) % 2 == 0:
            ans = "NO"
            break

print(ans)