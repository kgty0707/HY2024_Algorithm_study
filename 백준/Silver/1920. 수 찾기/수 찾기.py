N = int(input())
arr = list(map(int, input().split()))
M = int(input())
query = list(map(int, input().split()))

arr.sort()

def binary_search(k):
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == k:
            return 1
        if arr[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for q in query:
    print(binary_search(q))