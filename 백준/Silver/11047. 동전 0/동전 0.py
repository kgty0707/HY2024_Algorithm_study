import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

# 코인의 종류 리스트 만들기
for _ in range(N):
    coins.append(int(input()))

ans = 0

for coin in coins[::-1]:
    if K == 0: # 목표한 돈이 0이 되면 종료
        break
    ans += K // coin
    K %= coin

print(ans)