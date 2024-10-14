'''
BOJ 16163 - #15164_Report (https://www.acmicpc.net/problem/16163)

Given a string, print the number of palindrome substrings.
'''

import sys


# 1. TO GET THE INPUT

string = sys.stdin.readline().strip()
new_string = ["#"]
for idx in range(len(string)):
    new_string.append(string[idx])
    new_string.append("#")
string = "".join(new_string)


# 2. TO SOLVE THE PROBLEM - MANACHER

max_palindrome_end = 0
max_palindrome_center = 0

ans = 0
manacher = [0 for idx in range(len(string))]

for idx in range(len(string)):
    
    if idx > max_palindrome_end:
        manacher[idx] = 0
    else:
        manacher[idx] = min(manacher[2 * max_palindrome_center - idx], max_palindrome_end - idx)
    
    left = idx - manacher[idx] - 1
    right = idx + manacher[idx] + 1
    while 0 <= left and right < len(string) and string[left] == string[right]:
        manacher[idx] += 1
        left -= 1
        right += 1
    
    if max_palindrome_end < idx + manacher[idx]:
        max_palindrome_end = idx + manacher[idx]
        max_palindrome_center = idx

    if idx % 2 == 0:
        ans += (manacher[idx] + 1) // 2
    else:
        ans += manacher[idx] // 2 + 1

print(ans)