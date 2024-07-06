'''
BOJ 17392 - Depressing Vacation (https://www.acmicpc.net/problem/17392)

You have N appointments in M days.
Your mood can be represented by an integer. If your mood goes below 0, your depression index increases by pow(mood, 2).
If you have an appointment, your mood on the day equals the expected happiness of the appointment. Otherwise, your mood decreases by 1.
Minimize the sum of the depression index by adjusting appointments. 
'''

import sys


# 2. A FUNCTION FOR SUM OF SQUARES

def sum_square(val):

    return val * (val + 1) * (2 * val + 1) // 6


# 1. TO GET THE INPUT

appointment_count, day_count = map(int, sys.stdin.readline().split())
if appointment_count != 0:
    appointment_happiness = list(map(int, sys.stdin.readline().split()))


# 3. TO MINIMIZE THE DEPRESSION INDEX

if appointment_count == 0:

    print(day_count * (day_count + 1) * (2 * day_count + 1) // 6)

else:

    day_with_depression = max(0, day_count - sum(appointment_happiness) - len(appointment_happiness))

    group_count = appointment_count + 1
    base_depression = day_with_depression // group_count
    print(group_count * sum_square(base_depression) + pow(base_depression + 1, 2) * (day_with_depression % group_count))