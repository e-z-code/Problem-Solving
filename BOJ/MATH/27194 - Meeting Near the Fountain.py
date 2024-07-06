'''
BOJ 27194 - Meeting Near the Fountain (https://www.acmicpc.net/problem/27194)

You meet your friend after T minutes at a park of distance N from the initial point.
You drive an electric scooter.
You drive M meters at x m/s and y m/s for the remaining distance.
How long would it take for you to arrive?
'''

import sys
from math import ceil


# 1. TO GET THE INPUT

dist_to_goal, time_left = map(int, sys.stdin.readline().split())
dist_to_park = int(sys.stdin.readline())
city_speed, park_speed = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

time = dist_to_park / (city_speed * 60) + (dist_to_goal - dist_to_park) / (park_speed * 60)
if time <= time_left:
    print(0)
else:
    print(ceil(time - time_left))