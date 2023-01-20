numbers = input().split()
count = 0
while True:
    command = input()
    if command == "end":
        if len(numbers) > 0:
            print("Sorry you lose :(")
            print(f'{" ".join(str(num) for num in numbers)}')
        else:
            print(f"You have won in {count} turns!")
        break
    if len(numbers) == 0:
        print(f"You have won in {count} turns!")
        break
    count += 1
    command = command.split()
    first_index = int(command[0])
    second_index = int(command[1])
    if first_index >= len(numbers) or first_index < 0 or second_index >= len(numbers)\
            or second_index < 0 or first_index == second_index:
        middle_numbers = len(numbers) // 2
        numbers.insert(middle_numbers, f"-{count}a"), numbers.insert(middle_numbers, f"-{count}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if numbers[first_index] == numbers[second_index]:
            a = numbers[first_index]
            print(f"Congrats! You have found matching elements - {numbers[first_index]}!")
            numbers.remove(a), numbers.remove(a)

        else:
            print("Try again!")



