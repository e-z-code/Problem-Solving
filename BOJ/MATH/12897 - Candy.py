'''
BOJ 12897 - Candy (https://www.acmicpc.net/problem/12897)

Let's define f(K) = combinations(N, K) * pow(2, K).
Calculate f(1) + f(2) + ... + f(N).
'''

import sys
mod = 10 ** 9 + 7


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM
# According to the binomial theorem, f(0) + f(1) + ... + f(N) = 3 ^ N.

N = int(sys.stdin.readline())

ans = pow(3, N, mod)
if ans == 0:
    ans = mod - 1
else:
    ans -= 1
print(ans)