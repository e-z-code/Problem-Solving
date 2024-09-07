'''
BOJ 27483 - Round Corridor (https://www.acmicpc.net/problem/27483)

You are in a round corridor of two areas.
The inner area is divided by n sectors, and the outer area is equally divided by m sectors.
A wall exists between each pair of sectors of the same area, but there is no wall between the inner area and the outer area.
Answer q queries: Determine if you can move from room A to room B.
'''

import sys
from math import gcd


# 1. TO GET THE INPUT

inner_count, outer_count, query_count = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

key = gcd(inner_count, outer_count)
inner_in_sector = inner_count // key
outer_in_sector = outer_count // key

for query in range(query_count):
    
    locA, roomA, locB, roomB = map(int, sys.stdin.readline().split())
    
    if locA == 1:
        sectorA = (roomA - 1) // inner_in_sector
    else:
        sectorA = (roomA - 1) // outer_in_sector
    
    if locB == 1:
        sectorB = (roomB - 1) // inner_in_sector
    else:
        sectorB = (roomB - 1) // outer_in_sector
    
    if sectorA == sectorB:
        print("YES")
    else:
        print("NO")