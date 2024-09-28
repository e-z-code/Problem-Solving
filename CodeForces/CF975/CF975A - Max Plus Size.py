'''
CF975A - Max Plus Size (https://codeforces.com/contest/2019/problem/A)

There is an array A of length N.
You can color some elements red, but there cannot be two adjacent red elements.
Your score is the maximum value of a red element plus the number of red elements.
Find the maximum score you can get.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    size = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    
    best = max(arr)
    
    if size % 2 == 0:
        print(best + size // 2)
    else:
        
        even_idx = False
        
        for idx in range(size):
            if arr[idx] == best and idx % 2 == 0:
                even_idx = True
                break
        
        if even_idx:
            print(best + size // 2 + 1)
        else:
            print(best + size // 2)