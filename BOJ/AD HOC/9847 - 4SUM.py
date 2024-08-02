'''
BOJ 9847 - 4SUM (https://www.acmicpc.net/problem/9847)

Given four arrays - A, B, C, and D - choose an element from each array so that the sum is 0.
'''

import sys


# 1. TO GET THE INPUT

element_count = list(map(int, sys.stdin.readline().split()))

arrA = []
arrB = []
arrC = []
arrD = []

for idx in range(element_count[0]):
    num = int(sys.stdin.readline())
    arrA.append(num)

for idx in range(element_count[1]):
    num = int(sys.stdin.readline())
    arrB.append(num)

for idx in range(element_count[2]):
    num = int(sys.stdin.readline())
    arrC.append(num)

for idx in range(element_count[3]):
    num = int(sys.stdin.readline())
    arrD.append(num)


# 2. MEET IN THE MIDDLE

sum_AB = {}
for numA in arrA:
    for numB in arrB:
        sum_AB[numA + numB] = (numA, numB)

sum_CD = {}
for numC in arrC:
    for numD in arrD:
        sum_CD[numC + numD] = (numC, numD)

for num in sum_AB:
    if -num in sum_CD:
        numA, numB = sum_AB[num]
        numC, numD = sum_CD[-num]
        print(numA, numB, numC, numD)
        break