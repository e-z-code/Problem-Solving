'''
BOJ 15658 - Insert Operators 2 (https://www.acmicpc.net/problem/15658)

Given numbers and operators, insert operators and calculate the minimum and maximum possible result.
'''

import sys
from itertools import product
inf = float('inf')


# 2. FUNCTIONS FOR OPERATIONS

def calculate(op_num, x, y):
    if op_num == 0:
        return x + y
    elif op_num == 1:
        return x - y
    elif op_num == 2:
        return x * y
    else:
        if x * y < 0:
            return (-1) * (abs(x) // abs(y))
        else:
            return x // y


# 1. TO GET THE INPUT

num_count = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
op_count = list(map(int, sys.stdin.readline().split()))


# 3. TO SOLVE THE PROBLEM

operators = ["+", "-", "*", "/"]
operator_to_idx = {"+" : 0, "-" : 1, "*" : 2, "/" : 3}

largest = -inf
smallest = inf

for now_case in product(operators, repeat = num_count - 1):
    
    # See if operators are enough
    valid = True
    now_count = [0, 0, 0, 0]
    for op in now_case:
        now_count[operator_to_idx[op]] += 1
    for idx in range(4):
        if now_count[idx] > op_count[idx]:
            valid = False
    
    # Calculate
    if valid:
        now_result = nums[0]
        for idx in range(num_count - 1):
            now_result = calculate(operator_to_idx[now_case[idx]], now_result, nums[idx+1])
        largest = max(largest, now_result)
        smallest = min(smallest, now_result)

print(largest)
print(smallest)