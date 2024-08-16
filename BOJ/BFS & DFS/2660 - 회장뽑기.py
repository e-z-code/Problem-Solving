'''
BOJ 2660 - Choose the President (https://www.acmicpc.net/problem/2660)

Your organization needs to choose a new president.
A member gets a point according to his distance from the farthest member in a friendship network.
Given a friendship network, determine who will get the lowest point.
'''

import sys
from collections import deque
inf = float('inf')


# 2. BFS FUNCTION

def bfs(member):
    
    visited = [inf for member in range(member_count)]
    visited[member] = 0
    
    queue = deque([member])
    while queue:
        now_member = queue.popleft()
        for next_member in graph[now_member]:
            if visited[next_member] == inf:
                visited[next_member] = visited[now_member] + 1
                queue.append(next_member)
    
    return max(visited)


# 1. TO GET THE INPUT

member_count = int(sys.stdin.readline())

graph = {}
for member in range(member_count):
    graph[member] = []

while True:
    memberA, memberB = map(int, sys.stdin.readline().split())
    if memberA == -1 and memberB == -1:
        break
    memberA -= 1
    memberB -= 1
    graph[memberA].append(memberB)
    graph[memberB].append(memberA)


# 3. TO SOLVE THE PROBLEM

best_point = inf
best_list = []

for member in range(member_count):
    point = bfs(member)
    if point < best_point:
        best_point = point
        best_list = [member + 1]
    elif point == best_point:
        best_list.append(member + 1)

print(best_point, len(best_list))
print(" ".join(map(str, best_list)))