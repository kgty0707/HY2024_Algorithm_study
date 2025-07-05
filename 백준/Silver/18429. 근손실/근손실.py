N, K = map(int, input().split())
KIT = list(map(int, input().split()))
temp = []
result = 0
muscle_sum = 500
pre_muscle_sum = 0

def backtrack(muscle_sum, temp):
    global result

    if len(temp) == N:
        result += 1
        return result
    
    for i in range(N):
        if not temp:
            muscle_sum = 500

        pre_muscle_sum = muscle_sum
        muscle_sum += KIT[i] - K
        
        if muscle_sum >= 500 and i not in temp:
            temp.append(i)
            backtrack(muscle_sum, temp)
            temp.pop()            

        muscle_sum = pre_muscle_sum
            

backtrack(muscle_sum, temp)
print(result)