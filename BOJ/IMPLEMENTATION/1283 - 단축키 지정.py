'''
BOJ 1283 - Shortcut Keys (https://www.acmicpc.net/problem/1283)

There are N options in your program.
You choose a shortcut alphabet for each option as follows:

(1) From left to right, see the first letter of each word. If the letter is not chosen, it is the shortcut alphabet.
(2) From left to right, see every letter. If the letter is not chosen, it is the shortcut alphabet.

For each option, mark the shortcut alphabet for the option.
'''

import sys


# 1. TO GET THE INPUT

option_count = int(sys.stdin.readline())
used = [0 for alphabet in range(26)]

for option_num in range(option_count):
    
    option = list(sys.stdin.readline().strip().split())
    
    
    # 2. TO SOLVE THE PROBLEM
    
    done = False
    for idx in range(len(option)):
        word = option[idx]
        alphabet = ord(word[0].upper()) - 65
        if not used[alphabet]:
            done = True
            used[alphabet] = 1
            option[idx] = "[" + word[0] + "]" + word[1:]
            break
    
    for idx in range(len(option)):
        if not done:
            word = option[idx]
            for j in range(len(word)):
                alphabet = ord(word[j].upper()) - 65
                if not used[alphabet]:
                    done = True
                    used[alphabet] = 1
                    option[idx] = word[:j] + "[" + word[j] + "]" + word[j+1:]
                    break
    
    print(" ".join(option))