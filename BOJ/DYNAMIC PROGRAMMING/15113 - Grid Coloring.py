'''
BOJ 15113 - Grid Coloring (https://www.acmicpc.net/problem/15113)

There is an M X N grid.
You should color each square either red or blue. Some squares may be already painted.
For each blue square, all squares in the rectangle from the top left of the grid to that square must also be blue.
Determine the number of distinct colorings.
'''

import sys


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

grid = []
for row_num in range(row_count):
    row = list(sys.stdin.readline().strip())
    grid.append(row)


# 2. TO STORE THE POSITION OF RIGHTMOST BLUE AND LEFTMOST RED FOR EACH ROW

# The position of the rightmost blue

rightmost_blue = [0 for row_num in range(row_count)]

for row_num in range(row_count):
    
    rightmost_idx = 0
    for col_num in range(col_count-1, -1, -1):
        if grid[row_num][col_num] == "B":
            rightmost_idx = col_num+1
            break
    
    rightmost_blue[row_num] = rightmost_idx
    
    for row_compare in range(row_num):
        if rightmost_blue[row_compare] < rightmost_blue[row_num]:
            rightmost_blue[row_compare] = rightmost_blue[row_num]

# The position of the leftmost red

leftmost_red = [col_count+1 for row_num in range(row_count)]

for row_num in range(row_count):
    
    leftmost_idx = col_count+1
    for col_num in range(col_count):
        if grid[row_num][col_num] == "R":
            leftmost_idx = col_num+1
            break
    
    leftmost_red[row_num] = leftmost_idx
    
    if row_num != 0 and leftmost_red[row_num-1] < leftmost_red[row_num]:
        leftmost_red[row_num] = leftmost_red[row_num-1]


# 3. DYNAMIC PROGRAMMING
# dp[R][C] = The number of cases when C is the rightmost index of the blue cell for the R-th row

dp = [[0 for col_num in range(col_count+1)] for row_num in range(row_count)]

ans = None

for row_num in range(row_count):
    
    leftmost_possible_blue = rightmost_blue[row_num]
    rightmost_possible_blue = leftmost_red[row_num] - 1
    
    if leftmost_possible_blue > rightmost_possible_blue:
        ans = 0
        break
    else:
        for col_num in range(col_count+1):
            if row_num == 0:
                if leftmost_possible_blue <= col_num <= rightmost_possible_blue:
                    dp[row_num][col_num] = 1
            else:
                if leftmost_possible_blue <= col_num <= rightmost_possible_blue:
                    for last_blue_idx in range(col_num, col_count+1):
                        dp[row_num][col_num] += dp[row_num-1][last_blue_idx]

if ans == 0:
    print(ans)
else:
    print(sum(dp[-1]))    