'''
ABC367E - Permute K Times (https://atcoder.jp/contests/abc367/tasks/abc367_e)

You are given two sequences of length N: X and A.
Print the result of performing the following operation K times on A: Replace A with B such that B[i] = A[X[i]].
'''

import sys


# 1. TO GET THE INPUT

arr_length, op_count = map(int, sys.stdin.readline().split())
key = list(map(int, sys.stdin.readline().split()))
for idx in range(arr_length):
    key[idx] -= 1
arr = list(map(int, sys.stdin.readline().split()))


# 2. SPARSE TABLE

max_exp = 70
sparse_table = [[-1 for idx in range(arr_length)] for exp in range(max_exp)]

for idx in range(arr_length):
    sparse_table[0][idx] = key[idx]
for exp in range(1, max_exp):
    for idx in range(arr_length):
        sparse_table[exp][idx] = sparse_table[exp-1][sparse_table[exp-1][idx]]


# 3. TO SOLVE THE PROBLEM

for idx in range(arr_length):
    now = idx
    dist = op_count
    for exp in range(max_exp-1, -1, -1):
        if dist >= (1 << exp):
            now = sparse_table[exp][now]
            dist -= (1 << exp)
    print(arr[now], end = ' ')