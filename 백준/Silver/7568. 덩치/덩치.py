import sys

N = int(sys.stdin.readline())

people = []

for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    people.append((weight, height))

def compare(target, other):
    if target[0] < other[0] and target[1] < other[1]:
        return True
    else:
        return False

def rank(target, people):
    rank = 1
    for other in people:
        if compare(target, other):
            rank += 1
    return rank

result = []
for person in people:
    result.append(rank(person, people))
print(*result)
