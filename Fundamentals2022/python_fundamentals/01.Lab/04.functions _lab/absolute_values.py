sequence_of_numbers = input().split(" ")

abs_list = []

for i in sequence_of_numbers:
    current_abs = abs(float(i))
    abs_list.append(current_abs)


print(abs_list)