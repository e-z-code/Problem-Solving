'''
BOJ 13275 - Longest Palindrome Substring (https://www.acmicpc.net/problem/13275)

Given a string, print the length of the longest palindrome substring.
'''

import sys


# 1. TO GET THE INPUT

string = sys.stdin.readline().strip()

new_string = "#"
for idx in range(len(string)):
    new_string += string[idx] + "#"
string = new_string


# 2. MANACHER
# manacher[idx] = The length of the longest palindrome pattern when idx is the center of the longest palindrome string

max_palindrome_end = 0
max_palindrome_center = 0

manacher = [0 for idx in range(len(string))]

for idx in range(len(string)):
    
    if idx <= max_palindrome_end:
        manacher[idx] = min(manacher[2 * max_palindrome_center - idx], max_palindrome_end - idx)
    else:
        manacher[idx] = 0
    
    while 0 <= idx - manacher[idx] - 1 and idx + manacher[idx] + 1 < len(string) and string[idx - manacher[idx] - 1] == string[idx + manacher[idx] + 1]:
        manacher[idx] += 1
    
    if max_palindrome_end < idx + manacher[idx]:
        max_palindrome_end = idx + manacher[idx]
        max_palindrome_center = idx


# 3. TO SOLVE THE PROBLEM

ans = 0
for idx in range(1, len(string)):
    key = manacher[idx]
    if manacher[idx] % 2 != idx % 2:
        key += 1
    ans = max(ans, key)
print(ans)