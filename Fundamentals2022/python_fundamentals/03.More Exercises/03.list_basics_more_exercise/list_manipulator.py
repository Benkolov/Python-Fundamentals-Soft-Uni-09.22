numbers = list(map(int, input().split()))
command = input()
while command != "end":
    current_command = command.split()
    data = current_command[0]
    if data == "exchange":
        index = int(current_command[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            left_part = numbers[:index]
            right_part = numbers[index:]
            numbers = right_part + left_part
    elif data == "max":
        type_number = current_command[1]
        if type_number == "even":
            max_even = [max(numbers) for i in numbers if i % 2 == 0]
            print(max_even)
        elif type_number == "odd":
            max_odd = [max(numbers) for i in numbers if i % 2 != 0]
            print(max_odd)
    elif data == "min":
        type_number = current_command[1]
        if type_number == "even":
            min_even = [min(numbers) for i in numbers if i % 2 == 0]
            print(min_even)
        elif type_number == "odd":
            min_odd = [min(numbers) for i in numbers if i % 2 == 0]
            print(min_odd)
    elif data == "first":
        num = int(current_command[1])
        type_num = current_command[2]
        if type_num == "even":
            pass
        elif type_num == "odd":
            pass
    elif data == "last":
        num = int(current_command[1])
        type_num = current_command[2]
        if type_num == "even":
            pass
        elif type_num == "odd":
            pass

    command = input()