'''
BOJ 3161 - Election (https://www.acmicpc.net/problem/3161)

All M citizens put N candidates in order.
If the majority of the citizens put candidate A in front of candidate B, candidate A defeats candidate B.
The candidate wins the election if she has the greatest number of candidates she defeated.
Print the winner(s) of the election.
'''

import sys


# 1. TO GET THE INPUT

citizen_count, candidate_count = map(int, sys.stdin.readline().split())

result = []
for citizen in range(citizen_count):
    ballot = list(map(int, sys.stdin.readline().split()))
    result.append(ballot)


# 2. TO CALCULATE SCORE OF EACH CANDIDATE
# O(N^4) brute-force is enough. (M, N <= 50)

win_count = [0 for candidate in range(candidate_count + 1)]

for candidateA in range(1, candidate_count):
    for candidateB in range(candidateA + 1, candidate_count + 1):
        
        pointA = 0
        pointB = 0
        
        for ballot in result:
            indexA = ballot.index(candidateA)
            indexB = ballot.index(candidateB)
            if indexA < indexB:
                pointA += 1
            else:
                pointB += 1
        
        if pointA > pointB:
            win_count[candidateA] += 1
        elif pointB > pointA:
            win_count[candidateB] += 1


# 3. TO PRINT THE WINNER(S)

best_win = max(win_count)

for candidate in range(1, candidate_count + 1):
    if win_count[candidate] == best_win:
        print(candidate)