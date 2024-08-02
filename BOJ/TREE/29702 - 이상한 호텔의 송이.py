'''
BOJ 29702 - Song-Yi in Wonder-hotel (https://www.acmicpc.net/problem/29702)

You are staying in a complete binary tree-shaped hotel of 60 levels.
Given a room you are in, print room numbers in the path from your room to the root.
Room number consists of the level of the room and its index from the left.
'''

import sys


# 2. A FUNCTION TO GET THE ROOM NUMBER

def room_number(room):
    
    level = 0
    
    room_copy = room
    while room_copy != 0:
        room_copy >>= 1
        level += 1
    
    index = room - (1 << (level - 1)) + 1
    
    return str(level) + "0" * (18 - len(str(index))) + str(index)


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    room = int(sys.stdin.readline())
    
    
    # 3. TO SOLVE THE PROBLEM
    
    while room != 0:
        print(room_number(room))
        room >>= 1