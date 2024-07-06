'''
BOJ 17176 - Decipher (https://www.acmicpc.net/problem/17176)

You can create a code from plaintext by the following rules.

(1) 0 substitutes a blank.
(2) A number from 1 to 26 substitutes an uppercase alphabet.
(3) A number from 27 to 52 substitutes a lowercase alphabet.
(4) Randomize a code.

Given a code and a plaintext, check whether the code is valid.
'''

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())

code = list(map(int, sys.stdin.readline().split()))
text = sys.stdin.readline().strip()


# 2. TO CHECK THE VALIDITY

key = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

code_before_randomized = []
for index in range(length):
    code_before_randomized.append(key.index(text[index]))

code.sort()
code_before_randomized.sort()

if code == code_before_randomized:
    print('y')
else:
    print('n')