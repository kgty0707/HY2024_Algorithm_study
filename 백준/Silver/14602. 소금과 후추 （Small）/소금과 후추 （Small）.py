import sys

input = sys.stdin.readline

M, N, K, W = map(int, input().split())

A = []
for _ in range(M):
    row = list(map(int, input().split()))
    A.append(row)

median_index = (W * W) // 2

B = []

for i in range(M - W + 1):
    b_row = []
    for j in range(N - W + 1):
        window_1d = []
        for row_index in range(i, i + W):
            for col_index in range(j, j + W):
                window_1d.append(A[row_index][col_index])

        window_1d.sort()
        median_value = window_1d[median_index]
        
        b_row.append(median_value)
    
    B.append(b_row)

for row in B:
    print(*row)