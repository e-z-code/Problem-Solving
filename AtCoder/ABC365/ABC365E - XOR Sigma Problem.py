'''
ABC365E - XOR Sigma Problem (https://atcoder.jp/contests/abc365/tasks/abc365_e)

There is an array A.
Let's define F(X, Y) = A[X] + A[X+1] + ... + A[Y].
Then, G(X) = F(X, X+1) + F(X, X+2) + ... + F(X, N).
Calculate G(1) + G(2) + ... + G(N-1).
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

arr_length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

ans = 0

for exp in range(30):
    
    bit = 1 << exp

    # Construct a prefix XOR parity array.
    
    xor_parity = []
    for idx in range(arr_length):
        if idx == 0:
            if arr[idx] & bit:
                xor_parity.append(1)
            else:
                xor_parity.append(0)
        else:
            if arr[idx] & bit:
                xor_parity.append((xor_parity[-1] + 1) % 2)
            else:
                xor_parity.append(xor_parity[-1])
    
    # Calculate how many times each bit counts.
    
    zero_count = xor_parity.count(0)
    one_count = arr_length - zero_count
    
    xor_parity = deque(xor_parity)
    valid_parity = 1
    
    while len(xor_parity) != 0:
        
        num = xor_parity.popleft()
        
        if num == 1:
            one_count -= 1
        else:
            zero_count -= 1
        
        if valid_parity == 1:
            ans += bit * one_count
        else:
            ans += bit * zero_count
        
        if num == valid_parity:
            valid_parity = (valid_parity + 1) % 2

print(ans)