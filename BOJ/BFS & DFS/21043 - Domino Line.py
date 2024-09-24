'''
BOJ 21043 - Domino Line (https://www.acmicpc.net/problem/21043)

There are N dominoes.
You can connect dominoes one by one with the touching ends having the same value.
Determine the minimum number of domino-lines.
'''

import sys
from collections import deque


# 2. A FUNCTION TO FIND THE NUMBER OF ODD-DEGREE VERTICES IN A CONNECTED COMPONENT - BFS-BASED

def odd_degree(num):
    
    result = 0
    
    queue = deque([num])
    visited[num] = 1
        
    while queue:
        now_num = queue.popleft()
        if degree[now_num] % 2 == 1:
            result += 1
        for next_num in graph[now_num]:
            if visited[next_num] == 0:
                visited[next_num] = 1
                queue.append(next_num)
    
    return result


# 1. TO GET THE INPUT

domino_count = int(sys.stdin.readline())

graph = {}
for num in range(50000):
    graph[num] = []

degree = [0 for domino in range(50001)]

for domino in range(domino_count):
    
    num1, num2 = map(int, sys.stdin.readline().split())
    num1 -= 1
    num2 -= 1
    
    graph[num1].append(num2)
    graph[num2].append(num1)
    degree[num1] += 1
    degree[num2] += 1


# 3. TO SOLVE THE PROBLEM
# If you consider a domino as an edge connecting two numbers, the problem is equivalent to dividing a graph into the fewest Eulerian paths.
# If a connected component has 2N odd-degree vertices, it can be divided into N Eulerian path.

ans = 0
visited = [0 for num in range(50000)]

for num in range(50000):
    if len(graph[num]) != 0 and visited[num] == 0:
        ans += max(odd_degree(num) // 2, 1)

print(ans)