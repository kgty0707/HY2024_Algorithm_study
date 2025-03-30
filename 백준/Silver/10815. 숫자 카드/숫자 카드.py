import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
result = []

start = 0
end = N-1

for target in check:
    start = 0
    end = N-1
    label = False
    while start <= end:
        mid = (start + end) // 2
        data = cards[mid]

        if data == target:
            label = True
            result.append(1)
            break
        elif data > target:
            end = mid - 1

        else:
            start = mid + 1

    if not label:
        result.append(0)


print(*result)