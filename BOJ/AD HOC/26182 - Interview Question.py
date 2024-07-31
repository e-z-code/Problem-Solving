'''
BOJ 26182 - Interview Question (https://www.acmicpc.net/problem/26182)

You played modified FizzBuzz.
In modified FizzBuzz, you replace a multiple of X by Fizz and replace a multiple of Y by Buzz.
Given a transcript of the game, print a possible pair (X, Y).
'''

import sys


# 1. TO GET THE INPUT

start, end = map(int, sys.stdin.readline().split())
game_result = list(sys.stdin.readline().strip().split())


# 2. TO SOLVE THE PROBLEM

fizz_buzz_count = game_result.count("FizzBuzz")
fizz_count = game_result.count("Fizz") + fizz_buzz_count
buzz_count = game_result.count("Buzz") + fizz_buzz_count

fizz_num = 0
buzz_num = 0

if fizz_count == 0:
    fizz_num = end+1
elif fizz_count == 1:
    for idx in range(len(game_result)):
        if game_result[idx] == "Fizz" or game_result[idx] == "FizzBuzz":
            fizz_num = start + idx
else:
    first_fizz = 0
    second_fizz = 0
    for idx in range(len(game_result)):
        if game_result[idx] == "Fizz" or game_result[idx] == "FizzBuzz":
            if first_fizz == 0:
                first_fizz = start + idx
            else:
                second_fizz = start + idx
                break
    fizz_num = second_fizz - first_fizz

if buzz_count == 0:
    buzz_num = end+1
elif buzz_count == 1:
    for idx in range(len(game_result)):
        if game_result[idx] == "Buzz" or game_result[idx] == "FizzBuzz":
            buzz_num = start + idx
else:
    first_buzz = 0
    second_buzz = 0
    for idx in range(len(game_result)):
        if game_result[idx] == "Buzz" or game_result[idx] == "FizzBuzz":
            if first_buzz == 0:
                first_buzz = start + idx
            else:
                second_buzz = start + idx
                break
    buzz_num = second_buzz - first_buzz
    
print(fizz_num, buzz_num)