dp = [0] * 100

def dp_fibonacci(n):
    global dp_count

    dp[1] = dp[2] = 1

    for i in range(3, n+1):
        dp_count += 1
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


num = int(input())
dp_count = 0

value = dp_fibonacci(num)
print(value, dp_count)