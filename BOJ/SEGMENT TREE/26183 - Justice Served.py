'''
BOJ 26183 - Justice Served (https://www.acmicpc.net/problem/26183)

You are given N lines. 
If a line X contains line Y, X covers Y.
Convincing-ness of a line is 0 if the line is not covered by another line.
Otherwise, the convincing-ness of a line is one more than that of the most convincing line that covers the line.
For each line, print the convincing-ness. 
'''

import sys


# 4. FUNCTIONS FOR SEGMENT TREE

def get_max(end):
    
    left = end + ALIGN
    right = (1 << 19) - 1
    
    now_max = -1
    while left <= right:
        if left % 2 == 1:
            now_max = max(now_max, seg_tree[left])
            left += 1
        if right % 2 == 0:
            now_max = max(now_max, seg_tree[right])
            right -= 1
        left >>= 1 
        right >>= 1
    
    return now_max

def update(end, num):
    
    now = end + ALIGN
    seg_tree[now] = num
    now >>= 1
    
    while now != 0:
        seg_tree[now] = max(seg_tree[now << 1], seg_tree[(now << 1) | 1])
        now >>= 1


# 1. TO GET THE INPUT AND SORT

line_count = int(sys.stdin.readline())

line_to_num = {}
lines = []
ends = []

for line_num in range(line_count):
    start, duration = map(int, sys.stdin.readline().split())
    line_to_num[(start, duration)] = line_num
    lines.append((start, duration))
    ends.append(start + duration)

lines.sort(key = lambda x : (x[0], -x[1]))


# 2. COORDINATE COMPRESSION

end_to_num = {}

ends.sort()
num = 0
for idx in range(len(ends)):
    if ends[idx] not in end_to_num:
        end_to_num[ends[idx]] = num
        num += 1


# 3. TO CONSTRUCT A SEGMENT TREE

ALIGN = 1 << 18
seg_tree = [-1 for idx in range(1 << 19)]

ans = [-1 for idx in range(line_count)]


# 5. TO SOLVE THE PROBLEM

for start, duration in lines:
    
    end = end_to_num[start + duration]
    
    now_ans = get_max(end) + 1
    ans[line_to_num[(start, duration)]] = str(now_ans)
    update(end, now_ans)

print(" ".join(ans))