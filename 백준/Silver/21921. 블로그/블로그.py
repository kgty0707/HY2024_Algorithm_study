import sys

input = sys.stdin.readline
# 5, 2
N, X = map(int, input().split())

# 1 4 2 5 1
arr = [0] + list(map(int, input().split()))
sum_arr = []

temp = 0
for a in arr:
    temp += a
    sum_arr.append(temp)

result_arr = []

for i in range(X, N+1):
    if i-X < len(sum_arr):
        value = sum_arr[i] - sum_arr[i-X]
        result_arr.append(value)

# for i in range(1, N+1):
#     if i + (X-1) < len(arr):
#         temp = 0
#         for j in range(X):
#             temp += arr[i+j]
#         sum_arr.append(temp)

def max_visitor(sum_arr):
    num = 0
    max_value = max(sum_arr)
    if max_value == 0: return print("SAD")

    for value in sum_arr:
        if value == max_value:
            num += 1
    return print(f"{max_value}\n{num}")

max_visitor(result_arr)