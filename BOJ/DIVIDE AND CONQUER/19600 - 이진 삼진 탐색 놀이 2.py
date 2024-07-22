'''
BOJ 19600 - Binary and Ternary Search 2 (https://www.acmicpc.net/problem/19600)

Given an array A, X[i] = (The number of elements to access to find A[i] through ternary search) - (The number of elements to access to find A[i] through binary search).
Answer Q queries: Calculate X[a] + ... + X[b].
'''

import sys


# 2. FUNCTIONS FOR BINARY AND TERNARY SEARCH

def binary_search(length, count, left, right):

    mid = (left + right) // 2
    
    if binary_table[length][mid] == -1:
        binary_table[length][mid] = count
        
    if left <= mid-1:
        binary_search(length, count+1, left, mid-1)
    if mid+1 <= right:
        binary_search(length, count+1, mid+1, right)

def ternary_search(length, count, left, right):
    
    left_third = left + (right - left) // 3
    right_third = right - (right - left) // 3
    
    if ternary_table[length][left_third] == -1:
        ternary_table[length][left_third] = count
    if ternary_table[length][right_third] == -1:
        ternary_table[length][right_third] = count+1
    
    if left <= left_third-1:
        ternary_search(length, count+2, left, left_third-1)
    if left_third+1 <= right_third-1: 
        ternary_search(length, count+2, left_third+1, right_third-1)
    if right_third+1 <= right:
        ternary_search(length, count+2, right_third+1, right)


# 1. PRE-PROCESSING

binary_table = [[-1 for idx in range(length)] for length in range(5001)]
ternary_table = [[-1 for idx in range(length)] for length in range(5001)]

for length in range(1, 5001):

    binary_search(length, 0, 0, length-1)
    ternary_search(length, 0, 0, length-1)

    for idx in range(1, length):
        binary_table[length][idx] += binary_table[length][idx-1]
        ternary_table[length][idx] += ternary_table[length][idx-1]


# 3. TO ANSWER THE QUERIES

query_count = int(sys.stdin.readline())
for query in range(query_count):
    arr_length, start, end = map(int, sys.stdin.readline().split())
    if start == 0:
        print(ternary_table[arr_length][end] - binary_table[arr_length][end])
    else:
        print((ternary_table[arr_length][end] - ternary_table[arr_length][start-1]) - (binary_table[arr_length][end] - binary_table[arr_length][start-1]))