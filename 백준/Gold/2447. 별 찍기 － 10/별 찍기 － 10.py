import math
import sys

def star(num):
    if num == 0:
        return ["*"] 

    prev_pattern = star(num - 1) 
    size = len(prev_pattern)     
    new_pattern = []

    for line in prev_pattern:
        new_pattern.append(line + line + line)

    for line in prev_pattern:
        new_pattern.append(line + " " * size + line)

    for line in prev_pattern:
        new_pattern.append(line + line + line)

    return new_pattern

n = int(input())

num = 0
temp = n
while temp > 1:
    if temp % 3 != 0:
        sys.exit()
    temp //= 3
    num += 1

result = star(num)
result = "\n".join(result)
print(result)