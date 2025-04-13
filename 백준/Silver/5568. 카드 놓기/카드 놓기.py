import itertools

N = int(input())
K = int(input())
cards = [input().strip() for _ in range(N)]

perms = itertools.permutations(cards, K)
results = set()

for p in perms:
    num = ''.join(p)
    results.add(num)

print(len(results))
