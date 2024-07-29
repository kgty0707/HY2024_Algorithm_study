string_A = input().strip()
string_B = input().strip()

def print_lcs(string_A, string_B, LCS):
    i, j = len(string_A), len(string_B)
    result = []
    
    while i > 0 and j > 0:
        if string_A[i - 1] == string_B[j - 1]:
            result.append(string_A[i - 1])
            i -= 1
            j -= 1
        elif LCS[i - 1][j] > LCS[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(result))  # 결과 문자열을 뒤집어 반환

LCS = [[0] * (len(string_B) + 1) for _ in range(len(string_A) + 1)]

max_length = 0

for i in range(1, len(string_A) + 1):
    for j in range(1, len(string_B) + 1):
        if string_A[i - 1] == string_B[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
            max_length = max(max_length, LCS[i][j])
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(max_length)

if not max_length == 0:
    print(print_lcs(string_A, string_B, LCS))