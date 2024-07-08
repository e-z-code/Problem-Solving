'''
CF956D - Swap Dilemma (https://codeforces.com/contest/1983/problem/D)

There are two arrays: A and B.
You can choose some indexes L and R in A and swap A[L] and A[R].
Then you can choose some indexes L' and R' such that R - L = R' - L' and swap B[L'] and B[R'].
Determine if it is possible to make both arrays the same. 
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length = int(sys.stdin.readline())
    arrA = list(map(int, sys.stdin.readline().split()))
    arrB = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    # The parity of minimum necessary swap operation matters. (Proof TBA)
    
    if set(arrA) != set(arrB):
        
        print("No")
        
    else:
        
        loc = {}
        for idx in range(length):
            loc[arrA[idx]] = idx
        
        swap = 0
        for idx in range(length):
            now_num = arrA[idx]
            goal_num = arrB[idx]
            if now_num != goal_num:
                arrA[idx], arrA[loc[goal_num]] = arrA[loc[goal_num]], arrA[idx]
                loc[now_num], loc[goal_num] = loc[goal_num], loc[now_num]
                swap += 1
        
        if swap % 2 == 0:
            print("Yes")
        else:
            print("No")