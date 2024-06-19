'''
BOJ 27918 - Table Tennis (https://www.acmicpc.net/problem/27918)

Given the result of N rounds, print the match result.
If a player leads by 2, the game immediately ends and the subsequent rounds do not count. 
'''


import sys

# 1. TO SOLVE THE PROBLEM

round_count = int(sys.stdin.readline())

pointA = 0
pointB = 0
for round in range(round_count):
    winner = sys.stdin.readline().strip()
    if winner == 'D':
        pointA += 1
    else:
        pointB += 1
    if abs(pointA - pointB) == 2:
        break

print("{}:{}".format(pointA, pointB))