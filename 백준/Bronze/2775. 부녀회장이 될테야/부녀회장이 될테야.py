num = int(input())

for i in range(num):
    k = int(input())
    n = int(input())

    dp = [[0] * (n+1) for _ in range(k+1)]
    
    for i in range(1, n+1):
        dp[0][i] = i

    for f in range(1, k+1):
        for r in range(1, n+1):
            dp[f][r] = dp[f][r-1] + dp[f-1][r]

    print(dp[k][n])