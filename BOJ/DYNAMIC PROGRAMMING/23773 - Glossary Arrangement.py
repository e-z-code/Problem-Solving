'''
BOJ 23773 - Glossary Arrangement (https://www.acmicpc.net/problem/23773)

Given a list of filenames, determine an optimal column layout that minimizes the number of lines.
'''

import sys


# 1. TO GET THE INPUT

word_count, width = map(int, sys.stdin.readline().split())

words = []
for idx in range(word_count):
    word = sys.stdin.readline().strip()
    words.append(word)


# 2. TO GET THE MINIMUM ROW : BINARY SEARCH + DP

left = 0
right = word_count

ans_prev = [-1 for idx in range(word_count)]

while left + 1 < right:
    
    mid = (left + right) // 2
    
    # dp[i + j] = The minimum width when i is the last word of the column and j is the number of words for the next column
    
    dp = [float('inf') for idx in range(word_count)]
    prev = [-1 for idx in range(word_count)]
    
    max_length = 0
    for idx in range(mid):
        max_length = max(max_length, len(words[idx]))
        dp[idx] = max_length
    
    for i in range(word_count):
        
        max_length = 0
        for j in range(1, mid + 1):
            if i + j < word_count:
                max_length = max(max_length, len(words[i + j]))
                if dp[i + j] >= dp[i] + max_length + 1:
                    dp[i + j] = min(dp[i + j], dp[i] + max_length + 1)
                    prev[i + j] = i
    
    if dp[-1] <= width:
        right = mid
        ans_prev = prev
    else:
        left = mid


# 3. TO SOLVE THE PROBLEM (TRACKING)

row_count = right

col_count = 1
idx = word_count - 1
while ans_prev[idx] != -1:
    col_count += 1
    idx = ans_prev[idx]

length = [0 for col in range(col_count)]
ans = [["" for col in range(col_count)] for row in range(row_count)]

col = col_count - 1
idx = word_count - 1

while col >= 0:
    
    max_length = 0

    row = idx - ans_prev[idx] - 1
    
    while row >= 0:
        word = words.pop()
        ans[row][col] = word
        max_length = max(max_length, len(word))
        row -= 1

    length[col] = max_length
    col -= 1
    idx = ans_prev[idx]
    if idx == -1:
        break

for row in range(row_count):
    for col in range(col_count):
        if len(ans[row][col]) < length[col]:
            ans[row][col] += " " * (length[col] - len(ans[row][col]))

print(row_count, col_count)
print(" ".join(list(map(str, length))))
for row in ans:
    print(" ".join(row))