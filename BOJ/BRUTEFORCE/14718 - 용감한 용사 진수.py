'''
BOJ 14718 - Courageous Soldier Jin-su (https://www.acmicpc.net/problem/14718)

There are N enemies.
If a soldier's STR, AGI, and INT stats are not smaller than an enemy, the soldier can kill the enemy.
Determine the minimum stat point to kill K enemies.
'''

import sys


# 1. TO GET THE INPUT

enemy_count, kill_goal = map(int, sys.stdin.readline().split())

stats = []
for enemy in range(enemy_count):
    strength, agility, intelligence = map(int, sys.stdin.readline().split())
    stats.append([strength, agility, intelligence])


# 2. BRUTE-FORCING
# O(N ^ 4) brute-forcing works. (N <= 100)

ans = float('inf')

for str_idx in range(enemy_count):
    for agi_idx in range(enemy_count):
        for int_idx in range(enemy_count):
            
            strength, agility, intelligence = stats[str_idx][0], stats[agi_idx][1], stats[int_idx][2]
            kill_count = 0
            for enemy in stats:
                if strength >= enemy[0] and agility >= enemy[1] and intelligence >= enemy[2]:
                    kill_count += 1
            if kill_count >= kill_goal and strength + agility + intelligence < ans:
                ans = strength + agility + intelligence

print(ans)