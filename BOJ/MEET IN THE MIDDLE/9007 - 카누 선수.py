'''
BOJ 9007 - Canoe Player (https://www.acmicpc.net/problem/9007)

Given four arrays, choose an element from each array so that the sum is the closest to the given K.
'''

import sys
from bisect import bisect_left


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    goal, length = map(int, sys.stdin.readline().split())
    
    arrA = list(map(int, sys.stdin.readline().split()))
    arrB = list(map(int, sys.stdin.readline().split()))
    arrC = list(map(int, sys.stdin.readline().split()))
    arrD = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. MEET IN THE MIDDLE
    
    arrAB = []
    for numA in arrA:
        for numB in arrB:
            arrAB.append(numA + numB)
    
    arrCD = []
    for numC in arrC:
        for numD in arrD:
            arrCD.append(numC + numD)
    arrCD.sort()
    
    ans = float('inf')
    for num in arrAB:
        idx = bisect_left(arrCD, goal - num)
        if idx != 0:
            caseA = num + arrCD[idx-1]
            if abs(caseA - goal) < abs(ans - goal) or (abs(caseA - goal) == abs(ans - goal) and caseA < ans):
                ans = caseA
        if idx != len(arrCD):
            caseB = num + arrCD[idx]
            if abs(caseB - goal) < abs(ans - goal) or (abs(caseB - goal) == abs(ans - goal) and caseB < ans):
                ans = caseB
    
    print(ans)
        