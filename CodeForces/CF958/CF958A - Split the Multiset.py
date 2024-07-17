'''
CF958A - Split the Multiset (https://codeforces.com/contest/1988/problem/A)

There is an array.
In each operation, you can split a positive integer X to at most K numbers.
Determine the minimum number of operations to make the array consist of 1s.
'''

import sys


# 2. A FUNCTION FOR DIVISION WITH ITS QUOTIENT CEILED

def divide_ceil(x, y):
    if x % y == 0:
        return x // y
    else:
        return x // y + 1


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    num, divide_count = map(int, sys.stdin.readline().split())    
    print(divide_ceil(num - 1, divide_count - 1))