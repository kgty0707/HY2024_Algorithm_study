import sys

N = int(sys.stdin.readline())

count = 0

for _ in range(N):
    string = sys.stdin.readline()
    before = []
    char = ""
    for i in range(len(string)):
        if not char:
            char = string[i]
            before.append(char)   

        # 이전 문자랑 현재 문자가 같은지 검사
        # 만약 같지 않으면 이전에 있었던 문자랑 같은게 있는지 검사
        cur_char = string[i]
        # print(f"char: {char}, cur_char: {cur_char}, before_list: {before}")
        if char == cur_char:
            continue
        else:
            if cur_char in before:
                count -= 1
                break
            else:
                before.append(cur_char)
                char = cur_char
    count += 1

print(count)