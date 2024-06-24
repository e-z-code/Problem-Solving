'''
BOJ 4343 - Arctic Network (https://www.acmicpc.net/problem/4343)

There are N outposts.
If both outposts have a satellite channel, the outposts can be connected without edge.
Determine the length of the longest edge when there are S satellite channels. 
'''

import sys


# 2. FUNCTIONS TO GET THE DISTANCE BETWEEN TWO POINTS

def dist_squared(p1, p2):
    
    x1, y1 = p1
    x2, y2 = p2

    return pow(x1-x2, 2) + pow(y1-y2, 2)


# 3. UNION-FIND 

def find(vertex):
    
    if vertex != parent[vertex]:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(vertex1, vertex2):
    
    parent1 = find(vertex1)
    parent2 = find(vertex2)
    
    if parent1 <= parent2:
        parent[parent1] = parent2
    else:
        parent[parent2] = parent1


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    channel_count, outpost_count = map(int, sys.stdin.readline().split())

    outposts = []
    for outpost in range(outpost_count):
        x, y = map(int, sys.stdin.readline().split())
        outposts.append((x, y))

    edges = []
    for i in range(outpost_count):
        for j in range(i+1, outpost_count):
            edges.append((dist_squared(outposts[i], outposts[j]), i, j))
    edges.sort()
    

    # 4. KRUSKAL
    
    mst = []
    parent = [num for num in range(outpost_count)]
    
    for dist, i, j in edges:
        if find(i) != find(j):
            mst.append((dist, i, j))
            union(i, j)

    mst.sort(reverse=True)


    # 5. TO SOLVE THE PROBLEM
    
    ans = 0
    if channel_count < outpost_count:
        ans = mst[channel_count-1][0] ** (0.5)
    print(format(ans, ".2f"))