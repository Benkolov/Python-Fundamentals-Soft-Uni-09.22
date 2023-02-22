def swap_func(index1, index2, numbers):
    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    return numbers


def multiply_func(index1, index2, numbers):
    numbers[index1] = numbers[index1] * numbers[index2]
    return numbers


def decrease_func(numbers):
    numbers = [(num - 1) for num in numbers]
    return numbers


def array_modifier(numbers):
    while True:
        command = input()

        if command == 'end':
            print(", ".join([str(num) for num in numbers]))
            break
        command = command.split()
        current_command = command[0]
        if current_command == "decrease":
            pass
        else:
            first_line = int(command[1])
            second_line = int(command[2])

        if current_command == 'swap':
            numbers = swap_func(first_line, second_line, numbers)
        elif current_command == "multiply":
            numbers = multiply_func(first_line, second_line, numbers)
        elif current_command == "decrease":
            numbers = decrease_func(numbers)


number = list(map(int, input().split()))
array_modifier(number)