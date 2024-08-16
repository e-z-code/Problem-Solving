'''
BOJ 2320 - Word Relay (https://www.acmicpc.net/problem/2320)

You participate in a word relay competition.
Your point is the sum of the length of words you used.
Given N words, determine the maximum point you can get.
'''

import sys


# 1. TO GET THE INPUT

word_count = int(sys.stdin.readline())
words = []
for word_input in range(word_count):
    word = sys.stdin.readline().strip()
    words.append((word[0], word[-1], len(word)))


# 2. DYNAMIC PROGRAMMING
# DP[i][j] = Maximum point when the status is i and the last word is j.

dp = [[0 for last_word in range(word_count)] for state in range(1 << word_count)]

for state in range(1 << word_count):
    for last_word in range(word_count):

        if state & (1 << last_word):
            before_state = state ^ (1 << last_word)
            if before_state == 0:
                dp[state][last_word] = words[last_word][2]
            else:
                for before_last_word in range(word_count):
                    if before_state & (1 << before_last_word) and words[before_last_word][1] == words[last_word][0]:
                        dp[state][last_word] = max(dp[state][last_word], dp[before_state][before_last_word] + words[last_word][2])


# 3. TO SOLVE THE PROBLEM

ans = 0
for row in dp:
    ans = max(ans, max(row))
print(ans)