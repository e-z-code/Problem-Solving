'''
BOJ 18088 - Inverted Deck (https://www.acmicpc.net/problem/18088)

Determine if it is possible to sort the array into non-decreasing order by reversing just one substring.
If so, print the start index and end index of the substring.
'''

import sys


# 1. TO GET THE INPUT

card_count = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

distinct_cards = []

for idx in range(card_count):
    card = cards[idx]
    if len(distinct_cards) == 0 or card != distinct_cards[-1][0]:
        distinct_cards.append((card, [idx]))
    else:
        distinct_cards[-1][1].append(idx)

# Find the substring to reverse

possible = True

start_idx = None
end_idx = None

for idx in range(1, len(distinct_cards)):
    last_card, last_range = distinct_cards[idx-1]
    now_card, now_range = distinct_cards[idx]
    if last_card > now_card:
        if start_idx == None and end_idx == None:
            # Substring initialization
            start_idx = last_range[0]
            end_idx = now_range[-1]
        elif now_range[0] == end_idx + 1:
            # Extend the substring
            end_idx = now_range[-1]
        else:
            # If there are more than two substrings to reverse, it is impossible.
            possible = False
            break

if possible:
    if start_idx == None and end_idx == None:
        print(1, 1)
    else:
        # Reversal may not guarantee that the deck is sorted.
        new_cards = cards[:start_idx] + list(reversed(cards[start_idx:end_idx+1])) + cards[end_idx+1:]
        if new_cards == sorted(cards):
            print(start_idx + 1, end_idx + 1)
        else:
            print("impossible")
else:
    print("impossible")