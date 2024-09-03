'''
BOJ 32160 - Number Game (https://www.acmicpc.net/problem/32160)

There are numbers 1 to N on a blackboard.
You choose two numbers, delete them, and write the difference between them until a number is left.
How can you maximize the number?
'''

import sys


# 1. TO GET THE INPUT

max_num = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM

'''
1 2 -> 1
1 2 3 -> 1 3 -> 2
1 2 3 4 -> 1 1 4 -> 0 4 -> 4
1 2 3 4 5 -> 1 1 5 -> 0 5 -> 5
1 2 3 4 5 6 -> 1 1 1 6 -> 0 1 6 -> 5
1 2 3 4 5 6 7 -> 1 1 1 7 -> 0 1 7 -> 6
1 2 3 4 5 6 7 8 -> 1 1 1 1 8 -> 0 0 8 -> 8
1 2 3 4 5 6 7 8 9 -> 1 1 1 1 9 -> 0 0 9 -> 9
'''

# Result
if max_num % 4 == 0 or max_num % 4 == 1:
    print(max_num)
else:
    print(max_num - 1)

# Make 1s 
if max_num % 2 == 1:
    for num in range(1, max_num, 2):
        print(num, num+1)
else:
    for num in range(2, max_num, 2):
        print(num, num+1)

# Make 0s 
one_count = max_num // 2
zero_count = one_count // 2
for make_zero in range(zero_count):
    print(1, 1)
one_count %= 2

# Finish
for zero_diff in range(zero_count - 1):
    print(0, 0)

if one_count:
    if zero_count:
        print(0, 1)
    print(1, max_num)
else:
    print(0, max_num)