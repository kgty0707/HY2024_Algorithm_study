def binary_search(arr, target):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

result = []
for target in check:
    result.append(binary_search(cards, target))
print(*result)