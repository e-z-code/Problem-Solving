'''
CF973C - Password Cracking (https://codeforces.com/contest/2013/problem/C)

Your goal is to find a binary password of length N.
You can ask whether a binary string is a substring of the password at most 2 X N times.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    size = int(sys.stdin.readline())


    # 2. TO SOLVE THE PROBLEM
    
    now = ""
    
    # Until you find a suffix
    
    while len(now) != size:
        print("?", now + "0")
        sys.stdout.flush()
        result = int(sys.stdin.readline())
        if result == 1:
            now = now + "0"
            continue
        else:
            print("?", now + "1")
            sys.stdout.flush()
            result = int(sys.stdin.readline())
            if result == 1:
                now = now + "1"
                continue
            else:
                break
    
    # Fill the rest
    
    while len(now) != size:
        print("?", "0" + now)
        sys.stdout.flush()
        result = int(sys.stdin.readline())
        if result == 1:
            now = "0" + now
        else:
            now = "1" + now

    print("!", now)
    sys.stdout.flush()