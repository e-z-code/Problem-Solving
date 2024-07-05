'''
BOJ 16520 - Kaleidoscopic Palindromes (https://www.acmicpc.net/problem/16520)

You are given A, B, and K.
Determine the number of X such that A <= X <= B and X is palindrome for all bases of J (2 <= J <= K).
'''

import sys


# 2. FUNCTIONS TO CONVERT BASE AND CHECK PALINDROME

def base_convert(num, base):
    
    result = []
    while num != 0:
        result.append(num % base)
        num //= base
    return result

def is_palindrome(arr):
    
    result = True
    for idx in range(len(arr) // 2):
        if arr[idx] != arr[-idx-1]:
            result = False
            break
    return result


# 1. TO GET THE INPUT

A, B, K = map(int, sys.stdin.readline().split())

ans = 0
for num in range(A, B+1):
    result = True
    for base in range(2, K+1):
        if not is_palindrome(base_convert(num, base)):
            result = False
            break
    if result:
        ans += 1
print(ans)