'''
BOJ 10330 - Bit String Rearrangement (https://www.acmicpc.net/problem/10330)

There is a bit string S. You can swap adjacent two bits.
Given a string pattern, determine the minimum number of swaps to make a bit string that satisfies the pattern. 
'''

import sys
from collections import deque
inf = float('inf')


# 1. TO GET THE INPUT

bit_count, pattern_length = map(int, sys.stdin.readline().split())
start = int("".join(list(sys.stdin.readline().strip().split())), 2)

pattern = list(map(int, sys.stdin.readline().split()))

goal_zero = ""
goal_one = ""
for idx in range(pattern_length):
    if idx % 2 == 0:
        for repeat in range(pattern[idx]):
            goal_zero += "0"
            goal_one += "1"
    else:
        for repeat in range(pattern[idx]):
            goal_zero += "1"
            goal_one += "0"

goal_zero = int(goal_zero, 2)
goal_one = int(goal_one, 2)


# 2. BFS

visited = [inf for num in range(1 << bit_count)]
visited[start] = 0

queue = deque([start])
while queue:
    now_num = queue.popleft()
    for bit in range(bit_count - 1):
        
        # Swap Operation
        now_bit = now_num & (1 << bit)
        swap_bit = now_num & (1 << (bit + 1))
        next_num = now_num & ~(3 << bit) | (swap_bit >> 1) | (now_bit << 1)
        
        if visited[next_num] == inf:
            queue.append(next_num)
            visited[next_num] = visited[now_num] + 1

print(min(visited[goal_zero], visited[goal_one]))