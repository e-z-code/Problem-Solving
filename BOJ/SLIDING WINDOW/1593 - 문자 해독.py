'''
BOJ 1593 - Deciphering the Mayan Writing (https://www.acmicpc.net/problem/1593)

There are two strings: X and Y.
Count every sequence of a permutation of X in Y.  
'''

import sys


# 1. TO GET THE INPUT

key_length, string_length = map(int, sys.stdin.readline().split())

key = sys.stdin.readline().strip()
string = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM - SLIDING WINDOW

key_count = [0 for idx in range(150)]
for char in key:
    key_count[ord(char)] += 1

ans = 0

string_count = [0 for idx in range(150)]
for idx in range(string_length):
    
    if idx >= key_length:
        string_count[ord(string[idx - key_length])] -= 1
    string_count[ord(string[idx])] += 1

    if key_count == string_count:
        ans += 1

print(ans)