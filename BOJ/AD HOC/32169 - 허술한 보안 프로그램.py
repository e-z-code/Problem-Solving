'''
BOJ 32169 - Poor Security Program (https://www.acmicpc.net/problem/32169)

There is a hidden permutation X. 
You can enter a permutation at most twice.
If your permutation is Y, the result would be X | Y. 
Find the hidden permutation.
'''

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())


# 2. TO SEND QUERIES

arr = [0 for idx in range(length)]

# First query

first_query = [idx for idx in range(length)]
print("?", " ".join(map(str, first_query)))
sys.stdout.flush()

first_result = list(map(int, sys.stdin.readline().split()))
for idx in range(length):
    arr[idx] = idx ^ first_result[idx]

# Second query

second_query = [idx for idx in range(length)]
done = [0 for idx in range(length)]

idx = length-1
while idx >= 0:
    if not done[idx]:
        key = 0
        while key < idx:
            key = key * 2 + 1
        second_query[idx], second_query[key - idx] = second_query[key - idx], second_query[idx]
        done[idx] = 1
        done[key - idx] = 1
    idx -= 1
print("?", " ".join(map(str, second_query)))
sys.stdout.flush()

second_result = list(map(int, sys.stdin.readline().split()))
for idx in range(length):
    arr[idx] |= (second_query[idx] ^ second_result[idx])
print("!", " ".join(map(str, arr)))
sys.stdout.flush()