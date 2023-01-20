receive_string = input()

while True:
    command = input()
    if command == "End":
        break

    command = command.split()

    if command[0] == "Translate":
        char = command[1]
        replacement = command[2]
        receive_string = receive_string.replace(char, replacement)
        print(receive_string)

    elif command[0] == "Includes":
        substring = command[1]
        if substring in receive_string:
            print('True')
        else:
            print('False')

    elif command[0] == "Start":
        substring = command[1]
        starts = receive_string[:len(substring)]
        if substring == starts:
            print('True')
        else:
            print('False')

    elif command[0] == "Lowercase":
        receive_string = receive_string.lower()
        print(receive_string)

    elif command[0] == "FindIndex":
        char = command[1]
        list_index = []
        for index, i in enumerate(receive_string):
            if i == char:
                list_index.append(index)
        print(sorted(list_index)[-1])

    elif command[0] == "Remove":
        start_index = int(command[1])
        count = int(command[2])

        receive_string = receive_string[:start_index] + receive_string[start_index + count:]
        print(receive_string)