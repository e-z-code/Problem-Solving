'''
BOJ 1671 - Shark's Dinner (https://www.acmicpc.net/problem/1671)

If shark A has a bigger (or equal) size, a faster (or equal) speed, and better (or equal) intelligence than shark B, shark A can eat shark B.
A shark can eat at most two sharks.
If already eaten, a shark cannot eat another shark.
Determine the minimum number of sharks that can survive.
'''

import sys


# 3. BIPARTITE MATCHING

def bimatch(predator):
    
    if visited[predator]:
        return False
    visited[predator] = True
    
    result = False
    for prey in graph[predator]:
        
        if predator_assigned[prey] == -1 or bimatch(predator_assigned[prey]):
            result = True
            predator_assigned[prey] = predator
            break
    
    return result


# 1. TO GET THE INPUT

shark_count = int(sys.stdin.readline())

info_count = {}
for shark in range(shark_count):
    size, speed, intelligence = map(int, sys.stdin.readline().split())
    shark_info = (size, speed, intelligence)
    info_count[shark_info] = info_count.get(shark_info, 0) + 1

sharks = list(info_count.keys())
unique_shark_count = len(sharks)


# 2. TO CONSTRUCT BIPARTITE GRAPH
# When there are X same sharks, we only make one of them survive. 

graph = {}
now_key = 0

for i in range(unique_shark_count):
    
    edible_shark = []
    for j in range(unique_shark_count):
        if i != j and sharks[i][0] >= sharks[j][0] and sharks[i][1] >= sharks[j][1] and sharks[i][2] >= sharks[j][2]:
            edible_shark.append(j)

    for num in range(info_count[sharks[i]] + 1):
        graph[now_key] = edible_shark
        now_key += 1
        
predator_count = now_key


# 4. TO SOLVE THE PROBLEM

predator_assigned = [-1 for prey in range(unique_shark_count)]

for predator in range(predator_count):
    
    visited = [0 for predator in range(predator_count)]
    bimatch(predator)

print(predator_assigned.count(-1))