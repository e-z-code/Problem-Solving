'''
BOJ 12284 - Spaceship Defense (Small) (https://www.acmicpc.net/problem/12284)

You are given a directed graph and the colors of each vertex.
If two vertices have the same color, you can immediately move from one to another in 0 seconds with a teleport machine.
Answer Q queries: Calculate the minimum time required to move from vertex A to B.
'''

import sys, heapq
inf = float('inf')


# 2. DIJKSTRA FUNCTION

def dijkstra(start):
    
    min_dist = [inf for room in range(room_count)]
    min_dist[start] = 0
    
    heap = [(0, start)]
    while heap:
        now_dist, now_room = heapq.heappop(heap)
        if now_dist <= min_dist[now_room]:
            for next_room, dist in graph[now_room]:
                next_dist = now_dist + dist
                if next_dist < min_dist[next_room]:
                    min_dist[next_room] = next_dist
                    heapq.heappush(heap, (next_dist, next_room))
    
    return min_dist


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test_num in range(1, test_count + 1):
    
    room_count = int(sys.stdin.readline())
    
    room_color = []
    for room in range(room_count):
        color = sys.stdin.readline().strip()
        room_color.append(color)
    
    graph = {}
    for room in range(room_count):
        graph[room] = []
    
    edge_count = int(sys.stdin.readline())
    for edge in range(edge_count):
        start, end, dist = map(int, sys.stdin.readline().split())
        graph[start-1].append((end-1, dist))
    for roomA in range(room_count):
        for roomB in range(roomA+1, room_count):
            if room_color[roomA] == room_color[roomB]:
                graph[roomA].append((roomB, 0))
                graph[roomB].append((roomA, 0))
    
    
    # 3. TO SOLVE THE PROBLEM
    
    ans = []
    for room in range(room_count):
        min_dist = dijkstra(room)
        ans.append(min_dist)
    
    query_count = int(sys.stdin.readline())
    print("Case #{}:".format(test_num))
    for query in range(query_count):
        start, end = map(int, sys.stdin.readline().split())
        if ans[start-1][end-1] == inf:
            print(-1)
        else:
            print(ans[start-1][end-1])