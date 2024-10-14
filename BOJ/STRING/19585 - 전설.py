'''
BOJ 19585 - Legend (https://www.acmicpc.net/problem/19585)

You are given C color names and N nicknames.
Given Q team names, determine if a team name is a combination of a color name and a nickname.
'''

import sys


# 1. TRIE

def insert(root, word):
    now = root
    for char in word:
        if not now.get(char):
            now[char] = {}
        now = now[char]
    now["*"] = word

def prefix_search(root, word):
    now = root
    possible_cut = []
    for char in word:
        if not now.get(char):
            break
        now = now[char]
        if now.get("*"):
            possible_cut.append(len(now.get("*")))
    return possible_cut


# 2. TO GET THE INPUT

color_count, nickname_count = map(int, sys.stdin.readline().split())

color_trie = {}
for color_input in range(color_count):
    color = sys.stdin.readline().strip()
    insert(color_trie, color)

nickname_reversed_trie = {}
for nickname_input in range(nickname_count):
    nickname = sys.stdin.readline().strip()
    nickname_reversed = nickname[::-1]
    insert(nickname_reversed_trie, nickname_reversed)


# 3. TO SOLVE THE PROBLEM

team_count = int(sys.stdin.readline())
for team_input in range(team_count):
    
    team = sys.stdin.readline().strip()
    team_reversed = team[::-1]
    color_cut = prefix_search(color_trie, team)
    nickname_cut = set(prefix_search(nickname_reversed_trie, team_reversed))
    
    ans = False
    for idx in color_cut:
        if len(team) - idx in nickname_cut:
            ans = True
            break
    
    if ans:
        print("Yes")
    else:
        print("No")