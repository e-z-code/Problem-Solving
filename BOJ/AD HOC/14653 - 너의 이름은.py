'''
BOJ 14653 - Your Name (https://www.acmicpc.net/problem/14653)

Given a chat log (How many people have not read a message, who sent a message), determine who might have not read a given message.
'''

import sys


# 1. TO GET THE INPUT

people_count, message_count, target_num = map(int, sys.stdin.readline().split())

target_unread_count = 0
people_read = [set() for unread_count in range(people_count+1)]

for message_num in range(1, message_count+1):
    
    unread_count, sender = sys.stdin.readline().strip().split()
    unread_count = int(unread_count)
    if message_num == target_num:
        target_unread_count = unread_count
    
    for idx in range(unread_count+1):
        people_read[idx].add(sender)


# 2. TO SOLVE THE PROBLEM

alphabet_upper = set()
for ascii_num in range(65, 65 + people_count):
    alphabet_upper.add(chr(ascii_num))

if target_unread_count == 0:
    print(-1)
else:
    ans = sorted(list(alphabet_upper - people_read[target_unread_count] - set(["A"])))
    print(" ".join(ans))
