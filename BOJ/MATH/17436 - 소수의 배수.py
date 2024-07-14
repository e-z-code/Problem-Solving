'''
BOJ 17436 - Multiple of Prime Numbers (https://www.acmicpc.net/problem/17436)

You are given N prime numbers and the natural number X.
Calculate the number of 1 <= Y <= X such that Y is divisible by at least one of N prime numbers.
'''

import sys
from itertools import combinations


# 1. TO GET THE INPUT

prime_count, X = map(int, sys.stdin.readline().split())
prime_nums = list(map(int, sys.stdin.readline().split()))


# 2. INCLUSION-EXCLUSION PRINCIPLE

ans = 0

# A product of 12 distinct prime numbers always exceeds 10 ^ 12.

for choice_count in range(1, min(12, prime_count + 1)):
    
    cases = list(combinations(prime_nums, choice_count))
    for case in cases:
        
        num = 1
        for prime_num in case:
            num *= prime_num

        if choice_count % 2 == 1:
            ans += X // num
        else:
            ans -= X // num

print(ans)