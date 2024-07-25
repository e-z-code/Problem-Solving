'''
BOJ 16894 - Divisor Game (https://www.acmicpc.net/problem/16894)

There are two players and an integer X.
In each turn, a player can replace X with Y, a divisor of X. Y cannot be 1 or X.
If a player cannot replace a number anymore, the player wins.
Given X, determine who will win the game. 
'''

import sys


# 1. THE SIEVE OF ERATOSTHENES

prime = [1 for num in range(10000000)]
prime[0], prime[1] = 0, 0

for num in range(2, 10001):
    if prime[num]:
        for multiple in range(2 * num, 10000000, num):
            prime[multiple] = 0


# 2. FACTORIZATION

num = int(sys.stdin.readline())
prime_divisor = []

num_copy = num
for divisor in range(10000000):
    if prime[divisor]:
        while num_copy % divisor == 0:
            prime_divisor.append(divisor)
            num_copy //= divisor

if num_copy != 1:
    prime_divisor.append(num_copy)


# 3. TO SOLVE THE PROBLEM

if len(prime_divisor) == 2:
    print("cubelover")
else:
    print("koosaga")