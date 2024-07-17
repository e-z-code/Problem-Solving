'''
CF958B - Make Majority (https://codeforces.com/contest/1988/problem/B)

There is a binary array.
In each operation, you can select a sub-array and substitute it with the majority of the sub-array.

If the number of zero is equal to or greater than the number of zero, the majority is 0.
Otherwise, the majority is 1.

Determine if you can make the array to [1].
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    arr_length = int(sys.stdin.readline())
    arr = list(sys.stdin.readline().strip())
    
    
    # 2. TO SOLVE THE PROBLEM
    # We can minimize (zero_count - one_count) by compressing contiguous 0s.
    
    zero_count = 0
    one_count = 0
    
    stack = []
    for idx in range(arr_length):
        if arr[idx] == "0":
            if len(stack) == 0 or stack[-1] == 1:
                stack.append(0)
                zero_count += 1
        else:
            stack.append(1)
            one_count += 1
    
    if zero_count >= one_count:
        print("No")
    else:
        print("Yes")

