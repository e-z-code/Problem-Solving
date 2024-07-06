'''
BOJ 11578 - Team Recruit (https://www.acmicpc.net/problem/11578)

You recruit your team members.
You aim to make a team that can solve all problems with the minimum number of members.
Given problems each member can solve, print the minimum number of members.
'''

import sys


# 1. TO GET THE INPUT

problem_count, student_count = map(int, sys.stdin.readline().split())
students = []

for student in range(student_count):
    solvable_problem = list(map(int, sys.stdin.readline().split()))[1:]
    students.append(solvable_problem)


# 2. TO SOLVE THE PROBLEM

ans = -1
goal = set([problem for problem in range(1, problem_count+1)])

for case in range(1 << student_count):
    
    count = 0
    solvable_problem = []
    
    for idx in range(student_count):
        if (1 << idx) & case:
            count += 1
            solvable_problem.extend(students[idx])
    
    if set(solvable_problem) == goal:
        if ans == -1 or count < ans:
            ans = count

print(ans)