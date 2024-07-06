'''
BOJ 28702 - FizzBuzz (https://www.acmicpc.net/problem/28702)

Given consecutive 3 strings of FizzBuzz result, print the next string.
'''

import sys


# 1. TO GET THE INPUT

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
third = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM

string = ["Fizz", "Buzz", "FizzBuzz"]

# It is impossible for all 3 strings to be non-integer.
num = 0
if first not in string:
    num = int(first) + 3
else:
    if second not in string:
        num = int(second) + 2
    else:
        num = int(third) + 1

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)