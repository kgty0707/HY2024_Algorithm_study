import math

W, H, X, Y, P = map(int, input().split())

R = H/2


def check(x, y):
    flag = False
    if (x >= X and x <= X + W) and (y >= Y and y <= Y + H):
        flag = True
    else:
        if x < X:
            if R >= math.sqrt((x-X)**2 + (y-(Y+R))**2):
                flag = True
        else:
            if R >= math.sqrt((x-(X+W))**2 + (y-(Y+R))**2):
                flag = True

    return flag

result = 0

for i in range(P):
    x, y = map(int, input().split())
    flag = check(x, y)

    if flag:
        result += 1

print(result)