'''
BOJ 5545 - Best Pizza (https://www.acmicpc.net/problem/5545)

You make a pizza by putting some toppings on the dough.
Given the cost and calorie of each topping, calculate the highest calorie per cost unit possible.
'''

import sys


# 1. TO GET THE INPUT

topping_count = int(sys.stdin.readline())
dough_cost, topping_cost = map(int, sys.stdin.readline().split())
dough_cal = int(sys.stdin.readline())
toppings_cal = []
for topping in range(topping_count):
    topping_cal = int(sys.stdin.readline())
    toppings_cal.append(topping_cal)
toppings_cal.sort()


# 2. TO SOLVE THE PROBLEM

best_cal = dough_cal
best_cost = dough_cost

while toppings_cal:
    
    topping_cal = toppings_cal.pop()
    
    if best_cal / best_cost < (best_cal + topping_cal) / (best_cost + topping_cost):
        best_cal += topping_cal
        best_cost += topping_cost
    else:
        break

print(best_cal // best_cost)