'''
BOJ 25376 - Strange Switch (https://www.acmicpc.net/problem/25376)

There are N lights. You can only turn on lights.
Some lights are connected. If you turn on a light, the status of the connected lights will change.
Determine the minimum number you need to turn on a light to turn on all lights.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

light_count = int(sys.stdin.readline())
start_state = int("".join(map(str, reversed(list(map(int, sys.stdin.readline().split()))))), 2)

graph = {}
for light in range(light_count):
    graph[light] = []
    connected_lights = list(map(int, sys.stdin.readline().split()))[1:]
    for connected_light in connected_lights:
        graph[light].append(connected_light - 1)


# 2. TO SOLVE THE PROBLEM

visited = [-1 for state in range(1 << light_count)]
visited[start_state] = 0

queue = deque([start_state])
while queue:
    now_state = queue.popleft()
    for light in range(light_count):
        if now_state & (1 << light):
            continue
        else:
            next_state = now_state | (1 << light)
            for connected_light in graph[light]:
                next_state ^= (1 << connected_light)
            if visited[next_state] == -1:
                visited[next_state] = visited[now_state] + 1
                queue.append(next_state)

print(visited[(1 << light_count) - 1])