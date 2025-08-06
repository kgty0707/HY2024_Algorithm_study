M, N, B, W = map(int, input().split())

PICTURE = []
for _ in range(M):
    ary = list(map(int, input().split()))
    PICTURE.append(ary)

# print(PICTURE)
# print(PICTURE[0])
# print(PICTURE[0:1][0])
# print(PICTURE[0:1])

B_MATRIX = []
MEDIAN_INDEX = int(((W**2+1) / 2) - 1)
# print(f"MEDIAN_INDEX: {MEDIAN_INDEX}")

def calculate_median(matrix):
    # ★★★★★★★★★★★★★★★★★★★★★
    # flattened_array = sum(matrix, []) 
    flattened_array = [item for row in matrix for item in row]

    # print(flattened_array)
    flattened_array.sort()
    median_value = flattened_array[MEDIAN_INDEX]
    return median_value

result = []
for i in range(M-W+1):
    ary = []
    for j in range(N-W+1):
        # ★★★★★★★★★★★★★★★★★★★★★
        window = [row[j:j+W] for row in PICTURE[i:i+W]]
        # print(window)
        median = calculate_median(window)
        ary.append(median)
    print(*ary)
    result.append(ary)

# print(result)