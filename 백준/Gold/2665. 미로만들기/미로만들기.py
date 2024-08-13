from collections import deque
import sys

input = sys.stdin.readline

N = int(input().strip())

grid = []

for _ in range(N):
    row = list(map(int, input().strip()))
    grid.append(row)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

visited = [[-1 for _ in range(N)] for _ in range(N)]

def bfs(x, y):
    que = deque([(y, x)])
    visited[y][x] = 0

    while que:
        y, x = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                new_block = visited[y][x] + (1 if grid[ny][nx] == 0 else 0)

                if visited[ny][nx] == -1 or new_block < visited[ny][nx]:
                    visited[ny][nx] = new_block
                    que.append((ny, nx))  

bfs(0, 0)

min_block = visited[N-1][N-1]

print(min_block)