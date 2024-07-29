N = int(input())

def sumerization(n):
    if n == 0:
        return 1  # 0을 만드는 방법은 아무 것도 하지 않는 경우 1가지
    if n == 1:
        return 1  # 1을 만드는 방법은 1만 사용하는 경우 1가지
    if n == 2:
        return 2  # 2를 만드는 방법은 (1+1), (2) 2가지
    if n == 3:
        return 4  # 3을 만드는 방법은 (1+1+1), (1+2), (2+1), (3) 4가지

    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4

    for i in range(4, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    return memo[n]

for _ in range(N):
    num = int(input())
    result = sumerization(num)
    print(result)