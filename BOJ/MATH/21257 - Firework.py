'''
BOJ 21257 - Firework (https://www.acmicpc.net/problem/21257)

You need N minutes to make a single firework and M minutes to light all the remaining fireworks you made.
Each firework has a probability of P to function.
Calculate the minimum expected time before at least a firework correctly functions.
'''

import sys
from fractions import Fraction
inf = float('inf')


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    time_to_make, time_to_test, success_rate = map(int, sys.stdin.readline().split())
    failure_rate = 1 - success_rate / 10000
    
    
    # 2. TO SOLVE THE PROBLEM
    # Expected value of geometric distribution equals 1 / p.
    
    ans = inf
    
    make_count = 1
    now_failure_rate = 1
    
    while True:
        expected_make_time = make_count * time_to_make + time_to_test
        now_failure_rate *= failure_rate
        expected_count = 1 / (1 - now_failure_rate)
        if expected_make_time * expected_count < ans:
            ans = expected_make_time * expected_count
            make_count += 1
        else:
            break

    print(float(ans))