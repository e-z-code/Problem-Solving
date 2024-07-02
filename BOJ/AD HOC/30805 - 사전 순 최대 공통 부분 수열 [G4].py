'''
BOJ 30805 Lexicographical Common Subsequence - (https://www.acmicpc.net/problem/30805)

Given strings A and B, print a common subsequence that is lexicographically last.
'''

import sys


# 1. TO GET THE INPUT

length_arrA = int(sys.stdin.readline())
arrA = list(map(int, sys.stdin.readline().split()))

sorted_arrA = []
for idx in range(length_arrA):
    sorted_arrA.append((arrA[idx], idx))
sorted_arrA.sort(key = lambda x : (x[0], -x[1]))

length_arrB = int(sys.stdin.readline())
arrB = list(map(int, sys.stdin.readline().split()))

sorted_arrB = []
for idx in range(length_arrB):
    sorted_arrB.append((arrB[idx], idx))
sorted_arrB.sort(key = lambda x : (x[0], -x[1]))


# 2. TO SOLVE THE PROBLEM

ans = []

now_idx_arrA = -1
now_idx_arrB = -1

while len(sorted_arrA) != 0 and len(sorted_arrB) != 0:
    
    num_arrA, idx_arrA = sorted_arrA[-1]
    num_arrB, idx_arrB = sorted_arrB[-1]
    
    if num_arrA > num_arrB:
        sorted_arrA.pop()
    elif num_arrA < num_arrB:
        sorted_arrB.pop()
    else:
        if now_idx_arrA < idx_arrA and now_idx_arrB < idx_arrB:
            ans.append(num_arrA)
            now_idx_arrA = idx_arrA
            now_idx_arrB = idx_arrB
            sorted_arrA.pop()
            sorted_arrB.pop()
        else:
            if now_idx_arrA >= idx_arrA:
                sorted_arrA.pop()
            if now_idx_arrB >= idx_arrB:
                sorted_arrB.pop()

print(len(ans))
for num in ans:
    print(num, end = ' ')