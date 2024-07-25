'''
BOJ 11014 - Cheating 2 (https://www.acmicpc.net/problem/11014)

There is an N X M grid.
A student cannot sit in some cells.
A student cannot sit right next to another student or in front of another student diagonally.
Determine the maximum number of students who can sit. 
'''

import sys
sys.setrecursionlimit(10000)


# 3. A FUNCTION FOR BIPARTITE MATCHING

def bimatch(worker):
    
    if visited[worker]:
        return False
    visited[worker] = True
    
    result = False
    for work in graph[worker]:
        if worker_assigned[work] == -1 or bimatch(worker_assigned[work]):
            worker_assigned[work] = worker
            result = True
            break
    return result


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    row_count, col_count = map(int, sys.stdin.readline().split())
    available_seat = 0
    
    grid = []
    for row_num in range(row_count):
        row = list(sys.stdin.readline().strip())
        available_seat += row.count(".")
        grid.append(row)
    
    
    # 2. TO CONSTRUCT BIPARTITE GRAPH
    
    dy = [-1, 0, 1, -1, 0, 1]
    dx = [-1, -1, -1, 1, 1, 1]
    
    graph = {}
    
    for row_num in range(row_count):
        for col_num in range(col_count):
            
            worker_num = col_count * row_num + col_num
            graph[worker_num] = []
            
            if col_num % 2 == 1 and grid[row_num][col_num] == ".":
                for idx in range(6):
                    new_row_num = row_num + dy[idx]
                    new_col_num = col_num + dx[idx]
                    if 0 <= new_row_num < row_count and 0 <= new_col_num < col_count and grid[new_row_num][new_col_num] == ".":
                        work_num = col_count * new_row_num + new_col_num
                        graph[worker_num].append(work_num)


    # 4. TO SOLVE THE PROBLEM
    # According to Kőnig's theorem, the minimum vertex cover set and the maximum matching set have the same size.
    # The maximum independent set = The number of vertices - The minimum vertex cover set.
    
    worker_assigned = [-1 for work in range(row_count * col_count)]
    
    for worker in range(row_count * col_count):
        
        col_num = worker % col_count
        if col_num % 2 == 1:
            visited = [False for work in range(row_count * col_count)]
            bimatch(worker)
    
    match_count = 0
    for work in range(row_count * col_count):
        if worker_assigned[work] != -1:
            match_count += 1
    print(available_seat - match_count)