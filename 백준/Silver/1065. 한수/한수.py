import sys

N = int(sys.stdin.readline().strip())
X = 0
result = 0

while X < N:
    if N < 100:
        result = N
        break
    else:
        result = 99
        for i in range(100, N+1):
            X = str(i)
            prev_d = None
            is_hansu = True
            for j in range(len(X)-1):
                if j == 0:
                    d = int(X[j+1]) - int(X[j])
                else:
                    current_d = int(X[j+1]) - int(X[j])
                    if d != current_d:
                        is_hansu = False
                        break
            if is_hansu:
                result += 1
            X = i

print(result)