'''
BOJ 6137 - Best Cow Line (https://www.acmicpc.net/problem/6137)

You can create a new string T from a string S by repeating the following rules.

(1) Delete the first character of S and add it to T.
(2) Delete the last character of S and add it to T.

Determine the first string in a lexicographical order. 
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())

line = deque([])
for idx in range(length):
    char = sys.stdin.readline().strip()
    line.append(char)


# 2. TO SOLVE THE PROBLEM

ans = []
count = 0

while len(line) != 0:
    
    string = "".join(line)
    reverse_string = string[::-1]
    
    if string <= reverse_string:
        ans.append(line.popleft())
    else:
        ans.append(line.pop())
    count += 1
    
    if count % 80 == 0:
        ans.append("\n")
    
print("".join(ans))