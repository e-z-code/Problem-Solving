'''
BOJ 7989 - The Bridge (https://www.acmicpc.net/problem/7989)

The tourists want to cross the bridge with a torch.
However, they cannot cross it without the torch nor in groups larger than two.
Each tourist requires a certain amount of time to cross the bridge.
Two tourists crossing the bridge together need as much time as the slower of them.
Calculate the shortest time for all the tourists to cross the bridge.
'''

import sys


# 1. TO GET THE INPUT

people_count = int(sys.stdin.readline())

people_time = []
for people in range(people_count):
    time = int(sys.stdin.readline())
    people_time.append(time)
people_time.sort()


# 2. TO SOLVE THE PROBLEM

ans = 0

while len(people_time) > 3:

    # Let's assume A, B are two most fastest people and C, D are two most slowest people.
    # There are two ways to move C and D.
    # Case 1: AB -> A -> CD -> B (A + 2B + D)
    # Case 2: AC -> A -> AD -> A (2A + C + D)
    
    case1 = people_time[0] + 2 * people_time[1] + people_time[-1]
    case2 = people_time[0] * 2 + people_time[-1] + people_time[-2]
    ans += min(case1, case2)
    
    people_time.pop()
    people_time.pop()
    
if len(people_time) == 3:
    ans += sum(people_time)
else:
    ans += max(people_time)
    
print(ans)