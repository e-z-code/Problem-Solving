'''
BOJ 17043 - Wand (https://www.acmicpc.net/problem/17043)

There are N wizards. In the beginning, the wand belongs to the wizard 1.
If a wizard wins a dual and the wand belongs to the loser, the wizard can take the wand.
Given duels and winners of each duel, print who can end up with the wand.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

wizard_count, duel_count = map(int, sys.stdin.readline().split())

graph = {}
for wizard in range(1, wizard_count+1):
    graph[wizard] = []
for duel in range(duel_count):
    winner, loser = map(int, sys.stdin.readline().split())
    graph[loser].append(winner)


# 2. BFS
# Since the wizard 1 loses the wand at least once, we do not always initialize visited[1].  

visited = [0 for wizard in range(wizard_count+1)]
queue = deque([1])
if len(graph[1]) == 0:
    visited[1] = 1

while queue:
    
    now = queue.popleft()
    for next in graph[now]:
        if visited[next] == 0:
            visited[next] = 1
            queue.append(next)
    
print("".join(list(map(str, visited))[1:]))