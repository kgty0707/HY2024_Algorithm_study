
def mosaic_paper():
    # 0으로 채운 100x100 리스트를 만들어서 return
    mosaic = []
    for i in range(100):
        mosaic.append([0] * 100)
    return mosaic

# input: 100x100 리스트, 가리는 종이의 좌표값 왼쪽 아래 x, y, 오른쪽 위 x, y
# output: 가리는 종이의 좌표값을 받아서 1씩 더한 100x100 리스트를 return
def mosaic_calculator(mosaic, x_l, y_l, x_r, y_r):
    for i in range(y_l, y_r+1):
        for j in range(x_l, x_r+1):
            mosaic[i][j] += 1
    return mosaic

# input: 100x100 리스트, 최소 M값
def count_hide_paint(mosaic, M):
    count = 0
    for i in range(100):
        for j in range(100):
            if mosaic[i][j] > M:
                count += 1
    return count

def main():
    N, M = map(int, input().split())
    mosaic = mosaic_paper()
    for _ in range(N):
        x_l, y_l, x_r, y_r = map(int, input().split())
        mosaic = mosaic_calculator(mosaic, x_l-1, y_l-1, x_r-1, y_r-1)
    print(count_hide_paint(mosaic, M))


if __name__ == "__main__":
    main()