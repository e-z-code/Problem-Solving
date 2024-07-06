'''
BOJ 7881 - YAPTCHA (https://www.acmicpc.net/problem/7881)

f(n) = floor(((3k + 6)! + 1) / (3k + 7) - floor((3k + 6)! / (3k + 7)))
Given n, print f(1) + f(2) + ... + f(n)
'''

import sys


# 1. SIEVE OF ERATOSTHENES

prime = [1 for num in range(4000001)]
prime[0], prime[1] = 0, 0

now = 2
while now <= int(4000000 ** (0.5) + 1):
    if prime[now]:
        for multiple in range(now * 2, 4000001, now):
            prime[multiple] = 0
    now += 1


# 2. PREFIX SUM
# f(n) = 1 <=> (3k+6)! % (3k+7) = 3k+6. Otherwise, f(n) = 0.
# By Wilson's theorem, (n-1)! % n = n-1 <=> n is a prime.

ans = [0]
for num in range(1, 1000001):
    if prime[3 * num + 7]:
        ans.append(ans[-1] + 1)
    else:
        ans.append(ans[-1])


# 3. TO GET THE INPUT AND SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())
for query in range(query_count):
    num = int(sys.stdin.readline())
    print(ans[num])