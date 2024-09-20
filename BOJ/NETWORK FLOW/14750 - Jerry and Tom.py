import sys
from collections import deque


# 2. FUNCTIONS TO SEE IF A MOUSE CAN ENTER A HOLE

def ccw(p1, p2, p3):

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    result = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    if result > 0:
        return 1
    elif result == 0:
        return 0
    else:
        return -1

def point_on_seg(seg_p1, seg_p2, hole):

    x1, y1 = seg_p1
    x2, y2 = seg_p2
    x_hole, y_hole = hole

    result = False
    if ccw(seg_p1, seg_p2, hole) == 0 and min(x1, x2) <= x_hole <= max(x1, x2) and min(y1, y2) <= y_hole <= max(y1, y2):
        result = True
    return result

def intersect(seg_p1, seg_p2, hole, mouse):

    ccw1 = ccw(seg_p1, seg_p2, hole) * ccw(seg_p1, seg_p2, mouse)
    ccw2 = ccw(hole, mouse, seg_p1) * ccw(hole, mouse, seg_p2)

    if ccw1 < 0 and ccw2 < 0:
        return True
    else:
        return False

def valid(seg_p1, seg_p2, hole, mouse):
    
    if point_on_seg(seg_p1, seg_p2, hole):
        return True
    else:
        if point_on_seg(hole, mouse, seg_p1) or point_on_seg(hole, mouse, seg_p2):
            return False
        elif intersect(seg_p1, seg_p2, hole, mouse):
            return False
        else:
            return True


# 1. TO GET THE INPUT

point_count, max_capacity, hole_count, mice_count = map(int, sys.stdin.readline().split())

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

holes = []
for hole in range(hole_count):
    x, y = map(int, sys.stdin.readline().split())
    holes.append((x, y))

mice = []
for mouse in range(mice_count):
    x, y = map(int, sys.stdin.readline().split())
    mice.append((x, y))


# 3. TO CONSTRUCT A GRAPH
# Hole : 0 ~ hole_count - 1 / Mouse : hole_count ~ hole_count + mice_count - 1

node_count = hole_count + mice_count + 2

source = hole_count + mice_count
sink = hole_count + mice_count + 1

graph = [[0 for nodeB in range(node_count)] for nodeA in range(node_count)]
capacity = [[0 for nodeB in range(node_count)] for nodeA in range(node_count)]
flow = [[0 for nodeB in range(node_count)] for nodeA in range(node_count)]

for hole_num in range(hole_count):

    hole = holes[hole_num]

    graph[source][hole_num] = 1
    graph[hole_num][source] = 1
    capacity[source][hole_num] = max_capacity

    for mouse_num in range(mice_count):

        mouse = mice[mouse_num]

        possible = True
        for idx in range(point_count):
            if not valid(points[idx-1], points[idx], hole, mouse):
                possible = False
                break
        if possible:
            graph[hole_num][hole_count + mouse_num] = 1
            graph[hole_count + mouse_num][hole_num] = 1
            capacity[hole_num][hole_count + mouse_num] = 1
    
for mouse_num in range(mice_count):

    graph[hole_count + mouse_num][sink] = 1
    graph[sink][hole_count + mouse_num] = 1
    capacity[hole_count + mouse_num][sink] = 1


# 4. EDMOND-KARP

ans = 0

while True:
    
    parent = [-1 for node in range(node_count)]
    
    queue = deque([source])
    while queue and parent[sink] == -1:
        now_node = queue.popleft()
        for next_node in range(node_count):
            if graph[now_node][next_node] and parent[next_node] == -1 and capacity[now_node][next_node] > flow[now_node][next_node]:
                queue.append(next_node)
                parent[next_node] = now_node
    
    if parent[sink] == -1:
        break
    
    amount = float('inf')
    node = sink
    while node != source:
        amount = min(amount, capacity[parent[node]][node] - flow[parent[node]][node])
        node = parent[node]
    
    node = sink
    while node != source:
        flow[parent[node]][node] += amount
        flow[node][parent[node]] -= amount
        node = parent[node]
    ans += amount

if ans == mice_count:
    print("Possible")
else:
    print("Impossible")