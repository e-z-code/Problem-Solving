import sys
from functools import cmp_to_key


# 1. COMPARE FUNCTION

def compare(x, y):
    if x + y >= y + x:
        return -1
    else:
        return 1


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

num_count = int(sys.stdin.readline())
arr = list(sys.stdin.readline().strip().split())

ans = sorted(arr, key = cmp_to_key(compare))
print(int("".join(ans)))