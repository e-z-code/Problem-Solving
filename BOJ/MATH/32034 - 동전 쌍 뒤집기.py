'''
BOJ 32034 - Flip Coin Pair (https://www.acmicpc.net/problem/32034)

There are N coins in a row.
You can flip two adjacent coins if they are on the same side.
Determine the minimum number of flips to make all coins head.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    coin_count = int(sys.stdin.readline())
    coins = list(sys.stdin.readline().strip())
    
    
    # 2. TO SOLVE THE PROBLEM
    
    ans = 0
    stack = []
    
    for coin in coins:
        if coin == "H":
            if len(stack) != 0:
                if stack[-1] == "H":
                    stack.pop()
                    ans += len(stack) + 1
                else:
                    stack.append("H")
        else:
            if len(stack) == 0:
                stack.append("T")
            else:
                if stack[-1] == "H":
                    stack.append("T")
                else:
                    stack.pop()
                    ans += len(stack) + 1
    
    if len(stack) != 0:
        print(-1)
    else:
        print(ans)