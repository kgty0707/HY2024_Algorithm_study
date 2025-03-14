 # 분수찾기
# 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> 1/3 -> 1/4

n = int(input()) # 원하는 번호 1보다 큰 숫자
횟수 = 1
target = 1
분자 = 1
분모 = 1


while target != n:
    횟수 += 1
    if n == 1:
        break
    if 횟수 % 2 == 0: # 짝수
        for i in range(횟수-1):
            if target == n:
                break
            elif 분자 == 1:
                분모 += 1
            else:
                분자 -= 1
                분모 += 1

            target += 1
            # print(target, 분자, 분모, "짝수")
            
    if 횟수 % 2 == 1: # 홀수
        for i in range(횟수-1):
            
            if target == n:
                break
            elif 분모 == 1:
                분자 += 1
            else:
                분모 -= 1
                분자 += 1
            
            target += 1
            # print(target, 분자, 분모, "홀수")


print(f"{분자}/{분모}")
