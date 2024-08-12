import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

grid = []

for _ in range(N):
    row = list(map(int, input().strip()))
    grid.append(row)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

visited = [[(float('inf'), float('inf')) for _ in range(N)] for _ in range(N)]

def bfs(x, y):
    visited[y][x] = (1, 0)
    que = deque([(y, x)])

    while que:
        y, x = que.popleft()
        current_dist, current_block = visited[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < N and 0 <= nx < N):
                continue

            new_dist = current_dist + 1
            new_block = current_block + (1 if grid[ny][nx] == 0 else 0)

            if new_block < visited[ny][nx][1]:
                visited[ny][nx] = (new_dist, new_block)
                que.append((ny, nx))

bfs(0, 0)

min_block = visited[N-1][N-1][1]

print(min_block)