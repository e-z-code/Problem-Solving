'''
BOJ 16493 - Max Pages (https://www.acmicpc.net/problem/16493)

You need to return books after N days.
Once you read a book, you need to finish the book.
Given pages and expected time to finish each book, print the maximum number of pages you can read before the return.
'''

import sys


# 1. TO GET THE INPUT

day_count, book_count = map(int, sys.stdin.readline().split())

books = []
for book in range(book_count):
    day_needed, page_count = map(int, sys.stdin.readline().split())
    books.append((day_needed, page_count))


# 2. TO SOLVE THE PROBLEM
# Brute-forcing is enough. (M <= 20)

ans = 0

for case in range(1 << book_count):
    
    total_day = 0
    total_page = 0
    
    for idx in range(book_count):
        if case & (1 << idx):
            day_needed, page_count = books[idx]
            total_day += day_needed
            total_page += page_count
    
    if total_day <= day_count and total_page > ans:
        ans = total_page
        
print(ans)