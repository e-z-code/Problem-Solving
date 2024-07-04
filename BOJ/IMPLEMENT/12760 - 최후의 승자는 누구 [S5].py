'''
BOJ 12760 - Who is the winner? (https://www.acmicpc.net/problem/12760)

N players have M cards.
Players always use the card with the highest number at each turn.
If a player has a card with the highest number, the player gets a point.
Who will be the winner?
'''

import sys


# 1. TO GET THE INPUT 

player_count, card_count = map(int, sys.stdin.readline().split())

player_cards = []
for player in range(player_count):
    cards = list(map(int, sys.stdin.readline().split()))
    cards.sort()
    player_cards.append(cards)


# 2. TO SOLVE THE PROBLEM

score = [0 for player in range(player_count)]

for turn in range(card_count):

    turn_cards = []
    for cards in player_cards:
        turn_cards.append(cards.pop())

    for idx in range(player_count):
        if turn_cards[idx] == max(turn_cards):
            score[idx] += 1

for player in range(player_count):
    if score[player] == max(score):
        print(player+1, end = ' ')