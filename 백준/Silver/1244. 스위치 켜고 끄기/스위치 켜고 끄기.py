
N = int(input())
swithes = list(map(int, input().split()))
# print(swithes)
S = int(input())

for _ in range(S):
    gender, number = map(int, input().split())
    if gender == 1:
        i = 1
        multiple = number * i
        while multiple-1 < N:
            swithes[multiple-1] = int(not swithes[multiple-1])
            i += 1
            multiple = number * i
    if gender == 2:
        left = number - 2
        right = number
        swithes[number-1] = int(not swithes[number-1])
        while (right < N) and (left >= 0) and (swithes[left] == swithes[right]):
            swithes[left] = int(not swithes[left])
            swithes[right] = int(not swithes[right])
            left -= 1
            right += 1


count, remain = divmod(len(swithes), 20)

start = 0
for i in range(1, count+1):
    print(*swithes[start:i*20])
    start += 20

print(*swithes[count*20:count*20+remain])