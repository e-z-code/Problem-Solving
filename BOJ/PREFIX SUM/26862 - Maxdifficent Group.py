'''
BOJ 26862 - Maxdifficent Group (https://www.acmicpc.net/problem/26862)

You can divide an array by some groups.
The cost of each group is the sum of all elements in the group.
Calculate the maximum value of the difference of costs of two adjacent groups.
'''

import sys


# 1. TO GET THE INPUT

num_count = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))


# 2. PREFIX SUM

prefix_sum = [0]
for num in nums:
    prefix_sum.append(prefix_sum[-1] + num)

left_max = [0 for idx in range(len(prefix_sum))]
left_min = [0 for idx in range(len(prefix_sum))]

now_max = 0
now_min = 0
for idx in range(1, len(prefix_sum)):
    left_max[idx] = now_max
    left_min[idx] = now_min
    if prefix_sum[idx] > now_max:
        now_max = prefix_sum[idx]
    if prefix_sum[idx] < now_min:
        now_min = prefix_sum[idx]

right_max = [0 for idx in range(len(prefix_sum))]
right_min = [0 for idx in range(len(prefix_sum))]

now_max = prefix_sum[-1]
now_min = prefix_sum[-1]
for idx in range(len(prefix_sum) - 2, -1, -1):
    right_max[idx] = now_max
    right_min[idx] = now_min
    if prefix_sum[idx] > now_max:
        now_max = prefix_sum[idx]
    if prefix_sum[idx] < now_min:
        now_min = prefix_sum[idx]


# 3. TO SOLVE THE PROBLEM

# Let's assume P is a prefix sum array.
# Then, the problem is equal to calculate the maximum value of |P[x] + P[z] - 2P[y]|.
# You can solve the problem by fixing the index y.

ans = 0
for idx in range(1, len(prefix_sum) - 1):
    ans = max(ans, abs(left_max[idx] + right_max[idx] - 2 * prefix_sum[idx]), abs(left_min[idx] + right_min[idx] - 2 * prefix_sum[idx]))
print(ans)