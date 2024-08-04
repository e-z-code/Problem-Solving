'''
ABC365C - Transportation Expenses (https://atcoder.jp/contests/abc365/tasks/abc365_c)

The transportation cost for N people is given.
You decided to set a maximum limit of X for the transportation subsidy.
The sum of the transportation subsidies cannot exceed M.
Determine the maximum possible value of X.
'''

import sys


# 1. TO GET THE INPUT

people_count, budget = map(int, sys.stdin.readline().split())
costs = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM 

if sum(costs) <= budget:

    print("infinite")

else:
    
    left = 0
    right = max(costs)
    
    while left + 1 < right:
        
        mid = (left + right) // 2
        
        subsidy = 0
        for cost in costs:
            subsidy += min(cost, mid)
        
        if subsidy <= budget:
            left = mid
        else:
            right = mid
    
    print(left)