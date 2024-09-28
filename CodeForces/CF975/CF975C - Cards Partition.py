'''
CF975C - Cards Partition (https://codeforces.com/contest/2019/problem/C)

You have some integers, each between 1 and N.
You can buy at most K integers between 1 and N.
After buying the new integer, you must partition all your numbers according to the following rules.

(1) All groups must have the same size.
(2) There are no same integers in the same group.

Determine the maximum possible size of a group. 
'''

import sys


# 2. A FUNCTION FOR CEIL DIVISION

def ceil(x, y):
    if x % y == 0:
        return x // y
    else:
        return x // y + 1


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    num_count, coin_count = map(int, sys.stdin.readline().split())
    card_count = list(map(int, sys.stdin.readline().split()))
    
    
    # 3. TO SOLVE THE PROBLEM
    
    most_count = max(card_count)
    total_card = sum(card_count)

    for deque_size in range(num_count, 0, -1):
        
        target = most_count * deque_size
        if target < total_card:
            target += deque_size * ceil(total_card - target, deque_size)
        
        if target <= total_card + coin_count:
            print(deque_size)
            break