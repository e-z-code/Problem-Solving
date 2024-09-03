'''
BOJ 32166 - Drive Test (https://www.acmicpc.net/problem/32166)

There is a triangle road and two cars, A and B.
A and B start from a point and drive in the same direction.
Calculate how long it takes for each car to do a lap.
'''

import sys


# 1. TO GET THE INPUT

points = []
speeds = []
for point in range(3):
    x, y, speed = map(int, sys.stdin.readline().split())
    points.append((x, y))
    speeds.append(speed)

# Distance from point X to point X + 1.
dist = []
for idx in range(3):
    now_x, now_y = points[idx]
    next_x, next_y = points[(idx + 1) % 3]
    dist.append((pow(now_x - next_x, 2) + pow(now_y - next_y, 2)) ** 0.5)

width = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

no_point, slow_point, fast_point = 0, 0, 0
for idx in range(3):
    if speeds[idx] == 0:
        no_point = idx
    elif speeds[idx] == max(speeds):
        fast_point = idx
    else:
        slow_point = idx

slow_time = [0, 0, 0]
now_point = slow_point
for move in range(3):
    next_point = (now_point + 1) % 3
    slow_time[next_point] = slow_time[now_point] + dist[now_point] / speeds[slow_point]
    now_point = next_point

fast_time = [0, 0, 0]
now_point = fast_point
for move in range(3):
    next_point = (now_point + 1) % 3
    fast_time[next_point] = fast_time[now_point] + dist[now_point] / speeds[fast_point]
    now_point = next_point

added_time = 0
now_point = slow_point
while now_point != fast_point:
    next_point = (now_point + 1) % 3
    if slow_time[next_point] > fast_time[next_point]:
        if width[now_point] == 1:
            added_time += (slow_time[next_point] - fast_time[next_point])
        break
    now_point = next_point

for idx in range(3):
    if idx == no_point:
        print("-")
    elif idx == slow_point:
        print(max(slow_time))
    else:
        print(max(fast_time) + added_time)