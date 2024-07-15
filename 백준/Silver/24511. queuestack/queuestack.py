from collections import deque

N = int(input())

queuestack = list(map(int, input().strip().split()))
_list = list(map(int, input().strip().split()))

M = int(input())

_newlist = list(map(int, input().strip().split()))

queue = deque()

for i, index in enumerate(queuestack):
    if index == 0:
        queue.append(_list[i])

return_value = []

for num in _newlist:
    if 0 not in queuestack:
        return_value = _newlist.copy()
        break
    queue.appendleft(num)
    return_value.append(queue.pop())

print(' '.join(str(s) for s in return_value))