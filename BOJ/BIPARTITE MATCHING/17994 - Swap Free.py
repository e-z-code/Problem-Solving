'''
BOJ 17994 - Swap Free (https://www.acmicpc.net/problem/17994)

A set of words is swap-free if there is no way to turn any word in the set into any other word in the set by swapping a single pair of letters.
You are given N words that are all anagrams of each other.
Determine the size of the largest swap-free set.
'''

import sys
from collections import deque


# 4. BIPARTITE MATCHING

def bimatch(worker):
    
    if visited[worker]:
        return False
    visited[worker] = 1

    result = False
    for work in graph[worker]:
        if worker_assigned[work] == -1 or bimatch(worker_assigned[work]):
            worker_assigned[work] = worker
            result = True
            break
    
    return result


# 1. TO GET THE INPUT

word_count = int(sys.stdin.readline())
word_length = 0

words = []

for word_num in range(word_count):
    word = sys.stdin.readline().strip()
    word_length = len(word)
    words.append(word)


# 2. TO CONSTRUCT A GRAPH

graph = {}
for word_num in range(word_count):
    graph[word_num] = []


for i in range(word_count):
    for j in range(i+1, word_count):
        
        wordA = words[i]
        wordB = words[j]
        
        diff_count = 0
        for idx in range(word_length):
            if wordA[idx] != wordB[idx]:
                diff_count += 1
        
        if diff_count == 2:
            graph[i].append(j)
            graph[j].append(i)


# 3. TO DIVIDE A BIPARTITE GRAPH

is_worker = [0 for idx in range(word_count)]

visited = [-1 for worker in range(word_count)]

for idx in range(word_count):
    if visited[idx] == -1:
        
        queue = deque([idx])
        visited[idx] = 0
        is_worker[idx] = 1
        
        while queue:
            now = queue.popleft()
            for after in graph[now]:
                if visited[after] == -1:
                    visited[after] = visited[now] + 1
                    if visited[after] % 2 == 0:
                        is_worker[after] = 1


# 5. TO SOLVE THE PROBLEM
# According to Kőnig's theorem, the minimum vertex cover set and the maximum matching set have the same size.
# The maximum independent set = The number of vertices - The minimum vertex cover set.

worker_assigned = [-1 for work in range(word_count)]

for worker in range(word_count):
    if is_worker[worker] == 1:
        visited = [0 for worker in range(word_count)]
        bimatch(worker)

print(worker_assigned.count(-1))