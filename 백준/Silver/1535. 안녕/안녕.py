from sys import stdin

N = int(stdin.readline())
stamina_consum = [0] + list(map(int, stdin.readline().split()))
get_pleasure = [0] + list(map(int, stdin.readline().split()))

dp = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        if stamina_consum[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - stamina_consum[i]] + get_pleasure[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][99])