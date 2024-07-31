'''
BOJ 26180 - Going in Circles (https://www.acmicpc.net/problem/26180)

There is a cycle of N cells. Each cell has a light.
You can move left, right, or flip the status of the light in each turn.
Guess N in 3N + 500 turns. 
'''

import sys


# 1. Check if N <= 22 WITH 500 TURNS

start = int(sys.stdin.readline())

move = 0
while move != 22:
    
    # Move right
    print("? right")
    sys.stdout.flush()
    move += 1
    result = int(sys.stdin.readline())
    
    # If same
    if start == result:
        
        # Flip
        print("? flip")
        sys.stdout.flush()
        waste = int(sys.stdin.readline())
        
        # Move back to start cell
        start_check = None
        for left_move in range(move):
            print("? left")
            sys.stdout.flush()
            start_check = int(sys.stdin.readline())

        # If start has changed, we know the length of the cycle (<= 22)
        if start_check != start:
            print("!", move)
            sys.stdout.flush()
            sys.exit()
        else:
            for right_move in range(move):
                print("? right")
                sys.stdout.flush()
                waste = int(sys.stdin.readline())


# 2. USE A PATTERN TO MARK A START POINT

# A pattern should be long and random enough
pattern = [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]

# Mark the pattern
for idx in range(22):
    print("? right")
    sys.stdout.flush()
    result = int(sys.stdin.readline())
    if result != pattern[idx]:
        print("? flip")
        sys.stdout.flush()
        waste = int(sys.stdin.readline())

# Find the pattern to get the length of the cycle

ans = 0
compare = []

while True:
    
    print("? right")
    sys.stdout.flush()
    ans += 1
    result = int(sys.stdin.readline())
    
    compare.append(result)
    if len(compare) > 22 and compare[-22:] == pattern:
        print("!", ans)
        sys.stdout.flush()
        sys.exit()