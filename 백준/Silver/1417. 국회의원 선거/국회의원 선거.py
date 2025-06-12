N = int(input())

candidates = []

for i in range(N):
    candidate = int(input())
    candidates.append(candidate)    

flag = False
num1 = candidates[0]
candidates = candidates[1:N]

result = 0

while flag != True:
    if N==1:
        flag = True
        break
    candidates.sort(reverse=True)
    # print(num1, candidates)
    if num1 <= candidates[0]:
        # print(num1, candidates[0])
        num1 += 1
        candidates[0] = candidates[0] - 1
        result += 1

    for i in range(len(candidates)):
        if num1 <= candidates[i]:
            flag  = False
            break
        flag = True


print(result)