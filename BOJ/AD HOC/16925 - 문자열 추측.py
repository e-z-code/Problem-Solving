'''
BOJ 16925 - Guess the String (https://www.acmicpc.net/problem/16925)

There is a string S of length N.
Given all prefixes and suffixes of S except for S, print S.
'''

import sys

# 2. A FUNCTION TO GET ALL AFFIXES OF A STRING

def get_affixes(string):
    
    affixes = []
    for index in range(1, len(string)):
        affixes.append(string[:index])
    for index in range(1, len(string)):
        affixes.append(string[-index:])

    return affixes


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())

affixes = []
longest_affixes = []

for affix_input in range(2 * length - 2):
    affix = sys.stdin.readline().strip()
    if len(affix) == length - 1:
        longest_affixes.append(affix)
    affixes.append(affix)


# 3. TO GET THE ORIGINAL STRING

string = longest_affixes[0] + longest_affixes[1][-1]
if sorted(affixes) != sorted(get_affixes(string)):
    string = longest_affixes[1] + longest_affixes[0][-1]
print(string)


# 4. TO DISTINGUISH PREFIXES FROM SUFFIXES

prefixes = []
for index in range(1, len(string)):
    prefixes.append(string[:index])

ans = ""
for affix in affixes:
    if affix in prefixes:
        ans += "P"
        prefixes.remove(affix)
    else:
        ans += "S"
print(ans)