'''
BOJ 10023 - Mooo Moo (https://www.acmicpc.net/problem/10023)

There are N fields along a long, straight road. There is a microphone in each field.
If the volume of mooing in some field is X, it will contribute X-1 to the subsequent field, and so on.
You own cows of B different breeds, and each breed has a volume of mooing.
Given the volume of mooing in each field, determine the minimum possible number of cows.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

field_count, breed_count = map(int, sys.stdin.readline().split())

breed_volume = []
for breed in range(breed_count):
    volume = int(sys.stdin.readline())
    breed_volume.append(volume)

field_volume = []
for field in range(field_count):
    volume = int(sys.stdin.readline())
    field_volume.append(volume)


# 2. DYNAMIC PROGRAMMING USING DP

queue = deque([])
visited = [0 for volume in range(100001)]

for volume in breed_volume:
    queue.append(volume)
    visited[volume] = 1

while queue:
    now_volume = queue.popleft()
    for volume in breed_volume:
        next_volume = now_volume + volume
        if next_volume <= 100000 and visited[next_volume] == 0:
            visited[next_volume] = visited[now_volume] + 1
            queue.append(next_volume)


# 3. TO SOLVE THE PROBLEM

ans = 0

for idx in range(field_count):
    
    if idx == 0:
        new_volume = field_volume[idx]
    else:
        new_volume = field_volume[idx] - max(0, field_volume[idx-1] - 1)
        
    if new_volume < 0:
        ans = -1
        break
    if new_volume != 0 and visited[new_volume] == 0:
        ans = -1
        break
    ans += visited[new_volume]

print(ans)