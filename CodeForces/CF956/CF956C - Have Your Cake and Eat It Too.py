'''
CF956C - Have Your Cake and Eat It Too (https://codeforces.com/contest/1983/problem/C)

There are three arrays: A, B, and C. Their sums are equal.
Determine if it is possible to have a contiguous slice for each array that satisfies the following conditions.

(1) No index is assigned to more than one array.
(2) The sum of all sub-arrays >= ceil(sum(A) // 3)
'''

import sys


# 1. FUNCTIONS FOR PREFIX-SUM

def prefix_sum(arr):
    
    for idx in range(1, len(arr)):
        arr[idx] += arr[idx-1]
    return arr


# 3. FUNCTIONS TO SOLVE THE PROBLEM

def ceil_divided_by_three(num):
    
    if num % 3 == 0:
        return num // 3
    else:
        return num // 3 + 1

def solve(arrX, arrY, arrZ):
    
    left = length
    for idx in range(length):
        if arrX[idx] >= ceil_divided_by_three(total):
            left = idx
            break
    
    right = 0
    for idx in range(length-1, -1, -1):
        if arrZ[-1] - arrZ[idx] >= ceil_divided_by_three(total):
            right = idx + 1
            break
    
    if left + 1 < right and arrY[right - 1] - arrY[left] >= ceil_divided_by_three(total):
        return left, right
    else:
        return False


# 2. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length = int(sys.stdin.readline())
    total = 0
    
    arrA = list(map(int, sys.stdin.readline().split()))
    total = sum(arrA)
    arrA = prefix_sum(arrA)
    arrB = prefix_sum(list(map(int, sys.stdin.readline().split())))
    arrC = prefix_sum(list(map(int, sys.stdin.readline().split())))
    
    
    # 4. TO SOLVE THE PROBLEM
    
    if solve(arrA, arrB, arrC):
        left, right = solve(arrA, arrB, arrC)
        print(1, left+1, left+2, right, right+1, length)
    elif solve(arrA, arrC, arrB):
        left, right = solve(arrA, arrC, arrB)
        print(1, left+1, right+1, length, left+2, right)
    elif solve(arrB, arrA, arrC):
        left, right = solve(arrB, arrA, arrC)
        print(left+2, right, 1, left+1, right+1, length)
    elif solve(arrB, arrC, arrA):
        left, right = solve(arrB, arrC, arrA)
        print(right+1, length, 1, left+1, left+2, right)
    elif solve(arrC, arrA, arrB):
        left, right = solve(arrC, arrA, arrB)
        print(left+2, right, right+1, length, 1, left+1)
    elif solve(arrC, arrB, arrA):
        left, right = solve(arrC, arrB, arrA)
        print(right+1, length, left+2, right, 1, left+1)
    else:
        print(-1)