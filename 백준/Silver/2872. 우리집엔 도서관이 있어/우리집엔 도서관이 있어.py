# 난 도서관이 좋아

import sys
from collections import deque

# ex_input 
# 3
# 3
# 2
# 1

# ex_output
# 2

input = sys.stdin.readline

B = int(input())

books = deque()

for _ in range(B):
    books.append(int(input()))

max_book = max(books)
max_idx = books.index(max_book)

target_book = max_book-1
ans = 0

for i in range(max_idx, -1, -1):
    if books[i] == target_book:
        ans += 1
        target_book-=1

print(B-1-ans)
