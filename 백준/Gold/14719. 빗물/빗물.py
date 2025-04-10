H, W = map(int, input().split())
block_height = list(map(int, input().split()))


def search_max_value(right_flag, block_height):
    target_list = []
    max_height = 0

    if right_flag:
        block_height.reverse()

    for i in range(W):
        if max_height < block_height[i]:
            max_height = block_height[i]
        target_list.append(max_height)

    if right_flag:
        target_list.reverse()
    
    return target_list

left_max = search_max_value(0, block_height.copy())
right_max = search_max_value(1, block_height.copy())
water_height = 0

# print(left_max, right_max, block_height)

for i in range(W):
    height = min(left_max[i], right_max[i]) - block_height[i]
    if height > 0:
        water_height += height

print(water_height)