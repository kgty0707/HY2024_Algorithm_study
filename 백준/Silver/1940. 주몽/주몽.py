N = int(input().strip())
M = int(input().strip())
materials = list(map(int, input().split()))

materials.sort()


start_index = 0
end_index = len(materials) - 1
armor = 0

for i in range(end_index + 1):
    if start_index == end_index:
        break
    if materials[start_index] + materials[end_index] == M:
        armor += 1
        start_index += 1
    elif materials[start_index] + materials[end_index] < M:
        start_index += 1
    else:
        end_index -=1
        
print(armor)