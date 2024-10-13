'''
BOJ 7998 - Chocolate (https://www.acmicpc.net/problem/7998)

You can break chocolate along the vertical and horizontal lines.
The cost of a break is charged for every part you break.
Given the costs of breaking along vertical or horizontal lines, determine the minimal cost of breaking the whole chocolate into single squares.
'''


import sys


# 1. TO GET THE INPUT

x_count, y_count = map(int, sys.stdin.readline().split())

x_cost = []
for idx in range(x_count - 1):
    cost = int(sys.stdin.readline())
    x_cost.append(cost)
x_cost.sort()

y_cost = []
for idx in range(y_count - 1):
    cost = int(sys.stdin.readline())
    y_cost.append(cost)
y_cost.sort()


# 2. TO SOLVE THE PROBLEM
# The optimal solution is to choose the most expensive operation at every step.

x_used = 0
y_used = 0

ans = 0

while True:
    
    if len(x_cost) == 0:
        if len(y_cost) == 0:
            break
        else:
            ans += y_cost.pop() * (x_used + 1)
            y_used += 1
    else:
        if len(y_cost) == 0:
            ans += x_cost.pop() * (y_used + 1)
            x_used += 1
        else:
            if x_cost[-1] >= y_cost[-1]:
                ans += x_cost.pop() * (y_used + 1)
                x_used += 1
            else:
                ans += y_cost.pop() * (x_used + 1)
                y_used += 1

print(ans)