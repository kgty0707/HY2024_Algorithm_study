from collections import deque, defaultdict
import sys

edges = []

# 입력값
n, m = map(int, sys.stdin.readline().split())
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

# 인접 리스트 생성
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프

# 작은 번호부터 방문하도록 정렬
for v in graph:
    graph[v].sort()

# DFS
# def dfs(v, visited):
#     visited[v] = True
#     # print(v, end=' ')
#     for neighbor in graph[v]:
#         if not visited[neighbor]:
#             dfs(neighbor, visited)

# BFS
def bfs(start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        # print(v, end=' ')
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

count = 0
visited = [False] * (n + 1)

for v in range(1, n + 1):
    if not visited[v]:
        # dfs(v, visited) # DFS로 방문 처리
        # BFS로 방문 처리
        bfs(v, visited)
        count += 1


print(count)

# print("DFS (인접 리스트): ", end='')
# dfs(1, [False] * (n + 1))

# print("\nBFS (인접 리스트): ", end='')
# bfs(1)