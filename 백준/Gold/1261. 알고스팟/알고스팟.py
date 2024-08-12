from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

grid = []

for _ in range(N):
    row = list(map(int, input().strip()))
    grid.append(row)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 벽을 부순 횟수만을 기록하는 visited 배열
visited = [[-1 for _ in range(M)] for _ in range(N)]

def bfs(x, y):
    que = deque([(y, x)])
    visited[y][x] = 0  # 시작점에서 벽을 부순 적이 없으므로 0으로 초기화

    while que:
        y, x = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                new_block = visited[y][x] + (1 if grid[ny][nx] == 1 else 0)

                if visited[ny][nx] == -1 or new_block < visited[ny][nx]:
                    visited[ny][nx] = new_block
                    if grid[ny][nx] == 1:
                        que.append((ny, nx))  # 벽을 부순 경우 뒤에 넣기
                    else:
                        que.appendleft((ny, nx))  # 벽을 부수지 않은 경우 앞에 넣기

bfs(0, 0)

min_block = visited[N-1][M-1]

print(min_block)
