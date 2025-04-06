import sys

white = 0
blue = 0

def make_confetti(size, y, x):
    global white, blue
    color = two_array_list[y][x]
    same_flag = True

    for i in range(y, y + size):
        for j in range(x, x + size):
            if two_array_list[i][j] != color:
                same_flag = False
                break
        if not same_flag:
            break

    if same_flag:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        half = size // 2
        make_confetti(half, y, x)               # 왼쪽 위
        make_confetti(half, y, x + half)        # 오른쪽 위
        make_confetti(half, y + half, x)        # 왼쪽 아래
        make_confetti(half, y + half, x + half) # 오른쪽 아래

size = int(sys.stdin.readline())
two_array_list = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]

make_confetti(size, 0, 0)

print(white)
print(blue)