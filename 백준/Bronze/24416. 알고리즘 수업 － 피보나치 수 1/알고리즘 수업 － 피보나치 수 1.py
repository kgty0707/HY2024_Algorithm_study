

dp = [0] * 100

def dp_fibonacci(n):
    global dp_count

    dp[1] = dp[2] = 1

    for i in range(3, n+1):
        dp_count += 1
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


def recyrsive_fibonacci(n):
    global re_count
    # 여기서 count를 증가시키면 안되더라
    if n == 1 or n == 2:
        re_count += 1
        return 1
    return recyrsive_fibonacci(n-1) + recyrsive_fibonacci(n-2)



num = int(input())
re_count = 0
dp_count = 0

value = dp_fibonacci(num)
print(value, dp_count)
# value = recyrsive_fibonacci(num)
# print(value, re_count)
