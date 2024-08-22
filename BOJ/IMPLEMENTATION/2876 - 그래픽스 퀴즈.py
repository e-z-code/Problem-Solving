'''
BOJ 2876 - Professor (https://www.acmicpc.net/problem/2876)

There are N desks with two students in a row.
A professor can mark from desk X to desk Y if there is a student at each desk with common grades.
Given grades, determine the maximum number of desks the professor can mark.
'''

import sys


# 1. TO GET THE INPUT

desk_count = int(sys.stdin.readline())

desks = []
for desk in range(desk_count):
    studentA, studentB = map(int, sys.stdin.readline().split())
    desks.append((studentA, studentB))


# 2. TO SOLVE THE PROBLEM

ans_grade = 0
ans_student = 0

for grade in range(1, 6):
    now = 0
    for desk in desks:
        
        if grade in desk:
            now += 1
        else:
            now = 0
        
        if ans_student < now:
            ans_student = now
            ans_grade = grade

print(ans_student, ans_grade)