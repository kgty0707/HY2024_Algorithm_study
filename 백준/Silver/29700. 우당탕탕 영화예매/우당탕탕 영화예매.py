import sys

input = sys.stdin.readline

# N 세로줄 - / M 가로줄 | / K 동아리원 수
N, M, K = map(int, input().split())
SEAT = []

for _ in range(N):
    ary = list(map(int, input().strip()))
    SEAT.append(ary)

available = 0
# 각 세로 줄 마다
    # 마지막 인덱스가 가로 보다 작을 때 까지
        # k만큼 이동하는데, 추출한 K가 모두 0인 경우(False) + 1

for i in range(N):
    for j in range(M-K+1):
        selected_seat = SEAT[i][j:j+K]
        if not sum(selected_seat):
            available += 1
print(available)