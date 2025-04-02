import sys

a, b = map(str, sys.stdin.readline().split())

def cheak_string_length(a, b):
    prev_count = len(a) # a의 길이로 초기화
    char_length = len(b) - len(a)
    # print("char_length: ", char_length)
    if char_length == 0:
        count = cheak_similar_char(a, b)
        return count
    else:
        for i in range(char_length+1):
            new_b = b[i:i+len(a)] # 길이에 맞게 슬라이싱하면서 최적의 조건을 찾음음
            count = cheak_similar_char(a, new_b)

            if prev_count > count:
                prev_count = count

            # print("prev_count: ", prev_count)
        return prev_count

def cheak_similar_char(a, b):
    count = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1

    return count 


print(cheak_string_length(a, b))