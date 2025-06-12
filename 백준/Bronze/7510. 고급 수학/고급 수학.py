CASE = int(input())
results = []

def check(tri):
    result = "no"
    if tri[2]**2 == (tri[0]**2 + tri[1]**2):
        result = "yes"
    return result

for i in range(CASE):
    tri = list(map(int, input().split()))
    tri.sort()
    result = check(tri)
    results.append(result)


for i in range(CASE):
    if i == (CASE - 1):
        print(f"Scenario #{i+1}: \n{results[i]}")
    else:
        print(f"Scenario #{i+1}: \n{results[i]}\n")