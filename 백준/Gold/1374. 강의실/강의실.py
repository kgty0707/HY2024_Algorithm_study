import heapq

n = int(input())
lectures = []

for _ in range(n):
    _, start, end = map(int, input().split())
    lectures.append((start, end))

lectures.sort(key=lambda x: x[0])

heap = []

for start, end in lectures:
    if heap and start >= heap[0]:
        heapq.heappop(heap)

    heapq.heappush(heap, end)

print(len(heap))