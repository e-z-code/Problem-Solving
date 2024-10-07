'''
BOJ 5035 - Rain Fall (https://www.acmicpc.net/problem/5035)

You use a tube to measure rainfall.
However, the tube has a hole at height L.
If the water level is above the hole, the water drains at a rate of K.
Given the height of the water in the tube, determine the maximum and minimum rainfall.
'''

import sys


# 1. TO GET THE INPUT

leak_height, leak_rate, rain_duration, observe_time, observe_height = map(float, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

if observe_height < leak_height:

    max_rainfall = observe_height
    min_rainfall = observe_height

else:
    
    A = rain_duration
    B = (rain_duration + observe_time) * leak_rate + observe_height
    C = leak_height * leak_rate
    
    rain_rate = (B + (B * B - 4 * A * C) ** 0.5) / (2 * A) 
    max_rainfall = rain_rate * rain_duration
    
    if observe_height == leak_height:
        min_rainfall = observe_height
    else:
        min_rainfall = max_rainfall
    
print(min_rainfall, max_rainfall)