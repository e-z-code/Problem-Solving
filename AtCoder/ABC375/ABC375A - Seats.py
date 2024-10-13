'''
ABC375A - Seats (https://atcoder.jp/contests/abc375/tasks/abc375_a)

There is a string A of length N consisting of '#' and '.'.
Find the number of integers i such that A[i] = '.', A[i-1] = '#', and A[i+1] = '#'.
'''

import sys


# 1. TO GET THE INPUT

seat_count = int(sys.stdin.readline())
seats = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM

ans = 0
for idx in range(1, seat_count - 1):
    if seats[idx] == "." and seats[idx-1] == "#" and seats[idx+1] == "#":
        ans += 1
print(ans)