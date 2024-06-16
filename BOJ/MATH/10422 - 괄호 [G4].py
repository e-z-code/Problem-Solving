'''
BOJ 10422 - Parentheses (https://www.acmicpc.net/problem/10422)

Print the number of parenthesis strings of length L.
'''

import sys


# 1. CALCULATE CATALAN NUMBERS
# Catalan Number C(N) = C(1)C(N-1) + C(2)C(N-2) + ... = 2nCn / n+1

catalan = [1, 1]

while len(catalan) <= 2500:
    
    val = 0
    for idx in range(len(catalan)):
        val += catalan[idx] * catalan[len(catalan) - idx - 1]
        val %= 10 ** 9 + 7
    catalan.append(val)


# 2. TO SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length = int(sys.stdin.readline())
    
    if length % 2 == 0:
        print(catalan[length // 2])
    else:
        print(0)