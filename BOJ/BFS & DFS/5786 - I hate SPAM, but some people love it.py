'''
BOJ 5786 - I hate SPAM, but some people love it (https://www.acmicpc.net/problem/5786)

Given a network and information of each spam mail, determine how many people each person forwarded the mail to.
'''

import sys
from collections import deque


# 1. TO CONSTRUCT A GRAPH

while True:
    
    people_count = list(sys.stdin.readline().strip().split())
    if len(people_count) == 2:
        break
    else:
        people_count = int(people_count[0])
        if people_count == 0:
            break
    
    graph = {}
    for person in range(1, people_count + 1):
        friend = list(map(int, sys.stdin.readline().split()))
        graph[person] = friend[:-1]
    
    
    # 2. TO SOLVE THE PROBLEM
    
    ans = ["" for idx in range(people_count + 1)]
    name = ["" for idx in range(people_count + 1)]
    
    while True:
        
        spam_input = list(sys.stdin.readline().strip().split())
        if len(spam_input) == 1 and spam_input[0] == "0":
            break
        
        start, low_t, high_t, low_key, mid_key, high_key = spam_input
        start, low_t, high_t = int(start), int(low_t), int(high_t)
        
        # BFS to check whether one received a mail
        
        visited = [0 for person in range(people_count + 1)]
        
        queue = deque([start])
        visited[start] = 1
        while queue:
            now = queue.popleft()
            for next in graph[now]:
                if visited[next] == 0:
                    queue.append(next)
                    visited[next] = 1
        
        for person in range(1, people_count+1):
            friend_count = len(graph[person])
            if visited[person] == 0 or friend_count < low_t:
                ans[person] += low_key + " "
            elif friend_count < high_t:
                ans[person] += mid_key + " "
            else:
                ans[person] += high_key + " "
    
    for person in range(1, people_count + 1):
        name[person] = sys.stdin.readline().strip()
        print("{}: {}".format(name[person], ans[person]))