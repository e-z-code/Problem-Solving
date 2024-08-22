'''
BOJ 6875 - Professor (https://www.acmicpc.net/problem/6875)

Given a recursive crystal pattern, determine if a cell is blank or not.
'''

import sys


# 1. A FUNCTION TO SOLVE THE PROBLEM

def divide_conquer(start_x, end_x, start_y, end_y, target_x, target_y):

    size = end_x - start_x
    
    # Base
    if size == 5:
        if target_y == start_y:
            if start_x + 1 <= target_x < start_x + 4:
                return True
            else: 
                return False
        elif target_y == start_y + 1:
            if target_x == start_x + 2:
                return True
            else:
                return False
        else:
            return False
        
    # Recursion
    next_size = size // 5
    if start_y <= target_y < start_y + next_size:
        if start_x + next_size <= target_x < start_x + 4 * next_size:
            return True
        else:
            return False
    elif start_y + next_size <= target_y < start_y + 2 * next_size:
        if start_x + next_size <= target_x < start_x + 2 * next_size:
            return divide_conquer(start_x + next_size, start_x + 2 * next_size, start_y + next_size, start_y + 2 * next_size, target_x, target_y)
        elif start_x + 2 * next_size <= target_x < start_x + 3 * next_size:
            return True
        elif start_x + 3 * next_size <= target_x < start_x + 4 * next_size:
            return divide_conquer(start_x + 3 * next_size, start_x + 4 * next_size, start_y + next_size, start_y + 2 * next_size, target_x, target_y)
        else:
            return False
    elif start_y + 2 * next_size <= target_y < start_y + 3 * next_size:
        if start_x + 2 * next_size <= target_x < start_x + 3 * next_size:
            return divide_conquer(start_x + 2 * next_size, start_x + 3 * next_size, start_y + 2 * next_size, start_y + 3 * next_size, target_x, target_y)
        else:
            return False
    else:
        return False


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())

for query in range(query_count):
    
    level, x, y = map(int, sys.stdin.readline().split())
    if divide_conquer(0, pow(5, level), 0, pow(5, level), x, y):
        print("crystal")
    else:
        print("empty")