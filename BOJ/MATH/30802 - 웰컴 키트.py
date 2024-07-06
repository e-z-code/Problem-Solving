'''
BOJ 30802 - Welcome Kit (https://www.acmicpc.net/problem/30802)

You need to order shirts and pens.
You can only order T shirts at once, but it is okay to have extra shirts.
You can order one or P pens at once, but there should be no extra pens.
Determine how you should order shirts and pens.
'''

import sys


# 1. TO GET THE INPUT

member_count = int(sys.stdin.readline())
size = list(map(int, sys.stdin.readline().split()))

shirt_in_bundle, pen_in_bundle = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

shirt_bundle = 0
for size_count in size:
    if size_count % shirt_in_bundle == 0:
        shirt_bundle += size_count // shirt_in_bundle
    else:
        shirt_bundle += size_count // shirt_in_bundle + 1

pen_bundle = member_count // pen_in_bundle
pen = member_count % pen_in_bundle

print(shirt_bundle)
print(pen_bundle, pen)