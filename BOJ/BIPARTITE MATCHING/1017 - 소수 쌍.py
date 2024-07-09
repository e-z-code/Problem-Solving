'''
BOJ 1017 - Prime Number Pair (https://www.acmicpc.net/problem/1017)

You want to make pairs from an array such that the sum of each pair is a prime number.
Given that you succeeded in matching all elements, determine which element you matched with the first element.
'''

import sys


# 3. BIPARTITE MATCHING

def bimatch(worker):
    
    if visited[worker]:
        return False
    visited[worker] = True
    
    result = False
    for work in graph[worker]:
        if worker_assigned[work] == -1 or (worker_assigned[work] != 0 and bimatch(worker_assigned[work])):
            result = True
            worker_assigned[work] = worker
            break
    return result

    
# 1. THE SIEVE OF ERATOSTHENES 

prime = [1 for num in range(2001)]
prime[0], prime[1] = 0, 0

for num in range(2, 45):
    if prime[num]:
        for multiple in range(num * 2, 2001, num):
            prime[multiple] = 0
    num += 1


# 2. TO GET THE INPUT AND CONSTRUCT BIPARTITE GRAPH

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

graph = {}
for i in range(length):
    graph[i] = []
    for j in range(length):
        if i != j and prime[arr[i] + arr[j]]:
            graph[i].append(j)
        

# 4. TO SOLVE THE PROBLEM

ans = []

for work in graph[0]:
    
    worker_assigned = [-1 for idx in range(length)]
    worker_assigned[work] = 0
    
    for worker in range(1, length):
        
        visited = [False for worker in range(length)]
        bimatch(worker)
    
    if -1 not in worker_assigned:
        ans.append(arr[work])

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    print(" ".join(list(map(str, ans))))