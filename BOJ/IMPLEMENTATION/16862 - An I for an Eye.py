'''
BOJ 16862 - An I for an Eye (https://www.acmicpc.net/problem/16862)

Given a conversion table, print the converted string.

(1) Conversion should also be made inside words.
(2) If two letter sequences overlap, replace only the first one.
(3) If two letter sequences start at the same location, replace the long er one.
(4) If the letter sequence starts with an upper-case letter, then the abbreviation should also be in upper-case.
(5) No substituted letter should later be part of another substitution.
'''

import sys


# 1. TO GET THE INPUT

four_no_capital = {"four":"4"}
three_no_capital = {"and":"&", "one":"1", "won":"1", "two":"2", "for":"4"}
three_capital = {"sea":"c", "see":"c", "eye":"i", "owe":"o", "are":"r", "you":"u", "why":"y"}
two_no_capital = {"at":"@", "to":"2"}
two_capital = {"be":"b", "oh":"o"}

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    string = sys.stdin.readline().strip()
    
    
    # 2. TO SOLVE THE PROBLEM
    
    ans = ""
    stack = []
    for char in string:
        
        # For bee, bea, too
        if len(ans) >= 1 and len(stack) == 0:
            if (ans[-1] == "2" and char.lower() == "o") or (ans[-1].lower() == "b" and (char.lower() == "a" or char.lower() == "e")):
                continue
            
        stack.append(char)
        if len(stack) >= 4:
            word = "".join(stack[-4:])
            if word.lower() in four_no_capital:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                ans += "".join(stack) + four_no_capital[word.lower()]
                stack = []
        if len(stack) >= 3:
            word = "".join(stack[-3:])
            if word.lower() in three_no_capital:
                stack.pop()
                stack.pop()
                stack.pop()
                ans += "".join(stack) + three_no_capital[word.lower()]
                stack = []
            elif word.lower() in three_capital:
                stack.pop()
                stack.pop()
                stack.pop()
                if 65 <= ord(word[0]) <= 90:
                    ans += "".join(stack) + three_capital[word.lower()].upper()
                else:
                    ans += "".join(stack) + three_capital[word.lower()]
                stack = []
        if len(stack) >= 2:
            word = "".join(stack[-2:])
            if word.lower() in two_no_capital:
                stack.pop()
                stack.pop()
                ans += "".join(stack) + two_no_capital[word.lower()]
                stack = []
            elif word.lower() in two_capital:
                stack.pop()
                stack.pop()
                if 65 <= ord(word[0]) <= 90:
                    ans += "".join(stack) + two_capital[word.lower()].upper()
                else:
                    ans += "".join(stack) + two_capital[word.lower()]
                stack = []
    
    ans += "".join(stack)
    print(ans)