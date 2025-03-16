
import sys

def _stack(stack, v, num=0):
    if v == 1:
        stack.append(num)
    if v == 2:
        if stack:
            out = stack.pop()
            print(out)
        else:
            print(-1)
    if v == 3:
        print(len(stack))
    if v == 4:
        if stack:
            print(0)
        else:
            print(1)
    if v == 5:
        if stack:
            out = stack.pop()
            print(out)
            stack.append(out)
        else:
            print(-1)


stack = []
num = 0
order = int(sys.stdin.readline())

for _ in range(order):
    value = list(map(int,sys.stdin.readline().split()))

    if len(value) != 1:
        v, num = value
    else:
        v = value[0]

    _stack(stack, v, num)