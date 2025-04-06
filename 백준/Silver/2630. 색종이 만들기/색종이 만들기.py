import sys

white = 0
blue = 0

def make_confetti(two_array_list):
    global white, blue
    y_end_index = len(two_array_list) - 1
    x_end_index = len(two_array_list[0]) - 1

    if all(all(cell == 0 for cell in row) for row in two_array_list):
        white += 1
        return
    
    elif all(all(cell == 1 for cell in row) for row in two_array_list):
        blue += 1
        return
    
    else:
        if y_end_index % 2 == 0:
            y_end_index = int(y_end_index / 2)
        else:
            y_end_index = int(y_end_index / 2) + 1

        if x_end_index % 2 == 0:
            x_end_index = int(x_end_index / 2)
        else:
            x_end_index = int(x_end_index / 2) + 1

        first_half = [row[:x_end_index] for row in two_array_list[:y_end_index]]
        second_half = [row[x_end_index:] for row in two_array_list[:y_end_index]]
        third_half = [row[:x_end_index] for row in two_array_list[y_end_index:]]
        fourth_half = [row[x_end_index:] for row in two_array_list[y_end_index:]]
    
        make_confetti(first_half)
        make_confetti(second_half)
        make_confetti(third_half)
        make_confetti(fourth_half)


two_array_list = []
size = int(sys.stdin.readline().rstrip())

for i in range(size):
   array = list(map(int, sys.stdin.readline().rstrip().split()))
   two_array_list.append(array)

make_confetti(two_array_list)

print(white) 
print(blue)